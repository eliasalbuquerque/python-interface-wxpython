"""
Status Bar
"""

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        self.SetMinSize(wx.Size(500, 400))  # ajusta tamanho minimo da janela

        statusBar = self.CreateStatusBar(style=wx.BORDER_NONE)
        statusBar.SetStatusStyles([wx.SB_FLAT])
        statusBar.SetBackgroundColour('green')
        statusBar.SetStatusText('This is a Status Bar')

        panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)


class MyApp(wx.App):
    def OnInit(self):
        title = 'Status Bar'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
