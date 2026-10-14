import requests
from urllib.parse import unquote

# url where the vulnerable app is running locally
BASE_URL = "http://localhost:5000/search?q="

# Payloads to try against the search box
payloads = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(2)>",
    "%3Csvg%2Fonload%3Dalert(3)%3E"  # Encoded url so it tests if the encoded stuff still gets caught
]


def test_payload(payload):
    """
    Sends one payload to the search endpoint and checks if it comes
    back in the response (meaning it got reflected = vulnerable).
    """
    try:
        full_url = BASE_URL + payload
        response = requests.get(full_url, timeout=5)
        '''make sure the server gave a good response before checking anything. A bad status code should not be treated as secure'''
        if response.status_code != 200:
            print(f"[!]Non-200 response for payload: {payload}"
                  f"(status: {response.status_code})")
            return False

        response_text = response.text

        '''the app decodes the url before it puts it in the page, so an
        encoded payload like %3Csvg... actually shows up as <svg...>
        in the response. checking just the raw payload wasn't enough,
        had to also check the decoded version or it missed payload 3 '''
        candidates = {payload, unquote(payload)}
        is_reflected = any(c in response_text for c in candidates)

        if is_reflected:
            print(f"[VULNERABLE] Payload reflected: {payload}")
        else:
            print(f"[SECURE]     Payload not reflected: {payload}")

        return is_reflected

    except requests.exceptions.RequestException as e:
        # don't want one bad request to kill the whole scan, so just
        # print the error and keep going
        print(f"[!] Request failed for payload: {payload}")
        print(f"    Error: {e}")
        return False


def main():
    print("\n[+] Starting web vulnerability scan...\n")

    total = len(payloads)
    vulnerable_count = 0

    # loop through every payload
    for payload in payloads:
        if test_payload(payload):
            vulnerable_count += 1

    print("\n[+] Scan complete.")
    print(f"[+] Summary: {vulnerable_count} of {total} "
          f"payloads flagged as vulnerable.\n")


if __name__ == "__main__":
    main()
