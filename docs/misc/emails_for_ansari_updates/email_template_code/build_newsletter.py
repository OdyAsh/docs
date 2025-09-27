#!/usr/bin/env python3
"""
Newsletter Builder
Converts YAML configuration to HTML newsletter

Usage:
    python build_newsletter.py

This script reads newsletter-config.yaml and template.html to generate
a final HTML newsletter ready for email distribution.
"""

import yaml
import re
from pathlib import Path
from jinja2 import Template, Environment, FileSystemLoader


def markdown_to_html(text):
    """Simple markdown-like conversion for basic formatting"""
    if not isinstance(text, str):
        return text

    # Convert **bold** to <strong>
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    # Convert [text](url) to <a href="url">text</a>
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" style="color: #3d91c5;text-decoration: none;">\1</a>', text)

    # Convert *italic* to <em>
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)

    return text


def build_newsletter(config_file="newsletter-config.yaml", output_file="newsletter.html"):
    """Main function to build the newsletter"""
    current_dir = Path(__file__).parent

    # Load YAML configuration
    config_path = current_dir / config_file
    template_path = current_dir / "template.html"
    output_path = current_dir / output_file

    if not config_path.exists():
        print(f"Error: {config_path} not found!")
        return False

    if not template_path.exists():
        print(f"Error: {template_path} not found!")
        return False

    try:
        # Load configuration
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)

        # Setup Jinja2 environment
        env = Environment(loader=FileSystemLoader(current_dir))
        env.filters['markdown'] = markdown_to_html

        # Load template
        template = env.get_template('template.html')

        # Render newsletter
        html_content = template.render(**config)

        # Write output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"Newsletter built successfully: {output_path}")
        print(f"Ready for email distribution!")
        return True

    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")
        return False
    except Exception as e:
        print(f"Build error: {e}")
        return False


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else f"{Path(config_file).stem}-newsletter.html"
        build_newsletter(config_file, output_file)
    else:
        build_newsletter()