import importlib.metadata
import tiktoken

file_path="/home/radhakant-panda/Documents/LLMs/Tokenisation/Text_To_Token/temp.txt"
with open(file_path,'r',encoding="utf-8")as file:
    text_data=file.read()
#print(text_data)

tokeniser=tiktoken.get_encoding("gpt2")
integer=tokeniser.encode(text_data)
# print(integer)
print(type(integer))
print(len(integer))
token_to_str=tokeniser.decode(integer)
print(token_to_str)
# print(token_to_str==text_data)

