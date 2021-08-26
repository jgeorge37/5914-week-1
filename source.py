from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
import random


def setup_translator():
    api_key = ''

    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')
    return language_translator

    
def run_example(language_translator):
    translation = language_translator.translate(
        text='Hello, how are you today?',
        model_id='en-es').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    print("-----------------")
    print(translation['translations'][0]['translation'])

def read_input():
    print("Enter your vocab words as a space-separated list:")
    user_input = input()
    words = user_input.split(" ")
    return words




def do_quiz(language_translator, words):
    def do_question():
        # pick word and translate
        picked_word = random.choice(words_copy)
        response = language_translator.translate(text=picked_word, model_id='en_us').get_result()
        translated_word = response['translations'][0]['translation']

        # get possible answers
        choices = []
        choices.append(picked_word)
        words_copy = words[:]
        words_copy.remove(picked_word)

        for _ in range(3):
            picked_word = random.choice(words_copy)
            choices.append(picked_word)
            words_copy = words_copy[:]
            words_copy.remove(picked_word)

        random.shuffle(choices)



    if len(words < 4):
        print("Not enough words - minimum of 4 - exiting")
        return
    
    

        
if __name__ == "__main__":
    translator = setup_translator()
    run_example(translator)
    #words = read_input()
    #do_quiz(translator, words)

