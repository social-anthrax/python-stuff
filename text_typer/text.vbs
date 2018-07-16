Option Explicit
Dim WshShell
Set WshShell = WScript.CreateObject("WScript.Shell")
for i = 0 to 10
    WScript.Sleep 30
    WshShell.SendKeys("hello")
Next
