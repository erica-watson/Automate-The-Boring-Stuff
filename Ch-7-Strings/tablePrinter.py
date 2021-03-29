#takes a list of strings and displays in a right-justified table

tableData = [['apples', 'oranges', 'cherries', 'pears'],
    ['Bob', 'Ruby', 'Fauna', 'Savannah'],
    ['cat', 'rabbit', 'deer', 'zebra']]

def printTable(table):
    #find and store the longest strings for each column
    colWidths = [0] * len(table)
    for i in range(len(table)):
        stringLen = []
        for k in range(len(table[i])):
            stringLen.append(len(table[i][k]))
        colWidths[i] = max(stringLen)
    #print the table
    for j in range(len(colWidths)):
        for v in range(len(colWidths)):
            print(table[v][j].rjust(colWidths[v]), end = ' ')
        print()

print(printTable(tableData))
