from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
import random
from enum import Enum


class ModelIds(str, Enum):
    SPANISH = 'en-es'
    FRENCH = 'en-fr'
    GERMAN = 'en-de'


def setup_translator():
    api_key = 'p_8R7_hWnw_MOwrbqNoKgpoiBfQFy-O9xWXxBpC9bLDA'

    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')
    return language_translator

def get_languages(language_translator):
    response = language_translator.list_models().get_result()['models']
    model_ids = [x['model_id'] for x in response]
    print("MODEL IDS")
    print(model_ids)
    response = language_translator.list_languages().get_result()['languages']
    print("LANGUAGES")
    languages = [{"code": x['language'], "name": x["language_name"]} for x in response]
    for lang in languages:
        print(lang)
    
    #print(json.dumps(response, indent=2, ensure_ascii=False))

    
def run_example(language_translator):
    translation = language_translator.translate(
        text='Hello, how are you today?',
        model_id=ModelIds.SPANISH).get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    print("-----------------")
    print(translation['translations'][0]['translation'])

def read_input():
    model_ids = [ModelIds.SPANISH, ModelIds.GERMAN, ModelIds.FRENCH]
    picked_model_id = None
    while picked_model_id is None:
        print("Pick a language:")
        print("1. Spanish")
        print("2. German")
        print("3. French")
        user_input = input()
        try:
            user_input_number = int(user_input)
            if 0 < user_input_number <= len(model_ids):
                picked_model_id = model_ids[user_input_number-1]
            else:
                raise Exception()
        except:
            print("Error. Enter a valid number.")
        

    print("Enter your vocab words as a space-separated list:")
    user_input = input()
    words = user_input.split(" ")
    return words, picked_model_id


def do_quiz(language_translator, words, model):
    while True:
        words_copy = words[:]
        picked_word = random.choice(words_copy)
        original_word = picked_word
        response = language_translator.translate(text=picked_word, model_id=model).get_result()
        translated_word = response['translations'][0]['translation']

        # get possible answers
        choices = []
        choices.append(picked_word)
        words_copy.remove(picked_word)

        for _ in range(3):
            picked_word = random.choice(words_copy)
            choices.append(picked_word)
            words_copy = words_copy[:]
            words_copy.remove(picked_word)

        random.shuffle(choices)
        print(choices)

        print("One word was randomly chosen from your vocab words and translated to "+ ModelIds(model).name  +
        ". The translated word is: "  + translated_word + ". What is this word in English?")
        for i in range(4):
            print(str(i+1) + ") " + choices[i])
        user_choice = int(input())
        while(choices[user_choice-1] != (original_word)):
            print("Incorrect, please try again")
            user_choice = int(input())
        print("Correct")
        quit = input("Would you like to quit (y/n)?")
        if(quit == 'y'): break



    if len(words) < 4:
        print("Not enough words - minimum of 4 - exiting")
        return
    
    

        
if __name__ == "__main__":
    translator = setup_translator()
    #run_example(translator)
    words, model = read_input()
    do_quiz(translator, words, model)

