"""
Radion Button Group
"""

import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        self.SetMinSize(wx.Size(500, 400))  # ajusta tamanho minimo da janela

        panel = MyPanel(self)       # painel sem box sizer
        # panel = My2ndPanel(self)    # painel com box sizer


class MyPanel(wx.Panel):
    """ Radio buttons com espaçamento fixo """
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        # criar radio buttons
        self.rb1 = wx.RadioButton(
            self, label='Cat', pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(
            self, label='Dog', pos=(10, 40))
        self.rb3 = wx.RadioButton(
            self, label='Rat', pos=(10, 70))

        # criar texto statico
        self.label = wx.StaticText(self, label='', pos=(10, 100))

        self.Bind(wx.EVT_RADIOBUTTON, self.onRadioButton)

    def onRadioButton(self, event):
        rb = event.GetEventObject()
        self.label.SetLabelText('You have selected: ' + rb.GetLabel())


class My2ndPanel(wx.Panel):
    """ Radio buttons dentro do box sizer """
    def __init__(self, parent):
        super(My2ndPanel, self).__init__(parent)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.rb1 = wx.RadioButton(
            self, label='Cat', style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(
            self, label='Dog')
        self.rb3 = wx.RadioButton(
            self, label='Rat')

        self.label = wx.StaticText(self, label='')

        vbox.Add(self.rb1, 0, wx.ALL, 10)
        vbox.Add(self.rb2, 0, wx.ALL, 10)
        vbox.Add(self.rb3, 0, wx.ALL, 10)
        vbox.Add(self.label, 0, wx.ALL, 10)
        self.SetSizer(vbox)
        self.Bind(wx.EVT_RADIOBUTTON, self.onRadioButton)

    def onRadioButton(self, event):
        rb = event.GetEventObject()
        self.label.SetLabelText('You have selected: ' + rb.GetLabel())


class MyApp(wx.App):
    def OnInit(self):
        title = 'Radion Button Group'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
