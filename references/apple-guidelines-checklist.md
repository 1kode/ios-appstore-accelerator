# Apple App Store Guidelines Checklist

Complete reference for App Store Review Guidelines compliance. Use this to validate apps before submission.

## Table of Contents

1. Safety
2. Performance
3. Business
4. Design
5. Legal

---

## 1. Safety

### 1.1 Objectionable Content
- [ ] No offensive, insensitive, upsetting, or mean-spirited content
- [ ] No realistic violence depiction without purpose
- [ ] No content encouraging harmful behavior
- [ ] Religious/cultural references are respectful

### 1.2 User-Generated Content
If app includes UGC:
- [ ] Content filtering/moderation system in place
- [ ] Mechanism to report offensive content
- [ ] Mechanism to block abusive users
- [ ] Developer contact info visible to users
- [ ] Clear statement that developer doesn't tolerate objectionable content

### 1.3 Kids Category
If targeting children:
- [ ] No links out of app without parental gate
- [ ] No behavioral advertising
- [ ] Privacy practices comply with COPPA/GDPR-K

### 1.4 Physical Harm
- [ ] No content facilitating harm to self or others
- [ ] Medical apps include appropriate disclaimers
- [ ] No encouragement of excessive consumption

### 1.5 Developer Information
- [ ] Accurate contact information in App Store Connect
- [ ] Support URL functional and helpful

---

## 2. Performance

### 2.1 App Completeness
- [ ] App is final, complete version (no "beta" or "demo" labels)
- [ ] No placeholder content
- [ ] All features functional
- [ ] No dead links or empty sections
- [ ] Doesn't crash or freeze

### 2.2 Beta Testing
- [ ] Used TestFlight for beta, not App Store

### 2.3 Accurate Metadata
- [ ] Screenshots show actual app UI
- [ ] Description matches app functionality
- [ ] Name is relevant to app function
- [ ] Keywords are accurate and relevant
- [ ] What's New describes actual changes
- [ ] No mention of other platforms unnecessarily

### 2.4 Hardware Compatibility
- [ ] Works on all declared device types
- [ ] Required device capabilities accurate in Info.plist
- [ ] Graceful handling of missing hardware features

### 2.5 Software Requirements
- [ ] Minimum iOS version appropriate
- [ ] No deprecated APIs that will be removed
- [ ] No private API usage
- [ ] Runs in appropriate architecture (arm64)
- [ ] Uses latest stable Xcode for submission

---

## 3. Business

### 3.1 Payments

#### 3.1.1 In-App Purchase
- [ ] Digital goods/services use IAP (not external payment)
- [ ] Physical goods/services can use external payment
- [ ] No direct links to external purchase flows for digital goods

#### 3.1.2 Subscriptions
- [ ] Clear pricing displayed before purchase
- [ ] Subscription terms explained
- [ ] Easy cancellation path documented
- [ ] Free trial terms clearly stated

#### 3.1.3 Free Apps
- [ ] "Free" apps don't require payment to function
- [ ] No "bait and switch" tactics

### 3.2 Other Business Model Issues
- [ ] No fake reviews solicitation
- [ ] No artificial chart manipulation
- [ ] No incentivized downloads

---

## 4. Design

### 4.1 Copycats
- [ ] Not a clone of existing app
- [ ] Has unique value proposition
- [ ] Original design and branding

### 4.2 Minimum Functionality
- [ ] More than a simple website wrapper
- [ ] Provides meaningful iOS-specific functionality
- [ ] Not just a marketing brochure
- [ ] Has actual utility for users

### 4.3 Spam
- [ ] Not a duplicate of developer's other apps
- [ ] Not a template app with minimal changes
- [ ] Unique and useful contribution to App Store

### 4.4 Extensions
If using extensions:
- [ ] Extension has meaningful functionality
- [ ] Host app provides value beyond enabling extension
- [ ] Clear connection between app and extension

### 4.5 Apple Sites and Services
- [ ] Uses Apple technologies as intended
- [ ] No manipulation of system UI
- [ ] Respects Apple Human Interface Guidelines

### 4.6 Alternate App Icons
- [ ] All icon variants relate to app purpose
- [ ] No misleading icons

### 4.7 HTML5 Games and Apps
- [ ] Code not downloaded or updated post-submission
- [ ] No remote code execution

---

## 5. Legal

### 5.1 Privacy

#### 5.1.1 Data Collection and Storage
- [ ] Privacy policy URL provided and accessible
- [ ] Privacy policy covers all data practices
- [ ] User consent obtained before data collection
- [ ] Data minimization practiced
- [ ] Secure data transmission (HTTPS)
- [ ] Secure data storage

#### 5.1.2 Data Use and Sharing
- [ ] Third-party SDK data practices disclosed
- [ ] User consent for data sharing
- [ ] Privacy Nutrition Labels accurate
- [ ] Privacy Manifest complete (if required)

#### 5.1.3 Health and Health Research
If health-related:
- [ ] HealthKit disclosure accurate
- [ ] Medical disclaimers included
- [ ] Research ethics compliance

#### 5.1.4 Kids
If collecting kids' data:
- [ ] COPPA compliance
- [ ] Parental consent mechanisms
- [ ] No behavioral advertising

#### 5.1.5 Location
If using location:
- [ ] Clear purpose string in Info.plist
- [ ] Only minimum required precision
- [ ] Background location justified

### 5.2 Intellectual Property
- [ ] Own or license all content
- [ ] No trademark infringement
- [ ] No copyright infringement
- [ ] Third-party content properly licensed

### 5.3 Gaming, Gambling, and Lotteries
If applicable:
- [ ] Appropriate age rating
- [ ] Geographic restrictions honored
- [ ] No real-money gambling without license

### 5.4 VPN Apps
If VPN functionality:
- [ ] Clear data practices
- [ ] No enabling illegal activity
- [ ] Developer account in good standing

### 5.5 Developer Code of Conduct
- [ ] Accurate representations in review process
- [ ] No manipulation of reviews
- [ ] Cooperation with Apple review team

---

## Quick Reference: Info.plist Required Keys

```xml
<!-- Always Required -->
<key>CFBundleDisplayName</key>
<key>CFBundleIdentifier</key>
<key>CFBundleVersion</key>
<key>CFBundleShortVersionString</key>
<key>UIRequiredDeviceCapabilities</key>
<key>UISupportedInterfaceOrientations</key>

<!-- If Using Camera -->
<key>NSCameraUsageDescription</key>

<!-- If Using Photo Library -->
<key>NSPhotoLibraryUsageDescription</key>
<key>NSPhotoLibraryAddUsageDescription</key>

<!-- If Using Location -->
<key>NSLocationWhenInUseUsageDescription</key>
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>

<!-- If Using Microphone -->
<key>NSMicrophoneUsageDescription</key>

<!-- If Using Contacts -->
<key>NSContactsUsageDescription</key>

<!-- If Using Calendar -->
<key>NSCalendarsUsageDescription</key>

<!-- If Using Face ID -->
<key>NSFaceIDUsageDescription</key>

<!-- If Using Bluetooth -->
<key>NSBluetoothAlwaysUsageDescription</key>

<!-- If Using Health Data -->
<key>NSHealthShareUsageDescription</key>
<key>NSHealthUpdateUsageDescription</key>
```

---

## Screenshot Requirements Quick Reference

| Device | Portrait | Landscape |
|--------|----------|-----------|
| iPhone 6.7" | 1290×2796 | 2796×1290 |
| iPhone 6.5" | 1284×2778 | 2778×1284 |
| iPhone 5.5" | 1242×2208 | 2208×1242 |
| iPad Pro 12.9" (6th gen) | 2048×2732 | 2732×2048 |
| iPad Pro 12.9" (2nd gen) | 2048×2732 | 2732×2048 |

Minimum: 3 screenshots per device type
Maximum: 10 screenshots per device type
Format: PNG or JPEG, no alpha
