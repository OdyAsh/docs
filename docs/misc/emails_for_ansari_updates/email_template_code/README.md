# Ansari Newsletter Template System

This template system allows non-developers to easily create and customize Ansari newsletters by editing a simple YAML configuration file.

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Edit Content**
   - Open `newsletter-config.yaml`
   - Modify the content as needed
   - Save the file

3. **Build Newsletter**
   ```bash
   python build_newsletter.py
   ```

4. **Use Generated Newsletter**
   - The final HTML will be in `newsletter.html`
   - Copy this file for email distribution

## How to Edit Content

### Basic Information
```yaml
newsletter:
  title: "Ansari Update - May 2025"
  greeting: "Assalamu alaikum wa rahmatullahi wa barakatuh!"
```

### Adding/Removing Highlights
```yaml
highlights:
  highlights_list:
    - "**New Feature** description here"
    - "**Another Update** more details"
```

### Section Types

#### Platform Cards
```yaml
- type: "platforms"
  title: "Platform Availability"
  platforms:
    - name: "Web"
      link: "https://ansari.chat"
      link_text: "ansari.chat"
      icon: "icon-url-here"
```

#### Feature Grid
```yaml
- type: "features"
  title: "New Features"
  features:
    - title: "Feature Name"
      description: "Feature description"
```

#### Content Section
```yaml
- type: "content"
  title: "Section Title"
  paragraphs:
    - "Paragraph text with **bold** and [links](https://example.com)"
```

#### Contributors
```yaml
- type: "contributors"
  title: "Team Recognition"
  contributors:
    - name: "Person Name"
      description: "Their contribution details"
```

## Reordering Content

To change the order of sections, simply move them up or down in the `sections` list in the YAML file.

## Adding New Sections

Copy an existing section structure and modify the content. The system supports:
- `platforms` - App store/platform links with icons
- `features` - Grid layout of features
- `content` - Text paragraphs with markdown
- `contributors` - Team member highlights
- `feedback` - Contact information section

## Formatting

- Use `**text**` for bold
- Use `*text*` for italic
- Use `[text](url)` for links
- Icons should be full URLs (Google Drive links work)

## Tips for Non-Developers

1. **Always save your changes** to the YAML file before building
2. **Test your changes** by running the build script
3. **Keep backups** of working YAML files
4. **Indent carefully** - YAML is sensitive to indentation
5. **Use quotes** around text that contains special characters

## Troubleshooting

- **YAML errors**: Check indentation and special characters
- **Missing content**: Ensure all required fields are filled
- **Build fails**: Check that Python dependencies are installed

## Example: Creating a New Newsletter

📚 **See [creating_a_new_newsletter_example.md](creating_a_new_newsletter_example.md)** for a complete step-by-step walkthrough of creating the Ansari V4 development newsletter from technical documentation.

This example shows you:
- How to transform technical specs into user-friendly content
- Real-world content structure decisions
- Writing techniques for engaging newsletters
- How to add new section types when needed

## Multiple Newsletter Configs

You can create multiple newsletter configurations:

```bash
# Build from specific config file
python build_newsletter.py ansari-v4-newsletter-config.yaml ansari-v4-newsletter.html

# Build from default config
python build_newsletter.py
```

## File Structure

- `newsletter-config.yaml` - Default newsletter config
- `ansari-v4-newsletter-config.yaml` - Example V4 development newsletter
- `template.html` - HTML template (don't edit unless you know HTML)
- `build_newsletter.py` - Build script (don't edit)
- `newsletter.html` - Generated output (gets overwritten each build)
- `creating_a_new_newsletter_example.md` - Complete tutorial with real example