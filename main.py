import re
with open("the-verdict.txt", "r") as file:
    raw_text = file.read()

preprocessed = re.split(r'([,.;:?_"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(preprocessed[:30])