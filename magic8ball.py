#Magic 8 Ball

import json
import random
import time

# For text-to-speech API
import gtts
import os
from playsound import playsound


import multiprocessing




# Not working
# For music API
#need to do "pip install ytmusicapi" to get ytmusicapi working
from ytmusicapi import YTMusic

#YTMusic.setup(filepath="headers_auth.json")

# yt = YTMusic(filepath = "headers_auth.json", headers_raw = "")

# playlistId = yt.create_playlist('test', 'test description'

#generic search for youtube (not specific video)
# search_results = yt.search('lofi hip hop radio - beats to relax/study to')
# yt.add_playlist_items(playlistId, [search_results[0]['videoId']])




# pip3 install gTTS pyttsx3 playsound
# pip uninstall playsound
# pip install playsound==1.2.2

# Dictionary to store all magic 8 ball responses
responses = {
    # Positive Respones
    1: "It is certain.",
    2: "It is decidedly so.",
    3: "Without a doubt.",
    4: "Yes definitely.",
    5: "You may rely on it.",
    6: "As I see it, yes.",
    7: "Most likely.",
    8: "Outlook good.",
    9: "Yes.",
    10: "Signs point to yes.",
    # Neutral Responses
    11: "Reply hazy, try again.",
    12: "Ask again later.",
    13: "Better not tell you now.",
    14: "Cannot predict now.",
    15: "Concentrate and ask again.",
    # Negative Responses
    16: "Don't count on it.",
    17: "My reply is no.",
    18: "My sources say no.",
    19: "Outlook not so good.",
    20: "Very doubtful."
}

# Prints a random value from the 'reponses' dictionary
def getResponse():
    randomNumber = random.randrange(1, len(responses))
    print(responses[randomNumber])
    tts = gtts.gTTS(responses[randomNumber])
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")

# Prompts the user to ask a question
# Take in user input
# Wait before providing a response
# Repeat steps indefinitely
def magic8ball():
    
    while True:
        elevator_music = multiprocessing.Process(target=playsound, args=('/Users/user/Desktop/Clemson Classes/Fall2022/cpsc3720/Take-me-out-to-the-8-ball-game/elevator_music.mp3',))
        elevator_music.start()
        print("Please ask a question.")
        question = input()
        print("Thinking...")
        time.sleep(10.5)   #random.randrange(3, 5)     <--- alternative code to have randomized time
        elevator_music.terminate()
        getResponse()
        time.sleep(3)

# Main function
if __name__ == "__main__":
    magic8ball()
