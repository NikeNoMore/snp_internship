char = "abcdefghijklmnopqrstuvwxyz"


class BlockIter:
    def __init__(self, text, block_length, order, decrypt):
        self.text = text
        self.length = block_length
        self.order = order
        self.current = 0
        self.decrypt = decrypt

    def __next__(self):
        if (self.current + 1) * self.length <= len(self.text):
            block = self.text[self.current * self.length:(self.current + 1) * self.length]
        elif self.current * self.length < len(self.text):
            block = self.text[self.current * self.length:]
            block += (self.length - len(block)) * " "
        else:
            raise StopIteration
        encrypt_block = ""
        if not self.decrypt:
            for i in range(self.length):
                encrypt_block += block[self.order[i]]
        else:
            for i in range(self.length):
                encrypt_block += block[self.order.index(i)]
        if self.decrypt and (self.current + 1) * self.length == len(self.text):
            encrypt_block = encrypt_block.strip()
        self.current += 1
        return encrypt_block

    def __iter__(self):
        return self


class BlockTranspositionCipher:
    def __init__(self, text, key, decrypt=False):
        self.key = key.lower()
        self.text = text
        self.order = []
        self.decrypt = decrypt
        for a in self.key:
            if a not in char:
                raise ValueError("{0} in key is not an english character".format(a))
            num = ord(a) - 97
            if num in self.order:
                raise ValueError("there is more than one instance of {0} in the key".format(a))
            self.order.append(num)

    def __iter__(self):
        return BlockIter(self.text, len(self.order), self.order, self.decrypt)



text = "HELLOWORLD"
# BlockTranspositionCipher(text, "бва")
# BlockTranspositionCipher(text, "aba")
key = "bAc"
print("Процесс шифрования по блокам:")
cipher = BlockTranspositionCipher(text, key)
for i, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {i}: '{encrypted_block}'")

cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")

print("\nПроцесс дешифрования по блокам:")
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
for i, decrypted_block in enumerate(decipher, 1):
    print(f"Блок {i}: '{decrypted_block}'")

decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'")

cipher = BlockTranspositionCipher('CODE WITH PYTHON!', 'dacb')
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")

decipher = BlockTranspositionCipher('ECDOT IWYHP NTOH !  ', 'dacb', decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'")