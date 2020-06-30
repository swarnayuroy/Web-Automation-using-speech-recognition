import speech_recognition as sr
from selenium import webdriver

speech = sr.Recognizer()        #recognising user's  speech

try:
    #Listen to user
    with sr.Microphone() as source:
        print("Say a search engine")
        audio = speech.listen(source)
        s_engine = speech.recognize_google(audio)    #we get the search engine
        print("Engine recognised as", s_engine)
        
        print("\nSay what you want to search ? ")
        audio = speech.listen(source)
        searchItem = speech.recognize_google(audio)    #we get the searching object
        print("Searching...", searchItem)
        
    #Working with browser
    driver = webdriver.Chrome()
    if(s_engine in ['Google', 'google']):
        driver.get('https://google.com')
        searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        searchbox.send_keys(searchItem)
        searchButton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
        searchButton.click()
    elif(s_engine in ['YouTube', 'Youtube', 'youtube']):
        '''driver.get('https://youtube.com')
        searchbox = driver.find_element_by_xpath('//*[@id="search"]')
        searchbox.send_keys(searchItem)
        searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
        searchButton.click()'''
        if(" " in searchItem):
            searchItem = searchItem.replace(" ", "+")
        searchItem = "https://www.youtube.com/results?search_query=" + searchItem
        driver.get(searchItem)
    elif(s_engine in ['Wikipedia', 'Wiki', 'wikipedia']):
        driver.get('https://en.wikipedia.org/wiki/Main_Page')
        searchbox = driver.find_element_by_xpath('//*[@id="searchInput"]')
        searchbox.send_keys(searchItem)
        searchButton = driver.find_element_by_xpath('//*[@id="searchButton"]')
        searchButton.click()
    else:
        print("We couldn't recognize the search engine")
    print("\nExecution successful.")
except:
    print("\nService time out !")
