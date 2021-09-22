import pyttsx3
import subprocess

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0')

def text_to_file(text): # функция преобразования текста в звуковой файл
    mp3_file = 'data/test.mp3' # указываем путь для mp3 файла 
    ogg_file = 'data/test_out.ogg' # указываем путь для ogg файла
    engine.save_to_file(text, mp3_file) # текст, который набирается а телеграм преобразовывается в mp3 файл
    engine.runAndWait() # запуск получившегося mp3 файла
    subprocess.run(['ffmpeg', '-i', mp3_file, '-acodec', 'libopus', ogg_file, '-y']) # преобразование mp3 файла в ogg файл
    return ogg_file # исполнение ogg файла
    

