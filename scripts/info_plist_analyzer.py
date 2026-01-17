#!/usr/bin/env python3
"""
Info.plist Analyzer for iOS App Store Submission

Analyzes an Info.plist file and reports on App Store readiness.
Checks for required keys, privacy usage descriptions, and common issues.

Usage:
    python3 info_plist_analyzer.py <path-to-Info.plist>

Exit codes:
    0 - Analysis complete, no critical issues
    1 - Error or critical issues found
"""

import plistlib
import sys
from pathlib import Path


# Required keys for all apps
REQUIRED_KEYS = [
    'CFBundleDisplayName',
    'CFBundleIdentifier', 
    'CFBundleVersion',
    'CFBundleShortVersionString',
    'UILaunchStoryboardName',
]

# Privacy keys and their purposes
PRIVACY_KEYS = {
    'NSCameraUsageDescription': 'Camera access',
    'NSPhotoLibraryUsageDescription': 'Photo library read access',
    'NSPhotoLibraryAddUsageDescription': 'Photo library write access',
    'NSLocationWhenInUseUsageDescription': 'Location (in use)',
    'NSLocationAlwaysAndWhenInUseUsageDescription': 'Location (always)',
    'NSMicrophoneUsageDescription': 'Microphone access',
    'NSContactsUsageDescription': 'Contacts access',
    'NSCalendarsUsageDescription': 'Calendar access',
    'NSFaceIDUsageDescription': 'Face ID',
    'NSBluetoothAlwaysUsageDescription': 'Bluetooth access',
    'NSHealthShareUsageDescription': 'Health data read',
    'NSHealthUpdateUsageDescription': 'Health data write',
    'NSMotionUsageDescription': 'Motion data',
    'NSSpeechRecognitionUsageDescription': 'Speech recognition',
    'NSAppleMusicUsageDescription': 'Apple Music',
    'NSRemindersUsageDescription': 'Reminders',
    'NSHomeKitUsageDescription': 'HomeKit',
    'NSSiriUsageDescription': 'Siri',
    'NSLocalNetworkUsageDescription': 'Local network',
    'NSUserTrackingUsageDescription': 'App tracking (ATT)',
}

# Keys that indicate potential issues
WARNING_KEYS = {
    'UIRequiresFullScreen': 'App requires full screen - ensure this is intentional',
    'UIStatusBarHidden': 'Status bar hidden - may affect user experience',
}


def analyze_plist(plist_path: Path) -> dict:
    """
    Analyze an Info.plist file and return findings.
    
    Args:
        plist_path: Path to Info.plist file
        
    Returns:
        Dictionary with analysis results
    """
    results = {
        'app_info': {},
        'missing_required': [],
        'privacy_permissions': [],
        'warnings': [],
        'issues': [],
    }
    
    try:
        with open(plist_path, 'rb') as f:
            plist = plistlib.load(f)
    except Exception as e:
        results['issues'].append(f"Failed to parse plist: {e}")
        return results
    
    # Extract app info
    results['app_info'] = {
        'name': plist.get('CFBundleDisplayName', plist.get('CFBundleName', 'Unknown')),
        'bundle_id': plist.get('CFBundleIdentifier', 'Unknown'),
        'version': plist.get('CFBundleShortVersionString', 'Unknown'),
        'build': plist.get('CFBundleVersion', 'Unknown'),
        'min_ios': plist.get('MinimumOSVersion', 'Unknown'),
    }
    
    # Check required keys
    for key in REQUIRED_KEYS:
        if key not in plist:
            results['missing_required'].append(key)
    
    # Check privacy keys
    for key, purpose in PRIVACY_KEYS.items():
        if key in plist:
            value = plist[key]
            if value and len(value.strip()) > 10:
                results['privacy_permissions'].append({
                    'key': key,
                    'purpose': purpose,
                    'description': value[:100] + '...' if len(value) > 100 else value,
                    'status': 'OK'
                })
            else:
                results['privacy_permissions'].append({
                    'key': key,
                    'purpose': purpose,
                    'description': value,
                    'status': 'WARNING - Description too short'
                })
                results['warnings'].append(f"{key}: Description may be too short for App Review")
    
    # Check for warnings
    for key, message in WARNING_KEYS.items():
        if key in plist and plist[key]:
            results['warnings'].append(message)
    
    # Check for common issues
    if 'UIApplicationExitsOnSuspend' in plist and plist['UIApplicationExitsOnSuspend']:
        results['issues'].append("UIApplicationExitsOnSuspend is deprecated - remove this key")
    
    # Check device capabilities
    capabilities = plist.get('UIRequiredDeviceCapabilities', [])
    if capabilities:
        results['app_info']['required_capabilities'] = capabilities
    
    # Check supported orientations
    orientations = plist.get('UISupportedInterfaceOrientations', [])
    ipad_orientations = plist.get('UISupportedInterfaceOrientations~ipad', [])
    results['app_info']['orientations'] = {
        'iphone': orientations,
        'ipad': ipad_orientations
    }
    
    return results


def print_report(results: dict) -> None:
    """Print formatted analysis report."""
    
    print("\n" + "=" * 60)
    print("📱 INFO.PLIST ANALYSIS REPORT")
    print("=" * 60)
    
    # App Info
    info = results['app_info']
    print(f"\n📋 App Information:")
    print(f"   Name:      {info.get('name', 'Unknown')}")
    print(f"   Bundle ID: {info.get('bundle_id', 'Unknown')}")
    print(f"   Version:   {info.get('version', 'Unknown')}")
    print(f"   Build:     {info.get('build', 'Unknown')}")
    print(f"   Min iOS:   {info.get('min_ios', 'Unknown')}")
    
    # Missing Required Keys
    if results['missing_required']:
        print(f"\n❌ Missing Required Keys:")
        for key in results['missing_required']:
            print(f"   • {key}")
    else:
        print(f"\n✅ All required keys present")
    
    # Privacy Permissions
    if results['privacy_permissions']:
        print(f"\n🔐 Privacy Permissions Declared:")
        for perm in results['privacy_permissions']:
            status_icon = "✅" if perm['status'] == 'OK' else "⚠️"
            print(f"   {status_icon} {perm['purpose']}")
            print(f"      Key: {perm['key']}")
            print(f"      Description: \"{perm['description']}\"")
    else:
        print(f"\n🔐 No privacy permissions declared")
        print(f"   (This is fine if your app doesn't use protected resources)")
    
    # Warnings
    if results['warnings']:
        print(f"\n⚠️ Warnings:")
        for warning in results['warnings']:
            print(f"   • {warning}")
    
    # Issues
    if results['issues']:
        print(f"\n🚨 Critical Issues:")
        for issue in results['issues']:
            print(f"   • {issue}")
    
    # Summary
    print("\n" + "-" * 60)
    has_issues = bool(results['issues'] or results['missing_required'])
    if has_issues:
        print("❌ ISSUES FOUND - Address before submission")
    elif results['warnings']:
        print("⚠️ WARNINGS - Review before submission")
    else:
        print("✅ NO CRITICAL ISSUES DETECTED")
    print("-" * 60 + "\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 info_plist_analyzer.py <path-to-Info.plist>")
        print("\nExample:")
        print("  python3 info_plist_analyzer.py ./MyApp/Info.plist")
        sys.exit(1)
    
    # Security: Resolve path and validate
    try:
        plist_path = Path(sys.argv[1]).resolve()
    except (ValueError, OSError) as e:
        print(f"❌ Error: Invalid path: {e}")
        sys.exit(1)
    
    # Security: Check file exists and is a file (not directory/symlink to directory)
    if not plist_path.exists():
        print(f"❌ Error: File not found: {plist_path}")
        sys.exit(1)
    
    if not plist_path.is_file():
        print(f"❌ Error: Path is not a file: {plist_path}")
        sys.exit(1)
    
    # Security: Validate file extension
    if not plist_path.suffix == '.plist':
        print(f"⚠️ Warning: File does not have .plist extension")
    
    # Security: Check file size (prevent DoS with huge files)
    max_size = 10 * 1024 * 1024  # 10MB limit
    if plist_path.stat().st_size > max_size:
        print(f"❌ Error: File too large (>{max_size // 1024 // 1024}MB)")
        sys.exit(1)
    
    results = analyze_plist(plist_path)
    print_report(results)
    
    # Exit with error code if critical issues found
    if results['issues'] or results['missing_required']:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
