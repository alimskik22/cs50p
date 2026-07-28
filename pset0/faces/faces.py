def main():
    prompt = input("write smth w/ emoticon: ")
    wemoji = convert(prompt)
    print(wemoji)


def convert(prompt):
    prompt = prompt.replace(":)", "🙂").replace(":(", "🙁")
    return prompt


main()
