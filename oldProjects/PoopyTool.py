import speech_recognition as sr
from time import strftime
import webbrowser
import os
import random
import pyttsx3
from deep_translator import GoogleTranslator
import wikipedia

# pip install SpeechRecognition webbrowser pyttsx3 deep_translator wikipedia
# Вроде ничего не забыл | Автор Michi The Cat (делал для себя, так что судить право не имеешь)
# Телега: https://t.me/TeaTechnology | Версия: 1.2 (Ну я добавил ещё полезных себе команд и мне всё ещё лень делать код красивым, как ни как для себя же)

r, mic = sr.Recognizer(), sr.Microphone()
r.energy_threshold = 400
r.pause_threshold = 0.8
r.dynamic_energy_threshold = True
with mic as source: r.adjust_for_ambient_noise(source, duration=1)

volume = 1.0
rate = 200
def speak(text):
    global volume, rate
    engine = pyttsx3.init()
    engine.setProperty('volume', volume)
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

print("""Скажите 'Какашка козявка' и через секунду свой запрос:

Время - показывает время
Найди * - ищет что-то указанное через гугл
Выход - прекращение работы
Выключи компьютер - выключает компьютер
Голос - отвечает что слышит вас
Число - случайное число от 0 до 255
Кубик - случайное число от 1 до 6
Орёл или решка / Монетка - случайное булевое значение
Переведи на английский - перевод на английский
Переведи на русский - перевод на русский
Переведи на украинский - перевод на украинский
Вычисли [эксперементально] - вычисляет значения [работает адекватно только сумма и вычисление]
Случайное значени * и * [эксперементально] - возвращает значение в заданном диапозоне [иногда цифры определяются как строки, что мешает]
YouTube * - открыть ютуб с запросом
RuTube * - открыть рутюб с запросом
Википедия * - открыть википедию с запросом
Статья краткая * - находит статью в википедии и зачитывает строку
Статья полная * - находит статью в википедии и зачитывает её
Тише / Громче / Быстрее / Медленнее / Сброс - для регулирования озвучки\n""")
speak('Привет!')

while True:
    try:
        with mic as source: 
            audio = r.listen(source, timeout=2, phrase_time_limit=3)
        text = r.recognize_google(audio, language="ru-RU").lower()
        
        if "какашка козявка" in text:
            print("Слушает запрос...")
            speak(random.choice(["Чё?", "А?", "Слушаю", "Чего?"]))
            with mic as source: 
                command = r.recognize_google(r.listen(source), language="ru-RU")
            print(f"> Команда: {command}")
            command = command.lower()

            if "время" in command: 
                print(strftime("%H:%M"))
                speak(strftime("Сейчас %H:%M"))

            elif "найди" in command:
                webbrowser.open(f"https://www.google.com/search?q={command[5:]}")
                speak(strftime(f"Открываю '{command[5:]}'"))

            elif "выключи компьютер" in command:
                speak("Прощайте!")
                os.system("shutdown /s /t 0")

            elif "выход" in command: 
                speak(random.choice(['Пока', 'Выключаюсь', 'До встречи']))
                break

            elif "голос" in command:
                print("Слышу")
                speak(random.choice(['Гав гав', 'Да, я тут', 'Подаю голосовой сигнал']))

            elif "число" in command:
                num = random.randint(0, 255)
                print(num)
                speak(str(num))
                
            elif "кубик" in command:
                num = random.randint(1, 6)
                print(num)
                speak(str(num))

            elif ("орёл или решка" in command) or ("монетка" in command):
                num = bool(random.randint(0, 1))
                print(num)
                speak(str(num))

            elif "переведи на английский" in command:
                translated = GoogleTranslator(source='auto', target='en').translate(command[22:])
                print(translated)
                speak(translated)

            elif "переведи на русский" in command:
                translated = GoogleTranslator(source='auto', target='ru').translate(command[19:])
                print(translated)
                speak(translated)

            elif "переведи на украинский" in command:
                translated = GoogleTranslator(source='auto', target='uk').translate(command[22:])
                print(translated)
                speak(translated)

            elif "вычисли" in command:
                num = eval(command[7:])
                print(num)
                speak(str(num))

            elif "случайное значение" in command:
                _ = command[19:].split(" и ")
                num = random.randint(int(_[0]), int(_[1]))
                print(num)
                speak(str(num))

            elif "youtube" in command:
                webbrowser.open(f"https://www.youtube.com/results?search_query={command[7:]}")
                speak(strftime(f"Открываю на ютубе '{command[7:]}'"))

            elif "rutube" in command:
                webbrowser.open(f"https://rutube.ru/search/?query={command[6:]}")
                speak(strftime(f"Открываю на рутюбе '{command[6:]}'"))
            
            elif "википедия" in command:
                webbrowser.open(f"https://ru.wikipedia.org/wiki/{command[9:]}")
                speak(strftime(f"Открываю на википедии '{command[9:]}'"))

            elif "статья краткая" in command:
                topic = command[14:].strip()
                if topic:
                    wikipedia.set_lang("ru")
                    try:
                        summary = wikipedia.summary(topic, sentences=2)
                        print(summary)
                        speak(summary)
                    except:
                        print("Не удалось найти статью")
                        speak("Не удалось найти статью")

            elif "статья полная" in command:
                topic = command[13:].strip()
                if topic:
                    wikipedia.set_lang("ru")
                    try:
                        summary = wikipedia.summary(topic, sentences=10)
                        print(summary)
                        speak(summary)
                    except:
                        print("Не удалось найти статью")
                        speak("Не удалось найти статью")

            elif "громче" in command:
                if volume < 1.0:
                    volume += 0.1
                    print(volume)
            
            elif "тише" in command:
                if volume > 0.11:
                    volume -= 0.1
                    print(volume)

            elif "быстрее" in command:
                if rate < 4000:
                    rate += 50
                    print(rate)

            elif "медленнее" in command:
                if rate > 50:
                    rate -= 50
                    print(rate)

            elif "сброс" in command:
                rate = 200
                volume = 1.0
                print("Успешно!")

            else:
                print("> Команда не найдена")
                speak("Не понимаю")

    except: 
        continue