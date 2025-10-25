# 🐛 BugPilot AI - Advanced Security Testing Assistant

[![GitHub stars](https://img.shields.io/github/stars/letchupkt/BugPilot-Ai?style=social)](https://github.com/letchupkt/BugPilot-Ai/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/letchupkt/BugPilot-Ai?style=social)](https://github.com/letchupkt/BugPilot-Ai/network)
[![GitHub issues](https://img.shields.io/github/issues/letchupkt/BugPilot-Ai)](https://github.com/letchupkt/BugPilot-Ai/issues)
[![License](https://img.shields.io/badge/License-Educational-blue.svg)](LICENSE)

**Version:** 2025.10.25  
**Author:** LAKSHMIKANTHAN K (letchupkt)  
**© 2025 LAKSHMIKANTHAN K (letchupkt) - Enhanced MCP Kali Server**

## 🚀 **OVERVIEW**

BugPilot AI is a professional desktop application that provides an intelligent interface for security testing and penetration testing. It combines the power of AI with real security tools to assist security professionals, bug bounty hunters, and penetration testers in conducting comprehensive security assessments.

## ✨ **KEY FEATURES**

### **🤖 AI-Powered Security Assistant**
- **Real Tool Execution** - Executes actual security tools (no fake responses)
- **Intelligent Analysis** - AI analyzes real scan results and provides insights
- **Multiple AI Models** - Support for Ollama, OpenAI, and Google Gemini
- **Context Awareness** - Maintains conversation history and scan context
- **AutoPilot Mode** - Automatic tool execution based on AI recommendations

### **🛠️ Security Tools Integration (25+ Tools)**
- **Reconnaissance:** subfinder, amass, assetfinder, httpx, waybackurls, gau
- **Vulnerability Scanning:** nuclei, nikto, dalfox
- **Web Application Testing:** gobuster, ffuf, feroxbuster, katana
- **Network Scanning:** nmap, masscan, rustscan
- **Parameter Discovery:** arjun, paramspider
- **SQL Injection Testing:** sqlmap
- **Directory Enumeration:** dirsearch, dirb
- **Subdomain Takeover:** subjack, subzy
- **And many more specialized tools...**

### **💻 Professional GUI Interface**
- **Dark Hacker Theme** - Professional cybersecurity aesthetic
- **Tabbed Interface** - Chat, Tools, Results, Activity, Settings
- **Real-time Feedback** - Live tool execution status and progress
- **Typing Animations** - Visual feedback during AI processing
- **Results Management** - Organized scan results with timestamps
- **Export Functionality** - Save results and generate reports

### **🔧 Advanced Capabilities**
- **MCP Server Integration** - Connect to Kali Linux MCP server for remote tool execution
- **Fake Response Detection** - Warns when AI provides simulated results instead of real tool execution
- **Session Management** - Persistent conversation and scan history
- **Multi-target Support** - Handle multiple targets simultaneously
- **Custom Tool Integration** - Add your own security tools

## 📁 **PROJECT STRUCTURE**

```
BugPilot-AI/
├── 📄 bugpilot_ai.py          # Main application file (Protected)
├── 📄 kali_server.py          # MCP Kali server (Protected)
├── 📄 install.py              # Installation helper script
├── 🖼️ bugpilot-logo.ico       # Application icon
├── 📄 requirements.txt        # Python dependencies
├── 📖 README.md              # This comprehensive documentation
└── 📖 README2.md             # Additional documentation (merged here)
```

## 🔧 **INSTALLATION & SETUP**

### **Prerequisites**
- **Python 3.9+** (Python 3.9 recommended for building executables)
- **Windows/Linux/macOS** (GUI optimized for Windows)
- **Kali Linux Server** (optional, for MCP tools)
- **4GB RAM** minimum, 8GB recommended
- **Internet connection** for AI models and tool updates

### **Quick Installation**

#### **Method 1: Automated Installation**
```bash
# Clone the repository
git clone https://github.com/letchupkt/BugPilot-Ai.git
cd BugPilot-Ai

# Run automated installer
python install.py
```

#### **Method 2: Manual Installation**
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the application
python bugpilot_ai.py
```

#### **Method 3: Using Virtual Environment (Recommended)**
```bash
# Create virtual environment
python -m venv bugpilot_env

# Activate virtual environment
# Windows:
bugpilot_env\Scripts\activate
# Linux/macOS:
source bugpilot_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python bugpilot_ai.py
```

### **MCP Server Setup (Optional)**
```bash
# On your Kali Linux machine
python kali_server.py

# Server will start on port 5000
# Configure the server URL in BugPilot AI Settings
```

## 🚀 **BUILDING EXECUTABLE**

Create a standalone executable (.exe) file for easy distribution:

### **Using PyInstaller**
```bash
# Install PyInstaller (specific version for compatibility)
pip install pyinstaller==5.13.2

# Build executable
pyinstaller --onefile --windowed --icon=bugpilot-logo.ico --name=BugPilotAI bugpilot_ai.py

# Output will be in dist/ folder
```

### **Build Specifications**
- **File Size:** 50-80 MB standalone executable
- **Dependencies:** All Python libraries bundled
- **Compatibility:** Windows 10/11, portable across systems
- **No Installation Required:** Run directly from executable

## 🎯 **USAGE GUIDE**

### **Getting Started**

1. **Launch Application**
   ```bash
   python bugpilot_ai.py
   ```

2. **Configure AI Model** (First Time Setup)
   - Go to **Settings** tab
   - Choose your AI provider (Ollama/OpenAI/Gemini)
   - Enter API keys if required
   - Test connection

3. **Start Security Testing**
   ```
   User: "Scan example.com for subdomains"
   AI: I'll perform subdomain enumeration on example.com using multiple tools.
   
   EXECUTE_TOOL: subfinder
   PARAMETERS: {"domain": "example.com"}
   
   [Real tool executes and shows actual results]
   ```

### **Example Commands & Workflows**

#### **Reconnaissance Phase**
```bash
# Subdomain Discovery
"Find subdomains for example.com"
"Run amass on target.com with passive mode"
"Enumerate subdomains using multiple tools for example.com"

# Asset Discovery
"Discover assets for example.com"
"Find all URLs for example.com from wayback machine"
"Collect URLs using gau for example.com"
```

#### **Vulnerability Assessment**
```bash
# Web Application Testing
"Run nuclei on https://example.com"
"Test https://example.com for XSS vulnerabilities using dalfox"
"Check for common web vulnerabilities on https://example.com"

# Network Scanning
"Perform nmap scan on 192.168.1.1"
"Run a full port scan on example.com"
"Check for open ports on target network"
```

#### **Advanced Testing**
```bash
# Directory Enumeration
"Enumerate directories on https://example.com using gobuster"
"Find hidden directories on https://example.com"

# Parameter Discovery
"Find parameters for https://example.com/login using arjun"
"Discover hidden parameters on https://example.com"

# SQL Injection Testing
"Test https://example.com/login for SQL injection"
"Run sqlmap on https://example.com/search?q=test"
```

### **Advanced Features**

#### **AutoPilot Mode**
- Enable in Settings for automatic tool execution
- AI will run tools without manual confirmation
- Useful for automated reconnaissance workflows
- Follows logical testing progression

#### **Context Awareness**
- AI remembers previous scans and findings
- Suggests logical next steps based on results
- Maintains target information across sessions
- Builds comprehensive attack surface map

#### **Real-time Monitoring**
- Watch tool execution in real-time
- See progress indicators and status updates
- Get notified when scans complete
- View detailed execution logs

## ⚙️ **CONFIGURATION**

### **AI Model Configuration**

#### **Ollama (Local AI) - Recommended**
```bash
# Install Ollama on your system
curl -fsSL https://ollama.ai/install.sh | sh

# Download models
ollama pull llama2
ollama pull codellama

# BugPilot AI will auto-detect local Ollama installation
```

#### **OpenAI Configuration**
```python
# Get API key from https://platform.openai.com/
# In Settings > AI Model > OpenAI
API_KEY = "sk-your-openai-api-key-here"
MODEL = "gpt-4"  # or gpt-3.5-turbo
```

#### **Google Gemini Configuration**
```python
# Get API key from Google AI Studio
# In Settings > AI Model > Gemini
API_KEY = "your-gemini-api-key-here"
MODEL = "gemini-pro"
```

### **MCP Server Configuration**
```python
# In Settings > MCP Server
MCP_SERVER_URL = "http://YOUR_KALI_IP:5000"
TIMEOUT = 300  # seconds
RETRY_ATTEMPTS = 3

# On Kali Linux
python kali_server.py  # Starts server on port 5000
```

### **Tool Configuration**
```python
# Custom tool paths (if needed)
TOOL_PATHS = {
    "subfinder": "/usr/bin/subfinder",
    "nuclei": "/usr/bin/nuclei",
    "nmap": "/usr/bin/nmap"
}
```

## 🛡️ **SECURITY CONSIDERATIONS**

### **⚠️ Ethical Usage Guidelines**
- **ONLY test systems you own or have explicit written permission to test**
- Follow responsible disclosure practices for found vulnerabilities
- Comply with local laws and regulations regarding security testing
- Use for educational and authorized penetration testing only
- Respect rate limits and avoid causing service disruption

### **🔒 Network Security**
- MCP server communication uses HTTP (consider VPN/secure network)
- API keys are stored locally (secure your system appropriately)
- Scan results contain sensitive information (protect accordingly)
- Use secure networks when conducting tests

### **🛠️ Tool Safety**
- All tools execute with user permissions (no privilege escalation)
- Tools run in controlled environment with logging
- Results are logged for audit purposes
- No destructive operations without explicit confirmation

### **🔐 Code Protection**
This software contains protected and obfuscated code to ensure integrity and prevent unauthorized modifications. The protection includes:
- Encrypted application logic
- Anti-tampering mechanisms
- Secure tool execution environment
- Protected AI model integration

## 🔍 **TROUBLESHOOTING**

### **Common Issues & Solutions**

#### **AI Not Executing Tools**
```
Problem: AI provides fake responses instead of using EXECUTE_TOOL format
Solution: 
1. Check AI model configuration in Settings
2. Verify API keys are correct
3. Ensure internet connection for cloud models
4. Try switching to Ollama for local processing
```

#### **MCP Server Connection Failed**
```
Problem: Cannot connect to Kali MCP server
Solution:
1. Verify server is running: python kali_server.py
2. Check IP address and port in settings (default: port 5000)
3. Ensure firewall allows connection
4. Test connectivity: curl http://KALI_IP:5000/health
5. Check network connectivity between systems
```

#### **Tool Execution Errors**
```
Problem: Security tools fail to execute
Solution:
1. Verify tools are installed on target system
2. Check tool permissions and executable paths
3. Review error messages in Activity tab
4. Test tools manually: subfinder -d example.com
5. Update tools to latest versions
```

#### **Build/Installation Issues**
```
Problem: PyInstaller fails or dependencies missing
Solution:
1. Use Python 3.9 instead of newer versions
2. Use PyInstaller 5.13.2 specifically
3. Create clean virtual environment
4. Install dependencies one by one if needed
5. Check system architecture compatibility
```

#### **Performance Issues**
```
Problem: Application runs slowly or freezes
Solution:
1. Increase system RAM (8GB recommended)
2. Use local Ollama instead of cloud AI
3. Reduce concurrent tool executions
4. Clear old scan results and logs
5. Check antivirus interference
```

### **Debug Mode**
```bash
# Enable debug logging
python bugpilot_ai.py --debug

# Check application logs
tail -f bugpilot_ai.log

# Verbose MCP server logging
python kali_server.py --verbose
```

## 📊 **PERFORMANCE & OPTIMIZATION**

### **System Requirements**
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | Windows 10, Linux, macOS | Windows 11, Kali Linux |
| **RAM** | 4GB | 8GB+ |
| **Storage** | 500MB | 2GB+ (for results) |
| **CPU** | Dual-core | Quad-core+ |
| **Network** | Broadband | High-speed internet |

### **Performance Tips**
- **Use Local AI:** Ollama provides faster responses than cloud APIs
- **Optimize Network:** Configure MCP server on local network for speed
- **Manage Results:** Regular cleanup of old scan results improves performance
- **Concurrent Limits:** Adjust tool execution limits based on system capacity
- **Resource Monitoring:** Monitor CPU and memory usage during large scans

## 🔄 **UPDATES & MAINTENANCE**

### **Updating BugPilot AI**
```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Rebuild executable if needed
pyinstaller --onefile --windowed --icon=bugpilot-logo.ico --name=BugPilotAI bugpilot_ai.py
```

### **Updating Security Tools**
```bash
# On Kali Linux
sudo apt update && sudo apt upgrade

# Update Go-based tools
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

# Update Python tools
pip install --upgrade sqlmap
```

### **Backup & Restore**
```bash
# Backup configuration and results
mkdir backup
cp -r results/ backup/
cp config.json backup/
cp scan_history.db backup/

# Restore from backup
cp -r backup/results/ .
cp backup/config.json .
cp backup/scan_history.db .
```

## 🤝 **CONTRIBUTING**

### **How to Contribute**
1. **Fork the Repository**
   ```bash
   git fork https://github.com/letchupkt/BugPilot-Ai.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/new-tool-integration
   ```

3. **Make Changes**
   - Add new security tools
   - Improve AI model integration
   - Enhance UI/UX features
   - Fix bugs and issues

4. **Submit Pull Request**
   - Include detailed description
   - Add tests for new features
   - Follow coding standards
   - Update documentation

### **Development Guidelines**
- Follow PEP 8 coding standards
- Add comprehensive comments
- Include error handling
- Write unit tests for new features
- Update documentation

### **Bug Reports & Feature Requests**
- Use GitHub Issues for bug reports
- Include system information and error logs
- Provide steps to reproduce issues
- Suggest new security tools to integrate
- Request AI model improvements

## 📄 **LICENSE & LEGAL**

**© 2025 LAKSHMIKANTHAN K (letchupkt) - Enhanced MCP Kali Server**

This software is provided for **educational and authorized security testing purposes only**. 

### **Terms of Use**
- Users are responsible for complying with applicable laws
- Obtain proper authorization before testing any systems
- Follow responsible disclosure for discovered vulnerabilities
- Respect system owners and service providers
- Use only for legitimate security research and testing

### **Disclaimer**
- Software provided "as-is" without warranties
- Authors not responsible for misuse or damages
- Users assume all risks and responsibilities
- Compliance with local laws is user's responsibility

## 🙏 **ACKNOWLEDGMENTS**

### **Special Thanks**
- **Security Tools Developers:** Thanks to all open-source security tool creators
- **AI Model Providers:** OpenAI, Google, and Ollama teams for AI capabilities
- **PyQt5 Team:** For excellent GUI framework
- **MCP Protocol:** For enabling seamless tool integration
- **Security Community:** For continuous feedback and improvements

### **Inspiration**
- ProjectDiscovery for innovative security tools
- OWASP for security testing methodologies
- Bug bounty community for real-world testing scenarios
- Penetration testing professionals for workflow insights

## 📞 **SUPPORT & CONTACT**

### **Get Help**
- **GitHub Issues:** [Report bugs and request features](https://github.com/letchupkt/BugPilot-Ai/issues)
- **Documentation:** Check this README and inline help
- **Community:** Join discussions in GitHub Discussions

### **Author Information**
- **Name:** LAKSHMIKANTHAN K (letchupkt)
- **GitHub:** [@letchupkt](https://github.com/letchupkt)
- **Repository:** [BugPilot-Ai](https://github.com/letchupkt/BugPilot-Ai)

### **Professional Services**
For enterprise support, custom integrations, or professional security testing services, please contact through GitHub.

---

## 🌟 **STAR THE PROJECT**

If BugPilot AI helps you in your security testing journey, please consider:
- ⭐ **Starring the repository** on GitHub
- 🍴 **Forking** to contribute improvements
- 📢 **Sharing** with the security community
- 🐛 **Reporting bugs** to help improve the tool

---

**🚀 Happy Bug Hunting with BugPilot AI! 🐛**

*Professional security testing made intelligent, efficient, and accessible.*

**Transform your security testing workflow with AI-powered automation!**
