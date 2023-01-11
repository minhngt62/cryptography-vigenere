# Vigenere Cipher & Kasiski Method

The [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) (French pronunciation: ​[viʒnɛːʁ]) is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution. First described by Giovan Battista Bellaso in 1553, the cipher is easy to understand and implement, but *it resisted all attempts to break it until 1863, three centuries later*. This earned it the description le chiffrage indéchiffrable (French for 'the indecipherable cipher'). Many people have tried to implement encryption schemes that are essentially Vigenère ciphers. In 1863, Friedrich Kasiski was the first to publish a general method of deciphering Vigenère ciphers.

Our work is to implement the encryption and decryption of Vigenere cipher, then introduce Kasiski examination method with a usual cryptanalysis algorithm in order to break the cryptography.

<p align="center">
  <img src="https://user-images.githubusercontent.com/86721208/211774407-7f27727f-ff57-456a-818a-f8b68e841cbf.png" />
</p>

## Deep Learning - DSAI K65: Group 16
1. Nguyễn Tống Minh (Email: minh.nt204885@sis.hust.edu.vn)
2. Nguyễn Thị Hương Giang (Email: giang.nth200185@sis.hust.edu.vn)
3. Hoàng Long Vũ (Email: vu.hl204897@sis.hust.edu.vn)

## Project Structure

```
vigenere_cipher/               # source code
-- ./cryption/                 # encryption & decryption of Vigenere cipher
-- ./attacking/                # attack method: Kasiski & cryptanalysis
main.py                        # demo program
README.md
```
---
