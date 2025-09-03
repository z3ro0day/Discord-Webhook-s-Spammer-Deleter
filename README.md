# DISWEBSPAM (Educational Demo)

> ⚠️ **Disclaimer**  
> This project is for **educational and testing purposes only**.  
> Do **not** use it to spam, disrupt, or harass others. Misuse may result in account bans or violations of terms of service.  
> Always test only with your **own Discord webhooks** in a controlled environment.  

---

## 🐧 Setup on Kali Linux

1. **Update system packages:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Python 3 and pip (if not already installed):**
   ```bash
   sudo apt install python3 python3-pip -y
   ```

3. **Verify installation:**
   ```bash
   python3 --version
   pip3 --version
   ```

4. **Install required Python library (`requests`):**
   ```bash
   pip3 install requests
   ```

5. **Clone or download this project:**
   ```bash
   git clone https://github.com/yourusername/diswebspam.git
   cd diswebspam
   ```

6. **Run the script:**
   ```bash
   python3 script.py
   ```

---

## 📌 Overview
`DISWEBSPAM` is a Python 3 script that demonstrates:
- Sending HTTP requests to Discord webhooks
- Handling rate-limiting with retries
- Using multithreading to distribute tasks
- Building a simple command-line interface (CLI) menu system

Tested on **Kali Linux**, but it should run on any Linux distribution or OS with Python 3 installed.

---

## ⚙️ Requirements
- **Python 3.8+**
- `requests` (Python HTTP library)

Install dependencies with:

```bash
pip install requests
```

---

## 🚀 Usage

From the script menu:
- **[1] Paste Webhook** → enter your test Discord webhook URL  
- **[2] Send Messages** → specify number of messages and threads  
- **[3] Devs / Credits** → project credits  
- **[4] Exit** → quit program  

---

## 🖥️ Tested Environment
- **OS:** Kali Linux (Rolling)  
- **Python:** 3.11.2  
- **Dependencies:** `requests`  

---

## 🧪 Example (Safe Testing)
1. Create a **private Discord server** that you own.  
2. Generate a webhook (Server Settings → Integrations → Webhooks).  
3. Use that webhook URL in the script.  
4. Send a few messages to observe multithreading and rate-limit handling in action.  

---

## 👨‍💻 Credits
- Project: **DISWEBSPAM**  
- Author: [r8ck0](https://github.com/r8ck0)  
- Python 3 CLI, threading, and requests demo  

---
