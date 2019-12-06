import time
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
print("\033[1;31;40mBy ArSiFoX")
print("\033[1;31;40m_____________¶____¶ ")
print("\033[1;31;40m_________¶_¶¶¶¶¶¶¶¶¶¶ ")
print("\033[1;31;40m_____¶¶¶¶¶¶¶_________¶ ")
print("\033[1;31;40m___¶¶¶¶¶_____________¶ ")
print("\033[1;31;40m___¶_________________¶ ")
print("\033[1;31;40m____¶________________¶¶ ")
print("\033[1;31;40m____¶¶________________¶ ")
print("\033[1;31;40m_____¶________________¶¶ ")
print("\033[1;31;40m_____¶¶_______¶¶¶____¶¶¶ ")
print("\033[1;31;40m______¶_____¶¶___¶¶_¶___¶ ")
print("\033[1;31;40m______¶_____¶¶_____¶____¶ ")
print("\033[1;31;40m______¶¶____¶______¶¶¶¶¶¶¶ ")
print("\033[1;31;40m_______¶____¶¶__¶¶¶_____¶¶ ")
print("\033[1;31;40m______¶¶¶¶____¶¶¶¶_____¶¶ ")
print("\033[1;31;40m______¶¶¶_______________¶¶ ")
print("\033[1;31;40m_______¶¶¶______________¶¶ ")
print("\033[1;31;40m________¶_____¶¶¶¶¶¶¶¶¶¶¶ ")
print("\033[1;31;40m_______¶¶_______¶¶¶¶¶ ")
print("\033[1;31;40m______¶¶¶¶¶_____¶ ")
print("\033[1;31;40m___¶¶¶¶__¶¶¶¶¶¶¶¶ ")
print("\033[1;31;40m__¶¶____¶¶_____¶¶ ")
print("\033[1;31;40m_¶¶_____¶¶______¶¶ ")
print("\033[1;31;40m¶¶______¶¶_______¶¶ ")
print("\033[1;31;40m_¶¶¶¶¶___¶¶______¶¶ ")
print("\033[1;31;40m_¶__¶¶¶¶¶¶_______¶¶ ")
print("\033[1;31;40m¶¶____¶___________¶¶ ")
print("\033[1;31;40m¶____¶¶__________¶¶¶ ")
print("\033[1;31;40m¶____¶¶____________¶ ")
print("\033[1;31;40m¶_____¶___________¶¶¶") 
print("\033[1;31;40m¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶_¶ ")
print("\033[1;31;40m¶______¶_________¶___¶ ")
print("\033[1;31;40m¶¶¶¶__¶__________¶_¶¶¶ ")
print("\033[1;31;40m_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ")
print("\033[1;31;40m___¶¶¶¶¶¶¶¶¶____¶ ")
print("\033[1;31;40m___¶¶___¶__¶____¶ ")
print("\033[1;31;40m___¶____¶__¶____¶ ")
print("\033[1;31;40m___¶¶___¶__¶____¶¶ ")
print("\033[1;31;40m__¶_______¶¶¶¶¶¶¶¶¶¶ ")
print("\033[1;31;40m_¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶ ")
print("\033[1;31;40m_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")

vk_session = vk_api.VkApi(token='5dddcd98decaabd87db84c9891227331dae1b882a0b442c6ba5caa4b2c0d9819a8dcd753d3a3783fe5053') #токен вашей группы
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session,189437576) #цифровой id вашей группы
def main():

	keyboard1 = VkKeyboard(one_time=False) # False - клавиатура после нажатия не будет закрываться. True - будет.

	keyboard1.add_button('Остановить спам vto.pe', color=VkKeyboardColor.POSITIVE)	
	keyboard1.add_button('Остановить спам vto.pe', color=VkKeyboardColor.POSITIVE)	


	while True: 
		try: 
			for event in longpoll.listen():

				if event.type == VkBotEventType.MESSAGE_NEW:
					print("By ArSiFoX")
					while True:
						vk.messages.send(peer_id=event.object.peer_id, message="DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS DDOS  DDOS DDOS DDOS DDOS ",keyboard=keyboard1.get_keyboard(), random_id=0)	
					
			
		except Exception as e:
			print('') 

if __name__ == '__main__':
	main()
