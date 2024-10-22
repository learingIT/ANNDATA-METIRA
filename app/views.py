from django.shortcuts import render
from django.http import JsonResponse
from groq import Groq

# Initialize the Groq API client with your key
client = Groq(api_key="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")

def home(request):
    return render(request, 'home.html')

def generate_response(user_message):
    """Interact with Groq API and generate a response focused on farming."""
    farming_context = (
        "You are an AI assistant designed to provide information and assistance specifically for farmers. "
        "Please respond with advice, tips, and information related to agriculture, crop management, "
        "livestock care, sustainability, and related topics."
    )

    completion = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=[
            {"role": "system", "content": farming_context},  # Provide context to the AI
            {"role": "user", "content": user_message}
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=False,  # Disable streaming for backend response handling
    )

    # Correctly access the content from the message
    return completion.choices[0].message.content if completion.choices else "No response generated."

def chatbot(request):
    return render(request, "chatbot.html")

from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Only for debugging; should be removed in production!
def chat_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Load JSON data
            user_message = data.get('message')  # Get the user's message
            
            if user_message:
                response = generate_response(user_message)  # Your function to generate a response
                return JsonResponse({'response': response})
            else:
                return JsonResponse({'error': 'No message provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
