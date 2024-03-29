import openai

# Set up your OpenAI API key
openai.api_key = 'your-api-key'

def get_password(theme):
    # Call ChatGPT API to get suggestions
    responseAI = openai.ChatCompletion.create(
        model="text-davinci-003",  # Choose the model
        messages=[
            {"role": "system", "content": "You"}  # You can change "You" to any username you want
        ],
        prompt=f"Generate password for '{theme}' theme:"  # Prompt with user's theme
    )
    
    suggestions = [message['content'] for message in responseAI['choices'][0]['messages']]
    
    # Generate password based on suggestions
    # Your password generation logic here
    
    # For now, just return the suggestions
    return suggestions

def main():
    theme = input("Enter a theme or description for your password: ")
    password = get_password(theme)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
