import random
import time

# list of agent names that will randomly be generateted
agent = ["Zoey Lawrance", "Matt Styles", "Leonardo Owens", "Lana Garner", "Riley Fox", "Allan Ellison"]

# dictionary consisteing of keyword and response pair
responses = {
    "coffee": "The cafe opens from 7:30 AM to 6 PM on weekdays, serving variety of drinks and bakery items.The cafe provides a pleasant atmosphere for the students to hang out with their friends. ",
    "cafe": "The cafe opens from 7:30 AM to 6 PM on weekdays, serving variety of drinks and bakery items.The cafe provides a pleasant atmosphere for the students to hang out with their friends. ",
    "courses": "The University of Poppleton offers a wide range of undergraduate and postgraduate courses. Visit the courses section of website for more details details.",
    "programs": "The University of Poppleton offers a wide range of undergraduate and postgraduate courses. Visit the courses section of website for more details details.",
    "subjects": "The University of Poppleton offers a wide range of undergraduate and postgraduate courses. Visit the courses section of website for more details details.",
    "library": "The library is open from 6 AM to 8 PM on weekdays and from 10 AM to 6PM in the weekends, offering our students with peaceful space and extensive resources.",
    "sports": "Our university offers top-notch sports facilities to support our student's physical well being, such as a fully eqipped gym, swimming pool, tabble tennis and outdoor sports field.",
    "admissions": "Admissions for the upcoming semester are open! Applications can be submitted through the online admissions portal.",
    "scholarship": "Scholarship opportunities are available for students. For further information, please visit the scholarships section on our website. ",
    "dorm": "Comfortable on-campus accommodation with variety of room option are avilable to make you feel like home. Check out the dorm options on our website.",
    "room": "Comfortable on-campus accommodation with variety of room option are avilable to make you feel like home. Check out the dorm options on our website.",
    "fees": "Tuition fees vary by the course you choose. For a detailed fee structure please visit the admission section on our website.",
    "fee": "Tuition fees vary by the course you choose. For a detailed fee structure please visit the admission section on our website.",
    "events": "To engage students and foster a sense of community, our university host various events.  Kindly refer to the events calendar on our website for exact dates and details of our upcomming event.",
    "event": "To engage students and foster a sense of community, our university host various events.  Kindly refer to the events calendar on our website for exact dates and details of our upcomming event.",
    "exam": "The final exam schedule is published on the university portal. Students are advised to log in to view their routine.",
    "wifi": "Free Wi-Fi is available for all students. Login credentials are avilable in the IT Department Board.",
    "internet": "Free Wi-Fi is available for all students. Login credentials are avilable in the IT Department Board.",
    "clubs": "There are many student clubs on our university, including drama club, robotics club, debate club, sports club, and photography club.",
    "club": "There are many student clubs on our university, including drama club, robotics club, debate club, sports club, and photography club.",
    "canteen": "The canteen is open from 9 AM to 8:30 PM and offers a variety of meals, including both vegetarian and non-vegeterian options.",
    "medical": "The university infirmary is open 24/7 to provide medical help to students.",
    "health": "The university infirmary is open 24/7 to provide medical help to students.",
    "sick": "The university infirmary is open 24/7 to provide medical help to students.",
    "injury": "The university infirmary is open 24/7 to provide medical help to students.",
    "injured": "The university infirmary is open 24/7 to provide medical help to students.",
    "internships": "Career services help students find internships. Check the career portal for current oportunities.",
    "intern": "Career services help students find internships. Check the career portal for current oportunities.",
    "alumni": "The university has an active alumni network that supports current students through mentoring programs and organizing events.",
    "time": "The university operates both morning and day shifts. Morning shifts run from 7:00 AM to 10:30 AM, and day shifts run from 11:00 AM to 4:00 PM, accommodating diverse schedules for students and faculty.",
    "shift": "The university operates both morning and day shifts. Morning shifts run from 7:00 AM to 10:30 AM, and day shifts run from 11:00 AM to 4:00 PM, accommodating diverse schedules for students and faculty.",
    "shifts": "The university operates both morning and day shifts. Morning shifts run from 7:00 AM to 10:30 AM, and day shifts run from 11:00 AM to 4:00 PM, accommodating diverse schedules for students and faculty.",
    "timing": "The university operates both morning and day shifts. Morning shifts run from 7:00 AM to 10:30 AM, and day shifts run from 11:00 AM to 4:00 PM, accommodating diverse schedules for students and faculty.",
}
 # list of random responses if no keyword are found
random_responses = [
    "I'm not sure about that {user_name}, Can you provide me with more details?",
    "That's an interesting question {user_name}. Let me think about it. I'll get back to you with more details shortly",
    "I'm sorry {user_name}, I am not sure i have an answer for that right now.",
    "Hmm, I'm not sure. Could you clarify a bit more?",
    "I’ll need to check on that for you. Can I assist you with something else in the meantime?",
    "I'm not quite sure about that, but I'll find a way to get you an answer!",
    ]
# list of exit keywords
exit_keywords = ["quit", "exit", "bye", "goodbye", "end"]

# function to greet the user
def chatbot():
    # prompt user to input his/her name/
    user_name = input("Please enter your name: ").capitalize()
    # pick a random agent from the list
    agent_name = random.choice(agent)
    # a cherry greeting message for the user from their agent
    print(f"Welcome to the official website of the University of Poppleton!\nHello {user_name}, Hope you are having a good day. I am {agent_name} your virtual assistant, here to help you with any inquiries. How may I assist you today?")
    
    # start chat loop
    while True:
        # get question from the user
        queries_input = input(f"{user_name}: ").lower()
        words_in_input = queries_input.split()  # splits the sentence into words inside a list

        # exits the chat if the user decides to quit the program
        exit_detection=False
        for i in range(len(exit_keywords)):
        # check if current exit_keyword is in words_in_input list by comparing each word
            for j in range(len(words_in_input)):
                if exit_keywords[i] == words_in_input[j]: # comparing if the word matches
                    exit_detection=True
                    print(f"{agent_name}: It was a pleasure assisting you, {user_name}. Thank you for reaching out. If you have any more questions, feel free to reach out again. Have a wonderfulday!")
                    break # breaks inner loop
            j=j+1
            if exit_detection==True:
                break  # break outer loop
        i=i+1
        if exit_detection==True:
            break  # breaks the while loop 

        disconnect_choices = ["true", "false", "continue", "ok", "yes", "recommence"]
        disconnect = random.choice(disconnect_choices)  # Randomly choose if there's connectivity issue
        if disconnect=="false":
            print(f"{agent_name}:  Oops! It seems we have lost the connection. Trying to reconnect...")
            time.sleep(random.randint(3, 6))  # Simulate internet reconnecting
            print(f"{agent_name}: I am back online! Sorry for the brief interruption, {user_name}. Let’s continue.")

        # checks if keywords is present in the user's input
        response_available= False
        for keyword, response in responses.items():
            if keyword in queries_input:
                print(f"{agent_name}: {response}")
                response_avilable=True
                break

        # if no keywords are found, give a random response
        if response_available==False:
            no_keyword= random.choice(random_responses)
            print(f"{no_keyword.replace('{user_name}', user_name)}")

# Start the chatbot
chatbot()