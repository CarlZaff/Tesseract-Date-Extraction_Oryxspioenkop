Sub btn_overview_refresh()
    Sheets("Tesseract_Results").Calculate
    Sheets("Database_Oryx_Automated").Calculate
    Sheets("Graphical Overview").Calculate
End Sub
Sub btn_Insert_Tesseract_data_new()

Range("A2:B100000").Value = ""

    ' Define variables
    Dim filePath As String
    Dim fileContent As String
    Dim fileRows() As String
    Dim fileColumns() As String
    Dim i As Long
    Dim j As Long
    
    ' Open file dialog box to select file
    With Application.FileDialog(msoFileDialogFilePicker)
        .Title = "Select Text File"
        .Filters.Clear
        .Filters.Add "Text Files", "*.txt", 1
        If .Show = -1 Then
            filePath = .SelectedItems(1)
        Else
            Exit Sub
        End If
    End With
    
    ' Open file and read contents
    Open filePath For Input As #1
    fileContent = Input(LOF(1), 1)
    Close #1
    
    ' Split file contents into rows
    fileRows = Split(fileContent, vbLf)
    
    ' Loop through rows and input into cells starting at A2
    For i = 0 To UBound(fileRows)
        fileColumns = Split(fileRows(i), vbTab)
        For j = 0 To UBound(fileColumns)
            Range("A2").Offset(i, j).Value = fileColumns(j)
        Next j
    Next i
   
   Sheets("Tesseract_Results_New_Batch").Calculate
   Sheets("Tesseract_Results").Calculate
   
End Sub
