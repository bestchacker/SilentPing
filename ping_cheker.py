import os
import sys

def ping(host):
    """
    Send a ping request to the specified host and print the result.
    """
    response = os.system(f"ping -c 4 {host}")
    if response == 0:
        print(f"✅ {host} is reachable.")
    else:
        print(f"❌ {host} is not reachable.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ping_checker.py <host>")
    else:
        ping(sys.argv[1])
