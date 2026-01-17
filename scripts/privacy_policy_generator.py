#!/usr/bin/env python3
"""
Privacy Policy Generator for iOS Apps

Generates a comprehensive privacy policy based on app data practices.
Output is compliant with Apple App Store requirements and GDPR/CCPA basics.

Usage:
    python3 privacy_policy_generator.py --app-name "My App" --company "My Company" \
        --email "privacy@example.com" --data-types "analytics,user_content"

Options:
    --app-name      Name of the app (required)
    --company       Company or developer name (required)
    --email         Contact email for privacy inquiries (required)
    --website       Company website URL (optional)
    --data-types    Comma-separated data types collected (optional)
    --output-dir    Directory for output files (default: current directory)
    --effective-date Effective date (default: today)

Data Types:
    analytics, user_accounts, location, photos, camera, contacts, health,
    user_content, purchases, advertising, diagnostics, third_party_auth

Exit codes:
    0 - Success
    1 - Error
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path


# Data type descriptions for the policy
DATA_TYPE_INFO = {
    'analytics': {
        'name': 'Usage Analytics',
        'description': 'We collect anonymous usage data to understand how users interact with our app and improve the user experience.',
        'data_collected': ['App interactions', 'Feature usage patterns', 'Session duration', 'Crash reports'],
        'purpose': 'App improvement and performance optimization',
        'retention': '24 months',
    },
    'user_accounts': {
        'name': 'Account Information',
        'description': 'When you create an account, we collect information to provide personalized services.',
        'data_collected': ['Email address', 'Username', 'Profile information'],
        'purpose': 'Account management and authentication',
        'retention': 'Until account deletion',
    },
    'location': {
        'name': 'Location Data',
        'description': 'We collect location data to provide location-based features.',
        'data_collected': ['Precise or coarse location'],
        'purpose': 'Location-based features and services',
        'retention': 'Only while app is in use (unless otherwise specified)',
    },
    'photos': {
        'name': 'Photos and Media',
        'description': 'We access your photo library when you choose to upload or share photos.',
        'data_collected': ['Photos you select', 'Photo metadata'],
        'purpose': 'User-initiated photo sharing and uploads',
        'retention': 'As long as you keep the content in the app',
    },
    'camera': {
        'name': 'Camera Access',
        'description': 'We access your camera for features that require photo or video capture.',
        'data_collected': ['Photos or videos you capture'],
        'purpose': 'Photo/video capture features',
        'retention': 'As long as you keep the content in the app',
    },
    'contacts': {
        'name': 'Contacts',
        'description': 'We may access your contacts to help you connect with friends.',
        'data_collected': ['Contact names', 'Contact information'],
        'purpose': 'Social features and friend finding',
        'retention': 'Not stored on our servers (processed locally)',
    },
    'health': {
        'name': 'Health Data',
        'description': 'We access health data from HealthKit to provide health-related features.',
        'data_collected': ['Health metrics you authorize'],
        'purpose': 'Health tracking and fitness features',
        'retention': 'Stored locally on device or as specified',
    },
    'user_content': {
        'name': 'User-Generated Content',
        'description': 'Content you create and share within the app.',
        'data_collected': ['Text, images, or other content you create'],
        'purpose': 'Providing the core app functionality',
        'retention': 'Until you delete it',
    },
    'purchases': {
        'name': 'Purchase Information',
        'description': 'We process purchase information for in-app purchases.',
        'data_collected': ['Purchase history', 'Transaction IDs'],
        'purpose': 'Processing purchases and providing purchased features',
        'retention': 'As required for purchase verification',
    },
    'advertising': {
        'name': 'Advertising Data',
        'description': 'We may collect data for personalized advertising.',
        'data_collected': ['Advertising identifier', 'Ad interaction data'],
        'purpose': 'Delivering relevant advertisements',
        'retention': 'As specified by advertising partners',
    },
    'diagnostics': {
        'name': 'Diagnostic Data',
        'description': 'We collect diagnostic data to improve app stability.',
        'data_collected': ['Crash logs', 'Performance data', 'Error reports'],
        'purpose': 'Bug fixing and performance improvement',
        'retention': '12 months',
    },
    'third_party_auth': {
        'name': 'Third-Party Authentication',
        'description': 'When you sign in with third-party services, we receive basic profile information.',
        'data_collected': ['Name', 'Email', 'Profile picture'],
        'purpose': 'Account creation and authentication',
        'retention': 'Until account deletion',
    },
}

# Third-party SDKs and their data practices
COMMON_SDKS = {
    'firebase': 'Firebase (Google) - Analytics, crash reporting, and cloud services',
    'amplitude': 'Amplitude - Product analytics',
    'mixpanel': 'Mixpanel - User analytics',
    'appsflyer': 'AppsFlyer - Attribution and marketing analytics',
    'facebook': 'Facebook SDK - Social features and analytics',
    'google_ads': 'Google AdMob - Advertising',
    'stripe': 'Stripe - Payment processing',
    'sentry': 'Sentry - Error tracking',
    'segment': 'Segment - Customer data platform',
}


def generate_privacy_policy(
    app_name: str,
    company: str,
    email: str,
    website: str = None,
    data_types: list = None,
    effective_date: str = None,
    third_party_sdks: list = None,
) -> str:
    """Generate privacy policy markdown content."""
    
    if effective_date is None:
        effective_date = datetime.now().strftime("%B %d, %Y")
    
    if data_types is None:
        data_types = ['analytics', 'diagnostics']
    
    # Build policy content
    policy = f"""# Privacy Policy for {app_name}

**Effective Date:** {effective_date}

**Last Updated:** {effective_date}

{company} ("we", "our", or "us") operates the {app_name} mobile application (the "App"). This Privacy Policy describes how we collect, use, and share information when you use our App.

## 1. Information We Collect

"""
    
    # Add sections for each data type
    for dt in data_types:
        if dt in DATA_TYPE_INFO:
            info = DATA_TYPE_INFO[dt]
            policy += f"""### {info['name']}

{info['description']}

**Data collected:**
"""
            for item in info['data_collected']:
                policy += f"- {item}\n"
            
            policy += f"""
**Purpose:** {info['purpose']}

**Retention:** {info['retention']}

"""
    
    # Add standard sections
    policy += f"""## 2. How We Use Your Information

We use the information we collect to:

- Provide, maintain, and improve our App
- Process transactions and send related information
- Send technical notices, updates, and support messages
- Respond to your comments, questions, and requests
- Monitor and analyze trends, usage, and activities
- Detect, investigate, and prevent security incidents

## 3. Information Sharing

We do not sell your personal information. We may share information in the following circumstances:

- **Service Providers:** We may share information with third-party service providers who perform services on our behalf (analytics, hosting, etc.)
- **Legal Requirements:** We may disclose information if required by law or in response to valid requests by public authorities
- **Business Transfers:** In connection with any merger, sale, or acquisition of our business
- **With Your Consent:** We may share information with your consent or at your direction

"""
    
    # Add third-party SDK section if applicable
    if third_party_sdks:
        policy += """## 4. Third-Party Services

Our App uses the following third-party services that may collect information:

"""
        for sdk in third_party_sdks:
            if sdk in COMMON_SDKS:
                policy += f"- {COMMON_SDKS[sdk]}\n"
        
        policy += """
These services have their own privacy policies. We encourage you to review them.

"""
    else:
        policy += """## 4. Third-Party Services

Our App may use third-party services for analytics, crash reporting, or other functionality. These services may collect information according to their own privacy policies.

"""
    
    policy += f"""## 5. Data Security

We implement appropriate technical and organizational measures to protect your information. However, no method of transmission over the Internet or electronic storage is 100% secure.

## 6. Your Rights

Depending on your location, you may have the following rights:

- **Access:** Request access to your personal information
- **Correction:** Request correction of inaccurate information
- **Deletion:** Request deletion of your information
- **Portability:** Request a copy of your information in a portable format
- **Opt-out:** Opt out of certain data processing activities

To exercise these rights, contact us at {email}.

## 7. Children's Privacy

Our App is not intended for children under 13. We do not knowingly collect personal information from children under 13. If we learn we have collected such information, we will take steps to delete it.

## 8. Changes to This Policy

We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy in the App and updating the "Last Updated" date.

## 9. Contact Us

If you have questions about this Privacy Policy, please contact us:

- **Email:** {email}
"""
    
    if website:
        policy += f"- **Website:** {website}\n"
    
    policy += f"""
---

© {datetime.now().year} {company}. All rights reserved.
"""
    
    return policy


def markdown_to_html(markdown_content: str, title: str) -> str:
    """Convert markdown to basic HTML."""
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        h1 {{ color: #1a1a1a; border-bottom: 2px solid #007AFF; padding-bottom: 10px; }}
        h2 {{ color: #1a1a1a; margin-top: 30px; }}
        h3 {{ color: #333; }}
        ul {{ padding-left: 20px; }}
        li {{ margin: 5px 0; }}
        strong {{ color: #1a1a1a; }}
        a {{ color: #007AFF; }}
    </style>
</head>
<body>
"""
    
    # Basic markdown to HTML conversion
    lines = markdown_content.split('\n')
    in_list = False
    
    for line in lines:
        # Headers
        if line.startswith('# '):
            html += f"<h1>{line[2:]}</h1>\n"
        elif line.startswith('## '):
            html += f"<h2>{line[3:]}</h2>\n"
        elif line.startswith('### '):
            html += f"<h3>{line[4:]}</h3>\n"
        # List items
        elif line.startswith('- '):
            if not in_list:
                html += "<ul>\n"
                in_list = True
            html += f"<li>{line[2:]}</li>\n"
        # Bold text and paragraphs
        elif line.strip():
            if in_list:
                html += "</ul>\n"
                in_list = False
            # Convert **text** to <strong>text</strong>
            import re
            line = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
            html += f"<p>{line}</p>\n"
        elif in_list:
            html += "</ul>\n"
            in_list = False
    
    if in_list:
        html += "</ul>\n"
    
    html += """</body>
</html>"""
    
    return html


def main():
    parser = argparse.ArgumentParser(
        description='Generate privacy policy for iOS apps',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Data Types:
  analytics         Usage analytics and app interactions
  user_accounts     User registration and profiles
  location          Location data
  photos            Photo library access
  camera            Camera access
  contacts          Contacts access
  health            HealthKit data
  user_content      User-generated content
  purchases         In-app purchase data
  advertising       Advertising identifiers
  diagnostics       Crash logs and performance data
  third_party_auth  Sign in with Apple/Google/Facebook

Example:
  python3 privacy_policy_generator.py \\
    --app-name "BuyOrNah" \\
    --company "Your Company Name" \\
    --email "privacy@buyornah.com" \\
    --data-types "analytics,user_accounts,photos"
        """
    )
    
    parser.add_argument('--app-name', required=True, help='Name of the app')
    parser.add_argument('--company', required=True, help='Company or developer name')
    parser.add_argument('--email', required=True, help='Contact email for privacy inquiries')
    parser.add_argument('--website', help='Company website URL')
    parser.add_argument('--data-types', help='Comma-separated list of data types collected')
    parser.add_argument('--sdks', help='Comma-separated list of third-party SDKs used')
    parser.add_argument('--output-dir', default='.', help='Output directory')
    parser.add_argument('--effective-date', help='Effective date (default: today)')
    
    args = parser.parse_args()
    
    # Parse data types
    data_types = []
    if args.data_types:
        data_types = [dt.strip().lower() for dt in args.data_types.split(',')]
    else:
        data_types = ['analytics', 'diagnostics']  # Default minimal set
    
    # Parse SDKs
    sdks = []
    if args.sdks:
        sdks = [sdk.strip().lower() for sdk in args.sdks.split(',')]
    
    # Generate policy
    print(f"📝 Generating privacy policy for {args.app_name}...")
    
    markdown_content = generate_privacy_policy(
        app_name=args.app_name,
        company=args.company,
        email=args.email,
        website=args.website,
        data_types=data_types,
        effective_date=args.effective_date,
        third_party_sdks=sdks if sdks else None,
    )
    
    # Security: Validate and sanitize output directory
    try:
        output_dir = Path(args.output_dir).resolve()
    except (ValueError, OSError) as e:
        print(f"❌ Error: Invalid output path: {e}")
        return 1
    
    # Security: Prevent writing to sensitive system directories
    sensitive_paths = ['/etc', '/usr', '/bin', '/sbin', '/var', '/root', '/sys', '/proc']
    for sensitive in sensitive_paths:
        if str(output_dir).startswith(sensitive):
            print(f"❌ Error: Cannot write to system directory: {output_dir}")
            return 1
    
    # Security: Create directory with safe permissions
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print(f"❌ Error: Permission denied creating directory: {output_dir}")
        return 1
    except OSError as e:
        print(f"❌ Error: Could not create directory: {e}")
        return 1
    
    # Write markdown file
    md_path = output_dir / 'privacy-policy.md'
    try:
        md_path.write_text(markdown_content)
        print(f"✅ Created: {md_path}")
    except (PermissionError, OSError) as e:
        print(f"❌ Error writing markdown file: {e}")
        return 1
    
    # Write HTML file
    html_content = markdown_to_html(markdown_content, f"Privacy Policy - {args.app_name}")
    html_path = output_dir / 'privacy-policy.html'
    try:
        html_path.write_text(html_content)
        print(f"✅ Created: {html_path}")
    except (PermissionError, OSError) as e:
        print(f"❌ Error writing HTML file: {e}")
        return 1
    
    # Summary
    print(f"\n📋 Summary:")
    print(f"   App: {args.app_name}")
    print(f"   Data types covered: {', '.join(data_types)}")
    print(f"   Output files: {md_path}, {html_path}")
    print(f"\n💡 Next steps:")
    print(f"   1. Review and customize the generated policy")
    print(f"   2. Host the HTML file at a public URL")
    print(f"   3. Add the URL to App Store Connect")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
