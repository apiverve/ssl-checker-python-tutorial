#!/usr/bin/env python3
"""
SSL Certificate Checker - Tutorial Example

A simple CLI tool that checks SSL certificates using the APIVerve API.
https://apiverve.com/marketplace/sslchecker
"""

import requests
import sys
from datetime import datetime

# ============================================
# CONFIGURATION - Add your API key here
# Get a free key at: https://dashboard.apiverve.com
# ============================================
API_KEY = 'your-api-key-here'
API_URL = 'https://api.apiverve.com/v1/sslchecker'


def check_ssl(domain: str) -> dict:
    """
    Check SSL certificate for a domain.

    Args:
        domain: The domain to check (e.g., google.com)

    Returns:
        Dictionary with certificate details or error
    """
    if API_KEY == 'your-api-key-here':
        return {'error': 'API key not configured. Add your key to checker.py'}

    # Clean domain input
    domain = domain.strip().lower()
    domain = domain.replace('https://', '').replace('http://', '')
    domain = domain.split('/')[0]

    try:
        response = requests.get(
            API_URL,
            params={'domain': domain},
            headers={'x-api-key': API_KEY}
        )

        data = response.json()

        if data.get('status') == 'ok':
            cert = data['data']
            # Extract issuer CN (Common Name)
            issuer = cert.get('issuer', {})
            issuer_cn = issuer.get('CN', 'Unknown') if isinstance(issuer, dict) else str(issuer)

            # Extract subject CN
            subject = cert.get('subject', {})
            subject_cn = subject.get('CN', domain) if isinstance(subject, dict) else str(subject)

            return {
                'success': True,
                'domain': cert.get('domain', domain),
                'issuer': issuer_cn,
                'subject': subject_cn,
                'validFrom': cert.get('valid_from'),
                'validTo': cert.get('valid_to'),
                'serialNumber': cert.get('serialNumber'),
                'bits': cert.get('bits'),
                'ca': cert.get('ca', False)
            }
        else:
            return {'error': data.get('error', 'SSL check failed')}

    except requests.RequestException as e:
        return {'error': f'API request failed: {str(e)}'}
    except (KeyError, ValueError) as e:
        return {'error': f'Invalid response: {str(e)}'}


def get_status_icon(has_cert: bool) -> str:
    """Get status icon based on certificate presence."""
    return '✅' if has_cert else '❌'


def print_result(result: dict):
    """Print SSL check result in a formatted way."""
    if 'error' in result:
        print(f"\n{'='*50}")
        print(f"  ❌ Error: {result['error']}")
        print(f"{'='*50}\n")
        return

    icon = get_status_icon(result.get('success', False))

    print(f"\n{'='*50}")
    print(f"  SSL Certificate Check: {result['domain']}")
    print(f"{'='*50}")

    print(f"\n  {icon} Certificate Found")

    print(f"\n  📋 Certificate Details:")
    print(f"  {'-'*46}")
    print(f"  Subject:      {result.get('subject', 'N/A')}")
    print(f"  Issuer:       {result.get('issuer', 'N/A')}")

    if result.get('validFrom'):
        print(f"  Valid From:   {result['validFrom']}")
    if result.get('validTo'):
        print(f"  Valid To:     {result['validTo']}")

    if result.get('bits'):
        print(f"  Key Size:     {result['bits']} bits")
    if result.get('serialNumber'):
        serial = result['serialNumber']
        if len(serial) > 40:
            serial = serial[:40] + '...'
        print(f"  Serial:       {serial}")

    print(f"{'='*50}\n")


def interactive_mode():
    """Run the checker in interactive mode."""
    print("\n" + "="*50)
    print("  SSL Certificate Checker")
    print("  Powered by APIVerve")
    print("="*50)
    print("\nCheck SSL certificates for any domain")
    print("Type 'quit' to exit\n")

    while True:
        try:
            domain = input("Enter domain (e.g., google.com): ").strip()
            if domain.lower() == 'quit':
                break

            if not domain:
                print("Please enter a domain.\n")
                continue

            result = check_ssl(domain)
            print_result(result)

        except KeyboardInterrupt:
            print("\n")
            break

    print("Goodbye!\n")


def main():
    """Main entry point."""
    if len(sys.argv) == 2:
        # Command line mode: python checker.py google.com
        domain = sys.argv[1]
        result = check_ssl(domain)
        print_result(result)
    else:
        # Interactive mode
        interactive_mode()


if __name__ == '__main__':
    main()
