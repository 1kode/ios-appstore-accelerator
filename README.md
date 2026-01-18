# iOS App Store Accelerator

A Claude Code plugin that guides vibe coders through iOS App Store submission. Built for developers who build apps with Lovable, Vibecode, Bolt, or Claude Code but need help navigating Apple's submission process.

## 🚀 Quick Start

```bash
# Add the plugin
/plugin marketplace add 1Kode/ios-appstore-accelerator

# Install the plugin
/plugin install ios-appstore-accelerator
```
## 📖 How to Use

### Option 1: With Claude Code (Recommended)

If you have Claude Code CLI installed:
```bash
# Clone the plugin
git clone https://github.com/1Kode/ios-appstore-accelerator.git

# Go to your iOS project
cd your-ios-project

# Install the plugin
/plugin install ../ios-appstore-accelerator

# Run commands
/appstore:checklist
/appstore:privacy-policy
/appstore:metadata
/appstore:review-prepare
```

### Option 2: Run Scripts Directly

Works without Claude Code. Just need Python 3.8+
```bash
# Clone the repo
git clone https://github.com/1Kode/ios-appstore-accelerator.git
cd ios-appstore-accelerator/scripts

# Analyze your Info.plist
python3 info_plist_analyzer.py /path/to/your/Info.plist

# Check your screenshots
python3 screenshot_validator.py /path/to/screenshots/

# Validate your app icon
python3 app_icon_validator.py /path/to/AppIcon.png

# Generate a privacy policy
python3 privacy_policy_generator.py --app-name "YourApp" --company "Your Company" --email "privacy@yourapp.com"

# Check for Required Reason APIs
python3 privacy_manifest_checker.py /path/to/your/project/
```

### Option 3: Just Read the Guides

All the reference docs work standalone:

- `references/common-rejection-reasons.md` - Top 10 rejections and how to fix them
- `references/apple-guidelines-checklist.md` - Full compliance checklist
- `references/privacy-manifest-guide.md` - Privacy Manifest requirements
- `references/iap-compliance-checklist.md` - In-App Purchase rules
- `references/export-compliance-guide.md` - Encryption export questions
- `references/metadata-best-practices.md` - ASO optimization tips

## 📋 Commands

| Command | Description |
|---------|-------------|
| `/appstore:checklist` | Generate comprehensive compliance checklist |
| `/appstore:privacy-policy` | Auto-generate privacy policy from app analysis |
| `/appstore:metadata` | Create optimized App Store listing content |
| `/appstore:review-prepare` | Final pre-submission validation |

## 🛠️ Scripts

The plugin includes standalone Python scripts you can run directly:

```bash
# Analyze Info.plist for issues
python3 scripts/info_plist_analyzer.py ./MyApp/Info.plist

# Check Privacy Manifest requirements
python3 scripts/privacy_manifest_checker.py ./MyApp

# Generate privacy policy
python3 scripts/privacy_policy_generator.py \
  --app-name "MyApp" \
  --company "My Company" \
  --email "privacy@myapp.com" \
  --data-types "analytics,user_accounts"

# Validate screenshots
python3 scripts/screenshot_validator.py ./screenshots/
```

## 📚 References

| File | Content |
|------|---------|
| `apple-guidelines-checklist.md` | Complete App Review Guidelines checklist |
| `common-rejection-reasons.md` | Top 10 rejections with fixes |
| `privacy-manifest-guide.md` | Privacy Manifest requirements (2024+) |
| `metadata-best-practices.md` | ASO and metadata optimization |

## 📝 Templates

- `privacy-policy-template.md` - Fill-in-the-blank privacy policy
- `terms-of-service-template.md` - Terms of service template

## 💡 Who This Is For

- **Vibe coders** using no-code/low-code tools (Lovable, Vibecode, Bolt)
- **Indie developers** submitting their first iOS app
- **Teams** wanting a standardized submission process
- **Anyone** who wants to avoid common App Store rejections

## ✅ What It Covers

- Privacy Policy generation
- Privacy Manifest requirements (2024 APIs)
- Screenshot specifications and validation
- Info.plist validation
- App Store metadata optimization (ASO)
- Common rejection reasons and fixes
- Pre-submission checklist

## 🎯 Design Principles

- **Zero Config**: Works out of the box with any iOS project
- **Offline First**: All processing happens locally (SOC2 compliant)
- **Apple Aligned**: Matches current App Review Guidelines
- **One Command, One Job**: Each command does one thing perfectly

## 📦 Requirements

- Claude Code CLI
- Python 3.8+ (for scripts)
- Optional: Pillow (`pip install Pillow`) for screenshot dimension validation


## 💰 Recommended Tools

| Tool | What It Does | Bonus |
|------|--------------|-------|
| [**DigitalOcean**](https://m.do.co/c/e18421f27c6b) | Host your privacy policy page | $200 free credit |
| [**RevenueCat**](https://www.revenuecat.com) | Manage In-App Purchases | Free tier available |
| [**Fastlane**](https://fastlane.tools) | Automate App Store uploads | Open source |

*DigitalOcean link is an affiliate link. Using it supports this project at no extra cost to you.*


## 💜 Support This Project

If this plugin saved you time, consider [becoming a sponsor](https://github.com/sponsors/1Kode).



## 🤝 Contributing

Contributions welcome! Please open an issue or PR.

## 📄 License

MIT



Built with 💜 for the vibe coding community
