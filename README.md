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
- See issuer and subject details
- View validity dates
- Certificate key size
- Serial number information
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
$ python checker.py ebay.com

==================================================
  SSL Certificate Check: ebay.com
==================================================

  ✅ Certificate Found

  📋 Certificate Details:
  ----------------------------------------------
  Subject:      ebay.com
  Issuer:       Sectigo Public Server Authentication CA OV R36
  Valid From:   Jul 28 00:00:00 2025 GMT
  Valid To:     Jul 28 23:59:59 2026 GMT
  Key Size:     2048 bits
  Serial:       99F408949A6416EDC3B8F5EC77B2EBE5
==================================================
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
    "subject": {
      "C": "US",
      "ST": "California",
      "O": "eBay, Inc.",
      "CN": "ebay.com"
    },
    "issuer": {
      "C": "GB",
      "O": "Sectigo Limited",
      "CN": "Sectigo Public Server Authentication CA OV R36"
    },
    "valid_from": "Jul 28 00:00:00 2025 GMT",
    "valid_to": "Jul 28 23:59:59 2026 GMT",
    "serialNumber": "99F408949A6416EDC3B8F5EC77B2EBE5",
    "bits": 2048,
    "domain": "ebay.com"
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

## Free Plan Note

This tutorial works with the free APIVerve plan. Some APIs may have:
- **Locked fields**: Premium response fields return `null` on free plans
- **Ignored parameters**: Some optional parameters require a paid plan

The API response includes a `premium` object when limitations apply. [Upgrade anytime](https://dashboard.apiverve.com/plans) to unlock all features.

## License

MIT - see [LICENSE](LICENSE)

## Links

- [Get API Key](https://dashboard.apiverve.com?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial) - Sign up free
- [APIVerve Marketplace](https://apiverve.com/marketplace?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial) - Browse 300+ APIs
- [SSL Checker API](https://apiverve.com/marketplace/sslchecker?utm_source=github&utm_medium=tutorial&utm_campaign=ssl-checker-python-tutorial) - API details
