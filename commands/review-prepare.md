---
description: Run a comprehensive pre-flight check before App Store submission. Validates all requirements, assets, metadata, and identifies potential rejection risks. Use this as the final step before clicking Submit in App Store Connect.
---

# Pre-Submission Review Preparation

Final validation before submitting to App Store. This command runs all checks and produces a go/no-go recommendation.

## Execution Steps

1. **Run all validation scripts**:
   ```bash
   # Validate Info.plist
   python3 scripts/info_plist_analyzer.py <path-to-Info.plist>
   
   # Check Privacy Manifest requirements
   python3 scripts/privacy_manifest_checker.py <path-to-project>
   
   # Validate screenshots
   python3 scripts/screenshot_validator.py <path-to-screenshots>
   ```

2. **Verify App Store Connect readiness**:
   - All required fields populated
   - Build uploaded and processed
   - Screenshots uploaded for all required devices
   - Privacy questionnaire completed

3. **Review rejection risk factors**:
   - Cross-reference with `references/common-rejection-reasons.md`
   - Check for guideline-specific issues

4. **Generate pre-flight report**

## Output Template

```markdown
# 🚀 PRE-SUBMISSION REVIEW REPORT
**App:** [APP NAME]
**Version:** [VERSION]
**Build:** [BUILD NUMBER]
**Date:** [DATE]

---

## ✈️ PRE-FLIGHT STATUS: [READY ✅ / NOT READY ❌ / CAUTION ⚠️]

---

## 📋 CHECKLIST SUMMARY

### Technical Requirements
| Item | Status | Notes |
|------|--------|-------|
| Info.plist valid | ✅/❌ | [details] |
| Bundle ID matches ASC | ✅/❌ | [details] |
| Version/Build correct | ✅/❌ | [details] |
| Privacy Manifest | ✅/❌/N/A | [details] |
| No deprecated APIs | ✅/❌ | [details] |
| Tested on device | ✅/❌ | [manual check] |

### App Store Connect
| Item | Status | Notes |
|------|--------|-------|
| App name set | ✅/❌ | [value] |
| Subtitle set | ✅/❌ | [value] |
| Description complete | ✅/❌ | [char count] |
| Keywords set | ✅/❌ | [char count] |
| Privacy Policy URL | ✅/❌ | [URL] |
| Support URL | ✅/❌ | [URL] |
| Category selected | ✅/❌ | [category] |
| Age rating complete | ✅/❌ | [rating] |
| Pricing set | ✅/❌ | [price] |

### Visual Assets
| Item | Status | Notes |
|------|--------|-------|
| App icon (1024×1024) | ✅/❌ | [details] |
| iPhone 6.7" screenshots | ✅/❌ | [count] |
| iPhone 6.5" screenshots | ✅/❌ | [count] |
| iPad screenshots | ✅/❌/N/A | [count] |
| App preview video | ✅/❌/N/A | [duration] |

### Privacy & Legal
| Item | Status | Notes |
|------|--------|-------|
| Privacy Policy live | ✅/❌ | [accessible?] |
| Privacy labels accurate | ✅/❌ | [manual check] |
| Terms of Service | ✅/❌/N/A | [if required] |
| EULA | ✅/❌/N/A | [if custom] |

---

## ⚠️ REJECTION RISK ASSESSMENT

### High Risk Issues
[List any critical issues that will likely cause rejection]

### Medium Risk Issues  
[List issues that may cause rejection]

### Low Risk / Warnings
[List minor issues to be aware of]

---

## 📝 REVIEW NOTES RECOMMENDATION

If your app has features that may not be obvious to reviewers, prepare notes:

```
[Suggested review notes based on app analysis]

Demo Account (if login required):
- Username: [provide]
- Password: [provide]

Special Instructions:
- [Any special steps to access features]
- [Hardware requirements if any]
- [Location/region requirements if any]
```

---

## 🔒 EXPORT COMPLIANCE

Does your app use encryption?

- [ ] App uses HTTPS only (standard) → Select "No" in ASC
- [ ] App uses custom encryption → May need export compliance docs
- [ ] App is exempt under EAR → Select appropriate exemption

**Note:** Most apps using only HTTPS can select "No" for export compliance.

---

## ⏱️ EXPECTED REVIEW TIME

- **Standard review:** 24-48 hours (typical)
- **First submission:** May take longer (up to 7 days)
- **Expedited review:** Available for critical issues (request via ASC)

---

## ✅ FINAL CHECKLIST

Before clicking Submit:

- [ ] All status items above are ✅ or N/A
- [ ] Tested final build on physical device
- [ ] All placeholder content removed
- [ ] No debug/test code in production build
- [ ] Analytics/crash reporting configured for production
- [ ] Push notification certificates valid (if applicable)
- [ ] In-app purchases tested in sandbox (if applicable)
- [ ] Subscriptions properly configured (if applicable)
- [ ] Review notes prepared (if needed)
- [ ] Team notified of pending submission

---

## 📞 IF REJECTED

1. Don't panic - rejections are common and fixable
2. Read the rejection reason carefully in Resolution Center
3. Reference `references/common-rejection-reasons.md`
4. Fix the specific issue cited
5. Reply with clear explanation of what changed
6. Resubmit

---

## GO/NO-GO RECOMMENDATION

**[RECOMMENDATION]**

[Explanation of recommendation and any final notes]
```

## Validation Checks Detail

### Info.plist Checks
- CFBundleIdentifier matches App Store Connect
- CFBundleShortVersionString is valid semver
- CFBundleVersion is incremented from last submission
- All required usage descriptions present and detailed
- UIRequiredDeviceCapabilities appropriate
- LSRequiresIPhoneOS is true

### Privacy Checks
- Privacy Policy URL is publicly accessible (test with curl/wget)
- Privacy Manifest exists if Required Reason APIs detected
- Privacy Nutrition Labels in ASC match actual data collection

### Asset Checks
- App icon is exactly 1024×1024 PNG with no alpha
- Minimum 3 screenshots per required device size
- Screenshots match app's current UI
- No placeholder or Lorem Ipsum text visible

### Functionality Checks (Manual)
- App launches without crash
- All advertised features work
- No dead links or empty states
- Network errors handled gracefully
- Login/logout flow works (if applicable)
- Purchases complete successfully (if applicable)

## Common Last-Minute Issues

1. **Wrong build uploaded** - Always verify build number in ASC
2. **Privacy Policy 404** - Test URL is accessible
3. **Screenshots outdated** - Retake from current build
4. **Debug code left in** - Check for test flags, console logs
5. **Missing usage descriptions** - iOS will crash without them
6. **Expired certificates** - Check push notification certs

$ARGUMENTS
