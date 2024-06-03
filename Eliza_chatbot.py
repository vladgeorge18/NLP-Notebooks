import re
def swap_pronouns(phrase):
    phrase2 = phrase
    if "I'm" in phrase:
        phrase2 = re.sub("I'm","you're",phrase2)
    if "I am" in phrase:
        phrase2 = re.sub("I am","you are",phrase2)
    if 'I' in phrase:
        phrase2 = re.sub('I','you',phrase2)
    if 'my' in phrase:
        phrase2 = re.sub('my','your',phrase2)
    if 'My' in phrase:
        phrase2 = re.sub('My','your',phrase2)
    if 'was' in phrase:
        phrase2 = re.sub('was','were',phrase2)
    return phrase2
# MAIN
usertexts = ["Hello. My name is George",
 "How can I deal with my anxiety problem?",
 "What can I do in order to overcome my fears?",
 "It seems like there is nothing I can do about to feel better",
 "I am 25 years old",
 "Do you remember when I was singing outside?",
 "I feel like I don't have real friends",
 "What should I do to be more happy?",
 "I am sad",
 "It's cold",
 "I can't go outside",
 "Can you give me an advice about how to deal with  my nightmares?",
 "Sometimes it seems like nothing matters anymore",
 "I hate to take a walk in the nature",
 "My mom says I am depressed most of the time",
 "From time to time I feel like I want to give up",
 "Mario says I'm always sad all the time",
 "Thank you for helping me!",
 "Thanks a lot!"]

for t in usertexts:
    print('User: ',t)
    if re.search("(\d+) years old",t):
        print("ELIZA:","The age does not matter")
    elif re.search("How can I (.*)\?",t):
        match = re.search("How can I (.*)\?",t)
        response = "Hmm... Let's explore why you want to "+swap_pronouns(match.group(1))
        print("Eliza:",response)
    elif re.search("(.*)\W?\s?My name is (.*)",t):
        match = re.search("(.*)\W?\s?My name is (.*)",t)
        response = "Hello, "+match.group(2)+"! How can I help you today?"
        print("Eliza:",response)
    elif re.search("(.*) says (I'm|I am)(?: always)? (depressed|sad|anxious)(.*)",t):
        match = re.search("(.*) says (I'm|I am)(?: always)? (depressed|sad|anxious)(.*)",t)
        response = "I am sorry to hear that " + swap_pronouns(match.group(1)) + " says you are " + match.group(3)  
        print("ELIZA:",response)
    elif re.search("I am (sad|depressed|anxious)",t):
        match = re.search("I am (sad|depressed|anxious)",t)
        response = "Why are you " + match.group(1) + "?"
        print("ELIZA:",response)
    elif re.search("Do you remember when (.*)",t):
        match = re.search("Do you remember when (.*)",t)
        response = "No, what happened when " + swap_pronouns(match.group(1))
        print("ELIZA:",response)
    elif re.search("I (hate|can't) (.*)",t):
        match = re.search("I (hate|can't) (.*)",t)
        response = "Why do you think you " + match.group(1) +" " +swap_pronouns(match.group(2)) + "?"
        print("ELIZA:",response)
    elif re.search("(.*?) (advice|sugestion) (.*)",t):
        match = re.search("(.*?) (help|advice|sugestion) (about|for|on) (.*)",t)
        response = "What kind of " + match.group(2) +" are you looking for regarding on " + swap_pronouns(match.group(4))
        print("ELIZA:",response)
    elif re.search("(.*)(I|It|it) (feel|seems|feels) like (.*)",t):
        match = re.search("(.*)(I|It|it) (feel|seems|feels) like (.*)",t)
        response = "Feelings like " + swap_pronouns(match.group(4)) + " are justifiable.  What do you think might improve the situation?"
        print("ELIZA:",response)
    elif re.search("What (should|can) I do(?: to| about| in order to)?(.*)",t):
        match = re.search("What (should|can) I do(?: to| about| in order to)?(.*)",t)
        response = "Have you discussed with someone about how to"+swap_pronouns(match.group(2))
        print("ELIZA:",response)
    elif re.search("(.*)(Thanks|Thank|thank)( you)?(.*)",t):
        response = "You're welcome! If you have any more questions or need further assistance, feel free to ask "
        print("ELIZA:",response)
    else:
        print("ELIZA: Aha... continue.")