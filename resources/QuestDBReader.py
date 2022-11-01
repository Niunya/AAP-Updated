import pandas

tableinfoopen = pandas.DataFrame({'AAP.QuestIDDB = {'})
df = pandas.read_csv('PATHTOCSV')
tableinfoclose = pandas.DataFrame({'}'})
questIDparsed = df['ID']

tableinfoopen.to_csv('PATHTOLUA', sep='\n', header=False, index=False)
questIDparsed.to_csv('PATHTOLUA', mode = 'a', lineterminator=',\n', header=False, index=False)
tableinfoclose.to_csv('PATHTOLUA', mode = 'a',  sep='\n', header=False, index=False)