"""
Radio Button Box
"""

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        self.SetMinSize(wx.Size(500, 400))  # ajusta tamanho minimo da janela

        panel = MyPanel(self)


class MyPanel(wx.Panel):
    """ Radio buttons Box """

    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # criar radio buttons box
        labels = ['Cat', 'Dog', 'Rat']

        self.rbox = wx.RadioBox(
            self, label='Select animal', choices=labels, style=wx.RA_SPECIFY_ROWS)

        # criar texto statico
        self.label = wx.StaticText(self, label='')

        # organizar o box sizer
        vbox.Add(self.rbox, 0, wx.LEFT | wx.TOP, 50)
        vbox.Add(self.label, 0, wx.LEFT, 50)
        self.SetSizer(vbox)

        self.Bind(wx.EVT_RADIOBOX, self.onRadioBox)

    def onRadioBox(self, event):
        rboxSelection = self.rbox.GetStringSelection()
        self.label.SetLabelText('You have selected: ' + rboxSelection)


class MyApp(wx.App):
    def OnInit(self):
        title = 'Radio Box'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
