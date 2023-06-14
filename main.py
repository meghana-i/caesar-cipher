alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower() 
  shift = int(input("Type the shift number:\n"))
  
shift = shift % 26

def caesar(start_text, shift_no, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_no *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_pos = position + shift_no
      end_text += alphabet[new_pos]
    else:
      end_text += char
  print(cipher_direction, end_text) 
caesar(start_text = text, shift_no = shift, cipher_direction = direction)

result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if result == "no":
  should_continue = False
  print("Goodbye")
