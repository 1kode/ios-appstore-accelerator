#!/usr/bin/env python3
"""
Screenshot Validator for iOS App Store Submission

Validates screenshot files against Apple's App Store requirements.
Checks dimensions, format, and provides guidance for missing screenshots.

Usage:
    python3 screenshot_validator.py <path-to-screenshots-folder>
    python3 screenshot_validator.py <path-to-single-image>

Options:
    --device DEVICE    Check for specific device only
    --json             Output results as JSON
    --strict           Fail on warnings, not just errors

Exit codes:
    0 - All screenshots valid
    1 - Errors found
    2 - Warnings found (with --strict)
"""

import sys
import json
import argparse
from pathlib import Path

# Try to import PIL for image analysis
try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


# App Store screenshot requirements (2024)
SCREENSHOT_SPECS = {
    'iphone_6_7': {
        'name': 'iPhone 6.7" Display',
        'devices': ['iPhone 15 Pro Max', 'iPhone 15 Plus', 'iPhone 14 Pro Max'],
        'portrait': (1290, 2796),
        'landscape': (2796, 1290),
        'required': True,
        'min_count': 3,
        'max_count': 10,
    },
    'iphone_6_5': {
        'name': 'iPhone 6.5" Display',
        'devices': ['iPhone 14 Plus', 'iPhone 13 Pro Max', 'iPhone 12 Pro Max', 'iPhone 11 Pro Max', 'iPhone XS Max'],
        'portrait': (1284, 2778),
        'landscape': (2778, 1284),
        'required': True,  # Can use 6.7" as fallback
        'min_count': 3,
        'max_count': 10,
        'fallback': 'iphone_6_7',
    },
    'iphone_6_1': {
        'name': 'iPhone 6.1" Display',
        'devices': ['iPhone 15 Pro', 'iPhone 15', 'iPhone 14', 'iPhone 13', 'iPhone 12'],
        'portrait': (1179, 2556),
        'landscape': (2556, 1179),
        'required': False,
        'min_count': 0,
        'max_count': 10,
        'fallback': 'iphone_6_7',
    },
    'iphone_5_5': {
        'name': 'iPhone 5.5" Display',
        'devices': ['iPhone 8 Plus', 'iPhone 7 Plus', 'iPhone 6s Plus'],
        'portrait': (1242, 2208),
        'landscape': (2208, 1242),
        'required': False,
        'min_count': 0,
        'max_count': 10,
    },
    'ipad_pro_12_9_6th': {
        'name': 'iPad Pro 12.9" (6th gen)',
        'devices': ['iPad Pro 12.9" (6th gen)', 'iPad Pro 12.9" (5th gen)'],
        'portrait': (2048, 2732),
        'landscape': (2732, 2048),
        'required': False,  # Only if iPad supported
        'min_count': 0,
        'max_count': 10,
    },
    'ipad_pro_12_9_2nd': {
        'name': 'iPad Pro 12.9" (2nd gen)',
        'devices': ['iPad Pro 12.9" (2nd gen)', 'iPad Pro 12.9" (1st gen)'],
        'portrait': (2048, 2732),
        'landscape': (2732, 2048),
        'required': False,
        'min_count': 0,
        'max_count': 10,
    },
}

# Valid image formats
VALID_FORMATS = ['PNG', 'JPEG', 'JPG']
VALID_EXTENSIONS = ['.png', '.jpg', '.jpeg']


def get_image_info(image_path: Path) -> dict:
    """Get image dimensions and format."""
    if not HAS_PIL:
        # Fallback: just check extension
        ext = image_path.suffix.lower()
        return {
            'path': str(image_path),
            'name': image_path.name,
            'format': ext[1:].upper() if ext else 'UNKNOWN',
            'width': None,
            'height': None,
            'has_alpha': None,
            'error': 'PIL not installed - cannot read dimensions',
        }
    
    try:
        with Image.open(image_path) as img:
            return {
                'path': str(image_path),
                'name': image_path.name,
                'format': img.format,
                'width': img.width,
                'height': img.height,
                'has_alpha': img.mode in ('RGBA', 'LA', 'PA'),
                'mode': img.mode,
                'error': None,
            }
    except Exception as e:
        return {
            'path': str(image_path),
            'name': image_path.name,
            'format': None,
            'width': None,
            'height': None,
            'has_alpha': None,
            'error': str(e),
        }


def match_device(width: int, height: int) -> list:
    """Find matching device specs for given dimensions."""
    matches = []
    for device_id, spec in SCREENSHOT_SPECS.items():
        if (width, height) == spec['portrait']:
            matches.append((device_id, 'portrait'))
        elif (width, height) == spec['landscape']:
            matches.append((device_id, 'landscape'))
    return matches


def validate_screenshot(image_info: dict) -> dict:
    """Validate a single screenshot."""
    result = {
        'file': image_info['name'],
        'path': image_info['path'],
        'valid': True,
        'errors': [],
        'warnings': [],
        'device_match': None,
        'orientation': None,
        'dimensions': None,
    }
    
    if image_info['error']:
        result['valid'] = False
        result['errors'].append(f"Could not read image: {image_info['error']}")
        return result
    
    # Check format
    if image_info['format'] not in VALID_FORMATS:
        result['valid'] = False
        result['errors'].append(f"Invalid format: {image_info['format']}. Use PNG or JPEG.")
    
    # Check for alpha channel (not allowed for App Store icons, warned for screenshots)
    if image_info['has_alpha']:
        result['warnings'].append("Image has alpha channel (transparency). This may cause issues.")
    
    # Check dimensions
    width = image_info['width']
    height = image_info['height']
    result['dimensions'] = f"{width}×{height}"
    
    if width and height:
        matches = match_device(width, height)
        if matches:
            device_id, orientation = matches[0]
            result['device_match'] = SCREENSHOT_SPECS[device_id]['name']
            result['orientation'] = orientation
        else:
            result['valid'] = False
            result['errors'].append(
                f"Dimensions {width}×{height} don't match any App Store requirements"
            )
            # Suggest closest match
            result['warnings'].append("See output for required dimensions")
    
    return result


def validate_folder(folder_path: Path) -> dict:
    """Validate all screenshots in a folder."""
    results = {
        'folder': str(folder_path),
        'total_files': 0,
        'valid_files': 0,
        'screenshots': [],
        'device_coverage': {},
        'errors': [],
        'warnings': [],
        'recommendations': [],
    }
    
    # Find all image files
    image_files = []
    for ext in VALID_EXTENSIONS:
        image_files.extend(folder_path.glob(f'*{ext}'))
        image_files.extend(folder_path.glob(f'*{ext.upper()}'))
    
    results['total_files'] = len(image_files)
    
    if not image_files:
        results['errors'].append("No image files found in folder")
        return results
    
    # Validate each file
    device_counts = {device_id: {'portrait': 0, 'landscape': 0} for device_id in SCREENSHOT_SPECS}
    
    for image_path in sorted(image_files):
        image_info = get_image_info(image_path)
        validation = validate_screenshot(image_info)
        results['screenshots'].append(validation)
        
        if validation['valid']:
            results['valid_files'] += 1
            
            # Track device coverage
            if validation['device_match']:
                for device_id, spec in SCREENSHOT_SPECS.items():
                    if spec['name'] == validation['device_match']:
                        device_counts[device_id][validation['orientation']] += 1
                        break
    
    # Check device coverage
    for device_id, spec in SCREENSHOT_SPECS.items():
        portrait_count = device_counts[device_id]['portrait']
        landscape_count = device_counts[device_id]['landscape']
        total_count = portrait_count + landscape_count
        
        results['device_coverage'][spec['name']] = {
            'portrait': portrait_count,
            'landscape': landscape_count,
            'total': total_count,
            'required': spec['required'],
            'meets_minimum': total_count >= spec['min_count'],
        }
        
        if spec['required'] and total_count < spec['min_count']:
            fallback = spec.get('fallback')
            if fallback:
                fb_spec = SCREENSHOT_SPECS[fallback]
                fb_count = device_counts[fallback]['portrait'] + device_counts[fallback]['landscape']
                if fb_count >= spec['min_count']:
                    results['warnings'].append(
                        f"{spec['name']}: Using {fb_spec['name']} screenshots as fallback"
                    )
                else:
                    results['errors'].append(
                        f"{spec['name']}: Need at least {spec['min_count']} screenshots (have {total_count})"
                    )
            else:
                results['errors'].append(
                    f"{spec['name']}: Need at least {spec['min_count']} screenshots (have {total_count})"
                )
    
    # Generate recommendations
    if not any(device_counts['iphone_6_7']['portrait'] or device_counts['iphone_6_7']['landscape'] 
               for _ in [1]):
        if device_counts['iphone_6_7']['portrait'] + device_counts['iphone_6_7']['landscape'] == 0:
            results['recommendations'].append(
                "Add iPhone 6.7\" screenshots (1290×2796) - these can be used as fallback for other sizes"
            )
    
    return results


def print_report(results: dict) -> None:
    """Print formatted validation report."""
    
    print("\n" + "=" * 60)
    print("📸 SCREENSHOT VALIDATION REPORT")
    print("=" * 60)
    
    if 'folder' in results:
        print(f"\n📁 Folder: {results['folder']}")
        print(f"   Total files: {results['total_files']}")
        print(f"   Valid files: {results['valid_files']}")
        
        # Device coverage
        print(f"\n📱 Device Coverage:")
        for device_name, coverage in results['device_coverage'].items():
            status = "✅" if coverage['meets_minimum'] or not coverage['required'] else "❌"
            req_text = "(required)" if coverage['required'] else "(optional)"
            print(f"   {status} {device_name} {req_text}")
            print(f"      Portrait: {coverage['portrait']}, Landscape: {coverage['landscape']}")
        
        # Individual screenshots
        if results['screenshots']:
            print(f"\n📋 Screenshot Details:")
            for ss in results['screenshots']:
                status = "✅" if ss['valid'] else "❌"
                print(f"\n   {status} {ss['file']}")
                print(f"      Dimensions: {ss['dimensions']}")
                if ss['device_match']:
                    print(f"      Device: {ss['device_match']} ({ss['orientation']})")
                for error in ss['errors']:
                    print(f"      ❌ {error}")
                for warning in ss['warnings']:
                    print(f"      ⚠️ {warning}")
    else:
        # Single file validation
        ss = results
        status = "✅" if ss['valid'] else "❌"
        print(f"\n   {status} {ss['file']}")
        print(f"      Dimensions: {ss['dimensions']}")
        if ss['device_match']:
            print(f"      Device: {ss['device_match']} ({ss['orientation']})")
        for error in ss['errors']:
            print(f"      ❌ {error}")
        for warning in ss['warnings']:
            print(f"      ⚠️ {warning}")
    
    # Errors and warnings
    if 'errors' in results and results['errors']:
        print(f"\n❌ Errors:")
        for error in results['errors']:
            print(f"   • {error}")
    
    if 'warnings' in results and results['warnings']:
        print(f"\n⚠️ Warnings:")
        for warning in results['warnings']:
            print(f"   • {warning}")
    
    if 'recommendations' in results and results['recommendations']:
        print(f"\n💡 Recommendations:")
        for rec in results['recommendations']:
            print(f"   • {rec}")
    
    # Required dimensions reference
    print(f"\n📐 Required Dimensions Reference:")
    print(f"   iPhone 6.7\":  1290×2796 (portrait) or 2796×1290 (landscape)")
    print(f"   iPhone 6.5\":  1284×2778 (portrait) or 2778×1284 (landscape)")
    print(f"   iPhone 5.5\":  1242×2208 (portrait) or 2208×1242 (landscape)")
    print(f"   iPad 12.9\":   2048×2732 (portrait) or 2732×2048 (landscape)")
    
    # Summary
    print("\n" + "-" * 60)
    has_errors = bool(results.get('errors')) or (
        'screenshots' in results and 
        any(not ss['valid'] for ss in results['screenshots'])
    )
    if has_errors:
        print("❌ ISSUES FOUND - Fix before submission")
    elif results.get('warnings'):
        print("⚠️ WARNINGS - Review before submission")
    else:
        print("✅ ALL SCREENSHOTS VALID")
    print("-" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Validate App Store screenshots',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Required Dimensions:
  iPhone 6.7":  1290×2796 or 2796×1290
  iPhone 6.5":  1284×2778 or 2778×1284
  iPhone 5.5":  1242×2208 or 2208×1242
  iPad 12.9":   2048×2732 or 2732×2048

Examples:
  python3 screenshot_validator.py ./screenshots/
  python3 screenshot_validator.py ./hero-image.png
        """
    )
    
    parser.add_argument('path', help='Path to screenshot file or folder')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--strict', action='store_true', help='Treat warnings as errors')
    
    args = parser.parse_args()
    
    if not HAS_PIL:
        print("⚠️ Warning: Pillow (PIL) not installed. Install with: pip install Pillow")
        print("   Continuing with limited validation...\n")
    
    path = Path(args.path)
    
    if not path.exists():
        print(f"❌ Error: Path not found: {path}")
        sys.exit(1)
    
    if path.is_dir():
        results = validate_folder(path)
    else:
        image_info = get_image_info(path)
        results = validate_screenshot(image_info)
    
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_report(results)
    
    # Determine exit code
    has_errors = bool(results.get('errors')) or (
        'screenshots' in results and 
        any(not ss['valid'] for ss in results['screenshots'])
    )
    has_warnings = bool(results.get('warnings'))
    
    if has_errors:
        sys.exit(1)
    elif args.strict and has_warnings:
        sys.exit(2)
    sys.exit(0)


if __name__ == "__main__":
    main()
