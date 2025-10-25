# 🐛 BugPilot AI - AI-Powered Security Assistant
<img width="1700" height="460" alt="github-header-banner (2)" src="https://github.com/user-attachments/assets/376c65ed-48b3-40a3-a7c2-9701fd941e2a" />

[![GitHub stars](https://img.shields.io/github/stars/letchupkt/BugPilot-Ai?style=social)](https://github.com/letchupkt/BugPilot-Ai/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/letchupkt/BugPilot-Ai?style=social)](https://github.com/letchupkt/BugPilot-Ai/network)
[![GitHub issues](https://img.shields.io/github/issues/letchupkt/BugPilot-Ai)](https://github.com/letchupkt/BugPilot-Ai/issues)
[![License](https://img.shields.io/badge/License-Educational-blue.svg)](LICENSE)

**Version:** 2025.10.25  
**Author:** LAKSHMIKANTHAN K (letchupkt)  
**Enhanced MCP Kali Server**

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

### **🔧 Advanced Capabilities**
- **MCP Server Integration** - Connect to Kali Linux MCP server for remote tool execution
- **Fake Response Detection** - Warns when AI provides simulated results instead of real tool execution
- **Session Management** - Persistent conversation and scan history
- **Multi-target Support** - Handle multiple targets simultaneously

## 📁 **PROJECT STRUCTURE**

```
BugPilot-AI/
├── 📄 bugpilot_ai.py          # Main application file (Protected)
├── 📄 kali_server.py          # MCP Kali server (Protected)
├── 📄 install.py              # Installation helper script
├── 🖼️ bugpilot-logo.ico       # Application icon
├── 📄 requirements.txt        # Python dependencies
├── 📖 README.md               # This comprehensive documentation
```

## 🔧 **INSTALLATION & SETUP**

### **Prerequisites**
- **Python 3.9+** (Python 3.9 recommended for building executables)
- **Windows/Linux/macOS** (GUI optimized for Windows)
- **Kali Linux Server** (for MCP tools)
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
python3 kali_server.py

# Server will start on port 5000
# Configure the server URL in BugPilot AI Settings
```

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

```

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
- **InstaGram:** [@letchupkt](https://instagram.com/letchu_pkt)
- **Linkedin:** [@lakshmikanthank](https://linkedin.com/in/lakshmikanthank)


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



