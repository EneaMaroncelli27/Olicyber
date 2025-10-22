from challenge import get_words_by_prefix
import string

with open('words.txt','r') as f:
    words = list(sorted([word.strip() for word in f.readlines()]))

with open('stream.txt', 'r') as f:
    stream = [w.strip() for w in f.readlines()]

suggested_w= []

indici = [i for i, x in enumerate(stream) if x == 'end']


suggested_w.append(stream[0:indici[0]])

for i in range(len(indici)-1):
    suggested_w.append(stream[indici[i]+1:indici[i+1]])



prefix = b''
i = 0
changed = True
bad_combos = []
while True:
    changed = False
    for c in string.ascii_letters + string.digits + "_-":
        test_prefix = prefix + c.encode()
        if test_prefix in bad_combos:
            continue  
        expected_words = get_words_by_prefix(test_prefix)
        if len(expected_words) == len(suggested_w[i])-1:
            
            print(f'Found next char: {c}')
            print(f'Current prefix: {test_prefix.decode()}')
            changed = True
            break
           
    if not changed:
        print('No more chars found')
        i -= 1
        bad_combos.append(prefix)
        prefix = prefix[:-1]
    else:
        prefix = test_prefix
        i += 1
    if i >= len(suggested_w):
        break
print(f'Final prefix: {prefix.decode()}')
