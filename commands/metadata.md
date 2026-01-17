---
description: Generate optimized App Store metadata including app name, subtitle, description, keywords, and screenshot specifications. Analyzes the app to create compelling, ASO-optimized content.
---

# App Store Metadata Generator

Generate compelling App Store listing content optimized for discovery and conversion.

## Execution Steps

1. **Gather app information**:
   - App name and core functionality
   - Target audience
   - Key features (3-5 main features)
   - Competitive differentiators
   - Category (primary and secondary)

2. **Generate metadata components**:
   - App name options (max 30 characters)
   - Subtitle options (max 30 characters)
   - Full description (up to 4000 characters)
   - Keywords (max 100 characters total)
   - Promotional text (max 170 characters)
   - Screenshot text overlay suggestions

3. **Validate screenshot requirements**:
   ```bash
   python3 scripts/screenshot_validator.py <path-to-screenshots-folder>
   ```

4. **Output the complete metadata package**

## Output Template

```markdown
# 📱 App Store Metadata for [APP NAME]

Generated: [DATE]

---

## App Name Options (max 30 characters)

| Option | Characters | Notes |
|--------|------------|-------|
| [Name 1] | [XX] | [Primary recommendation] |
| [Name 2] | [XX] | [Alternative] |
| [Name 3] | [XX] | [Alternative] |

**Recommendation:** [Explain which name and why]

---

## Subtitle Options (max 30 characters)

| Option | Characters | Notes |
|--------|------------|-------|
| [Subtitle 1] | [XX] | [Benefit-focused] |
| [Subtitle 2] | [XX] | [Feature-focused] |
| [Subtitle 3] | [XX] | [Action-focused] |

**Recommendation:** [Explain which subtitle and why]

---

## Keywords (max 100 characters)

```
[keyword1],[keyword2],[keyword3],[keyword4],...
```

**Character count:** [XX]/100

**Strategy notes:**
- [Why these keywords were chosen]
- [Search volume considerations]
- [Competition notes]

**Keywords NOT to include** (already indexed from name/subtitle):
- [word1], [word2], [word3]

---

## Description

### First Paragraph (Most Important - Visible Before "More")

[Compelling opening that hooks the reader and explains core value proposition in 2-3 sentences]

### Full Description

[FULL DESCRIPTION TEXT - Up to 4000 characters]

**Character count:** [XXXX]/4000

---

## Promotional Text (max 170 characters)

[Promotional text for time-sensitive announcements or highlights]

**Character count:** [XXX]/170

**Note:** This can be updated without a new app version.

---

## What's New (for updates)

[Template for release notes]

**Version X.X.X**
• [New feature or improvement]
• [Bug fix or enhancement]
• [Performance improvement]

---

## Screenshot Specifications

### Required Devices

| Device | Dimensions | Required |
|--------|------------|----------|
| iPhone 6.7" | 1290×2796 | Yes |
| iPhone 6.5" | 1284×2778 | Yes (or use 6.7") |
| iPhone 5.5" | 1242×2208 | Optional |
| iPad Pro 12.9" | 2048×2732 | If iPad supported |

### Screenshot Strategy

**Screen 1 (Hero):** [Main value proposition - most important]
**Screen 2:** [Key feature #1]
**Screen 3:** [Key feature #2]
**Screen 4:** [Social proof or key feature #3]
**Screen 5:** [Call to action or additional feature]

### Text Overlay Suggestions

| Screen | Headline | Subheadline |
|--------|----------|-------------|
| 1 | [Headline] | [Subheadline] |
| 2 | [Headline] | [Subheadline] |
| 3 | [Headline] | [Subheadline] |
| 4 | [Headline] | [Subheadline] |
| 5 | [Headline] | [Subheadline] |

---

## Category Recommendations

**Primary:** [Category]
**Secondary:** [Category] (optional)

**Rationale:** [Why these categories]

---

## Age Rating Guidance

Based on app content, likely age rating: [4+/9+/12+/17+]

Content considerations:
- [ ] Infrequent/Mild [content type]
- [ ] [Other applicable content descriptors]
```

## Metadata Best Practices

### App Name
- Front-load with most important/searchable word
- Don't repeat words from subtitle
- Avoid generic descriptors if possible
- Consider localization needs

### Subtitle
- Complement the name, don't repeat it
- Focus on benefit or action
- Use strong verbs when possible

### Keywords
- Don't repeat words from name or subtitle (already indexed)
- Use singular OR plural, not both
- Separate with commas, no spaces
- Include common misspellings if relevant
- Prioritize relevance over volume

### Description
- First 1-3 sentences are critical (visible before "More")
- Lead with benefits, not features
- Use short paragraphs and line breaks
- Include social proof if available
- End with call to action

### Screenshots
- First screenshot is most important (shown in search)
- Show actual app UI, not marketing graphics only
- Use device frames for professionalism
- Text should be readable at small sizes
- Localize for major markets

See `references/metadata-best-practices.md` for detailed guidance.

$ARGUMENTS
