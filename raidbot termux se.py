# -*- coding: latin-1 -*-
import os, sys
import time
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
print("\033[1;32;40mVKRaidbot v5 By ArSiFoX")
time.sleep(1)

vk_session = vk_api.VkApi(token='5dddcd98decaabd87db84c9891227331dae1b882a0b442c6ba5caa4b2c0d9819a8dcd753d3a3783fe5053')
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session,189437576)
def main():

	keyboard1 = VkKeyboard(one_time=False)

	keyboard1.add_button('Остановить спам vto.pe', color=VkKeyboardColor.POSITIVE)	
	keyboard1.add_button('Остановить спам vto.pe', color=VkKeyboardColor.POSITIVE)	

	print ("Service runned!")
	while True: 
		try: 
			for event in longpoll.listen():

				if event.type == VkBotEventType.MESSAGE_NEW:
					print("Spam started!")
					while True:
						vk.messages.send(peer_id=event.object.peer_id, message="⃣⃣⃣⃣⃣⃣⃣⃣⃣⃣™⃣⃣⃣⃣⃣⃣⃣⃣⃣⃣™⃣⃣⃣⃣⃣⃣⃣⃣⃣⃣™⃣⃣⃣⃣⃣⃣⃣⃣⃣⃣™⃣⃣⃣⃣⃣⃣⃣⃣⃣⃣™⃣⃣⃣⃣⃣⃣⃣⃣⃣⃣™‼⁉™ℹ↔↕↖↗↘↙↩↪⌛⌚⏩⏪⏫⏬⏰⏳Ⓜ▪▫▶◀◻◼◽◾☀☁☑☕☔☎☝☺♈♉♊♋♌♍♏♎♐♑♒♓♠♥♣♦♨♻♿⚓⚠⚡⚫⚪⚽⚾⛅⛄⛎⛔⛪⛳⛲⛵⛺⛽✂✅✋✊✉✈✌✏✒✔✖✨✳✴❄❇❌❎❓❔❕❗❤➕➗➖➡➰➿⤴⤵⬅⬇⬆⬛⬜⭐⭕〰〽🀄🃏🅰🅱🅾🅿🆎🆑🆓🆕🆔🆒🆖🆗🆘🆚🆙🈁🌀🌄🌁🌃🌂🌅🌆🌈🌇🌉🌊🌋🌌🌎🌍🌏🌑🌐🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜🌝🌟🌞🌠🌰🌱🌲🌳🌴🌵🌸🌹🌺🌷🌻🌼🌽🌾🌿🍀🍁🍂🍄🍅🍃🍆🍇🍈🍉🍊🍋🍌🍍🍎🍏🍑🍓🍒🍐🍕🍔🍖🍗🍘🍙🍛🍚🍞🍜🍝🍟🍠🍣🍡🍦🍥🍢🍤🍩🍧🍪🍨🍫🍬🍮🍭🍯🍰🍱🍲🍳🍴🍶🍷🍵🍸🍺🍹🍼🍻🎁🎀🎂🎃🎄🎅🎇🎆🎈🎉🎊🎌🎋🎍🎏🎎🎐🎑🎒🎓🎢🎡🎠🎣🎥🎤🎦🎨🎧🎩🎫🎪🎭🎬🎰🎮🎯🎱🎲🎴🎳🎵🎶🎹🎸🎺🎷🎻🎼🎽🎾🎿🏀🏁🏂🏃🏄🏆🏇🏈🏉🏊🏠🏡🏣🏢🏤🏥🏧🏦🏨🏩🏪🏫🏭🏮🏬🏰🏯🐀🐁🐂🐄🐃🐅🐆🐇🐉🐈🐊🐍🐎🐌🐋🐏🐐🐑🐔🐒🐕🐓🐗🐖🐘🐙🐚🐛🐝🐜🐞🐟🐠🐡🐢🐤🐥🐦🐧🐩🐣🐨🐪🐫🐬🐭🐯🐱🐮🐲🐰🐳🐵🐷🐶🐴🐸🐹🐻🐼🐺🐽🐾👀👂👄👃👅👆👇👈👉👊👌👎👋👍👏👐👑👓👔👒👖👕👗👘👙👚👛👜👝👟👞👠👡👢👣👤👥👧👦👨👩👫👪👬👭👮👯👱👰👲👳👴👵👸👷👶👺👹👻👽👼👿👾💁💀💂💃💄💆💅💇💈💊💋💉💍💌💏💐💎💑💒💓💔💕💖💗💘💙💚💛💜💝💞💠💟💡💢💣💤💥💧💦💩💨💪💫💭💬💮💯💱💰💲💳💴💶💸💵💹💷💺💾💽💻💼📀💿📁📃📄📆📂📅📈📇📋📍📉📊📌📎📏📐📒📑📕📔📓📖📗📙📚📛📝📘📞📜📠📟📡📢📤📣📦📨📧📥📩📪📬📭📫📮📯📰📲📴📱📵📷📶📹📼📺📻🔂🔁🔀🔄🔃🔅🔇🔈🔆🔊🔋🔉📳🔌🔍🔎🔒🔏🔐🔑🔕🔓🔖🔔🔗🔘🔛🔙🔚🔜🔞🔝🔟🔡🔢🔥🔠🔣🔤🔧🔨🔦🔪🔩🔫🔭🔮🔬🔯🔰🔱🔳🔵🔴🔲🔶🔸🔺🔹🔷🔻🔼🔽🗻🗽🗾🗿😀🗼😁😂😃😄😅😇😈😆😉😋😊😌😍😏😑😎😐😒😓😔😗😕😘😖😙😚😜😛😝😟😠😞😡😣😤😥😢😦😧😩😨😪😫😬😭😮😱😰😯😲😵😷😳😶😹😼😻😺😾😿😴😽🙀😸🙅🙈🙊🙆🙇🙉🙋🙏🙎🙍🙌🚁🚀🚂🚄🚃🚅🚇🚆🚈🚉🚊🚋🚌🚎🚍🚏🚐🚒🚑🚓🚔🚖🚗🚕🚚🚘🚙🚝🚜🚛🚞🚠🚟🚢🚣🚡🚤🚥🚦🚧🚨🚩🚪🚬🚭🚫🚯🚮🚰🚱🚴🚵🚲🚶🚷🚳🚺🚹🚻🚼🚸🚽🚾🚿🛂🛀🛁🛅🛄🛃🇨🇳🇩🇪🇪🇸🇫🇷🇬🇧🇮🇹🇯🇵🇰🇷🇷🇺🇺🇸⃣⃣⃣⃣⃣⃣⃣⃣⃣⃣™‼⁉™ℹ↔↕↖↗↘↙↩↪⌛⌚⏩⏪⏫⏬⏰⏳Ⓜ▪▫▶◀◻◼◽◾☀☁☑☕☔☎☝☺♈♉♊♋♌♍♏♎♐♑♒♓♠♥♣♦♨♻♿⚓⚠⚡⚫⚪⚽⚾⛅⛄⛎⛔⛪⛳⛲⛵⛺⛽✂✅✋✊✉✈✌✏✒✔✖✨✳✴❄❇❌❎❓❔❕❗❤➕➗➖➡➰➿⤴⤵⬅⬇⬆⬛⬜⭐⭕〰〽🀄🃏🅰🅱🅾🅿🆎🆑🆓🆕🆔🆒🆖🆗🆘🆚🆙🈁🌀🌄🌁🌃🌂🌅🌆🌈🌇🌉🌊🌋🌌🌎⃣⃣⃣⃣⃣⃣⃣⃣⃣⃣™‼⁉™ℹ↔↕↖↗↘↙↩↪⌛⌚⏩⏪⏫⏬⏰⏳Ⓜ▪▫▶◀◻◼◽◾☀☁☑☕☔☎☝☺♈♉♊♋♌♍♏♎♐♑♒♓♠♥♣♦♨♻♿⚓⚠⚡⚫⚪⚽⚾⛅⛄⛎⛔⛪⛳⛲⛵⛺⛽✂✅✋✊✉✈✌✏✒✔✖✨✳✴❄❇❌❎❓❔❕❗❤➕➗➖➡➰➿⤴⤵⬅⬇⬆⬛⬜⭐⭕〰〽🀄🃏🅰🅱🅾🅿🆎🆑🆓🆕🆔🆒🆖🆗🆘🆚🆙🈁🌀🌄🌁🌃🌂🌅🌆🌈🌇🌉🌊🌋🌌🌎🌍🌏🌑🌐🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜🌝🌟🌞🌠🌰🌱🌲🌳🌴🌵🌸🌹🌺🌷🌻🌼🌽🌾🌿🍀🍁🍂🍄🍅🍃🍆🍇🍈🍉🍊🍋🍌🍍🍎🍏🍑🍓🍒🍐🍕🍔🍖🍗🍘🍙🍛🍚🍞🍜🍝🍟🍠🍣🍡🍦🍥🍢🍤🍩🍧🍪🍨🍫🍬🍮🍭🍯🍰🍱🍲🍳🍴🍶🍷🍵🍸🍺🍹🍼🍻🎁🎀🎂🎃🎄🎅🎇🎆🎈🎉🎊🎌🎋🎍🎏🎎🎐🎑🎒🎓🎢🎡🎠🎣🎥🎤🎦🎨🎧🎩🎫🎪🎭🎬🎰🎮🎯🎱🎲🎴🎳🎵🎶🎹🎸🎺🎷🎻🎼🎽🎾🎿🏀🏁🏂🏃🏄🏆🏇🏈🏉🏊🏠🏡🏣🏢🏤🏥🏧🏦🏨🏩🏪🏫🏭🏮🏬🏰🏯🐀🐁🐂🐄🐃🐅🐆🐇🐉🐈🐊🐍🐎🐌🐋🐏🐐🐑🐔🐒🐕🐓🐗🐖🐘🐙🐚🐛🐝🐜🐞🐟🐠🐡🐢🐤🐥🐦🐧🐩🐣🐨🐪🐫🐬🐭🐯🐱🐮🐲🐰🐳🐵🐷🐶🐴🐸🐹🐻🐼🐺🐽🐾👀👂👄👃👅👆👇👈👉👊👌👎👋👍👏👐👑👓👔👒👖👕👗👘👙👚👛👜👝👟👞👠👡👢👣👤👥👧👦👨👩👫👪👬👭👮👯👱👰👲👳👴👵👸👷👶👺👹👻👽👼👿👾💁💀💂💃💄💆💅💇💈💊💋💉💍💌💏💐💎💑💒💓💔💕💖💗💘💙💚💛💜💝💞💠💟💡💢💣💤💥💧💦💩💨💪💫💭💬💮💯💱💰💲💳💴💶💸💵💹💷💺💾💽💻💼📀💿📁📃📄📆📂📅📈📇📋📍📉📊📌📎📏📐📒📑📕📔📓📖📗📙📚📛📝📘📞📜📠📟📡📢📤📣📦📨📧📥📩📪📬📭📫📮📯📰📲📴📱📵📷📶📹📼📺📻🔂🔁🔀🔄🔃🔅🔇🔈🔆🔊🔋🔉📳🔌🔍🔎🔒🔏🔐🔑🔕🔓🔖🔔🔗🔘🔛🔙🔚🔜🔞🔝🔟🔡🔢🔥🔠🔣🔤🔧🔨🔦🔪🔩🔫🔭🔮🔬🔯🔰🔱🔳🔵🔴🔲🔶🔸🔺🔹🔷🔻🔼🔽🗻🗽🗾🗿😀🗼😁😂😃😄😅😇😈😆😉😋😊😌😍😏😑😎😐😒😓😔😗😕😘😖😙😚😜😛😝😟😠😞😡😣😤😥😢😦😧😩😨😪😫😬😭😮😱😰😯😲😵😷😳😶😹😼😻😺😾😿😴😽🙀😸🙅🙈🙊🙆🙇🙉🙋🙏🙎🙍🙌🚁🚀🚂🚄🚃🚅🚇🚆🚈🚉🚊🚋🚌🚎🚍🚏🚐🚒🚑🚓🚔🚖🚗🚕🚚🚘🚙🚝🚜🚛🚞🚠🚟🚢🚣🚡🚤🚥🚦🚧🚨🚩🚪🚬🚭🚫🚯🚮🚰🚱🚴🚵🚲🚶🚷🚳🚺🚹🚻🚼🚸🚽🚾🚿🛂🛀🛁🛅🛄🛃🇨🇳🇩🇪🇪🇸🇫🇷🇬🇧🇮🇹🇯🇵🇰🇷🇷🇺🇺🇸⃣⃣⃣⃣⃣⃣⃣⃣⃣⃣™‼⁉™ℹ↔↕↖↗↘↙↩↪⌛⌚⏩⏪⏫⏬⏰⏳Ⓜ▪▫▶◀◻◼◽◾☀☁☑☕☔☎☝☺",keyboard=keyboard1.get_keyboard(), random_id=0)	
					
			
		except Exception as e:
			print('Spam stopped') 

def mone():

	keyboard1 = VkKeyboard(one_time=False)

	keyboard1.add_button('Остановить спам vto.pe', color=VkKeyboardColor.POSITIVE)	
	keyboard1.add_button('Остановить спам vto.pe', color=VkKeyboardColor.POSITIVE)	

	print ("Service started!")
	while True: 
		try: 
			for event in longpoll.listen():

				if event.type == VkBotEventType.MESSAGE_NEW:
					print("Spam started!")
					while True:
						vk.messages.send(peer_id=event.object.peer_id, message="6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̡̛̹͕̩͖̲̞̩̝̝͒͐̀͒̌̆͝͝͠6̰̭̳̼̗͕̯͎̭̫͂̂̐͆͒̉͘͘͝͠6̤̜͍̣̪̝̙̘͎̟͒͛̽̐̽̔̿̇̇͝6̛͒͐̀͒͝͝͠",keyboard=keyboard1.get_keyboard(), random_id=0)	
					
			
		except Exception as e:
			print('Spam stopped!') 


def mime():
	keyboard1 = VkKeyboard(one_time=False)

	keyboard1.add_button('Остановить спам vto.pe', color=VkKeyboardColor.POSITIVE)	
	keyboard1.add_button('Остановить спам vto.pe', color=VkKeyboardColor.POSITIVE)	

	print ("Service started!")
	while True: 
		try: 
			for event in longpoll.listen():

				if event.type == VkBotEventType.MESSAGE_NEW:
					print("Spam started!")
					while True:
						vk.messages.send(peer_id=event.object.peer_id, message="Начался спам Начался спам Начался спам Начался спам Начался спам Начался спам Начался спам Начался спам Начался спам Начался спам Начался спам Начался спам Начался спам ",keyboard=keyboard1.get_keyboard(), random_id=0)	
					
			
		except Exception as e:
			print('Spam stopped!') 

	
def mine():
	print("Select function:")
	print("1. Start atack")
	print("2. Meet with author")
	print("3. About")
	print("0. Exit")
	ak = input("")
	if ak == "1":
		print("Select mode:")
		print("1. Strong")
		print("2. Medium")
		print("3. Weak")
		aj = input()
		if aj == "1":
			main()
		elif aj == "2":
			mone()
		elif aj == "3":
			mime()
		else:
			mine()
	elif ak == "2":
		print("vk.com/arsifox")
		mine()
	elif ak == "3":
		print("Raidbot v5 TERMUX SE!")
		print("")
		print("By ArSiFoX")
		mine()
	else:
		print("")
if __name__ == '__main__':
	mine()