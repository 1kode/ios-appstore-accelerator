#!/usr/bin/env python3
"""
Privacy Manifest Checker for iOS Apps

Scans an iOS project for Required Reason API usage and checks if a Privacy
Manifest (PrivacyInfo.xcprivacy) exists with appropriate declarations.

Usage:
    python3 privacy_manifest_checker.py <path-to-project>

Exit codes:
    0 - No issues found
    1 - Issues found or error
"""

import os
import re
import sys
import plistlib
from pathlib import Path


# Required Reason APIs and their detection patterns
REQUIRED_REASON_APIS = {
    'NSPrivacyAccessedAPICategoryFileTimestamp': {
        'name': 'File Timestamp APIs',
        'patterns': [
            r'NSFileCreationDate',
            r'NSFileModificationDate',
            r'NSURLContentModificationDateKey',
            r'NSURLCreationDateKey',
            r'getattrlist\s*\(',
            r'\bstat\s*\(',
            r'fstat\s*\(',
        ],
        'reasons': ['DDA9.1', 'C617.1', '3B52.1', '0A2A.1'],
    },
    'NSPrivacyAccessedAPICategorySystemBootTime': {
        'name': 'System Boot Time APIs',
        'patterns': [
            r'systemUptime',
            r'mach_absolute_time\s*\(',
        ],
        'reasons': ['35F9.1', '8FFB.1', '3D61.1'],
    },
    'NSPrivacyAccessedAPICategoryDiskSpace': {
        'name': 'Disk Space APIs',
        'patterns': [
            r'volumeAvailableCapacityKey',
            r'volumeAvailableCapacityForImportantUsageKey',
            r'volumeAvailableCapacityForOpportunisticUsageKey',
            r'volumeTotalCapacityKey',
            r'statfs\s*\(',
            r'statvfs\s*\(',
        ],
        'reasons': ['85F4.1', 'E174.1', '7D9E.1'],
    },
    'NSPrivacyAccessedAPICategoryActiveKeyboards': {
        'name': 'Active Keyboards APIs',
        'patterns': [
            r'activeInputModes',
        ],
        'reasons': ['3EC4.1', '54BD.1'],
    },
    'NSPrivacyAccessedAPICategoryUserDefaults': {
        'name': 'User Defaults APIs',
        'patterns': [
            r'UserDefaults',
            r'NSUserDefaults',
            r'\.standard\.',
        ],
        'reasons': ['CA92.1', '1C8F.1', 'C56D.1'],
    },
}

# File extensions to scan
CODE_EXTENSIONS = ['.swift', '.m', '.mm', '.h', '.c', '.cpp']


def find_project_files(project_path: Path) -> list:
    """Find all source code files in the project."""
    files = []
    for ext in CODE_EXTENSIONS:
        files.extend(project_path.rglob(f'*{ext}'))
    return files


def scan_file_for_apis(file_path: Path, api_patterns: dict) -> dict:
    """Scan a single file for Required Reason API usage."""
    findings = {}
    
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return findings
    
    for api_category, info in api_patterns.items():
        for pattern in info['patterns']:
            matches = re.findall(pattern, content)
            if matches:
                if api_category not in findings:
                    findings[api_category] = {
                        'name': info['name'],
                        'files': [],
                        'patterns_found': [],
                        'valid_reasons': info['reasons'],
                    }
                findings[api_category]['files'].append(str(file_path))
                findings[api_category]['patterns_found'].extend(matches)
    
    return findings


def find_privacy_manifest(project_path: Path) -> Path:
    """Find PrivacyInfo.xcprivacy in the project."""
    for manifest in project_path.rglob('PrivacyInfo.xcprivacy'):
        return manifest
    return None


def parse_privacy_manifest(manifest_path: Path) -> dict:
    """Parse the Privacy Manifest and return declared APIs."""
    try:
        with open(manifest_path, 'rb') as f:
            manifest = plistlib.load(f)
    except Exception as e:
        return {'error': str(e)}
    
    declared_apis = {}
    
    api_types = manifest.get('NSPrivacyAccessedAPITypes', [])
    for api in api_types:
        api_type = api.get('NSPrivacyAccessedAPIType', '')
        reasons = api.get('NSPrivacyAccessedAPITypeReasons', [])
        declared_apis[api_type] = reasons
    
    return {
        'tracking': manifest.get('NSPrivacyTracking', False),
        'tracking_domains': manifest.get('NSPrivacyTrackingDomains', []),
        'collected_data': manifest.get('NSPrivacyCollectedDataTypes', []),
        'declared_apis': declared_apis,
    }


def analyze_project(project_path: Path) -> dict:
    """Analyze an iOS project for Privacy Manifest compliance."""
    results = {
        'project_path': str(project_path),
        'apis_detected': {},
        'manifest_found': False,
        'manifest_path': None,
        'manifest_data': None,
        'issues': [],
        'recommendations': [],
    }
    
    # Scan for API usage
    files = find_project_files(project_path)
    if not files:
        results['issues'].append("No source files found in project")
        return results
    
    all_findings = {}
    for file_path in files:
        findings = scan_file_for_apis(file_path, REQUIRED_REASON_APIS)
        for api_cat, data in findings.items():
            if api_cat not in all_findings:
                all_findings[api_cat] = data
            else:
                all_findings[api_cat]['files'].extend(data['files'])
                all_findings[api_cat]['patterns_found'].extend(data['patterns_found'])
    
    results['apis_detected'] = all_findings
    
    # Find and parse Privacy Manifest
    manifest_path = find_privacy_manifest(project_path)
    if manifest_path:
        results['manifest_found'] = True
        results['manifest_path'] = str(manifest_path)
        results['manifest_data'] = parse_privacy_manifest(manifest_path)
        
        # Check if detected APIs are declared
        declared = results['manifest_data'].get('declared_apis', {})
        for api_cat in all_findings:
            if api_cat not in declared:
                results['issues'].append(
                    f"API '{all_findings[api_cat]['name']}' detected but not declared in Privacy Manifest"
                )
            else:
                # Check if reasons are valid
                declared_reasons = declared[api_cat]
                valid_reasons = all_findings[api_cat]['valid_reasons']
                for reason in declared_reasons:
                    if reason not in valid_reasons:
                        results['issues'].append(
                            f"Invalid reason '{reason}' for {all_findings[api_cat]['name']}. "
                            f"Valid reasons: {', '.join(valid_reasons)}"
                        )
    else:
        if all_findings:
            results['issues'].append("Privacy Manifest (PrivacyInfo.xcprivacy) not found")
            results['recommendations'].append(
                "Create PrivacyInfo.xcprivacy and declare the detected APIs"
            )
    
    return results


def print_report(results: dict) -> None:
    """Print formatted analysis report."""
    
    print("\n" + "=" * 60)
    print("🔐 PRIVACY MANIFEST ANALYSIS REPORT")
    print("=" * 60)
    print(f"\n📁 Project: {results['project_path']}")
    
    # APIs Detected
    if results['apis_detected']:
        print(f"\n📋 Required Reason APIs Detected:")
        for api_cat, data in results['apis_detected'].items():
            unique_files = list(set(data['files']))
            print(f"\n   🔹 {data['name']}")
            print(f"      Category: {api_cat}")
            print(f"      Found in {len(unique_files)} file(s)")
            print(f"      Valid reasons: {', '.join(data['valid_reasons'])}")
    else:
        print(f"\n✅ No Required Reason APIs detected")
    
    # Privacy Manifest Status
    print(f"\n📄 Privacy Manifest:")
    if results['manifest_found']:
        print(f"   ✅ Found: {results['manifest_path']}")
        if results['manifest_data']:
            md = results['manifest_data']
            print(f"   Tracking enabled: {md.get('tracking', False)}")
            print(f"   APIs declared: {len(md.get('declared_apis', {}))}")
            print(f"   Data types declared: {len(md.get('collected_data', []))}")
    else:
        print(f"   ❌ Not found")
    
    # Issues
    if results['issues']:
        print(f"\n⚠️ Issues Found:")
        for issue in results['issues']:
            print(f"   • {issue}")
    
    # Recommendations
    if results['recommendations']:
        print(f"\n💡 Recommendations:")
        for rec in results['recommendations']:
            print(f"   • {rec}")
    
    # Summary
    print("\n" + "-" * 60)
    if results['issues']:
        print("❌ ACTION REQUIRED - Fix issues before submission")
    elif results['apis_detected'] and results['manifest_found']:
        print("✅ Privacy Manifest appears properly configured")
    elif not results['apis_detected']:
        print("✅ No Required Reason APIs detected - Privacy Manifest may not be needed")
    print("-" * 60 + "\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 privacy_manifest_checker.py <path-to-project>")
        print("\nExample:")
        print("  python3 privacy_manifest_checker.py ./MyApp")
        print("  python3 privacy_manifest_checker.py ~/Developer/MyProject")
        sys.exit(1)
    
    project_path = Path(sys.argv[1])
    
    if not project_path.exists():
        print(f"❌ Error: Path not found: {project_path}")
        sys.exit(1)
    
    if not project_path.is_dir():
        print(f"❌ Error: Path is not a directory: {project_path}")
        sys.exit(1)
    
    results = analyze_project(project_path)
    print_report(results)
    
    # Exit with error if issues found
    if results['issues']:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
