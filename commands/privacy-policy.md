---
description: Generate a privacy policy for iOS app based on data practices analysis. Scans project for data collection patterns, third-party SDKs, and creates a compliant privacy policy ready for hosting.
---

# Privacy Policy Generator

Generate a comprehensive privacy policy by analyzing the app's data practices.

## Execution Steps

1. **Analyze the project for data collection patterns**:
   - Search for analytics SDKs (Firebase, Amplitude, Mixpanel, etc.)
   - Check for authentication (user accounts, login)
   - Look for network requests patterns
   - Identify third-party SDKs in Podfile, Package.swift, or SPM
   - Review Info.plist for privacy permission keys

2. **Run the privacy policy generator script**:
   ```bash
   python3 scripts/privacy_policy_generator.py \
     --app-name "APP_NAME" \
     --company "COMPANY_NAME" \
     --email "CONTACT_EMAIL" \
     --website "WEBSITE_URL" \
     --data-types "DATA_TYPES_COMMA_SEPARATED"
   ```

3. **Review and customize the output**:
   - Verify all data practices are covered
   - Add any app-specific disclosures
   - Update contact information

4. **Provide hosting instructions**:
   - Recommend hosting options (GitHub Pages, Notion, website)
   - Explain URL requirements for App Store Connect

## Data Collection Detection Patterns

### Analytics SDKs
```
Firebase|Analytics|Amplitude|Mixpanel|Segment|Flurry|AppsFlyer|Adjust|Branch
```

### Authentication Indicators
```
Auth|Login|SignIn|SignUp|User|Account|Firebase/Auth|Cognito|Auth0
```

### Network/API Indicators
```
URLSession|Alamofire|API|fetch|request|endpoint|backend
```

### Payment Indicators
```
StoreKit|IAP|Purchase|Stripe|Payment|Subscription
```

### Location Indicators
```
CLLocation|CoreLocation|MapKit|location
```

### Health/Fitness Indicators
```
HealthKit|HKHealthStore|workout|health
```

## Data Types Reference

When analyzing, categorize into Apple's Privacy Nutrition Label categories:

| Category | Examples |
|----------|----------|
| Contact Info | Name, email, phone, address |
| Health & Fitness | Health data, fitness data |
| Financial Info | Payment info, credit score |
| Location | Precise location, coarse location |
| Sensitive Info | Racial/ethnic data, biometric data |
| Contacts | Address book contacts |
| User Content | Photos, videos, documents, notes |
| Browsing History | Web browsing history |
| Search History | In-app search history |
| Identifiers | User ID, device ID, IDFA |
| Usage Data | App interactions, analytics |
| Diagnostics | Crash logs, performance data |

## Output Format

The generator creates two files:
1. `privacy-policy.md` - Markdown version for GitHub/Notion
2. `privacy-policy.html` - HTML version for web hosting

## Hosting Recommendations

### Option 1: GitHub Pages (Free)
1. Create public repo or use existing
2. Add privacy-policy.html to repo
3. Enable GitHub Pages in settings
4. URL: `https://username.github.io/repo/privacy-policy.html`

### Option 2: Notion (Free)
1. Create new Notion page
2. Paste Markdown content
3. Share page publicly
4. URL: Notion's public share URL

### Option 3: Your Website
1. Upload HTML to your hosting
2. URL: `https://yoursite.com/privacy`

### Requirements
- URL must be publicly accessible (no login)
- URL must be HTTPS
- Page must be accessible at time of review

## Privacy Manifest Reminder

If your app uses Required Reason APIs, you also need a Privacy Manifest (`PrivacyInfo.xcprivacy`). See `references/privacy-manifest-guide.md` for details.

$ARGUMENTS
