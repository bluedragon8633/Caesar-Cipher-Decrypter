alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print('Enter encrypted text:')
encrypted=input()
offset=0
for x in range(25):
    i=0
    decrypted=''
    for x in range(len(encrypted)):
        decrypted=decrypted+alphabet[alphabet.index(encrypted[i])+offset]
        i=i+1
    offset=offset+1
    if decrypted.count('a')==0 and decrypted.count('e')==0 and decrypted.count('i')==0 and decrypted.count('o')==0 and decrypted.count('u')==0 and decrypted.count('y')==0:
        i=0
    else:
        print(str(offset)+': '+decrypted)
