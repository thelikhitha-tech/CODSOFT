import re
import datetime
from colorama import init,Fore

#Initialize colorama
init() 
def get_time_based_greeting():
    hour = datetime.datetime.now().hour
    print(f"[DEBUG] Hour: {hour}")
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 < hour <17:
        return "Good afternoon!"
    elif 17 < hour <21:
        return "Good evening!"
    
def get_response(user_input):
    user_input = user_input.lower()

    # Rule-based responses using if-else and pattern matching
    if re.search(r'\bhi\b|\bhello\b|\bhey\b', user_input):
        return f"{get_time_based_greeting()} Hello! How can I assist you today?"
    
    elif "how are you" in user_input:
        return "I'm doing well,thank you! How can I help you?"

    elif "your name" in user_input:
        return "I'm a chatbot developed as part of an AI internship project."

    elif "what can you do" in user_input:
        return "I can chat with you and respond to basic questions using predefined rules!"

    elif "tell me a joke" in user_input:
        return "Why did the computer show up late to work? It had a hard drive!"

    elif "what is ai" in user_input:
        return "AI stands for Artificial Intelligence — it enables machines to mimic human intelligence."

    elif "help" in user_input:
        return "You can ask me things like: 'tell me a joke', 'what is AI', 'how are you', etc."

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I didn't understand that. Can you try asking differently?"

def chatbot():
    print(Fore.CYAN + "Chatbot: Hello! I'm your AI assistant. Type 'bye' to exit." + Fore.RESET)

    # Open a file to log the conversation
    with open("chat_log.txt", "a") as log:
        while True:
            user_input = input("You: ")
            response = get_response(user_input)
            print(Fore.GREEN + "Chatbot:", response + Fore.RESET)

            # Log the conversation
            log.write(f"You: {user_input}\nChatbot: {response}\n")

            if "goodbye" in response.lower():
                break
if __name__ == "__main__":
 chatbot()