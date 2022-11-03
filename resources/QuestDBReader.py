import pandas

df = pandas.read_csv('C:\\Program Files (x86)\\World of Warcraft\\_retail_\\Interface\Addons\\AAP-Updated\\resources\\WoW Quest DB\\questv2.csv')
questIDparsed = df['ID']

questIDparsed.to_csv('C:\\Program Files (x86)\\World of Warcraft\\_retail_\\Interface\Addons\\AAP-Updated\\resources\\Parsed files\\questIDDB.lua', mode = 'w', lineterminator=',\n', header=False, index=False)
f = open('C:\\Program Files (x86)\\World of Warcraft\\_retail_\\Interface\Addons\\AAP-Updated\\resources\\Parsed files\\questIDDB.lua', 'r+')
lines = f.readlines()
f.seek(0)
f.write('AAP.QuestIDDB = {\n')
for line in lines:
    f.write(line)
f.write('}')
f.close()
