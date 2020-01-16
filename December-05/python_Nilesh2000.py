# Author : Nilesh D
# December 5 - Convert CSV data to a HTML table
outfile = open("index.html", "w")

outfile.write("<html>\n")
outfile.write("<body>\n")
outfile.write("<table>\n")

infile = open("../src/res/csv_to_html_res.csv", "r")
firstLine = infile.readline().rsplit(',')
outfile.write("<tr>\n")
outfile.write("<th>%s</th>\n" % firstLine[0])
outfile.write("<th>%s</th>\n" % firstLine[1])
outfile.write("<th>%s</th>\n" % firstLine[2])
outfile.write("<th>%s</th>\n" % firstLine[3])
outfile.write("<th>%s</th>\n" % firstLine[4])
outfile.write("</tr>\n")

for line in infile:
    row = line.split(",")
    Name = row[0]
    Sex = row[1]
    Age = row[2]
    Height = row[3]
    Weight = row[4]

    outfile.write("<tr>\n")
    outfile.write("<td>%s</td>\n" % Name)
    outfile.write("<td>%s</td>\n" % Sex)
    outfile.write("<td>%s</td>\n" % Age)
    outfile.write("<td>%s</td>\n" % Height)
    outfile.write("<td>%s</td>\n" % Weight)
    outfile.write("</tr>\n")

outfile.write("</table>\n")
outfile.write("</body>\n")
outfile.write("</html>\n")

infile.close()
outfile.close()
