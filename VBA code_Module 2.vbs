Sub btn_tesseract_launch()

Sheets("Tesseract_Commands").Calculate

    Dim username As String
    username = Environ("username")
    
    Dim filePath As String
    filePath = "C:\Users\" & username & "\AppData\Local\Programs\Tesseract-OCR\winpath.exe"
    
    If Dir(filePath) = "" Then
        MsgBox "Can't find Tesseract installation. Please launch the program manually.", vbCritical, "Error"
    Else
        Dim shellID As Double
        shellID = Shell(filePath & " cmd", vbNormalFocus)
        Application.Wait (Now + TimeValue("0:00:02"))
        SendKeys Range("C10").Value & "{ENTER}", True
        SendKeys Range("C11").Value & "{ENTER}", True
    End If

End Sub
