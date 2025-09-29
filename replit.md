# Subash Baniya's Personal Website

## Overview
This is a static personal website for Subash Baniya featuring an article about Machine Learning. The site was built with Next.js and exported as static HTML files. It's now configured to run on Replit.

## Project Structure
- `index.html` - Main page with ML article content
- `fonts.html` - Font collection showcase page
- `fonts/` - Organized font collection
  - `Athemi.otf` - Athemi display font
  - `CawadRegular.ttf` - Cawad regular font
  - `Groote-Regular.otf` - Groote serif font
  - `Zetan.ttf` - Zetan display font
- `_next/static/` - Static assets (CSS, fonts, favicon)
  - `css/styles.css` - Compiled styles
  - `media/` - Original Next.js font files
  - `ico/favicon.ico` - Site icon
- `server.py` - Custom HTTP server with routing
- `LICENSE` - MIT License

## Current State
- ✅ Static website serving on port 5000
- ✅ Workflow configured with Python HTTP server
- ✅ Deployment configured for autoscale
- ✅ All assets loading correctly
- ✅ Font collection organized and accessible
- ✅ Custom fonts demo page with download links

## Setup Details
- **Server**: Python built-in HTTP server
- **Port**: 5000 (frontend)
- **Host**: 0.0.0.0 (allows Replit proxy)
- **Deployment**: Autoscale (perfect for static sites)

## Recent Changes (September 29, 2025)
- Organized font collection: moved Athemi.otf, CawadRegular.ttf, and Zetan.ttf to fonts/ folder
- Added Groote-Regular.otf to font collection from existing media assets
- Created custom fonts demo page at /fonts with clean, minimal design
- Implemented font showcase with preview text and download functionality
- Updated server routing to handle /fonts page without directory conflicts
- All 4 fonts now accessible with individual download links

## Previous Changes (September 20, 2025)
- Imported GitHub repository as static site
- Configured workflow to serve static files
- Set up deployment configuration
- Verified all assets load correctly

## User Preferences
- Static site requiring minimal configuration
- Simple HTTP server for serving files
- Autoscale deployment for cost efficiency