languages = {
    "hello": "హలో",
    "good morning": "శుభోదయం",
    "thank you": "ధన్యవాదాలు",
    "welcome": "స్వాగతం"
}

text = input("Enter English word: ").lower()

if text in languages:
    print("Translation:", languages[text])
else:
    print("Word not found")