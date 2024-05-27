"""
Toggle button
"""

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        self.SetMinSize(wx.Size(500, 400))  # ajusta tamanho minimo da janela
        self.SetMaxSize(wx.Size(700, 600))  # ajusta tamanho maximo da janela

        panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.label = wx.StaticText(self, label='Toggle Button')
        vbox.Add(self.label, 0, wx.EXPAND)

        self.toggleBtn = wx.ToggleButton(self, label='Click to on')
        vbox.Add(self.toggleBtn)
        self.toggleBtn.Bind(wx.EVT_TOGGLEBUTTON, self.onToggleClick)

        self.SetSizer(vbox)

    def onToggleClick(self, event):
        state = event.GetEventObject().GetValue()

        if state == True:
            self.label.SetLabelText('On')
            event.GetEventObject().SetLabel('Click to off')
        else:
            self.label.SetLabelText('Off')
            event.GetEventObject().SetLabel('Click to on')



class MyApp(wx.App):
    def OnInit(self):
        title = 'Toggle Button'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
