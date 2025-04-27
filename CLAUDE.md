# CLAUDE.md - Guide for Ansari Documentation

## Build Commands
- Build docs: `./build_docs.sh` (Builds to $PWD/build/docs)
- Serve docs locally: `mkdocs serve`
- Deploy docs: `./deploy_docs.sh` (Deploys to GCS bucket docs.ansari.chat)

## Documentation Style Guidelines
- Use markdown (.md) files for all documentation
- Follow existing document structure in mkdocs.yml
- Use H1 (#) for document title and H2 (##) for major sections
- Include relative links to other docs where appropriate
- Keep language simple, concise and accessible
- For Islamic terms, provide explanation on first use

## File Organization
- All docs go in the 'docs/' directory
- Main configuration in mkdocs.yml
- Navigation structure defined in mkdocs.yml nav section
- Build scripts in project root

## Contact
- For questions: feedback@ansari.chat