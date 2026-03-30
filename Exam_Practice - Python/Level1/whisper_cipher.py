# authorized function: none. 
# prototpye: write function only That creates a simple cipher by shifting letters 
# in a string by a given amount non-alphabetic characters should remain unchanged. 
# def whisper_cipher(text: str, shift: int)->str example: whisper_cipher("hello", 3) with output: "Khorr"

def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    shift = shift % 26

    for char in text:

        if "a" <= char <= "z":
            position = ord(char) - ord("a")
            position = position + shift
            position = position % 26
            result = result + chr(position + ord("a"))

        elif "A" <= char <= "Z":
            position = ord(char) - ord("A")
            position = position + shift
            position = position % 26
            result = result + chr(position + ord("A"))

        else:
            result = result + char

    return result


def main():
    text = "AbC"
    shift = 5

    encrypted = whisper_cipher(text, shift)

    print("Original :", text)
    print("Encrypted:", encrypted)


if __name__ == "__main__":
    main()

