# Chapter 1 practice set 
# 1.
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
Twinkle, twinkle, little star,
How I wonder what you are!

Then the traveller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.
Twinkle, twinkle, little star,
How I wonder what you are!

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
Till the sun is in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!

As your bright and tiny spark,
Lights the traveller in the dark,—
Though I know not what you are,
 Twinkle, twinkle, little star.
Twinkle, twinkle, little star,
How I wonder what you are! 
''')

# 2.from repl  - powershell
'''
>>> 5*1
5
>>> 5*2
10
>>> 5*3
15
>>> 5*4
20
>>> 5*5
25
>>> 5*6
30
>>> 5*7
35
>>> 5*8
40
>>> 5*9
45
>>> 5*10
50
'''

# 3.
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# 4.
import os

path = '/'  

try:
    entries = os.listdir(path)
    print(f"Contents of '{path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")

# 5.
import os

# Specify the directory path
path = '/path/to/directory'  # Replace with your desired path

try:
    # List all entries in the specified directory
    entries = os.listdir(path)
    print(f"Contents of '{path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")