Sub btn_ImageMagick_preprocessing()
Sheets("ImageMagick_Pre-Processing").Calculate

Dim textData As String

    Dim newFolderPath As String
    
    ' Get the name of the new folder from cell B2
    newFolderPath = Range("B2").Value & Range("B3").Value
    
    ' Check if the folder already exists
    If Dir(newFolderPath, vbDirectory) = "" Then
        ' If the folder doesn't exist, create it
        MkDir newFolderPath
       MsgBox "New folder created at " & newFolderPath
    Else
        ' If the folder already exists, continue without creating a new folder
        MsgBox "The folder already exists at " & newFolderPath
    End If
    

'----------------------------------------------------------------------------

' Set the range of cells to search
    Dim MyRange As Range
    Set MyRange = Range("A4:A150000") ' Change this to your desired range

     ' Open a file dialog box to allow the user to choose where to save the text file
    Dim dlgSave As FileDialog
    Set dlgSave = Application.FileDialog(msoFileDialogSaveAs)
    
    ' Creates batch script to preprocess using specified threshold value
   myFile = Range("B2").Value & Range("B3").Value & "\" & "0_ImageMagick_Threshold_" & Range("B1").Value & ".bat"
 
    With dlgSave
        .Title = "Save File As"
        .ButtonName = "Save"
        .AllowMultiSelect = False
        .InitialFileName = newFolderPath & "0_Image Names.txt"
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
                     ' ImageMacgick Requires new chcp for each line when running as a batch program, this is very slow. Recommended to copy the output into CMD to save time.
                        
                        ts.WriteLine Cell.Value & ".jpg" ' Write the value of the cell to the text file
                        textData = textData & "@chcp 1252" & vbNewLine & "magick " & """" & Range("B2").Value & "\" & Cell.Value & ".jpg" & """ -threshold " & Range("C1").Value & "%% -type bilevel " & """" & newFolderPath & "\" & Cell.Value & ".jpg""" & vbNewLine ' Write to CMD copy-script
                        
                      

                End If
            Next Cell
            
            textData = textData & "echo " & count & " file(s) copied" & vbNewLine & "echo Completed, all images are copied" & vbNewLine & "Pause"

            ' Close the text file
            ts.Close
             ' Save the batch script to a file
             
            Open myFile For Output As #1

            Print #1, textData
            Close #1

           Shell "explorer.exe " & newFolderPath, vbNormalFocus
            
        End If
    End With


End Sub

