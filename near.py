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
        "https://near.lava.build/lava-referer-a141e6b6-3c73-4556-be82-a04d6f219e8e/",
        "https://near-testnet.lava.build/lava-referer-a141e6b6-3c73-4556-be82-a04d6f219e8e/",
        "https://near.lava.build/lava-referer-fbd614bb-40a2-46c0-9f86-675e78683794/",
        "https://near-testnet.lava.build/lava-referer-fbd614bb-40a2-46c0-9f86-675e78683794/",
        "https://near.lava.build/lava-referer-fd9e82b1-645a-472f-b741-3c15df5dba76/",
        "https://near-testnet.lava.build/lava-referer-fd9e82b1-645a-472f-b741-3c15df5dba76/",
        "https://near.lava.build/lava-referer-b1c0bcc3-6f5a-4b6d-afc6-abf871cb75e5/",
        "https://near-testnet.lava.build/lava-referer-b1c0bcc3-6f5a-4b6d-afc6-abf871cb75e5/",
        "https://near.lava.build/lava-referer-091c45cb-8147-4d88-bcb8-999809246d46/",
        "https://near-testnet.lava.build/lava-referer-091c45cb-8147-4d88-bcb8-999809246d46/",
        "https://near.lava.build/lava-referer-9bb70aef-60be-4e76-b14e-95f2a45ed686/",
        "https://near-testnet.lava.build/lava-referer-9bb70aef-60be-4e76-b14e-95f2a45ed686/",
        "https://near.lava.build/lava-referer-21317879-982f-4a72-97fc-4a291e04c123/",
        "https://near-testnet.lava.build/lava-referer-21317879-982f-4a72-97fc-4a291e04c123/"
    ]

    while True:
        for url in urls:
            call_rpc_near(url)
            interval = random.randint(10, 20)  # Adjust interval as needed
            print(f"Waiting for {interval} seconds before the next call.")
            time.sleep(interval)
        print("Completed cycle of calling all URLs.\n")
