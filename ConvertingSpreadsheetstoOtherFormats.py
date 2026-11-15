#Converting Spreadsheets to Other Formats

import ezsheets

ss = ezsheets.upload('Inverse_copy.xlsx')

ss.downloadAsPDF()
