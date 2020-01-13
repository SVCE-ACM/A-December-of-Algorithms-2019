import pandas

csv_location = 'C:\\Users\\KAMALI\\Documents\\ACM.csv'
html_location = 'C:\\Users\\KAMALI\\Desktop\\table.html'

dfObj = pandas.read_csv(csv_location)
htmlData = dfObj.to_html()

with open(html_location, 'w') as infile:
	infile.write(htmlData)

