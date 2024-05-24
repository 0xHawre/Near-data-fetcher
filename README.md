# Near-data-fetcher
This Python script fetches block height data from specified NEAR RPC endpoints. It makes repeated requests to the endpoints, logs the responses, and includes a timestamp for each request.

Prerequisites
Ensure you have Python and the requests package installed on your system.

Install Python
If Python is not already installed, you can install it using the following commands:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
Install Required Python Packages
```

Install the requests package using pip:

```bash
pip3 install requests
```

Setup
Clone the Repository:

```bash
git clone https://github.com/Hafxhak/Near-data-fetcher
cd Near-data-fetcher

```
Edit the Script:
Open the script in a text editor:

```bash
nano ETH.py
```
Replace the placeholder URLs in the urls list with your own NEAR RPC endpoint URLs. Example: first main-net then test-net
```python
urls = [
    "https://near.lava.build/lava-referer-your-unique-id/",  # replace with your RPC
    "https://near-testnet.lava.build/lava-referer-your-unique-id/",  # replace with your RPC
]
```
Save and exit the editor (for nano, press CTRL + X, then Y, and Enter).

Running the Script
Install and Use Screen:

Install screen to run the script in a detached session:

```bash
sudo apt install screen -y
screen -S near
```
Run the Script:

Execute the script using Python 3:

```bash
python3 near.py
```
Example Output
The script will log the response from the RPC endpoint along with the block height for each request. Example output:

```bash
NEAR RPC has been called - Block Height: 12345678
Waiting for 15 seconds before the next call.
Completed cycle of calling all URLs.
```
Detach from the Screen Session:

Detach from the screen session without stopping the script by pressing CTRL + A, then D.
