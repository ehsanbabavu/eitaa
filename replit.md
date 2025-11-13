# Eitaa Web Automation Project

## Overview
This is a Python automation script designed to automate login process on Eitaa web messenger (https://web.eitaa.com/). The script uses Selenium WebDriver with Chrome to automatically enter a phone number and click the continue button.

## Current State
- **Language**: Python 3.11
- **Main Libraries**: Selenium, webdriver-manager
- **Target Platform**: Windows (requires real Chrome browser)
- **Status**: Completed and ready for download/use on Windows systems

## Project Architecture

### Core Files
1. **eitaa_automation.py** - Main automation script
   - Initializes Chrome WebDriver with appropriate settings
   - Navigates to Eitaa web messenger
   - Automatically enters phone number (9135621232)
   - Clicks the continue button
   - Provides English console logging for all steps

2. **requirements.txt** - Python dependencies
   - selenium==4.15.2
   - webdriver-manager==4.0.1

3. **README.md** - Persian documentation for end users
   - Installation instructions
   - Usage guide
   - Configuration steps

### Key Design Decisions

#### Why Not Headless Mode?
The Eitaa website does not load properly in headless Chrome/Chromium. Testing showed:
- Page returns `data:,` URL instead of actual content
- Page source is essentially empty (39 bytes)
- Anti-bot detection or JavaScript rendering requirements prevent headless operation

**Solution**: The script runs Chrome in visible mode (non-headless) on actual Windows systems where the user can see the browser window.

#### Page Load Strategy
- Uses `page_load_strategy = 'eager'` to prevent hanging on SPA page load events
- Sets 20-second page load timeout
- Catches and continues on timeout exceptions
- Uses explicit waits for DOM elements instead of relying on page load completion

#### ChromeDriver Management
- Uses `webdriver-manager` for automatic ChromeDriver download and version matching
- No manual driver installation required by end users
- Works on Windows, Linux, and macOS (though primarily designed for Windows)

## Important Notes

### Replit Limitations
This script **cannot run successfully on Replit** because:
1. Eitaa website blocks or doesn't load in headless browsers
2. Replit's NixOS environment doesn't have a display for visible Chrome
3. The website requires a real browser environment with JavaScript

### Intended Usage
Users should:
1. Download all project files
2. Install Python 3.11+ on their Windows computer
3. Install Google Chrome browser
4. Run `pip install -r requirements.txt`
5. Execute `python eitaa_automation.py` from command line

## Recent Changes (Nov 13, 2025)
- Installed Python 3.11 with selenium and webdriver-manager
- Created automation script with proper timeout and page load handling
- Added Persian README for Windows users
- Removed headless mode and Linux-specific paths for Windows compatibility
- Simplified ChromeDriver initialization to use webdriver-manager exclusively
- Set page_load_strategy to 'eager' to handle Eitaa's SPA architecture

## User Preferences
- Console output in English
- Documentation in Persian
- No emojis in code or documentation

## Next Steps (Future Enhancements)
- Support for multiple phone numbers via config file
- Automatic verification code entry (if API available)
- GUI interface in Persian
- Scheduled automation capabilities
- Session persistence for staying logged in
