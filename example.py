from src.translate import GoogleTranslate

text_to_translate = "Halo dunia."

# Complete list of all country ISO codes see "language.json"

from_lang = "id"
to_lang = "ko"

app = GoogleTranslate(text_to_translate, from_lang, to_lang)
result = app.translate()

print(result)