responses = {

    'hi' : 'hello!',
    'hey' : 'hi',
    'hello' : 'hey there!',
    'how are you?' : 'Im doing well how are you?',
    'i want to leave now' : 'sad to see you go! please type "exit"',
    'i go' : 'sad to see you go! please type "exit"',
    'help' : 'what would you like me to help you with?',
    'what can you do' : 'I can chat with you, tell bad jokes, and help you exit this script.',
    'what is the time' : 'Time for you to get a watch (I cannot read clocks yet)',
    'time?' : 'Kindly check your task bar :)',
    'tell me a joke' : 'What is an astronaut’s favorite part on a computer?                                   The space bar'

}

def sanitise(uinput):
    clean = uinput.lower().strip()
    return clean

def process (rclean):
    reply = responses.get(rclean, 'I don\'t understand, can you try again?')
    print(reply)

while True:
    uinput = input("you: ")
    rclean = sanitise(uinput)
    if rclean == 'exit':
        break
    process(rclean)