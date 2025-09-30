# Subash Portfolio & Font Collection

## Overview
This is a static portfolio website and font collection showcase created by Subash Baniya. The site was built using Next.js and exported as static HTML files for optimal performance and easy deployment.

## Project Structure
- **index.html** - Main landing page with article about Machine Learning
- **public/fonts.html** - Font collection showcase page with downloadable fonts
- **404.html** - Custom 404 error page
- **_next/static/** - Next.js static assets (CSS, fonts, media)
- **public/fonts/** - Font files collection (TTF and OTF formats)
- **server.py** - Python HTTP server for serving static files
- **next.config.js** - Next.js configuration with rewrite rules

## Technology Stack
- **Frontend**: Next.js (static export)
- **Server**: Python 3.11 HTTP server
- **Styling**: Tailwind CSS (compiled in static CSS)
- **Fonts**: Custom font collection (Groote, Athemi, Cawad, Zetan, Antesa, Chiffone, Evoxsy, Megivia, Modeline, Nativera, Stanley, Thoge)

## Development Setup
The project runs on port 5000 with a Python HTTP server that:
- Serves static HTML, CSS, and font files
- Implements URL rewriting (/fonts → /public/fonts.html)
- Handles 404 pages
- Includes cache-control headers for development

## Deployment
- **Deployment Type**: Autoscale (stateless static site)
- **Production Command**: `python3 server.py`
- The site is optimized for Replit deployment with proper routing and asset serving

## Pages
1. **Home (/)** - Portfolio article about Machine Learning fundamentals
2. **Fonts (/fonts)** - Font showcase with download links
3. **404** - Custom error page with navigation

## Recent Changes
- 2025-09-30: Initial Replit setup with Python static server
- 2025-09-30: Configured deployment for autoscale
- 2025-09-30: Verified all pages and routing working correctly

## User Preferences
None specified yet.
