from indic_transliteration import sanscript
import openai
from langdetect import detect
from googletrans import Translator


openai.api_key ="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"
print('Request in Telugu : ')
input_str = str(input())

# Specify the input and output scripts
input_script = sanscript.TELUGU
output_script = sanscript.ITRANS

# Transliterate the input string
msg = sanscript.transliterate(input_str, input_script, output_script)
print('Prompt for Chatgpt : ',msg)

output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": msg}])


# Print out the whole output dictionary
out_text=output['choices'][0]['message']['content']

def is_telugu(out_text):
    lang = detect(out_text)
    return lang == 'te'

def translate_to_telugu(out_text):
    translator = Translator()
    result= translator.translate(out_text, src='en',dest='te')
    return result.text

if not is_telugu(out_text):
    telugu_text = translate_to_telugu(out_text)
    print("Response from Chatgpt: ", telugu_text)
else:
    print("Response from Chatgpt: ", out_text)
