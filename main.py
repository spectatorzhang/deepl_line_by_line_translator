target_lang = 'ZH'
txt = 'Paste Source Text Here'
api = 'Paste Your DeepL Pro API Key Here'

# Pre-installation of deepl package is required
from datetime import datetime
import deepl

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d-%H-%M-%S")

#Output Saved File Will Be Named Under This Format:
file_name = "Output-"+formatted_time+".txt"

translator = deepl.Translator(api)
text_file = open (file_name, "w", encoding='utf-8')
i = 1
for line in txt.splitlines():
    if line=='':
        text_file.write('\n')
        i+=1
        continue
    result = translator.translate_text(line, target_lang=target_lang)
    #print(result.detected_source_lang)
    translated_text = result.text
    text_file.write(line)
    text_file.write('\n')
    text_file.write(translated_text)
    text_file.write('\n')
    print('Process:', i, 'Out of ', len(txt.splitlines()))
    i += 1
text_file.close()
print(target_lang + " Saved as " + file_name)
