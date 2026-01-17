# Export Compliance Guide

When submitting to the App Store, you'll be asked about encryption. This guide helps you answer correctly.

---

## The Question

App Store Connect asks:

> "Does your app use encryption?"

**Wrong answer = legal problems or rejection.**

---

## Quick Decision Tree

```
Does your app use ANY encryption?
│
├─► NO encryption at all
│   └─► Answer: "No" ✅
│
└─► YES, uses encryption
    │
    ├─► ONLY uses HTTPS/TLS for network calls?
    │   └─► Answer: "No" ✅ (exempt)
    │
    ├─► ONLY uses iOS built-in encryption (Data Protection, Keychain)?
    │   └─► Answer: "Yes" → Select exemption ✅
    │
    └─► Uses CUSTOM encryption or crypto libraries?
        └─► Answer: "Yes" → May need export documentation ⚠️
```

---

## Common Scenarios

### Scenario 1: Basic App with HTTPS
**Your app:** Makes API calls over HTTPS, stores data locally
**Answer:** "No"
**Why:** HTTPS/TLS is exempt under US export regulations

### Scenario 2: App with User Authentication
**Your app:** User login with password, uses HTTPS
**Answer:** "No"
**Why:** Standard authentication over HTTPS is exempt

### Scenario 3: App using Keychain for Passwords
**Your app:** Stores sensitive data in iOS Keychain
**Answer:** "Yes" → Then select exemption category
**Why:** iOS Keychain uses encryption, but it's exempt

### Scenario 4: App using Firebase
**Your app:** Uses Firebase (Auth, Firestore, Analytics)
**Answer:** "No"
**Why:** Firebase uses standard HTTPS, which is exempt

### Scenario 5: End-to-End Encrypted Messaging
**Your app:** Implements E2E encryption for messages
**Answer:** "Yes" → May need CCATS/ERN documentation
**Why:** Custom encryption implementation

### Scenario 6: VPN or Security App
**Your app:** Implements VPN or custom security protocols
**Answer:** "Yes" → Likely needs documentation
**Why:** Uses encryption as primary function

---

## The Follow-up Questions

If you answer "Yes", App Store Connect asks:

### Question 1: Is it exempt?

> "Does your app qualify for any of the exemptions provided in Category 5, Part 2 of the U.S. Export Administration Regulations?"

**Most apps can answer "Yes" if using:**
- Standard HTTPS/TLS
- iOS encryption APIs
- Common authentication

### Question 2: Documentation

> "Does your app contain, use, or implement cryptography that is classified as mass market under U.S. Export Administration Regulations?"

**For most standard apps:** Answer "Yes"

---

## Exemption Categories (EAR Category 5 Part 2)

| Exemption | Covers | Examples |
|-----------|--------|----------|
| (a) | Authentication | Login systems, password protection |
| (b) | Copy protection | DRM, license validation |
| (c) | Banking/money | Payment processing |
| (d) | Limited to <= 56-bit | Old/weak encryption (rare) |
| (e) | Mass market | Standard HTTPS, common crypto |

**Most apps qualify under (a) or (e).**

---

## When You Need Documentation

You may need to file for a CCATS (Commodity Classification Automated Tracking System) or ERN (Encryption Registration Number) if:

1. **Custom encryption algorithms** - You wrote your own
2. **Strong encryption as primary feature** - E2E messaging, VPN
3. **Government/military applications** - Special handling
4. **Export to embargoed countries** - Cuba, Iran, North Korea, etc.

### How to File

1. **CCATS:** File with BIS (Bureau of Industry and Security)
   - URL: https://www.bis.doc.gov
   - Takes 30 days typically

2. **ERN:** Self-classification registration
   - Simpler process for mass-market products

---

## What 99% of Vibe-Coded Apps Should Answer

If your app:
- Uses HTTPS for API calls ✅
- Uses Firebase, Supabase, or similar ✅
- Stores data in Keychain ✅
- Has user authentication ✅
- Uses Apple's built-in security ✅

**Answer:** "No" to the first question

---

## Red Flags (Consult a Lawyer)

⚠️ Get legal advice if your app:
- Implements custom encryption protocols
- Is a VPN or security tool
- Handles classified information
- Will be used by government agencies
- Targets specific countries with export restrictions

---

## App Store Connect Walkthrough

### Step 1: Export Compliance Screen
When you submit, you'll see:
> "Export Compliance Information"

### Step 2: Initial Question
> "Does your app use encryption?"

For most apps → Select **"No"**

### Step 3: If You Selected Yes
> "Does your app qualify for any exemptions?"

Select **"Yes"** and check applicable boxes:
- ☑️ Authentication
- ☑️ Mass market encryption

### Step 4: Confirmation
> "Have you added the required documentation?"

If exempt → Select **"Yes, my app is exempt"**

---

## Saving Your Answers

**Pro Tip:** In App Store Connect, you can save your export compliance answers so you don't have to answer them every submission.

1. Go to App Store Connect → Your App
2. Features → Encryption
3. Save your answers

---

## Summary

| App Type | First Question | Needs Docs? |
|----------|---------------|-------------|
| Basic app with HTTPS | No | No |
| App with login | No | No |
| Firebase/Supabase app | No | No |
| Uses iOS Keychain | Yes → Exempt | No |
| Custom encryption | Yes | Maybe |
| VPN/Security app | Yes | Likely |

**When in doubt:** The safest answer for simple apps is "No" - HTTPS is not considered "using encryption" in the export compliance context.

---

## Resources

- [Apple Export Compliance Documentation](https://developer.apple.com/documentation/security/complying_with_encryption_export_regulations)
- [BIS Encryption FAQ](https://www.bis.doc.gov/index.php/policy-guidance/encryption)
- [EAR Category 5 Part 2](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-740)
