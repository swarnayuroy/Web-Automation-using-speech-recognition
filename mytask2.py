# - *- coding: utf- 8 - *-
from textblob import TextBlob
import speech_recognition as sr
from googletrans import Translator
from selenium import webdriver

speech = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("Say a search engine: ")
        audio = speech.listen(source)
        s_engine = speech.recognize_google(audio)       #recognising the search engine
        print("Engine recognised as", s_engine)

         #listening, detecting the language and translating the item to be searched
        print("\nListening...")
        audio = speech.listen(source)   #listening to user's voice
        searchItem = speech.recognize_google(audio)
        word = TextBlob(searchItem)
        detect = word.detect_language()   #detecting the language
        if(detect != 'en'):
            translator = Translator()
            word = translator.translate(word, dest=detect).text  
            print("recognised " + word)
            word = translator.translate(word, dest='en').text   #translating the language to 'english' for search
        print("\nSearching...", word)

     #Working with browser
    driver = webdriver.Chrome()
    if(s_engine in ['Google', 'google']):
        driver.get('https://google.com')
        searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        searchbox.send_keys(word)
        searchButton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
        searchButton.click()
    elif(s_engine in ['YouTube', 'Youtube', 'youtube']):
        if(" " in searchItem):
            searchItem = word.replace(" ", "+")
        searchItem = "https://www.youtube.com/results?search_query=" + searchItem
        driver.get(searchItem)
    elif(s_engine in ['Wikipedia', 'Wiki', 'wikipedia', 'wiki']):
        driver.get('https://en.wikipedia.org/wiki/Main_Page')
        searchbox = driver.find_element_by_xpath('//*[@id="searchInput"]')
        searchbox.send_keys(word)
        searchButton = driver.find_element_by_xpath('//*[@id="searchButton"]')
        searchButton.click()
    else:
        print("We couldn't recognize the search engine")
    print("\nExecution successful.")
    
except Exception as e:
    print(e)
    print("Service time-out !")
