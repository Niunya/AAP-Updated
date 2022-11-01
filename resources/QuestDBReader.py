import pandas

tableinfoopen = pandas.DataFrame({'AAP.QuestIDDB = {'})
df = pandas.read_csv('C:\\Users\\matwright\\Desktop\\resources\\WoW Quest DB\\questv2.csv')
tableinfoclose = pandas.DataFrame({'}'})
questIDparsed = df['ID']

tableinfoopen.to_csv('C:\\Users\\matwright\\Desktop\\resources\\WoW Quest DB\\Parsed files\\questIDDB.lua', sep='\n', header=False, index=False)
questIDparsed.to_csv('C:\\Users\\matwright\\Desktop\\resources\\WoW Quest DB\\Parsed files\\questIDDB.lua', mode = 'a', lineterminator=',\n', header=False, index=False)
tableinfoclose.to_csv('C:\\Users\\matwright\\Desktop\\resources\\WoW Quest DB\\Parsed files\\questIDDB.lua', mode = 'a',  sep='\n', header=False, index=False)