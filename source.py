from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json


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

def read_input():
    pass

def do_quiz(language_translator):
    pass

if __name__ == "__main__":
    translator = setup_translator()
    run_example(translator)
    # read_input()
    # do_quiz(translator)

