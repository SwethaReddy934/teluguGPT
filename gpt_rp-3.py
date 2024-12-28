from indic_transliteration import sanscript
from langdetect import detect
from googletrans import Translator
import openai
#from apikey import APIKEY


openai.api_key ="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"




input_str = str(input())
# Set the input string
#input_str = 'తెలుగు లిపిని ఇంగ్లీష్‌కు మార్చేందుకు ఉపయోగించండి'

# Specify the input and output scripts
input_script = sanscript.TELUGU
output_script = sanscript.ITRANS

# Transliterate the input string
output_str = sanscript.transliterate(input_str, input_script, output_script)
msg=output_str
# Print the output string
print("prompt for gpt: ",output_str)



output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": msg}])


# Print out the whole output dictionary
#print(output)
out_text=output['choices'][0]['message']['content']
# Get the output text only
print("\nGpt output: \n",out_text)

def is_telugu(out_text):
    lang = detect(out_text)
    return lang == 'te'

def translate_to_telugu(text):
    translator = Translator()
    result= translator.translate(text, src='en',dest='te')
    return result.text

if not is_telugu(out_text):
    telugu_text = translate_to_telugu(out_text)
    print("Translated to Telugu:", telugu_text)
else:
    print("Text is already in Telugu.")

#output_str = sanscript.transliterate(text, output_script,input_script)
#print(output_str)
