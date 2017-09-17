import wx, sys, os, subprocess, playsound, threading

EXIT_SOUND = "media"+os.sep+"exit.wav"
ERROR_SOUND = "media"+os.sep+"error.wav"
LOAD_COMPLETE_SOUND = "media"+os.sep+"load-complete.wav"
PROCESS_STARTED_SOUND = "media"+os.sep+"process-started.wav"
VOICE_WELCOME = "media"+os.sep+"speech"+os.sep+"welcome.mp3"
VOICE_INSTRUCTIONS = "media"+os.sep+"speech"+os.sep+"instructions.mp3"

class WorkerThread(threading.Thread):
	def __init__(self, app):
		threading.Thread.__init__(self)
		self.app = app

	def run(self):
		playsound.playsound(LOAD_COMPLETE_SOUND)
		playsound.playsound(VOICE_WELCOME)
		playsound.playsound(VOICE_INSTRUCTIONS)

	def onKeyDown(self, event):
		try:
			keycode = event.GetKeyCode()
			if keycode == wx.WXK_ESCAPE:
				playsound.playsound(EXIT_SOUND)
				sys.exit()
			if keycode == wx.WXK_F1:
				subprocess.Popen(["nvda"+os.sep+"nvda.exe"])
				playsound.playsound(PROCESS_STARTED_SOUND)
			if keycode == wx.WXK_F5:
				subprocess.Popen(["windows_magnifier"+os.sep+"magnifier.bat"])
				playsound.playsound(PROCESS_STARTED_SOUND)
			if keycode == wx.WXK_F6:
				subprocess.Popen(["virtual_magnifier"+os.sep+"magnifier.exe"])
				playsound.playsound(PROCESS_STARTED_SOUND)
			if keycode == wx.WXK_F11:
				subprocess.Popen(["utils"+os.sep+"calculator"+os.sep+"Multimedia Calculator.exe"])
				playsound.playsound(PROCESS_STARTED_SOUND)
			event.Skip()
		except Exception as ex:
			playsound.playsound(ERROR_SOUND)

class Panel1(wx.Panel):
    def __init__(self, parent, id):
        # create the panel
        wx.Panel.__init__(self, parent, id)
        try:
            image_file = "media"+os.sep+"image.png"
            bmp1 = wx.Image(
                image_file, 
                wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            self.bitmap1 = wx.StaticBitmap(
                self, -1, bmp1, (0, 0))
            parent.SetTitle("Access Stick")
        except IOError:
            print "Image file %s not found" % imageFile
            raise SystemExit


app = wx.App(False)
worker = WorkerThread(app)
frame1 = wx.Frame(None, -1, "Access Stick", size=(1000, 1000))
panel1 = Panel1(frame1, -1)
frame1.Centre()
frame1.Show(True)
app.Bind(wx.EVT_KEY_DOWN, worker.onKeyDown)
worker.start()
app.MainLoop()
