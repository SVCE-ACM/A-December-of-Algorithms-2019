import os.path
_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    htmlString = openingHTML()
    
    csvFile = open(_dir + "/../src/res/csv_to_html_res.csv", 'r')
    htmlString += createTableHead(csvFile.readline())
    for line in csvFile:
        htmlString += createTableRow(line)
                
    htmlString += closingHTML()
    htmlFile = open(_dir + "/../src/res/html-KonradLL.html", 'w')
    htmlFile.write(htmlString)


def openingHTML():
    return "<html> \n\t<body> \n\t\t<table>"


def closingHTML():
    return "\n\t\t</table> \n\t</body> \n<html>"


def createTableHead(csvHead):
    columnHeaders = csvRowToArray(csvHead)
    htmlColumnHeaders = ''
    for columnHead in columnHeaders:
        htmlColumnHeaders += '<th>' + columnHead + '</th>'

    return encapsulateHtmlTableRow(htmlColumnHeaders)


def createTableRow(csvRow):
    rowItems = csvRowToArray(csvRow)
    htmlRowItems = ''
    for rowItem in rowItems:
        htmlRowItems += '<td>' + rowItem + '</td>'

    return encapsulateHtmlTableRow(htmlRowItems)


def csvRowToArray(csvRow):
    return (
        csvRow
        .replace('"','')
        .replace(' ','')
        .replace('\n','')
        .split(',')
    )


def encapsulateHtmlTableRow(row):
    return '\n\t\t\t<tr>' + row + '</tr>'


if __name__ == "__main__":
    main()