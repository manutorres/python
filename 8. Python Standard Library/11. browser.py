import webbrowser

print("Deployment completado")

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open("http://google.com")
