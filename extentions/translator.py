from deep_translator import GoogleTranslator

def translate_text(text, from_language='auto', target_language='en'):
    # Initialize GoogleTranslator with auto detection
    translator = GoogleTranslator(source=from_language, target=target_language)
    
    try:
        # Translate the text
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return None

