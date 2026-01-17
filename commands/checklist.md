---
description: Generate a comprehensive App Store submission checklist by analyzing the iOS project. Checks assets, Info.plist, privacy requirements, and common rejection risks.
---

# App Store Checklist

Generate a complete App Store submission checklist for this iOS project.

## Execution Steps

1. **Locate the Xcode project** - Find `.xcodeproj` or `.xcworkspace` in the current directory or subdirectories

2. **Analyze Info.plist** - Run `scripts/info_plist_analyzer.py` if Info.plist exists:
   ```bash
   python3 scripts/info_plist_analyzer.py <path-to-Info.plist>
   ```

3. **Check for required assets**:
   - App icon (1024×1024 PNG)
   - Launch screen or storyboard
   - Screenshots folder (if prepared)

4. **Scan for privacy indicators**:
   - Camera/photo library usage
   - Location services
   - User data collection
   - Third-party SDKs (check Podfile, Package.swift, or SPM)

5. **Generate checklist report** using the template below

## Output Template

```markdown
# 📱 App Store Submission Checklist
**Project**: [Project Name]
**Generated**: [Date]

---

## ✅ Required Items

### App Information
- [ ] App Name (max 30 characters): _______________
- [ ] Subtitle (max 30 characters): _______________
- [ ] Primary Category: _______________
- [ ] Secondary Category (optional): _______________

### Legal & Privacy
- [ ] Privacy Policy URL: _______________
- [ ] Support URL: _______________
- [ ] Marketing URL (optional): _______________

### Assets
- [ ] App Icon (1024×1024 PNG, no alpha)
- [ ] Screenshots for target devices:
  - [ ] iPhone 6.7" (1290×2796 or 2796×1290)
  - [ ] iPhone 6.5" (1284×2778 or 2778×1284)
  - [ ] iPad Pro 12.9" (2048×2732 or 2732×2048) - if iPad supported
- [ ] App Preview videos (optional)

### Technical
- [ ] Info.plist validated
- [ ] Bundle ID matches App Store Connect
- [ ] Version number set correctly
- [ ] Build number incremented
- [ ] Deployment target appropriate

---

## 🔐 Privacy Compliance

### Privacy Manifest Required?
[YES/NO based on API usage analysis]

If YES, ensure `PrivacyInfo.xcprivacy` includes:
- [ ] Required reason APIs declared
- [ ] Tracking domains listed (if applicable)
- [ ] Privacy nutrition labels match manifest

### Data Collection Declaration
Check all that apply for App Store Connect privacy labels:
- [ ] Contact Info
- [ ] Health & Fitness
- [ ] Financial Info
- [ ] Location
- [ ] Sensitive Info
- [ ] Contacts
- [ ] User Content
- [ ] Browsing History
- [ ] Search History
- [ ] Identifiers
- [ ] Usage Data
- [ ] Diagnostics
- [ ] Other Data

---

## ⚠️ Rejection Risk Assessment

### High Risk Items
[List any detected issues that commonly cause rejection]

### Medium Risk Items
[List potential concerns]

### Recommendations
[Specific actions to reduce rejection risk]

---

## 📋 Pre-Submission Checklist

- [ ] Tested on physical device
- [ ] All features work as described in metadata
- [ ] No placeholder content (Lorem ipsum, test data)
- [ ] No references to other platforms (Android, etc.)
- [ ] Demo account credentials prepared (if login required)
- [ ] Review notes written for complex features
- [ ] Export compliance documentation ready (if using encryption)

---

## Next Steps

1. Run `/appstore:privacy-policy` to generate privacy policy
2. Run `/appstore:metadata` to create App Store listing
3. Run `/appstore:review-prepare` for final validation
```

## Handling Missing Information

If project cannot be analyzed:
- Provide the checklist template with blank fields
- Note which automated checks couldn't be performed
- Recommend manual verification steps

$ARGUMENTS
