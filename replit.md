# Subash Portfolio & Font Collection

## Overview
This is a static portfolio website and font collection showcase created by Subash Baniya. The site has been converted from Next.js to pure HTML, CSS, and JavaScript for simplicity and portability.

## Project Structure
- **index.html** - Main landing page with article about Machine Learning
- **fonts.html** - Font collection showcase page with downloadable fonts
- **404.html** - Custom 404 error page
- **assets/** - Static assets directory
  - **css/styles.css** - Tailwind CSS styles (compiled)
  - **fonts/** - Font files (woff2, OTF for system fonts)
  - **icons/favicon.ico** - Site favicon
- **public/fonts/** - Font files collection (TTF and OTF formats for download)
- **server.py** - Python HTTP server for serving static files
- **metagraph-img.jpg** - Open Graph image

## Technology Stack
- **Frontend**: Pure HTML, CSS (Tailwind), and JavaScript
- **Server**: Python 3.11 HTTP server with custom routing
- **Styling**: Tailwind CSS (compiled in static CSS)
- **Fonts**: Custom font collection (Groote, Athemi, Cawad, Zetan, Antesa, Chiffone, Evoxsy, Megivia, Modeline, Nativera, Stanley, Thoge)

## Development Setup
The project runs on port 5000 with a Python HTTP server that:
- Serves static HTML, CSS, and font files
- Implements URL routing (/fonts → /fonts.html)
- Handles 404 pages
- Includes cache-control headers for development
- Allows address reuse for easier restarts

## Pages
1. **Home (/)** - Portfolio article about Machine Learning fundamentals
2. **Fonts (/fonts)** - Font showcase with download links
3. **404** - Custom error page with navigation

## Recent Changes
- 2025-09-30: Converted from Next.js static export to pure HTML/CSS/JS
- 2025-09-30: Reorganized assets into /assets directory structure
- 2025-09-30: Removed Next.js dependencies and simplified codebase
- 2025-09-30: Updated server.py with improved routing and address reuse
- 2025-09-30: Cleaned up theme switcher script to vanilla JavaScript

## Features
- Dark/light/system theme support with localStorage persistence
- Responsive design with mobile-first approach
- Custom font previews with download functionality
- Clean, semantic HTML structure
- No build process required - pure static files

## User Preferences
None specified yet.
