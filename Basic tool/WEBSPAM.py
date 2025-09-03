import requests
import time
import os
import threading

# Globals
WEBHOOK_URL = None
USERNAME = "DISWEB WEBHOOK"
MAX_MESSAGES = 1500


def clear():
    os.system("clear" if os.name == "posix" else "cls")


def banner():
    print(r"""
██╗    ██╗███████╗██████╗ ███████╗██████╗  █████╗ ███╗   ███╗
██║    ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║
██║ █╗ ██║█████╗  ██████╔╝███████╗██████╔╝███████║██╔████╔██║
██║███╗██║██╔══╝  ██╔══██╗╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
╚███╔███╔╝███████╗██████╔╝███████║██║     ██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
                                                             WEBSPAM
    """)


def send_message(content: str, username: str = USERNAME):
    if not WEBHOOK_URL:
        print("[!] No webhook set!")
        return False

    data = {"content": content, "username": username}
    while True:
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 204:  # Success
            return True

        elif response.status_code == 429:  # Rate limited
            retry_after = response.json().get("retry_after", 1)
            print(f"[!] Rate limited. Waiting {retry_after} sec...")
            time.sleep(retry_after)

        else:
            print(f"[!] Failed ({response.status_code}): {response.text}")
            return False


def spam_messages(msg, amount, threads=5):
    """
    Send messages using multiple threads.
    """
    if threads < 1:
        threads = 1

    sent = 0
    lock = threading.Lock()

    # Divide work between threads (even distribution)
    def worker(start, end):
        nonlocal sent
        for _ in range(start, end):
            if send_message(msg):
                with lock:
                    sent += 1
                    print(f"[+] Sent {sent}/{amount}")

    # Split message count across threads
    chunk = amount // threads
    remainder = amount % threads
    thread_list = []

    start = 0
    for i in range(threads):
        end = start + chunk + (1 if i < remainder else 0)
        if start >= end:
            break
        t = threading.Thread(target=worker, args=(start, end))
        t.start()
        thread_list.append(t)
        start = end

    for t in thread_list:
        t.join()

    print(f"[+] Done. Sent {sent} messages.")


def main_menu():
    global WEBHOOK_URL

    while True:
        clear()
        banner()
        print("=== DISWEBSPAM MENU ===")
        print("[1] Paste Webhook")
        print("[2] Send Messages (limit 1500, multithreaded)")
        print("[3] Devs / Credits")
        print("[4] Exit")
        choice = input("\nSelect an option: ")

        if choice == "1":
            WEBHOOK_URL = input("Enter Discord Webhook URL: ").strip()
            if WEBHOOK_URL:
                print("[+] Webhook set.")
            else:
                print("[!] Invalid webhook.")
            input("Press Enter to continue...")

        elif choice == "2":
            if not WEBHOOK_URL:
                print("[!] Please set a webhook first (Option 1).")
                input("Press Enter to continue...")
                continue

            try:
                amount = int(input(f"How many messages to send? (max {MAX_MESSAGES}): "))
                if amount > MAX_MESSAGES or amount < 1:
                    print(f"[!] Invalid amount. Must be between 1 and {MAX_MESSAGES}.")
                    input("Press Enter to continue...")
                    continue

                msg = input("Enter the message to send: ")
                threads = int(input("How many threads? (default 5): ") or 5)

                spam_messages(msg, amount, threads)

            except ValueError:
                print("[!] Invalid input.")
            input("Press Enter to continue...")

        elif choice == "3":
            clear()
            banner()
            print("=== Credits ===")
            print("(Made and runs with Python 3)")
            print("(Supported OS Kali Linux)")
            print("(Project: DISWEBSPAM)")
            print("(https://github.com/r8ck0)")
            input("\nPress Enter to return to menu...")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("[!] Invalid choice.")
            time.sleep(1)


if __name__ == "__main__":
    main_menu()
