with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
print(len(text))
characters = sorted(list(set(text)))
vocab_size = len(characters)
print(''.join(characters))
stoi = {char: i for i, char in enumerate(characters)}
itos = {i: char for i, char in enumerate(characters)}
encode = lambda s: [stoi[char] for char in s]
decode = lambda l: ''.join([itos[i] for i in l])
    
    
print(encode('hello'))
print(decode(encode('hello')))
