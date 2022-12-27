# JustaWebhook by fanta09tv ( github ) / DoubleEight#7814 ( discord )

import requests, os, time, json, ctypes
from urllib.request import Request, urlopen
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

showcredit  = True
os.system("color a")     
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
}

def deletewebhook(webhook): 
    try:
        r = requests.get(webhook, verify=False)
    except:
        notcorrect("\n Invalid URL OR Failed To Load URL")
    if(r.status_code==200):
        notcorrect("\n Webhook Online, We Will Now Try To Delete It..")
    else:
        notcorrect("\n Webhook Offline\n")
    if showcredit:
        sendwebhook("Got fucked by JustaWebhook : https://github.com/fanta09tv/JustaWebhook :smile:",1,webhook)    
    requests.delete(webhook)

    r = requests.get(webhook, verify=False)
    if(r.status_code==404):
        notcorrect("\n Webhook Deleted!\n")
    else:
        notcorrect("\n Failed To Delete\n")

def choosenumber():
    os.system("cls")
    printmenu()
    number = input("Input what to you want to do : ")
    
    if number == "1":
        os.system("cls")
        printlogo()
        print("JustaWebhook - Webhook spammer\n")
        ctypes.windll.kernel32.SetConsoleTitleW("JustaWebhook - Webhook spammer")
        print("1. | @everyone spam")
        print("2. | Custom spam (Just message)")
        print("3. | Custom spam (Embed message)\n")
        spam = input("What kind of spam would you like to do? : ") 
        num = ["1",'2','3']
        if spam not in num:
            notcorrect("\nPlease enter the correct number!")
            
        webhookinput = input("\nEnter webhook what do you want spam : ")  
        rr = requests.get(webhookinput).text
        
        if webhookinput.startswith("https://discord.com/api/webhooks/") and "token" in rr:
            rusure = input("\nDo you really want to start spamming? (y/n) : ")
            
            if rusure == "y": 
                if spam == "1":
                    os.system("cls")
                    printlogo()
                    print("JustaWebhook - @everyone spammer\n")
                    ctypes.windll.kernel32.SetConsoleTitleW("JustaWebhook - @everyone spammer")
                    ww = int(input("\nHow many times do you want to spam? : "))
                    print("\nSpamming! Please wait")
                    sendwebhook("@everyone @here",ww,webhookinput)
                    if showcredit:
                        sendwebhook("Spammed by JustaWebhook : https://github.com/fanta09tv/JustaWebhook :smile:",1,webhookinput)    
                    notcorrect("\nFinished spamming!")
                    
                elif spam == "2":
                    os.system("cls")
                    printlogo()
                    print("JustaWebhook - Custom spammer\n")
                    ctypes.windll.kernel32.SetConsoleTitleW("JustaWebhook - Custom spammer")
                    ww = int(input("\nHow many times do you want to spam? : "))
                    www = input("\nWhat do you want to spam? : ")
                    print("\nSpamming! Please wait")
                    sendwebhook(www,ww,webhookinput)
                    if showcredit:
                        sendwebhook("Spammed by JustaWebhook : https://github.com/fanta09tv/JustaWebhook :smile:",1,webhookinput)    
                    notcorrect("\nFinished spamming!")    
                    
                elif spam == "3":
                    os.system("cls")
                    printlogo()
                    print("JustaWebhook - Embed spammer\n")
                    ctypes.windll.kernel32.SetConsoleTitleW("JustaWebhook - Embed spammer")
                    wwwwww = input("\nEnter your embed url ( black for nothing ) : ")
                    wwwwwww = input("\nEnter your embed icon url ( black for nothing ) : ")
                    wwwwwwww = input("\nEnter your embed thumbnail url ( black for nothing ) : ")
                    wwwww = input("\nEnter your embed name ( black for nothing ) : ")
                    wwww = input("\nEnter your embed description ( black for nothing ) : ")
                    www = input("\nEnter your embed footer ( black for nothing ) : ")
                    ww = int(input("\nHow many times do you want to spam? : "))
                    print("\nSpamming! Please wait")
                    payload = json.dumps({'content': "​"}) 

                    for i in range(ww):
                        try:
                            req = Request(webhookinput, data=payload.encode(), headers=headers)
                            urlopen(req)
                            alert = {
                                "embeds": [
                                    {
                                        "author": {
                                        "name": wwwww,
                                        "icon_url": wwwwwww,
                                        "url": wwwwww
                                        },
                                    "description":wwww,
                                    "color": 0x00C7FF,
                                    "thumbnail":{
                                        "url":wwwwwwww
                                    },
                                    "footer": {
                                        "text": www
                                 }
                                }
                            ]
                            }
                            requests.post(webhookinput, json=alert)
                        except:
                            pass
                        
                    if showcredit:
                        sendwebhook("Spammed by JustaWebhook : https://github.com/fanta09tv/JustaWebhook :smile:",1,webhookinput)    
                    notcorrect("\nFinished spamming!")    
                else:
                    notcorrect("\nPlease enter the correct number!")
            elif rusure == "n":
                notcorrect("\nOk. It's up to you")
            else:
                notcorrect("\nPlease enter the correct letter!")
        else:
            notcorrect("\nPlease enter the correct webhook!")
    
    elif number == "2":
        os.system("cls")
        printlogo()
        print("JustaWebhook - Webhook deleter\n")
        ctypes.windll.kernel32.SetConsoleTitleW("JustaWebhook - Webhook deleter")
        webhookinput = input("Enter webhook what do you want to delete : ")
        if webhookinput.startswith("https://discord.com/api/webhooks/"):
            rusure = input("\nAre you sure want to delete this webhook? (y/n) : ")
            if rusure == "y":
                
                deletewebhook(webhookinput)
            elif rusure == "n":
                notcorrect("\nOk. It's up to you")
            else:
                notcorrect("\nPlease enter the correct letter!")
        else:
            notcorrect("\nPlease enter the correct webhook!")
            
    elif number == "3":
        os.system("cls")
        printlogo()
        print("JustaWebhook - Webhook chekcer\n")
        ctypes.windll.kernel32.SetConsoleTitleW("JustaWebhook - Webhook chekcer")
        if not os.path.exists("webhooks.txt"):
            print("webhooks.txt not found! Maked webhooks.txt\n \nPaste your webhooks in webhooks.txt!")
            f = open('webhooks.txt', 'a+')
            f.close()
            time.sleep(3)
            choosenumber()
        print("Put your webhooks in webhooks.txt\n \nValid webhooks will be saved in vaild.txt\n")
        errorcounts = 0
        invalidcounts = 0
        validcounts = 0
        vaild = ""
        
        for item in open("webhooks.txt", "r").readlines():
            r = requests.get(item.strip()).text
            if item.strip().startswith("https://discord.com/api/webhooks/"):
                if "token" in r:
                    print("[ VALID ] There is a valid webhook!")
                    vaild += str(item.strip()) + "\n"
                    validcounts += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Webhook checker - Valid[ {str(validcounts)} ]  Invalid [ {str(invalidcounts)} ]  Error [ {str(errorcounts)} ]")
                else:
                    print("[ INVAID ] This webhook is invalid")
                    invalidcounts += 1
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Webhook checker - Valid[ {str(validcounts)} ]  Invalid [ {str(invalidcounts)} ]  Error [ {str(errorcounts)} ]")
            else:
                errorcounts += 1
                ctypes.windll.kernel32.SetConsoleTitleW(f"Webhook checker - Valid[ {str(validcounts)} ]  Invalid [ {str(invalidcounts)} ]  Error [ {str(errorcounts)} ]")
                
        f = open("vaild.txt","w+")
        if showcredit:
            f.writelines("Webhook checked by JustaWebhook!\nhttps://github.com/fanta09tv/JustaWebhook\n \n" + vaild)
        else:
            f.writelines(vaild)
        f.close()
        notcorrect("\nFinished checking!")
                
    elif number == "4":
        rusure = input("\nAre you sure want to close justawebhook? (y/n) : ")
        if rusure == "y":
            notcorrect("\nOk. See ya!")
        elif rusure == "n":
            notcorrect("\nYAY!!!!!")
        else:
            notcorrect("\nPlease enter the correct letter!")
    else:
        notcorrect("\nPlease enter the correct number!")
   
def printlogo():
    print("""
         ░░ ░░    ░░ ░░░░░░░ ░░░░░░░░  ░░░░░  ░░     ░░ ░░░░░░░ ░░░░░░  ░░   ░░  ░░░░░░   ░░░░░░  ░░   ░░ 
         ▒▒ ▒▒    ▒▒ ▒▒         ▒▒    ▒▒   ▒▒ ▒▒     ▒▒ ▒▒      ▒▒   ▒▒ ▒▒   ▒▒ ▒▒    ▒▒ ▒▒    ▒▒ ▒▒  ▒▒  
         ▒▒ ▒▒    ▒▒ ▒▒▒▒▒▒▒    ▒▒    ▒▒▒▒▒▒▒ ▒▒  ▒  ▒▒ ▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒▒▒▒ ▒▒    ▒▒ ▒▒    ▒▒ ▒▒▒▒▒   
    ▓▓   ▓▓ ▓▓    ▓▓      ▓▓    ▓▓    ▓▓   ▓▓ ▓▓ ▓▓▓ ▓▓ ▓▓      ▓▓   ▓▓ ▓▓   ▓▓ ▓▓    ▓▓ ▓▓    ▓▓ ▓▓  ▓▓  
     █████   ██████  ███████    ██    ██   ██  ███ ███  ███████ ██████  ██   ██  ██████   ██████  ██   ██ \n""")
     
def printmenu():
    ctypes.windll.kernel32.SetConsoleTitleW("JustaWebhook : Advanced open sourced discord webhook tool made in python3 | ©fanta09tv in github")
    printlogo()
    print("1. | Webhook spammer")
    print("2. | Webhook deleter")
    print("3. | Webhook checker")
    print("4. | Exit program\n")
    print("Advanced open sourced discord webhook tool made in python3 | ©fanta09tv in github\n")
    
def notcorrect(object):
    print(object)
    time.sleep(1)
    choosenumber() 

def sendwebhook(object, time, webhook):
    """[sendwebhook summary]

    Args:
        object ([str]): [What do you want to spam]
        time ([int]): [How many times do you want to spam]
        webhook ([str]): [Your webhook to spam]
    """
    payload = json.dumps({'content': object})

    for i in range(time):
        try:
            req = Request(webhook, data=payload.encode(), headers=headers)
            urlopen(req)
            i += 1
        except:
             pass

choosenumber()
