# Privacy Manifest Guide (PrivacyInfo.xcprivacy)

Apple requires a Privacy Manifest file for apps that use certain "Required Reason APIs" or include specific third-party SDKs. This guide explains when you need one and how to create it.

---

## Table of Contents

1. Do I Need a Privacy Manifest?
2. Required Reason APIs
3. Creating the Privacy Manifest
4. Third-Party SDK Requirements
5. Validation and Testing

---

## 1. Do I Need a Privacy Manifest?

**Yes, if your app:**
- Uses any Required Reason APIs (see list below)
- Includes third-party SDKs that Apple has flagged
- Collects any data for tracking purposes

**Starting Spring 2024**, App Store Connect rejects apps using Required Reason APIs without a valid Privacy Manifest.

---

## 2. Required Reason APIs

These APIs require declared reasons in your Privacy Manifest:

### File Timestamp APIs
```
NSFileCreationDate
NSFileModificationDate
NSURLContentModificationDateKey
NSURLCreationDateKey
getattrlist()
stat()
fstat()
```

**Approved Reasons:**
- `DDA9.1` - Display to user
- `C617.1` - Access within app container
- `3B52.1` - Access with user permission
- `0A2A.1` - Third-party SDK access

### System Boot Time APIs
```
systemUptime
mach_absolute_time()
```

**Approved Reasons:**
- `35F9.1` - Measure elapsed time
- `8FFB.1` - Calculate absolute timestamps
- `3D61.1` - Include in user-facing timestamps

### Disk Space APIs
```
volumeAvailableCapacityKey
volumeAvailableCapacityForImportantUsageKey
volumeAvailableCapacityForOpportunisticUsageKey
volumeTotalCapacityKey
statfs()
statvfs()
```

**Approved Reasons:**
- `85F4.1` - Display to user
- `E174.1` - Check before writing files
- `7D9E.1` - App functionality management

### Active Keyboard APIs
```
activeInputModes
```

**Approved Reasons:**
- `3EC4.1` - Customize text entry
- `54BD.1` - Display correct keyboard

### User Defaults APIs
```
UserDefaults
NSUserDefaults
```

**Approved Reasons:**
- `CA92.1` - Access within app container
- `1C8F.1` - Access with user permission
- `C56D.1` - Third-party SDK access

---

## 3. Creating the Privacy Manifest

### Step 1: Create the File

In Xcode:
1. File → New → File
2. Select "App Privacy" under Resource
3. Name it `PrivacyInfo.xcprivacy`
4. Add to your main app target

### Step 2: Basic Structure

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <!-- Privacy Tracking -->
    <key>NSPrivacyTracking</key>
    <false/>
    
    <!-- Tracking Domains (if tracking is true) -->
    <key>NSPrivacyTrackingDomains</key>
    <array/>
    
    <!-- Collected Data Types -->
    <key>NSPrivacyCollectedDataTypes</key>
    <array>
        <!-- Add data type dictionaries here -->
    </array>
    
    <!-- Required Reason APIs -->
    <key>NSPrivacyAccessedAPITypes</key>
    <array>
        <!-- Add API reason dictionaries here -->
    </array>
</dict>
</plist>
```

### Step 3: Declare API Usage

For each Required Reason API you use:

```xml
<dict>
    <key>NSPrivacyAccessedAPIType</key>
    <string>NSPrivacyAccessedAPICategoryUserDefaults</string>
    <key>NSPrivacyAccessedAPITypeReasons</key>
    <array>
        <string>CA92.1</string>
    </array>
</dict>
```

### Step 4: Declare Collected Data

For each data type collected:

```xml
<dict>
    <key>NSPrivacyCollectedDataType</key>
    <string>NSPrivacyCollectedDataTypeEmailAddress</string>
    <key>NSPrivacyCollectedDataTypeLinked</key>
    <true/>
    <key>NSPrivacyCollectedDataTypeTracking</key>
    <false/>
    <key>NSPrivacyCollectedDataTypePurposes</key>
    <array>
        <string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>
    </array>
</dict>
```

---

## 4. Complete Example

App that uses UserDefaults and collects email for accounts:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>NSPrivacyTracking</key>
    <false/>
    
    <key>NSPrivacyTrackingDomains</key>
    <array/>
    
    <key>NSPrivacyCollectedDataTypes</key>
    <array>
        <dict>
            <key>NSPrivacyCollectedDataType</key>
            <string>NSPrivacyCollectedDataTypeEmailAddress</string>
            <key>NSPrivacyCollectedDataTypeLinked</key>
            <true/>
            <key>NSPrivacyCollectedDataTypeTracking</key>
            <false/>
            <key>NSPrivacyCollectedDataTypePurposes</key>
            <array>
                <string>NSPrivacyCollectedDataTypePurposeAppFunctionality</string>
            </array>
        </dict>
    </array>
    
    <key>NSPrivacyAccessedAPITypes</key>
    <array>
        <dict>
            <key>NSPrivacyAccessedAPIType</key>
            <string>NSPrivacyAccessedAPICategoryUserDefaults</string>
            <key>NSPrivacyAccessedAPITypeReasons</key>
            <array>
                <string>CA92.1</string>
            </array>
        </dict>
    </array>
</dict>
</plist>
```

---

## 5. Third-Party SDK Requirements

Apple maintains a list of SDKs that must provide their own Privacy Manifests. If you use these SDKs, ensure they are updated:

### Major SDKs Requiring Manifests
- Firebase (all products)
- Facebook SDK
- Google Analytics
- Amplitude
- Mixpanel
- AppsFlyer
- Adjust
- Branch
- Segment

### How to Check
1. Update SDKs to latest versions
2. Check SDK documentation for Privacy Manifest info
3. When archiving, Xcode will show aggregated privacy report

---

## 6. Validation and Testing

### In Xcode
1. Archive your app
2. In Organizer, select archive
3. Click "Generate Privacy Report"
4. Review the aggregated manifest

### Common Errors

**"Missing Required Reason"**
- Add the appropriate reason code for the API

**"Invalid Reason Code"**
- Check reason code matches Apple's documentation

**"SDK Missing Manifest"**
- Update third-party SDK to version with manifest

---

## Quick Reference: API Categories

| Category | Key |
|----------|-----|
| File Timestamp | `NSPrivacyAccessedAPICategoryFileTimestamp` |
| System Boot Time | `NSPrivacyAccessedAPICategorySystemBootTime` |
| Disk Space | `NSPrivacyAccessedAPICategoryDiskSpace` |
| Active Keyboards | `NSPrivacyAccessedAPICategoryActiveKeyboards` |
| User Defaults | `NSPrivacyAccessedAPICategoryUserDefaults` |

## Quick Reference: Data Types

| Type | Key |
|------|-----|
| Name | `NSPrivacyCollectedDataTypeName` |
| Email | `NSPrivacyCollectedDataTypeEmailAddress` |
| Phone | `NSPrivacyCollectedDataTypePhoneNumber` |
| Location | `NSPrivacyCollectedDataTypePreciseLocation` |
| Photos | `NSPrivacyCollectedDataTypePhotosorVideos` |
| Device ID | `NSPrivacyCollectedDataTypeDeviceID` |
| Crash Data | `NSPrivacyCollectedDataTypeCrashData` |
| Performance | `NSPrivacyCollectedDataTypePerformanceData` |

---

## Resources

- [Apple: Privacy Manifest Files](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files)
- [Apple: Required Reason APIs](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api)
- [WWDC23: Get started with privacy manifests](https://developer.apple.com/videos/play/wwdc2023/10060/)
