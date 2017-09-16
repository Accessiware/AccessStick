import wx, zipfile, os, urllib2

ACCESSIPAD_URL = "https://repo.accessiware.com/viscon/beta/application/application.zip"

def YesNo(parent, question, caption = 'Accessipad'):
	dlg = wx.MessageDialog(parent, question, caption, wx.YES_NO | wx.ICON_QUESTION)
	result = dlg.ShowModal() == wx.ID_YES
	dlg.Destroy()
	return result

def GetUSB():
	result = ""
	dialog = wx.DirDialog(None, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
	if dialog.ShowModal() == wx.ID_OK:
		result = dialog.GetPath()
	dialog.Destroy()
	return result

app = wx.App()
app.MainLoop()# Call Dialog
wx.MessageBox("Welcome.\nThis small program will help you download and install the latest version of Accessipad on an usb stick.\nBefore continuing, please insert your usb into the computer.\nWhen you've done that, press \"OK\".\n\n\nFor more information visit: https://accessiware.com/accessipad.", "Accessipad Downloader", style=wx.OK)
usb = GetUSB()
while True:
	q = YesNo(None, "Is \""+usb+"\" the correct usb?")
	if q == True:
		break;
	GetUSB()

dlg = wx.MessageDialog(None, "Please wait while the Accessipad is being downloaded and installed.", "Accessipad Downloader", wx.OK | wx.ICON_INFORMATION)
dlg.ShowModal()
dlg.Destroy()

f = urllib2.urlopen(ACCESSIPAD_URL)
data = f.read()
with open("accessipad.zip", "wb") as code:
	code.write(data)
zf = zipfile.ZipFile("accessipad.zip")
zf.extractall(path = usb)
zf.close()
os.remove("accessipad.zip")

dlg = wx.MessageDialog(None, "The Accessipad was successfully copied to " + usb, "Accessipad Downloader", wx.OK | wx.ICON_INFORMATION)
dlg.ShowModal()
dlg.Destroy()
