import re
import requests

BREVO_API_KEY = "CHANGE-API-KEY-HERE"
BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"

HEADERS = {
    "accept": "application/json",
    "api-key": BREVO_API_KEY,
    "content-type": "application/json"
}

FROM_EMAIL = {
    "email": "chrislethedimsum@gmail.com",
    "name": "ShopEZ Security Team (Demo)"
}

# --- STEP 1: Parse emails from credentials.log ---
def extract_emails(log_file="../server/credentials.log"):
    with open(log_file, "r") as f:
        content = f.read()

    emails = re.findall(r"Username:\s*([^\s]+@[^\s]+)", content)
    return list(set(emails))


# --- STEP 2: Send demo email ---
def send_demo_email(to_email):
    payload = {
        "sender": FROM_EMAIL,
        "to": [{"email": to_email}],
        "subject": "[Security Notice – Demo Simulation]",
        "htmlContent": """
        <p>This is a <b>security education demo</b>.</p>
        <p>Your account credentials were exposed due to a phishing attack simulation.</p>
        <p>This message demonstrates how attackers may follow up after a compromise.</p>
        <p><i>No real system or brand is involved.</i></p>
        """
    }

    try:
        response = requests.post(
            BREVO_API_URL,
            headers=HEADERS,
            json=payload,
            timeout=10
        )

        if response.status_code == 201:
            print(f"[OK] Demo email sent to {to_email}")
            return True
        else:
            print(f"[ERROR] {to_email} → Status {response.status_code}")
            print(f"[DEBUG] Response: {response.text}")
            return False
    except Exception as e:
        print(f"[ERROR] {to_email} → Exception: {str(e)}")
        return False


# --- STEP 3: Main flow ---
if __name__ == "__main__":
    emails = extract_emails()

    print(f"[INFO] Found {len(emails)} email(s) in credentials.log")

    for email in emails:
        # OPTIONAL SAFETY FILTER
        if email.endswith("@atinjo.com") or email.endswith("@testmail.com"):
            send_demo_email(email)
        else:
            print(f"[SKIP] {email} not in demo allowlist")
