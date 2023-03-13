Sub btn_download_images()

' Set up variables and objects
Dim FolderName As String
Dim ws As Worksheet
Dim lLastRow As Long
Dim oXMLHTTP As Object
Dim oBinaryStream As Object
Dim adTypeBinary As Integer
Dim aBytes() As Byte
Dim sPath As String
Dim sURI As String
Dim adSaveCreateOverWrite As Integer

' Set worksheet object to a specific sheet in the workbook
 Set ws = ThisWorkbook.Sheets("Image_Download")

' Get the last row of column D in the worksheet
 lLastRow = ws.Range("D" & ws.Rows.Count).End(xlUp).Row

' Get the folder name from cell D2 in the worksheet
 FolderName = ws.Range("D2").Value

' Create HTTP and binary stream objects
 Set oXMLHTTP = CreateObject("MSXML2.XMLHTTP.6.0")
 Set oBinaryStream = CreateObject("ADODB.Stream")
 adTypeBinary = 1
 oBinaryStream.Type = adTypeBinary

' Loop through each row of the worksheet
 For i = 5 To lLastRow
  ' Get the file path and URL from the worksheet
  sPath = FolderName & ws.Range("A" & i).Value
  sURI = ws.Range("D" & i).Value

  ' Try to download the image
  On Error GoTo HTTPError
  oXMLHTTP.Open "GET", sURI, False
  oXMLHTTP.Send
  aBytes = oXMLHTTP.responsebody
  On Error GoTo 0

  ' Save the image to the specified folder
  oBinaryStream.Open
  oBinaryStream.Write aBytes
  adSaveCreateOverWrite = 2
  oBinaryStream.SaveToFile sPath, adSaveCreateOverWrite
  oBinaryStream.Close

  ' Update the worksheet to show the file was downloaded
  ws.Range("E" & i).Value = "File successfully downloaded as JPG"
  
NextRow:
 Next i

' Exit the subroutine
 Exit Sub

' Handle errors while downloading the image
HTTPError:
 ws.Range("E" & i).Value = "Unable to download the file"
 Resume NextRow
 
End Sub
Sub btn_save_image_names()

    Dim MyRange As Range
    Dim myFile As String
    Dim textData As String
    Dim outputPath As String
    
    lLastRow = Range("D" & Rows.count).End(xlUp).Row
 
    ' Set the range to copy
    Set MyRange = Range("A5" & ":" & "A" & lLastRow)
    
    ' Get the output folder path from cell B1
    outputPath = Range("D2").Value
    
    ' Get the file name and path
    myFile = outputPath & "0_Image names.txt"
    
    ' Copy the range values to a string variable
    textData = ""
    For Each Cell In MyRange
        textData = textData & Cell.Value & vbNewLine
    Next Cell
    
    ' Save the text data to a file
    Open myFile For Output As #1
    Print #1, textData
    Close #1
    
    ' Notify the user that the file was saved
    MsgBox "Text file saved successfully!"
    
End Sub
Sub btn_Magick_Script()


    Dim MyRange As Range
    Dim myFile As String
    Dim textData As String
    Dim outputPath As String
    
    Set ws = ActiveWorkbook.Sheets("Image_Download")
     
    lLastRow = Range("B" & Rows.count).End(xlUp).Row
 
    ' Set the range to copy
    Set MyRange = Range("B2" & ":" & "B" & lLastRow)
    
    ' Get the output folder path from cell B1
    outputPath = ws.Range("D2").Value
    
    ' Get the file name and path
    myFile = outputPath & "0_MagickFix.bat"
    
    ' Copy the range values to a string variable
    textData = "@echo off" & vbNewLine
    textData = textData & "echo Starting conversion to .JPG" & vbNewLine
    textData = textData & "echo ___________________________" & vbNewLine
    textData = textData & "pause" & vbNewLine
    textData = textData & "@echo on" & vbNewLine
    For Each Cell In MyRange
        textData = textData & Cell.Value & vbNewLine
    Next Cell
    
    ' Save the text data to a file
    Open myFile For Output As #1
    Print #1, textData
    Close #1
    
    ' Notify the user that the file was saved
    MsgBox "Text file saved successfully!"
    
    Range("A2").Value = ""
    
    Sheets("MagickFix").Calculate
    
End Sub
Sub btn_fetch_links()

    Range("D5").Formula2 = "=FILTER(Database_Oryx_Automated!E:E,LEFT(Database_Oryx_Automated!E:E,10)=""https://i."","""")"
    Range("C5").Formula2 = "=FILTER(Database_Oryx_Automated!K:K,LEFT(Database_Oryx_Automated!E:E,10)=""https://i."","""")"
    Sheets("Tesseract_Results").Range("C2").Formula2 = "=FILTER(Database_Oryx_Automated!K:K,LEFT(Database_Oryx_Automated!E:E,10)=""https://i."","""")"
    Sheets("MagickFix").Range("A2").Formula2 = "=UNIQUE(Image_Download!A5:A10005,FALSE,FALSE)"
    Sheets("Image_Download").Calculate
    Sheets("MagickFix").Calculate
    
End Sub
Sub btn_clear_sheet()

    Range("D5").Value = ""
    Range("C5").Value = ""
    Range("E5:E15000").Value = ""
    Sheets("Image_Download").Calculate

End Sub

Sub btn_find_source()
    Dim folderPath As String
    
    ' Display the folder browse dialog box
    With Application.FileDialog(msoFileDialogFolderPicker)
        .Title = "Select a Folder"
        .AllowMultiSelect = False
        If .Show <> -1 Then Exit Sub ' User pressed cancel
        folderPath = .SelectedItems(1)
    End With
    
    ' Copy the selected folder path to cell B2
    Range("B2").Value = folderPath & "\"
End Sub
Sub btn_find_database()

    Dim filePath As String
    Dim fileName As String
    
    ' Display the file browse dialog box
    With Application.FileDialog(msoFileDialogFilePicker)
        .Title = "Select Oryx Source Text File"
        .Filters.Clear
        .Filters.Add "Text Files", "*.txt"
        .AllowMultiSelect = False
        If .Show <> -1 Then Exit Sub ' User pressed cancel
        filePath = .SelectedItems(1)
    End With
    
    ' Extract the selected file name from the full file path
    fileName = Mid(filePath, InStrRev(filePath, "\") + 1)
    
    ' Copy the selected file name to cell B3
    Range("B3").Value = fileName
    
End Sub
Sub btn_download_folder()

    Dim folderPath As String
    Dim selectedCell As Range
    
    ' Display the folder browse dialog box with the "New Folder" button enabled
    With Application.FileDialog(msoFileDialogFolderPicker)
        .Title = "Select a Folder or create a new"
        .ButtonName = "Choose Folder"
        .AllowMultiSelect = False
        If .Show <> -1 Then Exit Sub ' User pressed cancel
        folderPath = .SelectedItems(1)
    End With
    
    ' Copy the selected folder path to cell D2
    Set selectedCell = Range("D2")
    selectedCell.Value = folderPath & "\"
    Sheets("Setup").Range("B4").Value = folderPath & "\"
    
    
End Sub
Sub btn_tesseract_sourcefolder()

    Dim folderPath As String
    Dim selectedCell As Range
    
    ' Display the folder browse dialog box with the "New Folder" button enabled
    With Application.FileDialog(msoFileDialogFolderPicker)
        .Title = "Select a Folder or create a new"
        .ButtonName = "Choose Folder"
        .AllowMultiSelect = False
        If .Show <> -1 Then Exit Sub ' User pressed cancel
        folderPath = .SelectedItems(1)
    End With
    
    ' Copy the selected folder path to cell C1
    Set selectedCell = Range("C1")
    selectedCell.Value = folderPath & "\"
    
    Sheets("Tesseract_Commands").Calculate
    
End Sub
Sub btn_tesseract_imageList()

    Dim filePath As String
    Dim fileName As String
    
    ' Display the file browse dialog box
    With Application.FileDialog(msoFileDialogFilePicker)
        .Title = "Select Tesseract Input Text File"
        .Filters.Clear
        .Filters.Add "Text Files", "*.txt"
        .AllowMultiSelect = False
        If .Show <> -1 Then Exit Sub ' User pressed cancel
        filePath = .SelectedItems(1)
    End With
    
    Dim lastBackslashPos As Long
    lastBackslashPos = InStrRev(filePath, "\")
    
    ' Use the Left function to extract the left portion of the string up to the last backslash
    Dim pathWithoutFileName As String
    pathWithoutFileName = Left(filePath, lastBackslashPos)
    
    If pathWithoutFileName = Range("C1").Value Then
        ' Extract the selected file name from the full file path
        fileName = Mid(filePath, InStrRev(filePath, "\") + 1)
    
        ' Copy the selected file name to cell B3
        Range("C2").Value = fileName
    Else
        MsgBox "Error! Name list is not in the same folder as images to be processed. Control location of Input list.", vbCritical
    End If
    
    Sheets("Tesseract_Commands").Calculate
End Sub
