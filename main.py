# utils
secret = "a580758e"
secret2 = [111, 63, 53, 61, 63, 63, 53, 111]  # facut cvu new_secret_function()
byte_len = 255

'''
def new_secret_function():
    new_secret = []
    for character in secret:
        if ord(character) & 1:
            new_secret.append((ord(character) | (1 << 3) + 7) % 256)
        else:
            new_secret.append(ord(character) ^ 13)
    return new_secret'''


def encrypt(message: str) -> str:
    encrypted = []
    for char in message:
        encrypted.append((ord(char) << 2) | (ord(char) >> 6))

    for i in range(len(encrypted)):
        for j in range(len(secret2)):
            encrypted[(i + j) % len(encrypted)] = (encrypted[(i + j) % len(encrypted)]
                                                   & byte_len) ^ secret2[j]
            # AM FACUT XOR CU secret2 de j

    return "".join([f"{character:02x}" for char in encrypted])


def decrypt(message: str) -> list:
    answers = []
    for value in range(byte_len):
        ans = ""
        for i in range(len(message) // 2):
            temp = int(message[i * 2:i * 2 + 2], 16) ^ value
            ans += chr(((temp << 6) & byte_len) | temp >> 2)
        answers.append(ans)
    return answers


if __name__ == "__main__":
    # cypher_text = encrypt("")
    cyper_text = \
        "4b939386e3bbd38683d7860f4ba39793cb0fd38ba783cf93cbd786b39393d7d3c786d7bb86cf93979393b386e3bbd3cf86c7cfa3ef93"
    character = "abcd"
    # r = "".join([f"{c:02x}" for c in character])
    # print(r)
    results = decrypt(cyper_text)
    for r in results:
        print(r)
        