with open("Day 24/Mail Merge/Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()

with open("Day 24/Mail Merge/Input/Names/invited_names.txt") as names:
    names = names.readlines()
    for name in names:
        name = name.strip()
        newLetter = letter.replace("[name]", name)
        with open(f"Day 24/Mail Merge/Output/letter_for_{name}.txt", "w") as f:
            f.write(newLetter)
