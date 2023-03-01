def encrypt(message, secret):
    new_secret = []
    for character in secret:
        if ord(character) & 1:
            new_secret.append((ord(character) | (1 << 3) + 7) % 256)
        else:
            new_secret.append(ord(character) ^ 13)

    new_message = []
    for character in message:
        new_message.append((ord(character) << 2) | (ord(character) >> 6))

    for index in range(len(new_message)):
        for jndex in range(len(new_secret)):
            new_message[(index + jndex) % len(new_message)] = (new_message[(index + jndex) % len(new_message)] & (90 | 181)) ^ new_secret[jndex]

    return "".join([f"{character:02x}" for character in new_message])


def decrypt(message):
    answers = []
    for value in range(0xff):
        answer = ""
        for index in range(len(message) // 2):
            temp = int(message[index * 2:index * 2 + 2], 16) ^ value
            answer += chr(((temp << 6) & 0xff) | temp >> 2)

        answers.append(answer)

    return answers


if __name__ == "__main__":
    cyphertext = encrypt("", "")

    print(cyphertext)

    for answer in decrypt(cyphertext):
        if "test" in answer:
            print(answer)