

words = [
    "casa", "albero", "notte", "sole", "montagna", "fiume", "mare", "vento", "nuvola", 
    "pioggia", "strada", "amico", "sorriso", "viaggio", "tempo", "cuore", "stella", 
    "sogno", "giorno", "libro", "porta", "luce", "ombra", "silenzio", "fiore", "luna"
]

flag = 'fiume-amico-casa-mare-{-amico-tempo-viaggio-mare-_-sole-tempo-montagna-giorno-viaggio-libro-_-sorriso-montagna-casa-viaggio-_-giorno-montagna-notte-porta-sogno-montagna-_-mare-fiume-strada-giorno-amico-vento-vento-mare-}'

flag = flag.split('-')
real_flag = ''
for w in flag:
    if w in words:
        real_flag += chr(words.index(w) + ord('a'))
    else:
        real_flag += w

print(real_flag)