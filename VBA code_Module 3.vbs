Sub btn_input_oryxdata_formulas()

    
' Inserts correct formulas into sheet
    Dim lastRow As Long
    lastRow = Cells(Rows.count, "E").End(xlUp).Row ' get the last row with data in Column E
    
    Dim ii As Long
    For ii = 3 To lastRow ' loop through all rows with data in Column E, starting at row 3
        Cells(ii, "J").Formula = "=ROW()" ' input formula into corresponding cell in Column J
        Cells(ii, "A").Formula = "=IF(ROW()<=Overview!$B$6,Overview!$J$6,IF(ROW()<=Overview!$B$7,Overview!$J$7,IF(ROW()<=Overview!$B$8,Overview!$J$8,IF(ROW()<=Overview!$B$9,Overview!$J$9,IF(ROW()<=Overview!$B$10,Overview!$J$10,IF(ROW()<=Overview!$B$11,Overview!$J$11,IF(ROW()<=Overview!$B$12,Overview!$J$12,IF(ROW()<=Overview!$B$13,Overview!$J$13,IF(ROW()<=Overview!$B$14,Overview!$J$14,IF(ROW()<=Overview!$B$15,Overview!$J$15,IF(ROW()<=Overview!$B$16,Overview!$J$16,IF(ROW()<=Overview!$B$17,Overview!$J$17,IF(ROW()<=Overview!$B$18,Overview!$J$18,IF(ROW()<=Overview!$B$19,Overview!$J$19,IF(ROW()<=Overview!$B$20,Overview!$J$20,IF(ROW()<=Overview!$B$21,Overview!$J$21,IF(ROW()<=Overview!$B$22,Overview!$J$22,IF(ROW()<=Overview!$B$23,Overview!$J$23,IF(ROW()<=Overview!$B$24,Overview!$J$24,IF(ROW()<=Overview!$B$25,Overview!$J$25,IF(ROW()<=Overview!$B$26,Overview!$J$26,IF(ROW()<=Overview!$B$27,Overview!$J$27,IF(ROW()<=Overview!$B$28,Overview!$J$28,IF(ROW()<=Overview!$B$29,Overview!$J$29,))))))))))))))))))))))))"
        
        
        If Not IsEmpty(Cells(ii, "E").Value) Then ' check if cell in Column E is not empty
            Cells(ii, "G").Formula = "=RIGHT(INDIRECT(ADDRESS(ROW(),COLUMN()+2)),4)&""-""&LEFT(TEXT(INDIRECT(ADDRESS(ROW(),COLUMN()+1)),""MMMM""),3)" ' input formula into corresponding cell in Column G
            Cells(ii, "H").Formula = "=DATE(RIGHT(INDIRECT(ADDRESS(ROW(),COLUMN()+1)),4),LEFT(RIGHT(INDIRECT(ADDRESS(ROW(),COLUMN()+1)),7),2),LEFT(INDIRECT(ADDRESS(ROW(),COLUMN()+1)),2))"
            Cells(ii, "I").Formula = "=IF(INDIRECT(ADDRESS(ROW(),11))<>"""",XLOOKUP(INDIRECT(ADDRESS(ROW(),11)),Tesseract_Results!A:A,Tesseract_Results!B:B,"""",0,1),"""")"
            Cells(ii, "K").Formula = "=ROW()+1000000"
            Cells(ii, "L").Formula = "=IF(LEFT(INDIRECT(ADDRESS(ROW(),5)),10)=""https://i."",""Image"",IF(LEFT(INDIRECT(ADDRESS(ROW(),5)),10)=""https://tw"",""Twitter"",IF(LEFT(INDIRECT(ADDRESS(ROW(),5)),10)=""https://po"",""Website Image"",)))"
        End If
    Next ii
  
    
End Sub

Sub btn_refresh_oryxdata()

    Sheets("Database_Oryx_Automated").Calculate
    Sheets("Overview").Calculate
    Sheets("Graphical Overview").Calculate
    Sheets("Database_Oryx_Automated").Calculate

End Sub

