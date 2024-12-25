from telethon import TelegramClient, events
from telethon.errors import FloodWaitError
import asyncio
import random

# Replace these with your own API ID, API Hash, and Phone
API_ID = '22082973'
API_HASH = 'a3ad1a393cb93aa0f96ef848f379d1fd'
PHONE = '+94773366370'  # Include your country code

# Create the client and connect
client = TelegramClient('session_name', API_ID, API_HASH)

async def main():
    await client.start(PHONE)
    print("Client Created")

    # List of groups where you want to send messages
    groups = [
    'https://t.me/link_share4',    
    'https://t.me/Srilanka_Link_Lanthe',   
    'https://t.me/Links_share_chat_group',
    'https://t.me/unlimitedreflinkshareSL',  
    'https://t.me/mypanschatroom',
    'https://t.me/linksharesagare',
    'https://t.me/linkshearall1',
    'https://t.me/linkshareallinone',    
    'https://t.me/LinksShareTelegram',
    'https://t.me/temusheinusa',
    'https://t.me/LinkShareUltimateSL',
    'https://t.me/linkbuwa',
    'https://t.me/temucodeslinkss',
    'https://t.me/temusheingroup',
    'https://t.me/linksharing90',
    'https://t.me/links_shere98',
    'https://t.me/linksharelktelegram',
    'https://t.me/FreePromoteReferralLink',
    'https://t.me/cryptocurunc',
    'https://t.me/shere_linkku',
    'https://t.me/slanylinkshare',
    'https://t.me/+SbDne-A3_385MzFl',
    'https://t.me/share_link_promotionfree',   
    'https://t.me/linkshare11',
    'https://t.me/Airdroplink_sharee',
    'https://t.me/RLvista',
    'https://t.me/telelinkshub',
    'https://t.me/dollerbuysellgrp',
    'https://t.me/BEBAS_SHERE_ALL_APP',
    'https://t.me/sherelinks0',   
    'https://t.me/tx38_wallet',
    'https://t.me/medfoxwin6',
    'https://t.me/+GTo1abjtP_c1ODdl',
    'https://t.me/linksharegroupnew',
    'https://t.me/batmnf',
    
   
]


    # List of messages to send (with Markdown formatting)
    messages = [  '''🙇‍♀️අලුත්ම කෙල්ලන්ගේ සෙල්ලම් ටික තාම බැලුවේ නැද්ද

💋HOW SADDD

💞එහෙනම් ඉක්මනට පහල Channel එකට Join වෙන්න
https://tinyurl.com/slnewleek
😅අත මරන එක නවත්තන්න බැරිවෙනවා ෂුවර්''',
'''🔴ඔන්න  ලංකාවේ තියෙන සියලුම වැල් නැරැඹීමට  දැන් ඔබට පුලුවන්  🤩🥰

වැල් 25000  🤭😌

අතන මෙතන link හොයන්නේ නැතුව ගියපු ගමන් ad එක skip කරා බලන්න තමා තියෙන්නේ 🔞🙃

වෙන කොහෙවත්ම නෑ මෙවගේ එවා😍

🔴🔴🔴පහල link එකෙන් යන්න 👇👇👇👇👇

https://tinyurl.com/slnewleek

Link එක Expired වෙන්න කලින් බලන්න 🔞❤️''',
'''ක්ලාස් කට් කරලා කැලේ පැන්න මැණිකේ Sri Lankan College Student Lucky to Fuck Hot Teen after School Xxx
❤️❤️❤️❤️❤️❤️❤️❤️
https://tinyurl.com/slnewleek
👉තාම බැලුවේ නැද්ද 👙🍑👈
👇👇👇👇👇👇👇👇👇👇👇
https://tinyurl.com/slnewleek
''',
'''🔞 new XXX groups 🔞

😻 cp videos : 5200 💋https://tinyurl.com/slnewleek
😻 cctv videos : 21000 💋https://tinyurl.com/slnewleek
😻 mom son videos : 1000 💋https://tinyurl.com/slnewleek
😻 rep videos : 1400 💋https://tinyurl.com/slnewleek
😻 sri lanka videos : 50000💋 https://tinyurl.com/slnewleek
😻 india videos : 35000💋 https://tinyurl.com/slnewleek
😻 sri lanka cp videos : 200💋 https://tinyurl.com/slnewleek
😻 anty videos : 2100💋 https://tinyurl.com/slnewleek
😻 gay videos : 1800💋 https://tinyurl.com/slnewleek
😻 lesbian videos : 60000💋https://tinyurl.com/slnewleek

              💎 Telegram channel
             
💋 Free Join💋''',
'''✅sri lanka lik videos : 43000
✅ cp videos : 4000    
✅ indian cp videos : 2500
✅indian lik videos : 36000
✅ cctv videos         : 8000
✅ tamil videos       : 7000
✅mom son videos : 2600
✅anty videos         : 1000
✅gay cp videos : 4500
✅gay videos      : 20000
✅ lesbian videos : 42000
✅ japan videos   : 35000

   

cctv videos / cp videos / sri lanka videos / indian videos /   indian cp videos / animal videos / thaththa & duwa videos / mom son videos / lesbian videos / gay cp videos / tamil videos / anty videos / japan videos / 
https://tinyurl.com/slnewleek''',
'''🔥🔥🔥👉 ලින්ක් ක්ලික් කර කර ඉන්න ඕනිත් නෑ. 😮 චැනල් එකට ගියා බැලුවා 😍

 ⛔️ (Report ගහන උන් නම් රිංගන්න එපා )

❌ලින්ක් ශෙයා කරන්න නෑ
❌යාලුවො ඇඩ් කරන්න නෑ


🔗https://tinyurl.com/slnewleek

  🫴   ලෙස්බියන්
🧖‍♀️ child porn
📵 hot cp
👙   සිංහල ඕනේ තරම්
📷 ලීක් වෙලා නැති ඒව
🥕 Daily වැල් ඕනෙ තරම් දෙනවා
🔞 සියලුම ලීක් එකම තැනකින්
🇱🇰   Sri Lanka Full Cam Show Record Free
👩‍🎤  නිළියන්ගෙ වැල
🍆 ලංකාවේ සුපිරිම වැල එකතුව
🤦🏾‍♀️ ඇන්ටා පාරවල් වල වීඩියෝ🇱🇰
🏠 ස්පා වීඩියෝ🇱🇰
🤳 ලංකාවේ වීඩියෝ කෝල් රෙකෝඩ් ලීක් වීඩියෝ

❤️වැල බලන්න කැමති අය විතරක් 🙏ජොයින් වෙන්න 
   
   🔞  👀 +18 අය විතරක් එන්න ලමායි . 😑 


🔗 https://tinyurl.com/slnewleek


🤷‍♀️  සීමිත පිරිසක් සදහා පමනයි දැන්ම අපිලත් එක්ක සෙට් වෙන්න''',
'''පහල collection හැම එකක්ම තියෙනව.. 

⭕️ 🇱🇰 Video Collection 

⭕️ 🇱🇰 Photo Collection

⭕️ 🇱🇰 school girl video collection

⭕️ 🇱🇰 Aunty Video VIP

⭕️ Indian leak Video Collection

⭕️ Indian ©P Video Collection

⭕️ ♏️🅾️♏️ 💲⭕️N VIP

⭕️ New Rape Videos 

⭕️ New children's Videos

⭕️ Mom And Son Videos 

⭕️ Upskirt Videos (Not sl)

⭕️ Hidden Ip Videos 

⭕️ Gay Videos & Photos

⭕️ Gay BDSM Videos 

⭕️ 🇱🇰 video mega collection  

⭕️ Cuckold Videos 

⭕️ CP VIP 

⭕️ Lesbion Videos 

⭕️ Shemale Videos 

⭕️ BDSM Videos 

⭕️ Japan Videos


💥 Special Mega package Available 

💥 Hidden ©p, Hidden Adults, Girls with animals All IN one VIP Available 

https://tinyurl.com/slnewleek
''',
'''❗️ලංකාවේ ලොකුම වැල තියෙන Channel එක❗️

🔥🥵ටීචලට ගහන වැල

🔥🥵ස්කොලෙ කෙල්ලන්ට ගහන වැල

🔥🥵හොරෙන් වීඩියෝ කරපු වැල

🔥🥵පෙට්ටි කඩන ඒවා

🔥🥵යාලුවගේ ගෑනිට ගහපු ඒවා

🔥🥵නංගිලට ගහන ඒවා

🔥🥵අක්කලට ගහන ඒවා

🔥🥵කෑම්පස් කෑලි වලට ගහන ඒවා
https://tinyurl.com/slnewleek
🔞ඉක්මනට Join වෙන්න Link එක Expire වෙනවා ටික වෙලාවකින්💦

🌟සුපිරිම බඩු VIP video දානවා අපේ preMIUM group එකට නොමිලේම  join වෙන්නත් පුලුවන් ඉක්මනින් අපේ teligrame group එකට join වෙන්න
https://tinyurl.com/slnewleek
ඔන්න ආයම VIP ඒවා එකම තැනකින් 😍

🎭 බලෙන් හුකපුවා
🎭 එහා ගෙදර ගෑනිට ගහපුවා
🎭 හොර ගෑනිට ගහපුවා

🤤 යාලුවගේ කැල්ලට ගහපුවා
🤤 නංගිගේ යාලුවට ගහපුවා
🤤 Gf ගේ අම්මට ගහපුවා

😍 ඇන්ටි පාරවල්
😍 School වැල්
😍 පොඩි කෙල්ලො

😉 සිංහල බඩසම
😉 කක්කෝල්ඩ්
😉 අලුත් ලීක් 

🔥ලින්ක් එක අයින් කරන්න කලින් JOIN වෙන්න ❗️
https://tinyurl.com/slnewleek


🔴ලංකාවේ සිංහල වැල් 

🔴බඩු ගහපුවා 

🔴ඉන්දියාවේ වැල්

🔴පෙට්ටි කඩපුවා

🔴Short films 18+

🔴New Leek Videos 

🔴Old films 18+

💥හැමදාම වීඩියෝස් අප්ලෝඩ් කරනවා 
Link share කරන්න නෑ

💥Join උනා බැලුවා දැන්ම සෙට් වෙන්න
👇👇👇👇
https://tinyurl.com/slnewleek
🔴ලංකාවේ සිංහල වැල් 

🔴බඩු ගහපුවා 

🔴ඉන්දියාවේ වැල්

🔴පෙට්ටි කඩපුවා

🔴Short films 18+

🔴New Leek Videos 

🔴Old films 18+

💥හැමදාම වීඩියෝස් අප්ලෝඩ් කරනවා 
Link share කරන්න නෑ

💥Join උනා බැලුවා දැන්ම සෙට් වෙන්න
👇👇👇👇
❗️ලංකාවේ ලොකුම වැල තියෙන Channel එක❗️

🔥🥵ටීචලට ගහන වැල

🔥🥵ස්කොලෙ කෙල්ලන්ට ගහන වැල

🔥🥵හොරෙන් වීඩියෝ කරපු වැල

🔥🥵පෙට්ටි කඩන ඒවා

🔥🥵යාලුවගේ ගෑනිට ගහපු ඒවා

🔥🥵නංගිලට ගහන ඒවා

🔥🥵අක්කලට ගහන ඒවා

🔥🥵කෑම්පස් කෑලි වලට ගහන ඒවා
https://tinyurl.com/slnewleek
🔞ඉක්මනට Join වෙන්න Link එක Expire වෙනවා ටික වෙලාවකින්💦''',

'''
🌟සුපිරිම බඩු VIP video දානවා අපේ preMIUM group එකට නොමිලේම  join වෙන්නත් පුලුවන් ඉක්මනින් අපේ teligrame group එකට join වෙන්න
https://tinyurl.com/slnewleek
ඔන්න ආයම VIP ඒවා එකම තැනකින් 😍

''',
'''මේන්න දැන් ලීක් උන ඉන්දියාවෙ නයනතාරගේ වීඩියෝ එක😱ඒකනම් පිස්සුවක්

https://tinyurl.com/slnewleek

ඩිලිට් කරන්න කලින් ඉක්මන්ට බලපල්ලා...අවුරුද්දේ සුපිරුම විඩියෝ එක මේකනම් 😱🥵''',
'''🚨 Attention Action Fans! 🚨

The wait is over! 🕵️‍♀️ Special Ops: Lioness Season 1 is here, and it’s packed with non-stop action, espionage, and jaw-dropping twists! 🔥

Follow Zoe Saldaña and Laysla De Oliveira as they lead a secret CIA mission that will keep you on the edge of your seat!

🔒 Ready for a mission you won’t forget? Download it NOW and get immersed in the world of high-stakes covert ops! 🚁💥

https://tinyurl.com/slnewleek

#SpecialOpsLioness #SpyThriller #DownloadNow''',
'''වල් කතා කියවන්න කැමති අය වෙනුවෙන්මයි 🫦💃

    💥 සිංහල වල් කතා
    💥 චිත්‍ර වල් කතා
    💥 පවුලේ වල් කතා
    💥 ලෙස්බියන් වල් කතා 

🔖වැනි එකි මෙකි  සියලුම වර්ගයේ වල් කතා කියවන්න අදම එකතු වෙන්න. 

🔖කියවන්න කැමති අය ජොයින් වෙන්න.කියවලා නැති අයත් කියවලා බලන්න. 

📌📌📌📌📌📌📌📌📌📌📌

https://t.me/SecretNightWalkers

💥💥💥💥💥💥💥💥💥💥💥

මේ වෙනකං දාපු සියලුම කතා බලන්න මේ ලින්ක් එකෙන් යන්න

https://t.me/SecretNightWalkers''',
'''🚨 Leaked! Watch Now Before Release! 🚨

🔥 The War of the Rohirrim
🔥 Mufasa: The Lion King
🔥 Sonic the Hedgehog 3

💥 Don’t miss out—download NOW and be the first to see these epic films! Limited access, act fast! 🚀

👉 For more leaks: Film Blitz New Leaks
https://filmblitznewleeks.blogspot.com/''',
'''අනූ කනූගෙ වීඩියෝ එක ලීක් කරපු කෙනා අලුත්ම වීඩියෝ එකක් ලීක් කර‍යි.!!!!
එතකොට මේ එයාලගෙ ලීක් උන පස් වෙනි වීඩියෝ එකද?
https://aluthekanew.blogspot.com/2024/12/blogger-page_49.html''',
'''
🔴 ලංකාවේ ලොකුම වැල් තියෙන channel එක තුන්මන් හන්දිය ආයෙත් හැදුවා.

⚠️ මේ ටිකේම බොරු බයිලා කාරයෝ අපේ channel name එකෙන් ලින්ක් දාල ඒවාට අහුවුණා නේ.

❌ මෙන්න original එක. Video 15000+, cam show තියෙන ලොකුම channel එක.

https://tinyurl.com/slnewleek

🔴 Report කාක්කන්ට පෙන්න එක්කම සේරම video Free දැන් හැබැයි හැමදාම නෙමෙ👻👻

https://tinyurl.com/slnewleek

💋 School සෙස්
💋 සිංහල BDSM
💋 ඇන්ටා පාරවල්
💋 හොරෙන් ගත්තුවා
😈 Hidden කැම්
😈 ලීක් Photos 
😈 නිලියන්ගෙ වීඩියෝ
😈 මුස්ලිම් කෙල්ලො
👅 පොඩි උන්ගෙ
👅 Mom Son 
👅 ත්‍රීසම් 
👅 කක්කෝල්ඩ්

🥵 තුන්මන් හන්දියෙට awith⚠️ සැපක් ගමුත 👻🤧🥵🥵''',
'''වැල් විඩියෝ කියලා එක එක බොරු රෙද්දවල් වලට අහුවෙලාද. 
විඩියෝ බලන්න ලින්ක් කීයක් CLICK කරාද. 😃 
බොරු බයිලා කාරයෝ කියකට අහු උනාද. 😑 

අලුත් ම වැල් බලන්න දැන් ම සෙට් වෙන්න 

Link එක Touch කරලා ගෲප් එකට එන්න   

12 වසරෙ කෙල්ලගෙ ලීක් එක 
➜ https://tinyurl.com/slnewleek

රූම් එකේදි මෝල් වුන කෑල්ල 
➜https://tinyurl.com/slnewleek

එයා මගෙ උරලා දෙන සැප 
➜ https://tinyurl.com/slnewleek

අක්කයි මල්ලි ගන්න සැප 
➜ https://tinyurl.com/slnewleek

මේ සැපට තමයි ගෑනු කැමතිම 
➜https://tinyurl.com/slnewleek

බලෙන් ම කරපු වැඩේ මේකිට 
➜ https://tinyurl.com/slnewleek

නංගි තනියම ඉද්දි කරපු වැඩේ  
➜  https://tinyurl.com/slnewleek

රෑට හොරෙන් කොටුවක් පැනලා සැප 
➜ https://tinyurl.com/slnewleek

හොස්ටල් කෙල්ලට කරපු වැඩේ 
➜ https://tinyurl.com/slnewleek

පොඩි එකීගෙ ලීක් එක 
➜ https://tinyurl.com/slnewleek

කැම්පස් එකේ ලීක් එක 
➜ https://tinyurl.com/slnewleek

පොඩි කෙල්ල ගන්න සැපක් 
➜ https://tinyurl.com/slnewleek''',
'''2019 දී කුඩම්මගෙ දුවත් එක්ක කාමරේ ඇතුලෙ
 සෙක්ස් කරල වීඩියෝ කරල ලීක් කරපු
 කොල්ලගෙයි කෙල්ලගෙයි වීඩියෝ එක මතකද !!
එයාල ඒ ගත්තු ෆන් එක ආයෙත් පාරක් බලමුද
ඔන්න එහෙනම් https://tinyurl.com/slnewleek''',
'''ඉස්කෝලෙ පිටිපස්සෙ කෑල්ලත්
 එක්ක දාපු ආතල් එක මෙන්න
https://tinyurl.com/slnewleek''',

'''🌟 Ready to Discover Your Perfect Match? 💘

💑 Want to know how much you and your partner really match?
Unlock exciting quizzes, tips, and relationship insights on Match Your GF Blog!

💖 Find out your compatibility score and improve your relationship 💬
✨ Fun, interactive, and filled with great advice!
🎯 Join us now and let the journey begin!

🔗 Click here to explore: https://sites.google.com/view/match-your-gf-bf?usp=sharing''',
'''රන්ජන් පියුමි මහා රෑ කරපු දේ https://tinyurl.com/slnewleek ''',
'''කෙල ගාලා නග්ගලා ඇතුළට දාන දේ, 😂 | ලොකු හිල් වලට විතරක් දාන්න පුලුවන් යුරේනි 😅
https://tinyurl.com/slnewleek''',
'''බ්‍රා එකත් නෑ කුක්කු එලියේ දාගන නටන විසි අටේ ඉස්කෝල ටීච https://tinyurl.com/slnewleek''',
'''බාප්පා පිට අතුල්ලන්න හොඳට දන්නවනේ https://tinyurl.com/slnewleek''',
'''මනීෂගෙයි අශේන්ගෙයි එළියට ආපු අලුත්ම වීඩියෝව https://tinyurl.com/slnewleek''',
'''නාඩගම්කාරයො එකේ  සුදු චූටිත්
 ලීක් කරගත්ත කියල දන්නවද.
ලීක් කරගත්ත කියල වැඩිය ප්‍රශිද්ද උනේ නෑ නේද.
මෙන්න මෙතනින් බලන්න වීඩියෝ එකට රිපෝට් වදින්න කලින්
https://tinyurl.com/slnewleek''',
'''ෆොටෝ ශූට් එක වෙලාවෙ පෑන්ටිය ගැලවුන අක්කගෙ
ගැලවිල PART 2
ගැලවිල කිව්වට හරියටම ගැලවුනෙ මෙ වෙලාවෙ https://attaraya2025.blogspot.com/2024/12/blogger-page_85.html''',
'''ඩොක්ටර් නෝනගෙ අලුත් එක
උණු උණු ආප්ප බලන්න එන්න
 https://aluthekanew.blogspot.com/2024/12/blogger-page_15.html''',
 '''අලුත් එක ඕනෙද https://attaraya2025.blogspot.com/2024/12/blogger-page_52.html''',
 ''' අලුත් එක .අනේ  ඒ ආදරේ https://attaraya2025.blogspot.com/2024/12/blogger-page_52.html''',
 '''තන් දෙක පේන්න නටපු නංගිගෙ එක් දැක්කද
https://aluthekanew.blogspot.com/2024/12/blogger-page_21.html''',
'''ආදිත්‍යා සින්දු කියද්දි ස්ටේජ් එකේදි උන දේ.මොකුත් දැක්කෙ නෑ නේද https://aluthekanew.blogspot.com/2024/12/blogger-page_58.html''',
'''අම්මො ඒ දෙකේ ලොකු https://aluthekanew.blogspot.com/2024/12/blogger-page_50.html''',
'''ගල් තලාවෙ එක බැලුවද https://attaraya2025.blogspot.com/2024/12/blogger-page_27.html''',
'''ආවා ආවා.මෙන්න අලුත් එකක් ආවා.ෆුල් එකම විනාඩි දොලහක් https://attaraya2025.blogspot.com/2024/12/blogger-page_23.html
''',
'''අනේ මල්ලි දැන්නම් ඇති.අලුත් එක බැලුවද https://attaraya2025.blogspot.com/2024/12/blogger-page_13.html'''
        
    ]

    # Dictionary to track slow mode wait times for each group
    slow_mode_groups = {}

    while True:
        for group in groups:
            if group in slow_mode_groups:
                # Check if the wait time has expired
                if slow_mode_groups[group] <= 0:
                    # Remove from slow mode tracking
                    del slow_mode_groups[group]
                else:
                    # Decrease the wait time
                    slow_mode_groups[group] -= 1
                    continue  # Skip sending to this group

            try:
                # Randomly select one message from the list
                message_to_send = random.choice(messages)

                # Send the selected message with Markdown formatting
                await client.send_message(group, message_to_send, parse_mode='markdown')
                print(f'Message sent to {group}')
                await asyncio.sleep(30)
            except FloodWaitError as e:
                # If slow mode is triggered, print the wait time and skip this group for now
                print(f"Slow mode active in {group}. Need to wait for {e.seconds} seconds.")
                # Store the wait time in slow_mode_groups
                slow_mode_groups[group] = e.seconds
                continue
            except Exception as e:
                # Catch any other unexpected errors
                print(f"An error occurred while sending message to {group}: {e}")
                continue

        # Wait for 15 minutes before sending the next batch
        await asyncio.sleep(1000)  # Sleep for 15 minutes

# Run the client
with client:
    client.loop.run_until_complete(main())


