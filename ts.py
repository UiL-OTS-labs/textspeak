from gtts import gTTS

mytextlist = [
        'ball',
        'key',
        'car',
        'chair',
        'mug',
        'phone',
        'shoe',
        'house',
        'boat']

language = 'en'

for mytext in mytextlist:
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(mytext.replace(' ','_') + ".mp3")
    print ("saved: " + mytext + ".mp3")

print ('-------- done --------')
