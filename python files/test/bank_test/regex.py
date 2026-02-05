import re

search = re.fullmatch(r"\d+", "1239876").group()
print(search)