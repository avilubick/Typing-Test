from wonderwords import RandomSentence
import keyboard
import time
import os

s = RandomSentence()
wlist = []

for i in range(5):
    wlist.append(s.bare_bone_with_adjective())

for val,x in enumerate(wlist):
    x = x.replace(".","")
    wlist[val-1] = x.lower()

sent = ""
for j in wlist:
    sent += j
    sent += " "

start = time.time()
print(sent)
for val2, i in enumerate(sent):
    if val2 == len(sent)-1:
        break
    keyboard.wait(i)
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')
    print(sent[:val2+1].upper(),sent[val2+1:])

end = time.time()

ttime = end - start
wpm = 60 / ttime * 24

print(f"Typing speed: {int(wpm)}wpm")
