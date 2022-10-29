with open("./Input/Letters/starting_letter.txt") as letter_template_file:
    letter_template = str(letter_template_file.read())

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        name = name.strip()
        current_letter_body = letter_template.replace("[name]", name)
        with open("./Output/ReadyToSend/letter_to_" + name + ".txt", "w") as current_letter_file:
            current_letter_file.writelines(current_letter_body)

