# In-App Purchase (IAP) Compliance Checklist

Guideline 3.1.1 is a top rejection reason. This checklist ensures your in-app purchases are compliant.

---

## Quick Rules

1. **Digital goods = Apple IAP required** (30% or 15% cut)
2. **Physical goods = External payment OK** (Uber, Amazon, DoorDash)
3. **Services performed in-app = IAP required**
4. **Services performed outside app = External OK** (Airbnb, hiring apps)

---

## What REQUIRES Apple IAP

| Content Type | IAP Required? | Example |
|--------------|---------------|---------|
| Premium features | ✅ Yes | Unlock pro mode |
| Subscriptions | ✅ Yes | Monthly access |
| Virtual currency | ✅ Yes | Coins, gems |
| Consumables | ✅ Yes | Extra lives |
| Digital content | ✅ Yes | E-books, music |
| Ad removal | ✅ Yes | Remove ads purchase |
| Tip jar (digital) | ✅ Yes | Support creator |
| Loot boxes | ✅ Yes | Random rewards |

---

## What Does NOT Require IAP

| Content Type | IAP Required? | Example |
|--------------|---------------|---------|
| Physical products | ❌ No | E-commerce apps |
| Real-world services | ❌ No | Uber, Airbnb |
| Person-to-person services | ❌ No | Tutoring, consulting |
| Tickets (events) | ❌ No | Concert tickets |
| Food delivery | ❌ No | DoorDash, UberEats |
| Professional services | ❌ No | Legal, medical appointments |

---

## Special Cases

### Reader Apps
Apps that let users access previously purchased content (Netflix, Kindle, Spotify) can:
- ✅ Let users access content purchased elsewhere
- ❌ Cannot have "Sign Up" or purchase buttons in app
- ❌ Cannot link to external purchase

### Multi-platform Apps
If users can buy on your website:
- ✅ They can use the purchase in your iOS app
- ❌ You cannot tell them to buy on website
- ❌ You cannot link to purchase page

### Free Trials
- ✅ Can offer free trials through IAP
- ✅ Must clearly state when trial ends
- ✅ Must clearly state post-trial price
- ❌ Cannot auto-upgrade without consent

---

## IAP Types

| Type | Description | Restores? |
|------|-------------|-----------|
| Consumable | Used once, then gone | ❌ No |
| Non-Consumable | Permanent unlock | ✅ Yes |
| Auto-Renewable Subscription | Recurring charge | ✅ Yes |
| Non-Renewing Subscription | One-time subscription | ✅ Yes |

---

## Required UI Elements

### Before Purchase
- [ ] Clear price displayed
- [ ] Clear description of what's included
- [ ] For subscriptions: billing period stated
- [ ] For free trials: trial duration stated
- [ ] Link to Terms of Service
- [ ] Link to Privacy Policy

### For Subscriptions
- [ ] Clear cancellation instructions
- [ ] Statement that payment charged to iTunes
- [ ] Auto-renewal disclosure
- [ ] Management instructions

### Example Disclosure Text
```
• Payment will be charged to your Apple ID account
• Subscription automatically renews unless canceled at least 24 hours before the end of the current period
• Account will be charged for renewal within 24 hours prior to the end of the current period
• Subscriptions may be managed and auto-renewal turned off in Account Settings
• Any unused portion of a free trial will be forfeited if you purchase a subscription
```

---

## Restore Purchases

**Required:** All apps with non-consumables or subscriptions MUST have a "Restore Purchases" button.

### Placement
- Settings screen ✅
- Purchase screen ✅
- Hidden in menu ❌ (must be easily findable)

### Implementation
```swift
// Must implement
SKPaymentQueue.default().restoreCompletedTransactions()
```

### Testing
- [ ] Test restore on new device
- [ ] Test restore with active subscription
- [ ] Test restore with expired subscription

---

## Sandbox Testing Checklist

### Before Submission
- [ ] Tested all IAP products in sandbox
- [ ] Tested purchase flow
- [ ] Tested restore flow
- [ ] Tested cancellation (subscriptions)
- [ ] Tested renewal (subscriptions)
- [ ] Tested upgrade/downgrade (subscriptions)
- [ ] Tested interrupted purchase
- [ ] Tested network failure during purchase

### Sandbox Test Accounts
1. Create in App Store Connect
2. Sign out of real Apple ID on device
3. Launch app and attempt purchase
4. Sign in with sandbox account when prompted

---

## Common Rejection Reasons

### 3.1.1 - In-App Purchase

**"Your app uses a mechanism other than in-app purchase to unlock features."**

Fix: Remove external payment, use StoreKit

**"The app does not include a restore mechanism."**

Fix: Add "Restore Purchases" button

**"Subscription terms are not clear."**

Fix: Add required disclosure text

### 3.1.2 - Subscriptions

**"Subscription management instructions not included."**

Fix: Add instructions to cancel/manage subscription

**"Free trial terms not clearly stated."**

Fix: State trial duration and post-trial price

---

## StoreKit 2 vs StoreKit 1

### StoreKit 2 (Recommended)
- Modern Swift API
- Async/await
- Automatic transaction handling
- Better testing tools

### StoreKit 1 (Legacy)
- Objective-C based
- Callback-based
- Still supported
- More documentation

**Recommendation:** Use StoreKit 2 for new apps

---

## Server-Side Validation

For subscriptions and valuable purchases:

1. **Never trust client-side only**
2. **Validate receipts on your server**
3. **Use App Store Server API**
4. **Handle subscription notifications**

### App Store Server Notifications
- Configure in App Store Connect
- Receive real-time updates on:
  - New subscriptions
  - Renewals
  - Cancellations
  - Refunds

---

## Pricing Best Practices

### Price Tiers
- Use Apple's price tiers (not custom prices)
- Apple handles currency conversion
- Prices vary by country

### Free Trials
- 3, 7, or 14 days most common
- Longer trials = higher conversion but more abuse
- Always require payment method upfront

### Promotional Offers
- Introductory offers (new subscribers)
- Promotional offers (lapsed subscribers)
- Offer codes (marketing)

---

## Pre-Submission Checklist

### App Store Connect
- [ ] All IAP products created
- [ ] Products in "Ready to Submit" state
- [ ] Screenshots uploaded for IAP (if required)
- [ ] Review notes explain how to test IAP

### In-App
- [ ] All prices displayed correctly
- [ ] Purchase flow works in sandbox
- [ ] Restore purchases works
- [ ] Subscription terms displayed
- [ ] Links to Privacy Policy and Terms
- [ ] Error handling for failed purchases

### Code
- [ ] Using StoreKit (not external SDK for payments)
- [ ] Receipt validation implemented
- [ ] Restore functionality implemented
- [ ] Transaction processing completed properly

---

## Review Notes Template

If your app has IAP, include this in review notes:

```
IN-APP PURCHASE TESTING:

Our app offers the following in-app purchases:
- [Product Name] - [Price] - [Description]

To test:
1. [Steps to reach purchase screen]
2. [Any special conditions]

All purchases use Apple's In-App Purchase system via StoreKit 2.
Restore Purchases can be found in Settings > Account > Restore Purchases.

[If subscription:]
Subscription terms are displayed before purchase, including:
- Billing period
- Auto-renewal terms  
- Cancellation instructions
```

---

## Resources

- [App Store Review Guidelines 3.1](https://developer.apple.com/app-store/review/guidelines/#in-app-purchase)
- [StoreKit 2 Documentation](https://developer.apple.com/storekit/)
- [Offering Subscriptions](https://developer.apple.com/app-store/subscriptions/)
- [Receipt Validation](https://developer.apple.com/documentation/storekit/in-app_purchase/validating_receipts_with_the_app_store)
