"""
Check Box
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

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.cb1 = wx.CheckBox(self, label='Cat')
        self.cb2 = wx.CheckBox(self, label='Dog')
        self.cb3 = wx.CheckBox(self, label='Rat')
        self.label = wx.StaticText(self, label='')

        vbox.Add(self.cb1)
        vbox.Add(self.cb2)
        vbox.Add(self.cb3)
        vbox.Add(self.label)
        self.SetSizer(vbox)

        self.Bind(wx.EVT_CHECKBOX, self.onChecked)

    def onChecked(self, event):
        cb = event.GetEventObject()

        # Desmarca os outros checkboxes = radio button
        # NOTE: caso a necessidade seja marcar mais de um, entao remova esse 
        # trecho
        # if cb == self.cb1:
        #     self.cb2.SetValue(False)
        #     self.cb3.SetValue(False)
        # elif cb == self.cb2:
        #     self.cb1.SetValue(False)
        #     self.cb3.SetValue(False)
        # elif cb == self.cb3:
        #     self.cb1.SetValue(False)
        #     self.cb2.SetValue(False)

        self.label.SetLabelText('You have selected: ' + cb.GetLabel())


class MyApp(wx.App):
    def OnInit(self):
        title = 'Check Box'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
