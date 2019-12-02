outfile = open("index.html", "w");

outfile.write("<html>")
outfile.write("<body>")
outfile.write('<table>');

infile = open("csv_to_html_res.csv", "r");
firstLine = infile.readline().rsplit(',');
outfile.write("<tr>");
outfile.write("<th>%s</th>" %firstLine[0])
outfile.write("<th>%s</th>" %firstLine[1]);
outfile.write("<th>%s</th>" %firstLine[2]);
outfile.write("<th>%s</th>" %firstLine[3]);
outfile.write("<th>%s</th>" %firstLine[4]);
outfile.write("</tr>");

for line in infile:
  row = line.split(",")
  Name = row[0]
  Sex = row[1]
  Age = row[2]
  Height = row[3]
  Weight = row[4]

  outfile.write("<tr>");
  outfile.write("<td>%s</td>" % Name);
  outfile.write("<td>%s</td>" % Sex);
  outfile.write("<td>%s</td>" % Age);
  outfile.write("<td>%s</td>" % Height);
  outfile.write("<td>%s</td>" % Weight);
  outfile.write("</tr>");

outfile.write("</table>")
outfile.write("</body>")
outfile.write("</html>")

infile.close()
outfile.close()
