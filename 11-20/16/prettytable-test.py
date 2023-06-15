import prettytable


table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.padding_width = 1
table.max_width = 30
table.hrules = prettytable.ALL
table.vrules = prettytable.ALL
table.border = True
table.header = True

print (table)
