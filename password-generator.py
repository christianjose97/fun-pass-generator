import openai

openai.api_key = 'your-api-key'

def get_password(theme, name):
    # Call ChatGPT API to get suggestions
    responseAI = openai.ChatCompletion.create(
        model="text-davinci-003",  # Choose the model
        messages=[
            {"role": "system", "content": name}  # You can change "You" to any username you want
        ],
        prompt=f"Generate password for '{theme}' theme:"  # Prompt with user's theme
    )
    
    suggestions = [message['content'] for message in responseAI['choices'][0]['messages']]
    
    # Generate password based on suggestions
    # Add generation logic here
    
    # For now, Ill just return the suggestions
    return suggestions

def main():
    name = input("Enter a username you would like the chat to use")
    theme = input("Enter a theme or description for your password: ")
    password = get_password(theme, name)
    print("Generated Password:", password)
    print ("Make sure to save this AI generated password somewhere safe!")

if __name__ == "__main__":
    main()
