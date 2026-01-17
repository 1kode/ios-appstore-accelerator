#!/usr/bin/env python3
"""
App Icon Validator for iOS App Store Submission

Validates app icon files against Apple's App Store requirements.
Checks dimensions, format, alpha channel, and color space.

Usage:
    python3 app_icon_validator.py <path-to-icon.png>
    python3 app_icon_validator.py <path-to-Assets.xcassets>

Requirements:
    Pillow (PIL): pip install Pillow

Exit codes:
    0 - Icon valid
    1 - Errors found
"""

import sys
from pathlib import Path

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


# App Store icon requirements
APPSTORE_ICON_SIZE = (1024, 1024)
VALID_FORMATS = ['PNG']


def validate_icon(icon_path: Path) -> dict:
    """
    Validate an app icon file.
    
    Args:
        icon_path: Path to icon file
        
    Returns:
        Dictionary with validation results
    """
    result = {
        'file': str(icon_path),
        'valid': True,
        'errors': [],
        'warnings': [],
        'info': {},
    }
    
    if not HAS_PIL:
        result['errors'].append("Pillow not installed. Run: pip install Pillow")
        result['valid'] = False
        return result
    
    if not icon_path.exists():
        result['errors'].append(f"File not found: {icon_path}")
        result['valid'] = False
        return result
    
    try:
        with Image.open(icon_path) as img:
            result['info'] = {
                'format': img.format,
                'size': f"{img.width}×{img.height}",
                'mode': img.mode,
                'has_alpha': img.mode in ('RGBA', 'LA', 'PA'),
            }
            
            # Check format
            if img.format not in VALID_FORMATS:
                result['errors'].append(
                    f"Invalid format: {img.format}. Must be PNG."
                )
                result['valid'] = False
            
            # Check dimensions
            if (img.width, img.height) != APPSTORE_ICON_SIZE:
                result['errors'].append(
                    f"Invalid dimensions: {img.width}×{img.height}. "
                    f"Must be exactly 1024×1024 pixels."
                )
                result['valid'] = False
            
            # Check for alpha channel (transparency)
            if img.mode in ('RGBA', 'LA', 'PA'):
                # Check if alpha channel is actually used
                if img.mode == 'RGBA':
                    alpha = img.split()[-1]
                    alpha_values = list(alpha.getdata())
                    has_transparency = any(a < 255 for a in alpha_values)
                    
                    if has_transparency:
                        result['errors'].append(
                            "Icon has transparency (alpha channel with transparent pixels). "
                            "App Store icons must be opaque with no transparency."
                        )
                        result['valid'] = False
                    else:
                        result['warnings'].append(
                            "Icon has alpha channel but no transparent pixels. "
                            "Consider converting to RGB to avoid potential issues."
                        )
                else:
                    result['errors'].append(
                        f"Icon mode '{img.mode}' may have transparency. "
                        "Convert to RGB mode without alpha channel."
                    )
                    result['valid'] = False
            
            # Check for rounded corners (approximate check)
            # App Store will add rounded corners automatically
            if img.mode in ('RGBA', 'LA', 'PA'):
                result['warnings'].append(
                    "Note: Do NOT add rounded corners to your icon. "
                    "Apple will apply the correct corner radius automatically."
                )
            
            # Check color mode
            if img.mode not in ('RGB', 'RGBA', 'P'):
                result['warnings'].append(
                    f"Unusual color mode: {img.mode}. "
                    "Consider converting to RGB for best compatibility."
                )
            
            # Check for very small file size (might be placeholder)
            file_size = icon_path.stat().st_size
            if file_size < 10000:  # Less than 10KB is suspicious
                result['warnings'].append(
                    f"File size is only {file_size} bytes. "
                    "This might be a placeholder or low-quality image."
                )
            
            result['info']['file_size'] = f"{file_size / 1024:.1f} KB"
            
    except Exception as e:
        result['errors'].append(f"Could not read image: {e}")
        result['valid'] = False
    
    return result


def find_appstore_icon(assets_path: Path) -> Path:
    """Find the App Store icon in an Assets.xcassets folder."""
    
    # Common locations
    search_patterns = [
        'AppIcon.appiconset/icon_1024*.png',
        'AppIcon.appiconset/*1024*.png',
        'AppIcon.appiconset/AppStore*.png',
        '**/AppIcon*1024*.png',
        '**/icon-1024*.png',
    ]
    
    for pattern in search_patterns:
        matches = list(assets_path.glob(pattern))
        if matches:
            return matches[0]
    
    return None


def print_report(result: dict) -> None:
    """Print formatted validation report."""
    
    print("\n" + "=" * 60)
    print("🎨 APP ICON VALIDATION REPORT")
    print("=" * 60)
    
    print(f"\n📁 File: {result['file']}")
    
    if result['info']:
        info = result['info']
        print(f"\n📋 Icon Information:")
        print(f"   Format:    {info.get('format', 'Unknown')}")
        print(f"   Size:      {info.get('size', 'Unknown')}")
        print(f"   Mode:      {info.get('mode', 'Unknown')}")
        print(f"   Has Alpha: {info.get('has_alpha', 'Unknown')}")
        print(f"   File Size: {info.get('file_size', 'Unknown')}")
    
    if result['errors']:
        print(f"\n❌ Errors:")
        for error in result['errors']:
            print(f"   • {error}")
    
    if result['warnings']:
        print(f"\n⚠️ Warnings:")
        for warning in result['warnings']:
            print(f"   • {warning}")
    
    # Requirements reminder
    print(f"\n📐 App Store Icon Requirements:")
    print(f"   • Exactly 1024×1024 pixels")
    print(f"   • PNG format")
    print(f"   • No transparency (no alpha channel)")
    print(f"   • No rounded corners (Apple adds these)")
    print(f"   • sRGB or P3 color space")
    
    # Summary
    print("\n" + "-" * 60)
    if result['valid']:
        if result['warnings']:
            print("⚠️ ICON VALID WITH WARNINGS")
        else:
            print("✅ ICON VALID - Ready for App Store")
    else:
        print("❌ ICON INVALID - Fix errors before submission")
    print("-" * 60 + "\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 app_icon_validator.py <path-to-icon.png>")
        print("       python3 app_icon_validator.py <path-to-Assets.xcassets>")
        print("\nExample:")
        print("  python3 app_icon_validator.py ./AppIcon.png")
        print("  python3 app_icon_validator.py ./MyApp/Assets.xcassets")
        sys.exit(1)
    
    if not HAS_PIL:
        print("❌ Error: Pillow library required.")
        print("   Install with: pip install Pillow")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    
    if not path.exists():
        print(f"❌ Error: Path not found: {path}")
        sys.exit(1)
    
    # If directory, try to find icon
    if path.is_dir():
        icon_path = find_appstore_icon(path)
        if icon_path:
            print(f"📍 Found icon: {icon_path}")
            path = icon_path
        else:
            print(f"❌ Error: Could not find App Store icon in {path}")
            print("   Looking for 1024x1024 icon in AppIcon.appiconset")
            sys.exit(1)
    
    result = validate_icon(path)
    print_report(result)
    
    sys.exit(0 if result['valid'] else 1)


if __name__ == "__main__":
    main()
