file1 = open('../src/res/csv_to_html_res.csv','r')
file2 = open('example.html','a')
open('example.html', 'w').close()
openTag = "<html>\n^<body>\n^^<table>\n"
closeTag = "^^^</table>\n^^</body>\n</html>\n"
result = ""
result += openTag
flag = 0
for line in file1:
    values = line.split(',')
    tmp = ""
    if(flag == 0):
        for e in values:
            e = e.replace('\n','')
            tmp += "<th>{}</th>".format(e)
        flag = 1
    else:
        for e in values:
            e = e.replace('\n','')
            tmp += "<td>{}</td>".format(e)
    tr = "^^^^<tr>{}</tr>\n".format(tmp)
    result += tr
result += closeTag
file2.write(result.replace('^','    '))
file1.close()
file2.close()


    