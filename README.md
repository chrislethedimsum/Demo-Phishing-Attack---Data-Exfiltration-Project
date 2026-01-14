# Demo Phishing & Data Exfiltration Project

## ⚠️ Disclaimer

**This project is strictly for educational and research purposes only.** 
It demonstrates phishing attack techniques and social engineering tactics in a controlled environment. 

**Unauthorized access to computer systems is illegal.** 
This code should only be used:
- In authorized security research environments
- With explicit written permission from the target organization
- For educational demonstrations in classroom/lab settings
- For improving security awareness and defensive measures

Misuse of this code for illegal activities is strictly prohibited and subject to legal consequences.

---

## Project Overview

This project demonstrates two key components of a phishing attack campaign:

1. **Phishing Server** - A fake Shopee-like login page that captures user credentials
<img width="1440" height="887" alt="Fake Shoppe Wepage" src="https://github.com/user-attachments/assets/6c5fa39e-95ab-4370-85d9-1e631806dfe7" />
Figure 1. Fake Shopee-login (non-production).

<img width="342" height="450" alt="Data is collected after users submit" src="https://github.com/user-attachments/assets/3e8e391e-39d7-4ab6-b56d-97f0d333cbe5" />
Figure 2. Data is collected after users submit.
3. **Data Exfiltration** - Sending harvested credentials via email to simulate attacker communication
<img width="1438" height="744" alt="Email is sent for new targets" src="https://github.com/user-attachments/assets/77fa3244-700f-4456-931c-b98943320293" />
Figure 3. Email is sent by attackers using collected data.

The project serves as a hands-on learning tool for understanding how phishing attacks work and how organizations can defend against them.

---

## Project Structure

```
demostrations/
├── attacker/
│   ├── phishing_message.py          # Phishing email template
│   └── demo_followup_email.py       # Email exfiltration script
├── server/
│   ├── server.js                    # Express.js server
│   ├── package.json                 # Node.js dependencies
│   ├── credentials.log              # Captured credentials (auto-generated)
│   └── views/
│       ├── fakelogin.html           # Fake Shopee login page
│       └── fakelogin_files/         # CSS/JS assets for the fake page
```

---

## Demonstration 1: Phishing Server

### Overview
The phishing server hosts a convincing replica of a popular e-commerce platform's login page (Shopee Vietnam). When users enter their credentials, the data is captured and logged.

### Key Files
- **server.js** - Express.js server handling HTTP requests
- **fakelogin.html** - Fake login interface with CSS/JS styling
- **credentials.log** - Log file storing captured usernames and passwords

### How It Works

1. **Server Setup**
   - Serves the fake login page at `http://localhost:3000/buyer/login`
   - Static files (CSS, JavaScript, images) are served from the `views/` directory
   - Form submissions are captured at the `/login` POST endpoint

2. **Credential Capture**
   - Users enter credentials in the fake login form
   - Form data is captured with fields: `loginKey` (username) and `password`
   - All submissions are logged to `credentials.log` with timestamp

3. **Server Response**
   - After credential capture, user is redirected to `https://shopee.vn/`
   - This creates a more realistic phishing experience

### Setup & Usage

```bash
# Navigate to server directory
cd server/

# Install dependencies
npm install

# Start the server
node server.js
```

Server runs on: `http://localhost:3000`

### Example Credentials Log Output
```
[DEMO ONLY]
Username: bakinoh373@atinjo.com
Password: Bakinoh373
Time: 2026-01-14T06:06:04.197Z
---------------------------
```

---

## Demonstration 2: Email Data Exfiltration

### Overview
After harvesting credentials through the phishing server, attackers often send follow-up emails to victims. This demonstration shows how exfiltrated data can be sent to attacker-controlled email addresses.

### Key Files
- **demo_followup_email.py** - Python script to send phishing follow-up emails
- **phishing_message.py** - Email template for phishing campaigns

### How It Works

1. **Credential Extraction**
   - Reads the `credentials.log` file from the phishing server
   - Extracts email addresses using regex pattern matching
   - Filters emails based on whitelist (demo/test domains only)

2. **Email Sending**
   - Uses Brevo SMTP API for reliable email delivery
   - Sends emails with security-themed subject lines
   - Each email is logged with status (OK/ERROR)

3. **Safety Features**
   - Whitelist filter restricts emails to demo domains:
     - `@atinjo.com`
     - `@testmail.com`
   - Prevents accidental targeting of real email addresses
   - Provides detailed error logging for debugging

### Setup & Usage

```bash
# Navigate to attacker directory
cd attacker/

# Install Python dependencies
pip install requests

# Run the email exfiltration script
python3 demo_followup_email.py
```

### Configuration

Edit `demo_followup_email.py` to configure:
- **BREVO_API_KEY** - Your Brevo email service API key
- **FROM_EMAIL** - Sender email address (must be verified in Brevo)
- **Email content** - Modify the htmlContent section for different messages

### Example Output
```
[INFO] Found 4 email(s) in credentials.log
[SKIP] poorguy123@rich.com not in demo allowlist
[SKIP] moneyman@poor.com not in demo allowlist
[OK] Demo email sent to bakinoh373@atinjo.com
```

---

## Complete Workflow

### Step 1: Start Phishing Server
```bash
cd server/
npm install
node server.js
```

### Step 2: Direct Victims to Fake Login Page
Send phishing emails or social engineering messages directing users to `http://localhost:3000/`

### Step 3: Collect Credentials
Users enter credentials on the fake login page. Data is saved to `credentials.log`

### Step 4: Exfiltrate Data
```bash
cd attacker/
pip install requests
python3 demo_followup_email.py
```

The script sends follow-up emails to harvested email addresses.

---

## Technical Details

### Technologies Used
- **Backend**: Node.js, Express.js
- **Frontend**: HTML, CSS, JavaScript
- **Email Service**: Brevo SMTP API
- **Language**: Python 3, JavaScript

### API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/buyer/login` | GET | Serve fake login page |
| `/login` | POST | Capture credentials |
| `https://shopee.vn/` | GET | Redirect after "successful" login |

### Credential Fields Captured
- **loginKey** - Username, email, or phone number
- **password** - User's password
- **timestamp** - When credentials were submitted

---

## Detection & Prevention

### How Organizations Can Defend:

1. **Email Security**
   - SPF, DKIM, DMARC authentication
   - Email filtering and sandboxing
   - Suspicious URL detection

2. **User Education**
   - Phishing awareness training
   - Recognizing fake login pages
   - Reporting suspicious emails

3. **Technical Measures**
   - Multi-factor authentication (MFA)
   - Password managers
   - Browser security warnings for phishing sites

4. **Monitoring**
   - Credential monitoring services
   - Network traffic analysis
   - Unauthorized login alerts

---

## Learning Objectives

After studying this project, you should understand:

1. ✅ How phishing attacks are structured
2. ✅ How fake login pages capture credentials
3. ✅ How attackers exfiltrate and distribute stolen data
4. ✅ Social engineering techniques used in phishing campaigns
5. ✅ Defense mechanisms against phishing attacks

---

## Requirements

### For Phishing Server:
- Node.js 14+ 
- npm or yarn
- Modern web browser

### For Email Exfiltration:
- Python 3.6+
- `requests` library
- Brevo email service account
- API key with SMTP permissions

---

## Installation Summary

```bash
# Install Node.js dependencies
cd server/
npm install

# Install Python dependencies
cd ../attacker/
pip install requests
```

---

## Ethical Considerations

⚠️ **Remember:**
- Only run this in **authorized environments**
- Obtain **explicit written consent** before any testing
- Use **isolated lab networks** to prevent real harm
- Document all activities for **audit trails**
- Comply with **local laws and regulations**
- Report findings **responsibly** to affected organizations

---

## Support & Further Learning

For more information on cybersecurity and phishing:
- OWASP Top 10 Web Application Security Risks
- NIST Cybersecurity Framework
- Phishing simulation tools (Gophish, King Phisher)
- Security research conferences and publications

---

## License

This project is provided for educational purposes. Users are responsible for compliance with applicable laws and regulations.

---

**Created**: January 2026  
**Purpose**: Cybersecurity Research & Education  
**Status**: Demo/Educational Use Only
