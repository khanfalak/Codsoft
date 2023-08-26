# Rule-based chatbot with predefined responses
from http.client import responses
import random
class RuleBasedChatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hello! How can I assist you?","What can i do for you?"],
            "hi":["Hello! How can I assist you?","What can i do for you?"],
            "heya":["Hello! How can I assist you?","What can i do for you?"],
            "hey":["Hello! How can I assist you?","What can i do for you?"],
            "how are you": ["I'm good,How about you?","Great!"],
            "tell me a joke":["Why dont scientists trust atoms? Because they make up everything!","What do you call fake spaghetti? An impasta!","Why dont skeletons fight each other? They dont have the guts!"],
            "some more jokes":["Why dont scientists trust atoms? Because they make up everything!","What do you call fake spaghetti? An impasta!"],
            "goodbye!": ["Goodbye! Have a great day!","Sure! Have a great day!"],
            "bye": ["Goodbye! Have a great day!","Sure! Have a great day!"],
            "see you soon": ["Goodbye! Have a great day!","Sure! Have a great day!"],
            "what is your age": ["I'm a chatbot and don't have an age.","Robots do not age"],
            "how is the weather today": ["I'm sorry, I can't provide real-time weather information.","Its better if you searched the exact thing on Google"],
            "default": ["I'm sorry, I don't understand that.","Its better if you searched the exact thing on Google","I'm afraid i don't know it"]
            
        }
    

    def get_response(self, user_input):
        user_input = user_input.lower()
        for keyword, responses in self.responses.items():
            if keyword in user_input:
                return random.choice(responses)  # Select a random response from the list
        return random.choice(self.responses["default"])

# Main loop
def main():
    chatbot = RuleBasedChatbot()
    print("Chatbot: Hello! How can I assist you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
