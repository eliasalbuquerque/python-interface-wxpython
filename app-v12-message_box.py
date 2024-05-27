"""
Message Box
"""

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        self.SetMinSize(wx.Size(500, 400))  # ajusta tamanho minimo da janela

        panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        # criar layouts
        vbox = wx.BoxSizer(wx.VERTICAL)
        widgetPanel = wx.Panel(self)
        widgetSizer = wx.BoxSizer(wx.VERTICAL)

        # criar widgets
        self.button = wx.Button(widgetPanel, label='Open Message (Info)')
        self.button2 = wx.Button(widgetPanel, label='Open Message (Warning)')
        self.button3 = wx.Button(widgetPanel, label='Open Message (Error)')

        # organizar widgets no layout
        widgetSizer.Add(self.button)
        widgetSizer.Add(self.button2, 0, wx.TOP, 10)
        widgetSizer.Add(self.button3, 0, wx.TOP, 10)
        widgetPanel.SetSizer(widgetSizer)

        vbox.Add(widgetPanel, 0, wx.LEFT | wx.TOP, 100)
        self.SetSizer(vbox)

        # add eventos aos widgets
        self.Bind(wx.EVT_BUTTON, self.MessageBox.Info, self.button)
        self.Bind(wx.EVT_BUTTON, self.MessageBox.Warn, self.button2)
        self.Bind(wx.EVT_BUTTON, self.MessageBox.Error, self.button3)

    class MessageBox:
        def Info(self):
            wx.MessageBox('Message box Info icon', 'Dialog',
                          wx.OK | wx.ICON_INFORMATION)

        def Warn(self):
            wx.MessageBox('Message box Warning icon',
                          'Dialog', wx.OK | wx.ICON_WARNING)

        def Error(self):
            wx.MessageBox('Message box Error icon',
                          'Dialog', wx.OK | wx.ICON_ERROR)


class MyApp(wx.App):
    def OnInit(self):
        title = 'Message Box'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
