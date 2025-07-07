# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal blog site (www.contenthere.net) built with Pelican, a Python-based static site generator. The site uses the Blue Penguin theme and is hosted on AWS S3.

## Key Architecture

- **Static Site Generator**: Pelican (Python-based)
- **Theme**: Blue Penguin theme (located in `blue-penguin-theme/`)
- **Content**: Markdown files in `content/` organized by year/month
- **Output**: Generated HTML in `output/` directory
- **Hosting**: AWS S3 bucket (www.contenthere.net)
- **Dependencies**: Managed with Pipenv

## Development Commands

### Building the Site
```bash
# Generate the site for development
make html
# OR
invoke build

# Generate with deletion of existing output
make clean && make html
# OR
invoke rebuild

# Generate for production (with feeds)
make publish
# OR
invoke preview
```

### Development Server
```bash
# Serve locally at http://localhost:8000
make serve
# OR
invoke serve

# Serve with auto-regeneration
make devserver
# OR
invoke livereload

# Auto-regenerate on file changes
make regenerate
# OR
invoke regenerate
```

### Content Creation
```bash
# Create new blog post
invoke newpost --title "Post Title" --tags "tag1, tag2"
```

### Publishing
```bash
# Sync to S3 bucket (production)
make s3_upload
# OR
invoke publish

# Alternative sync command
s3cmd sync -r output/ s3://www.contenthere.net
```

## Project Structure

- `content/`: Blog posts organized by year/month in Markdown format
- `blue-penguin-theme/`: Custom theme templates and assets
- `output/`: Generated static site (not committed to git)
- `pelicanconf.py`: Main Pelican configuration
- `publishconf.py`: Production-specific configuration
- `tasks.py`: Invoke tasks for automation
- `Makefile`: Traditional make commands
- `import.py`: Content import utility

## Configuration Files

- **pelicanconf.py**: Main settings including timezone, plugins, theme path
- **publishconf.py**: Production overrides (SITEURL, feeds, S3 settings)
- **Pipfile**: Python dependencies managed with Pipenv

## Content Format

Blog posts use Pelican's Markdown format with metadata:
```markdown
Title: Post Title
Date: YYYY-MM-DD HH:MM:SS
Modified: YYYY-MM-DD HH:MM:SS
Category: misc
Tags: tag1, tag2
Slug: url-slug
Authors: Seth Gottlieb
```

## Dependencies

Install dependencies with:
```bash
pipenv install
```

The site uses:
- Pelican for static site generation
- Jinja2 for templating
- Slugify for URL generation
- Invoke for task automation
- AWS CLI for S3 deployment