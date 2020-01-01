try:
	source = open('E:/csv_to_html_res.csv','r')
except:
	print('Please copy the resource file to the E drive and try again')
else:
	data = source.readlines()
	source.close()
	destination = open('E:/csv_to_html_des.html', 'w')
	destination.write("<html>\n<body>\n<table border=1 align=center>\n")
	for line in data:
	    words = line.split(',')
	    destination.write('<tr>\n')
	    for word in words:
	        destination.write('<td>'+word.strip()+'</td>\n')
	    destination.write('</tr>\n')
	destination.write("</table>\n</body>\n</html>\n")
	destination.close()
	print('HTML FILE GENERATED SUCCESSFULLY IN E DRIVE')