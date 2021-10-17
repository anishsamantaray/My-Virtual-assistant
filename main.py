def run_26():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+ time)


    elif 'who is' in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'out' in command:
        talk("Ya sure let's hang out together")
    elif 'love' in command:
        talk("I love you too Anish ")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'best' in command:
        talk("Prime Factor is the best")
    elif "which day " in command:
        tellDay()
    elif 'search' in command:
        search = command.replace('search', '')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what i found for ' + search)
        talk('Here is what i found for ' + search)

    elif 'can you find the location of' in command:
        location = command.replace('can you find the location of', '')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the map of ' + location)
        talk('Here is the map of ' + location)
    elif 'how are you' in command:
        talk('I am fine. Thank You! How about you?')

    elif 'what are you doing' in command:
        talk('I am free , what about you')

    elif 'exit' in command:
        exit()
