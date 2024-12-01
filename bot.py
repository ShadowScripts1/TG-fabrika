import requests
import json
import time
from datetime import datetime, timedelta
import colorama
from colorama import Fore, Back, Style
import random  # For randomizing count

colorama.init(autoreset=True)

def print_welcome_message():
    print(Fore.WHITE + r"""
 ____  _   _    _    ____   _____        __
/ ___|| | | |  / \  |  _ \ / _ \ \      / /
\___ \| |_| | / _ \ | | | | | | \ \ /\ / / 
 ___) |  _  |/ ___ \| |_| | |_| |\ V  V /  
|____/|_| |_/_/   \_\____/ \___/  \_/\_/   
 ____   ____ ____  ___ ____ _____ _____ ____  ____  
/ ___| / ___|  _ \|_ _|  _ \_   _| ____|  _ \/ ___| 
\___ \| |   | |_) || || |_) || | |  _| | |_) \___ \ 
 ___) | |___|  _ < | ||  __/ | | | |___|  _ < ___) |
|____/ \____|_| \_\___|_|    |_| |_____|_| \_\____/ 
          """)
    print(Fore.GREEN + Style.BRIGHT + "Shadow Scripters Friends Factory Bot")
    print(Fore.YELLOW + Style.BRIGHT + "Telegram: https://t.me/shadowscripters")

def load_accounts():
    with open('data.txt', 'r') as file:
        return [line.strip() for line in file if line.strip()]

def login_telegram(payload):
    url = "https://api.ffabrika.com/api/v1/auth/login-telegram"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
    }
    data = {"webAppData": {"payload": payload}}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['data']['accessToken']['value']
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Login failed: {str(e)}")
        return None

def get_profile(token):
    url = "https://api.ffabrika.com/api/v1/profile"
    headers = {"cookie": f"acc_uid={token}"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to retrieve profile: {str(e)}")
        return None

def get_factory_details(token, factory_id):
    url = f"https://api.ffabrika.com/api/v1/factories/{factory_id}"
    headers = {"cookie": f"acc_uid={token}"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to retrieve factory data: {str(e)}")
        return None

def collect_factory_rewards(token):
    url = "https://api.ffabrika.com/api/v1/factories/my/rewards/collection"
    headers = {"cookie": f"acc_uid={token}"}
    
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 204:
            print(Fore.GREEN + "Rewards successfully collected.")
        else:
            print(Fore.YELLOW + f"Reward collection status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to collect rewards: {str(e)}")

def assign_worker_tasks(token, task_type="longest"):
    url = "https://api.ffabrika.com/api/v1/factories/my/workers/tasks/assignment"
    headers = {
        "cookie": f"acc_uid={token}",
        "Content-Type": "application/json"
    }
    payload = {"type": task_type}
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 204:
            print(Fore.GREEN + "Workers successfully assigned.")
        else:
            print(Fore.YELLOW + f"Task assignment status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to assign worker tasks: {str(e)}")

def get_tasks(token):
    url = "https://api.ffabrika.com/api/v1/tasks"
    headers = {"cookie": f"acc_uid={token}"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to retrieve tasks: {str(e)}")
        return None

def get_daily_tasks(token):
    url = "https://api.ffabrika.com/api/v1/daily-tasks"
    headers = {"cookie": f"acc_uid={token}"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to retrieve daily tasks: {str(e)}")
        return None

def complete_task(token, task_id):
    url = f"https://api.ffabrika.com/api/v1/tasks/completion/{task_id}"
    headers = {"cookie": f"acc_uid={token}"}
    
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to complete task: {str(e)}")
        return None

def complete_daily_task(token, task_id):
    url = f"https://api.ffabrika.com/api/v1/daily-tasks/completion/{task_id}"
    headers = {"cookie": f"acc_uid={token}"}
    
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()['data']
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to complete daily task: {str(e)}")
        return None

def receive_daily_reward(token):
    url = "https://api.ffabrika.com/api/v1/daily-rewards/receiving"
    headers = {"cookie": f"acc_uid={token}"}
    
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        print(Fore.GREEN + "Daily reward successfully received")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to receive daily reward: {str(e)}")

def send_scores_request(token):
    url = "https://api.ffabrika.com/api/v1/scores"
    headers = {
        "Content-Type": "application/json",
        "cookie": f"acc_uid={token}"
    }
    
    count = random.randint(80, 150)
    data = {"count": count}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print(Fore.GREEN + f"Taps {count} successful")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Failed to send request: {str(e)}")
        return None

def process_account(payload):
    token = login_telegram(payload)
    if not token:
        return
    
    profile = get_profile(token)
    if not profile:
        return
    
    print(Fore.CYAN + f"Processing account: {profile['username']}")
    print(Fore.YELLOW + f"Name: {profile['firstName']} {profile['lastName'] or ''}")
    print(Fore.YELLOW + f"Status: {profile['status']}")
    print(Fore.YELLOW + f"Total score: {profile['score']['total']}")
    print(Fore.YELLOW + f"League: {profile['league']['name']}")
    print(Fore.YELLOW + f"Energy: {profile['energy']['balance']}/{profile['energy']['limit']}")
    print(Fore.YELLOW + f"Uncompleted social tasks: {profile['uncompletedSocialTasksQuantity']}")
    print(Fore.YELLOW + f"Uncompleted daily tasks: {profile['uncompletedDailyTasksQuantity']}")
    
    if not profile['dailyReward']['isRewarded']:
        receive_daily_reward(token)
    else:
        print(Fore.YELLOW + "Daily reward already received")
    
    factory_data = profile.get('factory')
    if factory_data:
        print(Fore.CYAN + f"Processing factory ID: {factory_data['id']}")
        print(Fore.YELLOW + f"Available rewards: {factory_data['rewardCount']}")
        
        if factory_data['rewardCount'] > 0:
            collect_factory_rewards(token)
        else:
            print(Fore.YELLOW + "No rewards to collect.")
        
        if factory_data['isPlanted'] == False and factory_data['isDestroyed'] == False:
            assign_worker_tasks(token)
        else:
            print(Fore.YELLOW + "Factory not available for tasks.")
    else:
        print(Fore.RED + "No factory data in profile.")
    
    tasks = get_tasks(token)
    if tasks:
        for task in tasks:
            if not task['isCompleted']:
                result = complete_task(token, task['id'])
                if result:
                    print(Fore.GREEN + f"Task '{task['description']}' completed. Reward: {task['reward']}")
    
    daily_tasks = get_daily_tasks(token)
    if daily_tasks:
        print(Fore.CYAN + "Daily Tasks:")
        for task in daily_tasks:
            print(Fore.YELLOW + f"- {task['description']}: Progress {task['progress']}/{task['goal']}, Reward: {task['reward']}")
            if not task['isCompleted'] and task['progress'] >= task['goal']:
                result = complete_daily_task(token, task['id'])
                if result:
                    print(Fore.GREEN + f"Daily task '{task['description']}' completed. Reward: {task['reward']}")
    
    while profile['energy']['balance'] > 0:
        print(Fore.YELLOW + f"Remaining Energy: {profile['energy']['balance']}")
        response = send_scores_request(token)
        if response:
            profile = get_profile(token)
            if not profile:
                return
        else:
            print(Fore.RED + "Failed to send request. Stopping loop.")
            break
    
    print(Fore.CYAN + "Energy depleted, finished processing account\n")

def main():
    print_welcome_message()
    accounts = load_accounts()
    total_accounts = len(accounts)
    
    print(Fore.YELLOW + f"Total accounts: {total_accounts}")
    
    for i, payload in enumerate(accounts, 1):
        print(Fore.CYAN + f"Processing account {i} of {total_accounts}")
        process_account(payload)
        if i < total_accounts:
            print(Fore.YELLOW + "Waiting 5 seconds before next account...")
            time.sleep(5)
    
    print(Fore.GREEN + "All accounts have been processed.")
    
    while True:
        target_time = datetime.now() + timedelta(days=0.01157)
        while datetime.now() < target_time:
            remaining_time = target_time - datetime.now()
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(Fore.YELLOW + f"\rTime remaining: {hours:02d}:{minutes:02d}:{seconds:02d}", end="", flush=True)
            time.sleep(1)
        
        print(Fore.GREEN + "\nRestarting process...")
        main()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(Fore.RED + f"An error occurred: {str(e)}")
        print(Fore.YELLOW + "Continuing to the next task...")