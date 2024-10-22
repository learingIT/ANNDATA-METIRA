from groq import Groq

# Initialize the Groq API client with your key
client = Groq(api_key="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")

def generate_response(user_message, language):
    """Interact with Groq API and generate a streaming response focused on farming."""
    
    # Language context for the AI
    language_context = {
        "english": "You are an AI assistant designed to provide information and assistance specifically for farmers. Please respond in English with advice, tips, and information related to agriculture, crop management, livestock care, sustainability, and related topics.",
        "hindi": "आप एक एआई सहायक हैं जिसे किसानों के लिए जानकारी और सहायता प्रदान करने के लिए डिज़ाइन किया गया है। कृपया कृषि, फसल प्रबंधन, पशुपालन देखभाल, स्थिरता और संबंधित विषयों से संबंधित सलाह, टिप्स और जानकारी हिंदी में प्रदान करें।",
        "marathi": "तुम्ही एक एआय सहाय्यक आहात जो शेतकऱ्यांना माहिती आणि सहाय्य प्रदान करण्यासाठी डिझाइन केलेले आहे. कृपया कृषी, पिक व्यवस्थापन, पशुपालन देखभाल, टिकाव आणि संबंधित विषयांवर मराठीत सल्ला, टिपा आणि माहिती द्या."
    }

    completion = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=[
            {"role": "system", "content": language_context[language]},  # Provide context to the AI based on selected language
            {"role": "user", "content": user_message}
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=True,  # Enable streaming for dynamic response
    )

    print("AI:", end=" ", flush=True)
    for chunk in completion:
        # Stream the response as it's generated
        print(chunk.choices[0].delta.content or "", end="", flush=True)
    print("\n")  # Print a new line at the end of the message

def chatbot():
    """Main loop to interact with the chatbot focused on farmers."""
    print("Welcome to the AnnadattaMitra AI Chatbot! Type 'quit' to exit.\n")
    print("Please select your language:")
    print("1. English")
    print("2. Hindi")
    print("3. Marathi")
    
    language_choice = input("Enter the number of your choice: ")
    if language_choice == "1":
        language = "english"
    elif language_choice == "2":
        language = "hindi"
    elif language_choice == "3":
        language = "marathi"
    else:
        print("Invalid choice. Defaulting to English.")
        language = "english"

    print(f"You selected: {language.capitalize()}. Please ask any farming-related questions or request assistance.")
    
    while True:
        user_input = input(f"You ({language.capitalize()}): ")
        if user_input.lower() == "quit":
            print("Goodbye! See you soon.")
            break
        generate_response(user_input, language)

if __name__ == "__main__":
    chatbot()
