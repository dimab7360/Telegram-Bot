import telebot
import configbot
import random

from telebot import types

bot = telebot.TeleBot(configbot.TOKEN)
# Приветствие 
@bot.message_handler(commands=['start'])
def welcome(message):
	#keyboard	
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Pop music😵‍")
	item2 = types.KeyboardButton("Rock🤐")
	item3 = types.KeyboardButton("Rap🥴")
 
	markup.add(item1, item2, item3)

	#Картинка D:\Prikoly\BD_BD\BD_BOT.py
	sti = open('D:\\Prikoly\\BOT\\channels4_profile.jpg', 'rb')
	bot.send_photo(message.chat.id, sti)


	#Приветствие 
	bot.send_message(message.chat.id, "Здравствуй дорогой,{0.first_name}\n. Я - <b>{1.first_name}</b>, создан для удобства прослушивания твоей любимой музыки.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup )

@bot.message_handler(content_types=['text'])
def choice(message):
	if message.chat.type == 'private':
		

		#POP
		if message.text == 'Pop music😵‍':
			#Клава POP
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Lukas Graham", callback_data='lukas_graham')
			item2 = types.InlineKeyboardButton("One Direction", callback_data='One direction')

			markup.add(item1, item2)		

			bot.send_message(message.chat.id, 'Выбирай что по нраву в моей библиотеке😉😏', reply_markup=markup)
		#ROCK
		elif message.text == 'Rock🤐':
			#Клава ROCK
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("ACDC", callback_data='ACDC')
			item2 = types.InlineKeyboardButton("Nirvana", callback_data='Nirvana')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, 'Выбирай что по нраву в моей библиотеке😉😏', reply_markup=markup)		
		#RAP
		elif message.text == 'Rap🥴':
			#Клава RAP
			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Coolio", callback_data='Coolio')
			item2 = types.InlineKeyboardButton("Eminem", callback_data='Eminem')
			item3 = types.InlineKeyboardButton("Atl", callback_data = 'Atl')
			markup.add(item1, item2, item3)

			bot.send_message(message.chat.id, 'Выбирай что по нраву в моей библиотеке😉😏', reply_markup=markup)
	
	else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			#Lukas Graham
			if call.data == 'lukas_graham':
				markup_reply = types.InlineKeyboardMarkup(row_width=2)
				item_yes = types.InlineKeyboardButton("First" , callback_data='lukas_graham1')
				item_no = types.InlineKeyboardButton("Second", callback_data='lukas_graham2')

				markup_reply.add(item_yes, item_no)

				bot.send_message(call.message.chat.id, 'Выбирете альбом из библиотеки', reply_markup=markup_reply)

			#One direction	
			elif call.data == 'One direction':
				markup_reply = types.InlineKeyboardMarkup(row_width=2)
				item_yes = types.InlineKeyboardButton("Up All Night" , callback_data='One direction1')
				item_no = types.InlineKeyboardButton("Teenage kicks", callback_data='One direction2')

				markup_reply.add(item_yes, item_no)

				bot.send_message(call.message.chat.id, 'Выбирете альбом из библиотеки', reply_markup=markup_reply)

			#ACDC
			elif call.data == 'ACDC':
				markup_reply = types.InlineKeyboardMarkup(row_width=2)
				item_yes = types.InlineKeyboardButton("The Razor’s Edge" , callback_data='ACDC1')
				item_no = types.InlineKeyboardButton("Highway to hell", callback_data='ACDC2')

				markup_reply.add(item_yes, item_no)

				bot.send_message(call.message.chat.id, 'Выбирете альбом из библиотеки', reply_markup=markup_reply)
			#NIRVANA	
			elif call.data == 'Nirvana':
				markup_reply = types.InlineKeyboardMarkup(row_width=2)
				item_yes = types.InlineKeyboardButton("In Utero" , callback_data='Nirvana1')
				item_no = types.InlineKeyboardButton("Nevermind", callback_data='Nirvana2')

				markup_reply.add(item_yes, item_no)

				bot.send_message(call.message.chat.id, 'Выбирете альбом из библиотеки', reply_markup=markup_reply)
			#COOLIO
			elif call.data == 'Coolio':
				sti = open('D:\\Prikoly\\BOT\\Music\\RAP\\Coolio\\coolio_-_gangstas_paradise_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti)				
				bot.send_message(call.message.chat.id, 'Моя библиотека не слишком велика, но если надо мы её доработаем😔👉🏻👈🏽✊✊')
			#EMINEM
			elif call.data == 'Eminem':
				markup_reply = types.InlineKeyboardMarkup(row_width=2)
				item_yes = types.InlineKeyboardButton("8 Mile" , callback_data='eminem1')
				item_no = types.InlineKeyboardButton("The Eminem Show", callback_data='eminem2')
				item_yo = types.InlineKeyboardButton("The Slim Shady LP", callback_data='eminem3')
				markup_reply.add(item_yes, item_no, item_yo)

				bot.send_message(call.message.chat.id, 'Выбирете альбом из библиотеки', reply_markup=markup_reply)
			#ATL
			elif call.data == 'Atl':
				markup_reply = types.InlineKeyboardMarkup(row_width=2)
				item_1= types.InlineKeyboardButton("За упокой", callback_data = 'atl1')
				item_2= types.InlineKeyboardButton("Марабу", callback_data = 'atl2')
				item_3= types.InlineKeyboardButton("Карма х Кома", callback_data = 'atl3')
				item_4= types.InlineKeyboardButton("Лимб", callback_data = 'atl4')
				item_5= types.InlineKeyboardButton("Дисторшин", callback_data = 'atl5')
				item_6= types.InlineKeyboardButton("КРИВОЙ ЭФИР", callback_data = 'atl6')
				item_7= types.InlineKeyboardButton("Радио апокалипсис", callback_data = 'atl7')
				
				markup_reply.add(item_1,item_2,item_3,item_4,item_5,item_6,item_7)
				
				bot.send_message(call.message.chat.id, 'Выбирете альбом из библиотеки', reply_markup=markup_reply)
			#Альбом Lukas Graham
			elif call.data == 'lukas_graham1':
				sti = open('D:\\Prikoly\\BOT\\Music\\POP\\Lukas\\lukas_graham_-_7_years_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "First"')
			elif call.data == 'lukas_graham2':
				sti = open('D:\\Prikoly\\BOT\\Music\\POP\\Lukas\\grammy_2017_lukas_graham_n_kelsea_ballerini_perform_peter_pan_and_7_years_live_-_grammy_2017_lukas_graham_n_kelsea_ballerini_perform_peter_pan_and_7_years_live_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Second"')
			
			#Альбом One direction 
			elif call.data == 'One direction1':
				sti = open('D:\\Prikoly\\BOT\\Music\\POP\\One direction\\One direction-what Make .mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti)				
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Up All Night"')
			elif call.data == 'One direction2':	
				sti = open('D:\\Prikoly\\BOT\\Music\\POP\\One direction\\one_direction_-_one_way_or_another_teenage_-_one_direction_-_one_way_or_another_teenage_kicks_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti)				
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Teenage kicks"')

			#Альбом ACDC

			elif call.data == 'ACDC1':
				sti1 = open('D:\\Prikoly\\BOT\\Music\\ROCK\\ACDC\\acdc_acdc_-_thunderstruck_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti1)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "The Razor’s Edge"')
			elif call.data == 'ACDC2':
				sti2 = open('D:\\Prikoly\\BOT\\Music\\ROCK\\ACDC\\acdc_iz_seriala_sverhestestvennoe_-_highway_to_hell_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti2)				
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Highway to hell"')
			
			#Альбом Nirvana
			elif call.data == 'Nirvana1':
				sti1 = open('D:\\Prikoly\\BOT\\Music\\ROCK\\Nirvana\\nirvana_-_nirvana_2002_-_nirvana_-_heart_-_shaped_box_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti1)
				sti2 = open('D:\\Prikoly\\BOT\\Music\\ROCK\\Nirvana\\nirvana_nirvana_-_rape_me_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti2)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "In Utero"')
			elif call.data == 'Nirvana2':
				sti3 = open('D:\\Prikoly\\BOT\\Music\\ROCK\\Nirvana\\nirvananirvana_-_come_as_you_are_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti3)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Nevermind"')
			#Альбом Eminem
			elif call.data == 'eminem1':
				sti1 = open('D:\\Prikoly\\BOT\\Music\\RAP\\Eminem\\eminem_-_lose_yourself_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti1)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "8 mile"')
			elif call.data == 'eminem2':	
				sti2 = open('D:\\Prikoly\\BOT\\Music\\RAP\\Eminem\\eminem_-_without_me_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti2)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "The Eminem Show"')
			elif call.data == 'eminem3':			
				sti3 = open('D:\\Prikoly\\BOT\\Music\\RAP\\Eminem\\luchshie_hiti_2000_-_eminem_-_the_real_slim_shady_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti3)	
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "The slim shady LP"')
			#Альбом Atl
			#за упокой
			elif call.data == 'atl1':
				sti = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Za upokoy\\photo_2022-01-21_00-14-40.jpg', 'rb')
				bot.send_photo(call.message.chat.id, sti)
				sti1 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Za upokoy\\atl_-_c4_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti1)
				sti2 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Za upokoy\\atl__fckswg_x_za_upokoj_mixtape_2015_-_13_no_matter_feat_eecii_mcfly_komandi_prod_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti2)
				sti3 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Za upokoy\\atl_fckswg_x_za_upokoj_-_4_kamenolomnja_ft_eecii_mcfly__baauer__rl_grime_instr__2015_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti3)
				sti4 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Za upokoy\\atl_fckswg_x_za_upokoj_-_lastochki_ft_lok_dog_2015_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti4)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "За упокой"')
			#Марабу
			elif call.data == 'atl2':
				sti = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Marabu\\photo_2022-01-21_00-13-57.jpg', 'rb')
				bot.send_photo(call.message.chat.id, sti)
				sti1 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Marabu\\atl_-_atl_-__areola_salad_killaz_prod_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti1)
				sti2 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Marabu\\atl_-_demoni_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti2)
				sti3 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Marabu\\atl_-_marabu_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti3)
				sti4 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Marabu\\atl_aztecs_-_marabu_2015_-_atl_aztecs_-_areola_salad_killaz_prod_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti4)
				sti5 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Marabu\\atl_aztecs_-_marabu_2015_-_atl_aztecs_-_krokodil_ritmo_prod_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti5)
				sti6 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Marabu\\atl_aztecs_-_marabu_2015_-_atl_aztecs_-_piljuli_dark_faders_prod_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti6)
				sti7 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Marabu\\atl_aztecs_-_marabu_2015_-_atl_aztecs_-_podsnezhnik_dark_faders_prod_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti7)
				sti8 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Marabu\\atl_aztecs_-_marabu_2015_-_atl_aztecs_-_iskra_dark_faders_prod_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti8)
				sti9 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\Marabu\\atl_aztecs_-_marabu_2015_-_atl_aztecs_-_udobreniem_sda_prod_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti9)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Марабу"')
			#Карма х Кома
			elif call.data == 'atl3':
				sti = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\KxK\\photo_2022-01-21_00-12-59.jpg', 'rb')
				bot.send_photo(call.message.chat.id, sti)
				sti1 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\KxK\\atl_-_didzhej_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti1)
				sti2 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\KxK\\atl_-_karma_x_koma_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti2)
				sti3 = open('D:\\Prikoly\\BOT\\Music\\RAP\\ATL\\KxK\\atl_-_poka_molodoj_karma_h_koma_2016_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti3)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Карма х Кома"')
			#Лимб
			elif call.data == 'atl4':
				sti = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Limb\\photo_2022-01-21_00-11-33.jpg', 'rb')
				bot.send_photo(call.message.chat.id, sti)
				sti1 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Limb\\atl_-_svjashchennij_rejf_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti1)
				sti2 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Limb\\atl_-_tancujte_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti2)
				sti3 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Limb\\atl_aztecs_-_limb_2017_-_atl_aztecs_-_1000_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti3)
				sti4 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Limb\\atl_aztecs_-_limb_2017_-_atl_aztecs_-_arhitektor_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti4)
				sti5 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Limb\\atl_aztecs_-_limb_2017_-_atl_aztecs_-_astronavt_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti5)
				sti6 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Limb\\atl_aztecs_-_limb_2017_-_atl_aztecs_-_gori_jasno_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti6)
				sti7 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Limb\\atl_aztecs_-_limb_2017_-_atl_aztecs_-_majk_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti7)
				sti8 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Limb\\atl_aztecs_-_limb_2017_-_atl_aztecs_-_shaman_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti8)
				sti9 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Limb\\atl_aztecs_-_limb_2017_-_atl_aztecs_-_voronij_graj_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti9)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Лимб"')
			#Дисторшин
			elif call.data == 'atl5':
				sti = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Dist\\photo_2022-01-21_00-10-00.jpg', 'rb')
				bot.send_photo(call.message.chat.id, sti)
				sti1 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Dist\\atl__stewart_-_ne_beda_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti1)
				sti2 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Dist\\atl_aztecs_-_distorshn_2017_-_atl_aztecs_-_petlja_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti2)
				sti3 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Dist\\atl_aztecs_-_distorshn_2017_-_atl_aztecs_-_splin_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti3)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Дисторшин"')
			#Кривой Эфир
			
			elif call.data == 'atl6':
				sti = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Krivoy\\photo_2022-01-21_00-08-25.jpg', 'rb')
				bot.send_photo(call.message.chat.id, sti)
				sti1 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Krivoy\\atl_-_serpantin_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti1)
				sti2 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Krivoy\\atl__stewart_-_maneken_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti2)
				sti3 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Krivoy\\atl_-_zabil_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti3)
				sti4 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Krivoy\\atl_feat_lazernaja_boroda_-_vodjanoj_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti4)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Кривой Эфир"')
			#Радио апокалипсис
			elif call.data == 'atl7':
				sti = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Radio\\photo_2022-01-21_00-01-27.jpg', 'rb')
				bot.send_photo(call.message.chat.id, sti)
				sti1 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Radio\\atl_-_adrenohrom_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti1)
				sti2 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Radio\\atl_-_jashchik_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti2)
				sti3 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Radio\\atl_-_junost-89_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti3)
				sti4 = open('E:\\Prickoli\\BOT\\Music\\RAP\\ATL\\Radio\\atl_feat_zaraza_-_urozhaj_(z2.fm).mp3', 'rb')
				bot.send_audio(call.message.chat.id, sti4)
				bot.send_message(call.message.chat.id, 'Вот трек лист из альбома "Радио апокалипсис"')
				
			elif message.text == ''	:
				bot.send_message(message.chat.id, 'ERROR')		
			
			
			
	except Exception as e:
    		print(repr(e))
 
#run
bot.polling(none_stop=True)


