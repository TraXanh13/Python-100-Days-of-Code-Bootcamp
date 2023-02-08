import prettytable

table = prettytable.PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.add_row(["Bulbasaur", "Grass, Poison"])
table.add_row(["Caterpie", "Bug"])
table.add_row(["Metapod", "Bug"])
table.add_row(["Butterfree", "Bug, Flying"])
table.add_row(["Weedle", "Bug, Poison"])
table.add_row(["Kakuna", "Bug, Poison"])
table.add_row(["Beedrill", "Bug, Poison"])

table.align = "l"  # Center align

print(table)
