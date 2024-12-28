from indic_transliteration import sanscript
import json
import openai

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
print(output_str)

# Load your API key from an environment variable or secret management service
openai.api_key ="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"


response = openai.Completion.create(model="text-davinci-003", prompt=msg, temperature=0, max_tokens=80)

response_json = json.dumps(response, indent=2)

json_dict = json.loads(response_json)
text_field = json_dict['choices'][0]['text']
print(text_field)

output_str = sanscript.transliterate(text_field, output_script,input_script)
print(output_str)

