# 🔗 J Masked Link - Professional URL Masking Tool

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)
![J-Wrapper](https://img.shields.io/badge/J--Wrapper-Compatible-success)

A sophisticated and professional URL masking application that generates secure, disguised links using multiple URL shortening services with advanced customization options.

---

## ✨ Features

### 🎯 Core Functionality
- **Multi-Service Support**: Generate masked URLs using 8 different shortening services
- **Custom Domain Masking**: Disguise URLs with legitimate-looking domains
- **Security Keywords**: Add convincing keywords to enhance credibility
- **Real-time Generation**: Parallel processing with progress tracking
- **J-Wrapper Integration**: Seamless executable packaging support

### 🎨 User Experience
- **Modern Dark/Light Theme**: Beautiful, professional interface with theme toggle
- **Responsive Design**: Scrollable layout optimized for all screen sizes
- **Visual Feedback**: Color-coded status indicators and progress bars
- **One-Click Copy**: Easy copying of generated URLs to clipboard

### 🛡️ Security & Reliability
- **Input Validation**: Comprehensive URL and domain validation
- **Error Handling**: Robust error handling with user-friendly messages
- **Rate Limiting**: Respectful API usage with built-in delays
- **Threaded Operations**: Non-blocking UI during URL generation

---

## 🚀 Supported Services

| Service | Icon | Status | Features |
|---------|------|--------|----------|
| **TinyURL** | 🔗 | ✅ Working | Fast & reliable |
| **Is.gd** | ⚡ | ✅ Working | Simple API |
| **V.gd** | 🚀 | ✅ Working | Custom URLs |
| **Da.gd** | 🔒 | ✅ Working | Secure shortening |
| **Osdb** | 🌐 | ✅ Working | Open source |
| **T1p** | 📎 | ✅ Working | German service |
| **Shorturl** | ✂️ | ✅ Working | Multiple formats |
| **U0** | 🔐 | ✅ Working | Privacy focused |

---

## 📦 Installation

### STEP 1: Python Script
#### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

#### Step-by-Step Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/jprojectplatform/J-MASKED-LINK.git
   cd J-MASKED-LINK
   ```

2. **Install Dependencies**
   ```bash
   python3 -m venv j-masked-env
   source j-masked-env/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python j-masked.py
   ```

### STEP 2: Using J-Wrapper For run on anywhere on your Termanal


 **Download Pre-built Executable**
   - Visit [J-Wrapper Releases](https://github.com/jprojectplatform/J-Wrapper/)
   - Download the tool 
   - See how to use and apply on J-MASKED-LINK


### Dependencies
The following packages are automatically installed:
- `tkinter` - GUI framework
- `requests` - HTTP library for API calls
- `validators` - URL validation utilities

---

## 🎮 Usage Guide

### Basic Workflow

1. **Enter Target URL**
   - Input the destination URL you want to mask
   - Example: `https://your-target-site.com`

2. **Set Custom Domain**
   - Choose a convincing domain for masking
   - Example: `gmail.com`, `facebook.com`, `microsoft.com`

3. **Add Security Keywords**
   - Include relevant keywords separated by commas
   - Example: `login, verify, security, update`

4. **Generate URLs**
   - Click "GENERATE MASKED URLS" to create links across all services
   - Monitor progress in real-time

5. **Copy & Use**
   - Click "COPY URL" on any successful generation
   - Use the masked URLs as needed

### Output Format
Generated URLs follow this pattern:
```
https://[custom-domain]-[keywords]@[service-domain]/[short-code]
```

Example:
```
https://gmail.com-login-verify-security@tinyurl.com/abc123
```

---

## 🏗️ Architecture

### Code Structure
```
J-MASKED-LINK/
├── j-masked.py          # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # This documentation
├── LICENSE.md          # License information

```

### J-Wrapper Integration
This project is fully compatible with **[J-Wrapper](https://github.com/jprojectplatform/J-Wrapper)** 


### Key Components
- **JMaskedLink Class**: Main application controller
- **Theme Management**: Dynamic dark/light mode switching
- **Service Handlers**: Individual URL shortener implementations
- **Threading System**: Background processing for smooth UI
- **Validation Engine**: Input sanitization and verification

---

## 🎨 Customization

### Adding New Services
Extend the application by adding new shortener services:

```python
def shorten_newservice(self, url):
    """Shorten URL using NewService"""
    try:
        api_url = "https://newservice.com/api"
        payload = {"url": url}
        response = requests.post(api_url, json=payload, timeout=10)
        if response.status_code == 200:
            return response.json().get('short_url')
        return None
    except:
        return None
```

### Theme Customization
Modify colors in the `themes` dictionary:
```python
self.themes = {
    'dark': {
        'bg': '#0f0f23',
        'fg': '#e0e0e0',
        'accent': '#ff6b9d',
        # ... more colors
    }
}
```

### Building Custom Executables
Use J-Wrapper to create specialized builds:

```bash
# Basic build
python j-wrapper.py --input j-masked.py --output MyMaskedLink.exe

# Build with custom icon
python j-wrapper.py --input j-masked.py --output J-Masked-Link.exe --icon custom.ico

# Build with console window (for debugging)
python j-wrapper.py --input j-masked.py --output J-Masked-Link.exe --console
```

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Reporting Issues
- Use GitHub Issues to report bugs or request features
- Include detailed descriptions and reproduction steps

### Code Contributions
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 coding standards
- Include comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting PRs
- Ensure J-Wrapper compatibility for new dependencies

---

## 📄 License

This project is licensed under the J Project License (JPL) - see the [LICENSE](LICENSE.md) file for details.

---

## 👥 Team & Acknowledgments

### Project Owner
- **jh4ck3r** - Creator & Maintainer
- **J Project Platform** - Development Team

### Related Projects
- **[J-Wrapper](https://github.com/jprojectplatform/J-Wrapper)** - Advanced Python to EXE converter
- **J Project Platform** - Suite of security and utility tools

### Special Thanks
- Contributors and testers
- URL shortening service providers
- Open source community

---

## 🌐 Connect With Us

- **Website**: [J Project Platform](https://jprojectplatform.com)
- **GitHub**: [jprojectplatform](https://github.com/jprojectplatform)
- **J-Wrapper**: [Run Anywhere from Terminal](https://github.com/jprojectplatform/J-Wrapper)
- **More Tools**: Explore our other security and utility applications

---

## ⚠️ Disclaimer

This tool is intended for:
- Educational purposes
- Security research
- Authorized penetration testing
- Legitimate URL management

**Please use responsibly and in compliance with all applicable laws and regulations.** The developers are not responsible for misuse of this software.

---

## 🐛 Troubleshooting

### Common Issues

**"Service unavailable" errors**
- Check your internet connection
- Verify the target URL is accessible
- Some services may have temporary downtime

**GUI not loading (Python version)**
- Ensure Python and tkinter are properly installed
- Try running with administrative privileges
- Check for conflicting Python installations

**Executable not running (J-Wrapper version)**
- Ensure you have .NET Framework 4.5+ installed
- Try running as administrator
- Check Windows Defender exclusion if needed

**Copy function not working**
- Some systems require additional clipboard utilities
- Try manual copy if automatic fails

### Getting Help
1. Check existing GitHub issues
2. Review the documentation
3. Create a new issue with detailed information

---



<div align="center">

### ⭐ Star us on GitHub if you find this project useful!


**Made with ❤️ by J Project Platform**

*Hands With Universal Technology*

</div>
