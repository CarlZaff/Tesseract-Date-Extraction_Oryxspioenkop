Sub btn_tesseract_transfer_dates()

    Dim wb As Workbook
    Set wb = ActiveWorkbook
    
    ' Get the source and destination sheets
    Dim sourceSheet As Worksheet
    Set sourceSheet = wb.Sheets("Tesseract_Results_New_Batch")
    Dim destSheet As Worksheet
    Set destSheet = wb.Sheets("Tesseract_Results")
    
    ' Get the last row of the source sheet
    Dim lastRow As Long
    lastRow = sourceSheet.Cells(sourceSheet.Rows.count, "B").End(xlUp).Row
    
    ' Loop through each row in the source sheet
    Dim i As Long
    For i = 1 To lastRow
        
        ' Check if the cell in column B is not empty
        If sourceSheet.Cells(i, "B").Value <> "" Then
            
            ' Get the serial number in column A
            Dim serialNumber As String
            serialNumber = sourceSheet.Cells(i, "A").Value
            
            ' Find the row in the destination sheet that has the same serial number
            Dim destRow As Range
            Set destRow = destSheet.Columns("A").Find(serialNumber, LookIn:=xlValues, lookat:=xlWhole)
            
            ' If the serial number is found, copy the value from column B in the source sheet to column B in the destination sheet
            If Not destRow Is Nothing Then
                destSheet.Cells(destRow.Row, "B").Value = sourceSheet.Cells(i, "B").Value
            End If
            
        End If
        
    Next i
    
    Sheets("Tesseract_Results_New_Batch").Calculate
    Sheets("Tesseract_Results").Calculate
    Sheets("Database_Oryx_Automated").Calculate
    Sheets("Graphical Overview").Calculate
    Sheets("Tesseract_Results").Calculate
End Sub
Sub btn_create_new_batch_2()
Dim textData As String
Dim count As Long
count = 0

 Range("C2:C100000").Value = ""


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
        Sheets("Setup").Range("B6").Value = folderPath
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
    ' Clear old tesseract data and refresh
    Range("A2:B100000").Value = ""
      Sheets("Tesseract_Results_New_Batch").Calculate
End Sub
