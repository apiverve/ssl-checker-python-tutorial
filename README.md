# SSL Certificate Checker | APIVerve API Tutorial

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![Python](https://img.shields.io/badge/Python-3.7+-3776ab)](https://python.org)
[![APIVerve | SSL Checker](https://img.shields.io/badge/APIVerve-SSL_Checker-purple)](https://apiverve.com/marketplace/sslchecker?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial)

A Python CLI tool that checks SSL certificates for any domain. View certificate details, expiry dates, and security status.

![Screenshot](https://raw.githubusercontent.com/apiverve/ssl-checker-python-tutorial/main/screenshot.jpg)

---

### Get Your Free API Key

This tutorial requires an APIVerve API key. **[Sign up free](https://dashboard.apiverve.com?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial)** - no credit card required.

---

## Features

- Check SSL certificates for any domain
- View certificate expiry with countdown
- See issuer and subject details
- Visual status indicators (valid/warning/expired)
- Protocol and cipher information
- Interactive mode or command-line arguments

## Quick Start

1. **Clone this repository**
   ```bash
   git clone https://github.com/apiverve/ssl-checker-python-tutorial.git
   cd ssl-checker-python-tutorial
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API key**

   Open `checker.py` and replace the API key:
   ```python
   API_KEY = 'your-api-key-here'
   ```

4. **Run the checker**

   Interactive mode:
   ```bash
   python checker.py
   ```

   Command line mode:
   ```bash
   python checker.py google.com
   ```

## Usage Examples

### Check a domain
```bash
$ python checker.py github.com

==================================================
  SSL Certificate Check: github.com
==================================================

  ✅ Status: Valid
  ⏰ Expires in: 245 days

  📋 Certificate Details:
  ----------------------------------------------
  Subject:      github.com
  Issuer:       DigiCert Inc
  Valid From:   2024-03-15T00:00:00Z
  Valid To:     2025-03-14T23:59:59Z
  Protocol:     TLSv1.3
  Cipher:       TLS_AES_128_GCM_SHA256
==================================================
```

### Certificate expiring soon
```
  ⚠️ Status: Valid
  ⏰ Expires in: 12 days (WARNING)
```

### Expired certificate
```
  ❌ Status: Invalid
  ⏰ Certificate: EXPIRED
```

## Project Structure

```
ssl-checker-python-tutorial/
├── checker.py          # Main Python script
├── requirements.txt    # Dependencies (requests)
├── screenshot.jpg      # Preview image
├── LICENSE             # MIT license
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## How It Works

1. User provides a domain name
2. Script cleans and validates the input
3. API checks the SSL certificate
4. Script calculates days until expiry
5. Results displayed with status indicators

### The API Call

```python
response = requests.get(
    'https://api.apiverve.com/v1/sslchecker',
    params={'domain': domain},
    headers={'x-api-key': API_KEY}
)
```

## API Reference

**Endpoint:** `GET https://api.apiverve.com/v1/sslchecker`

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `domain` | string | Yes | Domain to check (e.g., "google.com") |

**Example Response:**

```json
{
  "status": "ok",
  "error": null,
  "data": {
    "valid": true,
    "issuer": "DigiCert Inc",
    "subject": "github.com",
    "validFrom": "2024-03-15T00:00:00Z",
    "validTo": "2025-03-14T23:59:59Z",
    "daysRemaining": 245,
    "protocol": "TLSv1.3",
    "cipher": "TLS_AES_128_GCM_SHA256",
    "serialNumber": "0A1B2C3D..."
  }
}
```

## Use Cases

- **DevOps monitoring** - Check certificate expiry dates
- **Security audits** - Verify SSL configuration
- **Website maintenance** - Prevent expired certificate downtime
- **Compliance checking** - Ensure proper SSL setup
- **Domain management** - Monitor multiple domains

## Customization Ideas

- Add email alerts for expiring certificates
- Monitor multiple domains from a list
- Save results to CSV/JSON
- Build a web dashboard
- Integrate with Slack/Discord notifications
- Add scheduling with cron

## Related APIs

Explore more APIs at [APIVerve](https://apiverve.com/marketplace?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial):

- [DNS Lookup](https://apiverve.com/marketplace/dnslookup?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial) - Check DNS records
- [WHOIS Lookup](https://apiverve.com/marketplace/whoislookup?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial) - Domain registration info
- [Website Screenshot](https://apiverve.com/marketplace/webscreenshots?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial) - Capture website screenshots

## License

MIT - see [LICENSE](LICENSE)

## Links

- [Get API Key](https://dashboard.apiverve.com?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial) - Sign up free
- [APIVerve Marketplace](https://apiverve.com/marketplace?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial) - Browse 300+ APIs
- [SSL Checker API](https://apiverve.com/marketplace/sslchecker?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial) - API details
