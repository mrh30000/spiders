import re
text = """

"""

print(re.sub(r'(.*?):(.*)',r'"$1":"$2",',text,re.S))