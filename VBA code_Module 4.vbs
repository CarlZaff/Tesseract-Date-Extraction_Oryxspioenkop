Sub btn_Insert_Tesseract_data()

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
   
   Sheets("Tesseract_Results").Calculate
   Sheets("Tesseract_Results_New_Batch").Calculate
   
End Sub
Sub btn_Tesseract_fix_Rows()

    Dim lastRow As Long
    Dim i As Long
    lastRow = Range("C" & Rows.count).End(xlUp).Row ' Find the last row in column C
    
    For i = 2 To lastRow ' Loop through each row in column C starting from row 2
        If Cells(i, 3).Value <> "" Then ' If the cell in column C is not empty
            Cells(i, 1).Value = Cells(i, 3).Value ' Copy the value to column A
        End If
    Next i
    
   Sheets("Tesseract_Results").Calculate
      Sheets("Tesseract_Results_New_Batch").Calculate
      Sheets("Database_Oryx_Automated").Calculate
      Sheets("ImageMagick_Pre-Processing").Calculate
      
End Sub

Sub btn_create_new_batch()

Dim textData As String
Dim count As Long
count = 0
Sheets("Tesseract_Results_New_Batch").Range("C2:C100000").Value = ""



        ' Set folder path to copy images from Original download folder.
        folderPathResize = Sheets("Setup").Range("B4").Value



            ' Display a message box to indicate completion
            MsgBox "Choose existing, or create new folder for Images that need to be re-processed."
            
                ' Display the folder browse dialog box with the "New Folder" button enabled
    With Application.FileDialog(msoFileDialogFolderPicker)
        .Title = "Select a Folder or create a new"
        .ButtonName = "Choose Folder"
        .AllowMultiSelect = False
        If .Show <> -1 Then Exit Sub ' User pressed cancel
        folderPath = .SelectedItems(1)
        Sheets("Setup").Range("B5").Value = folderPath
    End With
    
'-----------------------------------------------------------------------------------------------------

     
    MsgBox "The following promt will generate a .txt list that contain names of images to be re-processed. Choose a name and save the file."

    ' Set the range of cells to search
    Dim MyRange As Range
    Set MyRange = Range("A:B") ' Change this to your desired range

    ' Open a file dialog box to allow the user to choose where to save the text file
    Dim dlgSave As FileDialog
    Set dlgSave = Application.FileDialog(msoFileDialogSaveAs)
    
    ' Creates batch script to copy required images
    myFile = folderPath & "\" & "0_Copy_Files.bat"
     ' Swedish encoding for CMD to support Latin letter as well as "å" "ä" and "ö"
    textData = "@chcp 1252" & vbNewLine
    textData = textData & "@echo off" & vbNewLine
    textData = textData & "echo Start copying Images" & vbNewLine
    textData = textData & "echo ___________________________" & vbNewLine
    textData = textData & "pause" & vbNewLine
    
    With dlgSave
        .Title = "Save File As"
        .ButtonName = "Save"
        .AllowMultiSelect = False
        .InitialFileName = folderPath & "\" & "0_Image Names.txt"
        If .Show = -1 Then
            ' Create a new text file and open it for writing
            Dim fso As Object
            Set fso = CreateObject("Scripting.FileSystemObject")
            Dim ts As Object
            Set ts = fso.CreateTextFile(.SelectedItems(1), True)

            ' Loop through each cell in the range and write to the text file if the corresponding cell in column B is empty
            Dim Cell As Range
            For Each Cell In MyRange
                If Not IsEmpty(Cell) Then ' Check if cell in column A is not empty
                    If Cell.Column = 1 And IsEmpty(Cell.Offset(0, 1)) Then ' Check if cell in column B is empty
                        count = count + 1
                        ts.WriteLine Cell.Value & ".jpg" ' Write the value of the cell to the text file
                        textData = textData & "Copy " & """" & folderPathResize & "\" & Cell.Value & ".jpg" & """ " & """" & folderPath & """" & vbNewLine ' Write to CMD copy-script
                        Sheets("Tesseract_Results_New_Batch").Range("C1").Offset(count).Value = Cell.Value

                        
                      
                    End If
                End If
            Next Cell
            
            textData = textData & "echo " & count & " file(s) copied" & vbNewLine & "echo Completed, all images are copied" & vbNewLine & "Pause"

            ' Close the text file
            ts.Close
             ' Save the batch script to a file
             
            Open myFile For Output As #1
            'textData = StrConv(textData, vbFromUnicode, 1252)
            
            Print #1, textData
            Close #1

            ' Display a message box to indicate completion
            MsgBox "Export complete! Added script into " & """" & folderPath & """" & " to copy images"
            
            Shell "explorer.exe " & folderPath, vbNormalFocus
            
        End If
    End With
    
'-----------------------------------------------------------------------------------------------------

      Sheets("Tesseract_Results").Calculate
      Sheets("Tesseract_Results_New_Batch").Calculate
      Sheets("Database_Oryx_Automated").Calculate
      Sheets("ImageMagick_Pre-Processing").Calculate
End Sub

