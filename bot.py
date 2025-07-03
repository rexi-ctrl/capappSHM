import os
import time
import random
import json
from web3 import Web3
from dotenv import load_dotenv
from telegram import Bot

# === LOAD ENV ===
load_dotenv()
RPC_URL = "https://carrot.megaeth.com/rpc"
CONTRACT_ADDRESS = "0xe9b6e75c243b6100ffcb1c66e8f78f96feea727f"
MINT_COUNT = int(os.getenv("MINT_COUNT", 3))
TOKEN_AMOUNT = int(os.getenv("TOKEN_AMOUNT", 1000))
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

DELAY_MIN = 10
DELAY_MAX = 20

# === TELEGRAM ===
tg_bot = Bot(token=BOT_TOKEN)

def send_telegram(msg):
    try:
        tg_bot.send_message(chat_id=CHAT_ID, text=msg)
    except Exception as e:
        print(f"❌ Gagal kirim Telegram: {e}")

# === ABI KONTRAK ===
ABI = [
    {
        "inputs": [
            {"internalType": "address", "name": "receiver", "type": "address"},
            {"internalType": "uint256", "name": "amount", "type": "uint256"}
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    }
]

# === SETUP WEB3 ===
w3 = Web3(Web3.HTTPProvider(RPC_URL))
contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=ABI)

if not w3.is_connected():
    raise Exception("❌ Gagal konek ke RPC")

# === LOAD WALLET LIST ===
with open('wallets.json') as f:
    wallets = json.load(f)

# === BALANCE CHECK ===
def get_balance(address):
    try:
        balance_wei = contract.functions.balanceOf(Web3.to_checksum_address(address)).call()
        return w3.from_wei(balance_wei, 'ether')
    except:
        return "N/A"

# === MINT FUNCTION ===
def mint_tokens(private_key, address):
    print(f"\n🔑 Wallet: {address}")
    send_telegram(f"🚀 Mulai mint untuk wallet: {address[:6]}...{address[-4:]}")
    for i in range(MINT_COUNT):
        try:
            nonce = w3.eth.get_transaction_count(address)
            tx = contract.functions.mint(address, Web3.to_wei(TOKEN_AMOUNT, 'ether')).build_transaction({
                'from': address,
                'nonce': nonce,
                'gas': 250000,
                'gasPrice': w3.to_wei('0.01', 'gwei'),
            })

            signed_tx = w3.eth.account.sign_transaction(tx, private_key)
            tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
            print(f"🔃 Mint ke-{i+1}: TX → {w3.to_hex(tx_hash)}")

            receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
            status = "✅ SUCCESS" if receipt.status == 1 else "❌ FAILED"
            print(f"   ↳ Status TX: {status}")

            balance = get_balance(address)
            print(f"   💰 Saldo cUSD: {balance}\n")

            send_telegram(f"{status} TX ke-{i+1}\nHash: {w3.to_hex(tx_hash)}\nSaldo: {balance} cUSD")

        except Exception as e:
            print(f"🚨 Error TX ke-{i+1}: {e}")
            send_telegram(f"❌ ERROR TX ke-{i+1}: {e}")
            time.sleep(5)

        delay = random.randint(DELAY_MIN, DELAY_MAX)
        print(f"⏳ Delay {delay} detik...\n")
        time.sleep(delay)

    send_telegram(f"✅ Mint selesai untuk wallet {address[:6]}...{address[-4:]}")


# === RUN UNTUK SEMUA WALLET ===
for w in wallets:
    mint_tokens(w["private_key"], Web3.to_checksum_address(w["address"]))

print("\n🎉 Semua wallet selesai!")
send_telegram("🎉 Semua mint selesai untuk seluruh wallet!")
