import importlib.metadata
import tiktoken
print("version-",importlib.metadata.version("tiktoken"))
tokenizer=tiktoken.get_encoding("gpt2")
textforllm=(
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
    "of someunknownPlace."
)
integers=tokenizer.encode(textforllm, allowed_special={"<|endoftext|>"})
print(integers)
strings=tokenizer.decode(integers)
print(strings)

i=tokenizer.encode("bcuiw bfu ' ; [ ' ; [   2356    ?///]] bfyg bsyug fuiq")
print(i)
s=tokenizer.decode(i)
print(s)