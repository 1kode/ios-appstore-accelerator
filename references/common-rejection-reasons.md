# Common App Store Rejection Reasons

Top 10 rejection reasons with specific fixes. Reference when app is rejected or during pre-submission review.

---

## 1. Guideline 2.1 - App Completeness (Crashes & Bugs)

**What triggers it:**
- App crashes on launch or during normal use
- Features don't work as described
- Buttons lead nowhere
- Infinite loading states
- Memory leaks causing termination

**How to fix:**
1. Test on physical device (not just simulator)
2. Test all user flows end-to-end
3. Test on oldest supported iOS version
4. Test with poor network connectivity
5. Use Xcode Instruments for memory profiling
6. Check crash logs in Xcode Organizer

**Example rejection:**
> "We discovered one or more bugs in your app when reviewed on iPhone running iOS 17.2 on Wi-Fi. The app crashed when we tapped the 'Save' button."

**Response template:**
> "We have identified and fixed the crash. The issue was [root cause]. We have added error handling for [scenario] and tested on [devices/iOS versions]. Please re-review."

---

## 2. Guideline 2.3 - Accurate Metadata

**What triggers it:**
- Screenshots don't match actual app
- Description promises features that don't exist
- App name is misleading
- Keywords are irrelevant or manipulative
- "What's New" doesn't describe actual changes
- References to other platforms ("Also on Android!")

**How to fix:**
1. Take fresh screenshots from latest build
2. Audit description against actual features
3. Remove platform references
4. Make keywords relevant to actual functionality
5. Write specific release notes

**Example rejection:**
> "The screenshots do not sufficiently reflect the app in use. We noticed the screenshots display features not present in the app."

**Response template:**
> "We have updated the screenshots to accurately reflect the current app functionality. All screenshots were captured from the latest build."

---

## 3. Guideline 5.1.1 - Data Collection and Storage

**What triggers it:**
- Missing privacy policy URL
- Privacy policy doesn't cover all data practices
- Collecting data without consent
- Privacy Nutrition Labels don't match actual collection
- Missing Privacy Manifest for required APIs

**How to fix:**
1. Create comprehensive privacy policy (use `/appstore:privacy-policy`)
2. Host privacy policy at stable URL
3. Audit all data collection in app
4. Update Privacy Nutrition Labels in App Store Connect
5. Add Privacy Manifest if using required-reason APIs

**Example rejection:**
> "Your app collects user data but does not have a privacy policy URL."

**Response template:**
> "We have added a privacy policy URL at [URL]. The policy covers all data collection practices including [list data types]."

---

## 4. Guideline 4.2 - Minimum Functionality

**What triggers it:**
- App is essentially a website wrapper
- Single-function apps that could be a website
- Apps that are glorified RSS readers
- Marketing brochure apps
- Apps with no real utility

**How to fix:**
1. Add native iOS features (notifications, widgets, Siri)
2. Implement offline functionality
3. Add features that justify native app
4. Use device capabilities (camera, sensors, etc.)
5. Consider if app should be a web app instead

**Example rejection:**
> "Your app is limited to a web experience and does not provide enough native iOS functionality."

**Response template:**
> "We have enhanced the app with native iOS functionality including [features]. The app now provides value beyond what's available in a web browser."

---

## 5. Guideline 2.5.1 - Software Requirements (Deprecated APIs)

**What triggers it:**
- Using APIs marked for deprecation
- UIWebView (deprecated since iOS 12)
- OpenGL ES (deprecated, use Metal)
- AddressBook framework (use Contacts)
- Using private APIs

**How to fix:**
1. Run `grep -r "UIWebView" .` to find usage
2. Replace UIWebView with WKWebView
3. Update third-party SDKs to latest versions
4. Check for deprecation warnings in Xcode
5. Remove any private API usage

**Example rejection:**
> "We identified one or more issues with your app. ITMS-90809: Deprecated API Usage - App updates must not use UIWebView."

**Response template:**
> "We have removed all UIWebView usage and migrated to WKWebView. We have also updated all third-party SDKs to their latest versions."

---

## 6. Guideline 3.1.1 - In-App Purchase

**What triggers it:**
- Digital goods purchased outside IAP
- Links to external payment for digital content
- "Unlocking" features without IAP
- Subscription without using StoreKit

**How to fix:**
1. Use StoreKit for all digital purchases
2. Remove external payment links
3. Implement proper IAP restore functionality
4. Physical goods can use external payment
5. "Reader" apps have limited exemptions

**Example rejection:**
> "Your app uses a mechanism other than the in-app purchase API to unlock features."

**Response template:**
> "We have implemented in-app purchase for all digital content using StoreKit 2. External payment links have been removed."

---

## 7. Guideline 4.3 - Spam

**What triggers it:**
- App is duplicate of developer's other apps
- Template app with minimal customization
- Multiple apps that should be one app
- Apps created from app generators without value

**How to fix:**
1. Consolidate similar apps into one
2. Add unique, meaningful features
3. Differentiate from other apps in catalog
4. Remove redundant apps from App Store

**Example rejection:**
> "Your app duplicates the content and functionality of other apps you have submitted."

**Response template:**
> "We have differentiated this app by [unique features]. Alternatively, we will remove [duplicate app] from the App Store."

---

## 8. Guideline 1.2 - User Generated Content

**What triggers it:**
- UGC without moderation
- No way to report offensive content
- No way to block users
- Missing contact information

**How to fix:**
1. Implement content reporting
2. Add user blocking functionality
3. Display developer contact info
4. Implement content moderation (automated or manual)
5. Add terms of service with content guidelines

**Example rejection:**
> "Your app includes user-generated content but does not have all the required features."

**Response template:**
> "We have implemented content reporting at [location], user blocking at [location], and added developer contact information. Our moderation policy is available at [URL]."

---

## 9. Guideline 5.1.2 - Data Use and Sharing

**What triggers it:**
- Third-party SDKs not disclosed
- Data sharing without consent
- Tracking without ATT prompt
- Privacy Manifest missing SDK info

**How to fix:**
1. Audit all third-party SDKs
2. Update Privacy Nutrition Labels
3. Implement ATT prompt for tracking
4. Add required SDK info to Privacy Manifest
5. Get user consent before sharing data

**Example rejection:**
> "Your app uses third-party SDKs that collect user data, but you have not disclosed this in your privacy information."

**Response template:**
> "We have updated our Privacy Nutrition Labels and Privacy Manifest to include all third-party SDK data practices including [SDKs]."

---

## 10. Guideline 4.0 - Design (Copycat)

**What triggers it:**
- App looks like existing popular app
- Uses similar name/icon to established app
- Mimics Apple's own app design
- No original value proposition

**How to fix:**
1. Redesign to be distinctive
2. Choose unique name and icon
3. Focus on what makes your app different
4. Don't copy other apps' UI directly

**Example rejection:**
> "Your app appears to be a copy of [existing app] and does not provide unique value."

**Response template:**
> "We have redesigned the app with unique branding and UI. Our app differentiates by [unique features]."

---

## Resolution Center Best Practices

1. **Read carefully** - Understand exactly what triggered rejection
2. **Be specific** - Detail exactly what you changed
3. **Be professional** - Reviewers are human, be respectful
4. **Provide evidence** - Screenshots, videos if helpful
5. **Ask questions** - If unclear, ask for clarification
6. **Request call** - For complex issues, request phone review

## Appeal Process

If you believe rejection is incorrect:
1. Reply in Resolution Center with explanation
2. Reference specific guideline interpretation
3. Provide documentation/precedent if available
4. Request App Review Board appeal if needed

Average response time: 24-48 hours
