import requests
import json
import random
import time  # Importing the time module for sleep function

def call_rpc_near(url):
    try:
        payload = {
            "jsonrpc": "2.0",
            "id": "HappyCuanAirdrop",
            "method": "block",
            "params": {"finality": "final"}
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            block_height = data.get("result", {}).get("header", {}).get("height")
            if block_height is not None:
                print(f"NEAR RPC has been called - Block Height: {block_height}")
            else:
                print("Error: Block height not found in response.")
        else:
            print(f"Error in NEAR RPC: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error in NEAR RPC: {e}")

if __name__ == "__main__":
    urls = [
        "https://near.lava.build/lava-referer-b3ebd262-006d-4555-8273-6d1508c4e92d/",
        "https://near-testnet.lava.build/lava-referer-b3ebd262-006d-4555-8273-6d1508c4e92d/",
   
    ]

    while True:
        for url in urls:
            call_rpc_near(url)
            interval = random.randint(10, 20)  # Adjust interval as needed
            print(f"Waiting for {interval} seconds before the next call.")
            time.sleep(interval)
        print("Completed cycle of calling all URLs.\n")
