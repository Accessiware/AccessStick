import wx, zipfile, os, urllib2

DOWNLOAD_URL = "https://repo.accessiware.com/accessstick/accessstick.zip"

def YesNo(parent, question, caption = 'Access Stick'):
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
wx.MessageBox("Welcome.\nThis small program will help you download and install the latest version of Access Stick on an usb.\nBefore continuing, please insert your usb into the computer.\nWhen you've done that, press \"OK\".\n\n\nFor more information visit: https://accessiware.com/accessstick.", "Access Stick Downloader", style=wx.OK)
usb = GetUSB()
if usb == "":
	dlg = wx.MessageDialog(None, "No folder selected. The Access Stick Downloader will now exit.", "Access Stick Downloader", wx.OK | wx.ICON_INFORMATION)
	dlg.ShowModal()
	dlg.Destroy()
	sys.exit()
while True:
	q = YesNo(None, "Is \""+usb+"\" the correct usb?")
	if q == True:
		break;
	GetUSB()

dlg = wx.MessageDialog(None, "Please wait while the Access Stick is being downloaded and installed.", "Access Stick Downloader", wx.OK | wx.ICON_INFORMATION)
dlg.ShowModal()
dlg.Destroy()

f = urllib2.urlopen(DOWNLOAD_URL)
data = f.read()
with open("accessstick.zip", "wb") as code:
	code.write(data)
zf = zipfile.ZipFile("accessstick.zip")
zf.extractall(path = usb)
zf.close()
os.remove("accessstick.zip")

dlg = wx.MessageDialog(None, "The Access Stick was successfully copied to " + usb, "Access Stick Downloader", wx.OK | wx.ICON_INFORMATION)
dlg.ShowModal()
dlg.Destroy()
