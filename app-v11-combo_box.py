"""
Combo Box (caixa de selecao)
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

        # criar os layouts
        vbox = wx.BoxSizer(wx.VERTICAL) # layout principal
        widgetPanel = wx.Panel(self) # container dos widgets
        widgetSizer = wx.BoxSizer(wx.VERTICAL) # layout dos widgets

        # criar labels
        self.label = wx.StaticText(
            widgetPanel, label='Select your favorite programming language')
        self.label2 = wx.StaticText(
            widgetPanel, label='')

        # criar widgets combo box (caixa de selecao)
        languages = ['Python', 'Java', 'C++', 'Ruby', 'Rust', 'PHP']
        self.combobox = wx.ComboBox(widgetPanel, choices=languages)

        # organiza widgets no layout
        # vbox.Add(self.label, 0, wx.LEFT | wx.TOP, 30)
        # vbox.Add(self.combobox, 0, wx.LEFT, 30)
        # vbox.Add(self.label2, 0, wx.LEFT, 30)
        # self.SetSizer(vbox)
        
        # organiza widgets no layout
        widgetSizer.Add(self.label)
        widgetSizer.Add(self.combobox)
        widgetSizer.Add(self.label2)
        widgetPanel.SetSizer(widgetSizer)

        vbox.Add(widgetPanel, 0, wx.LEFT|wx.TOP, 30)
        self.SetSizer(vbox)



        # adiciona evento aos widgets
        self.Bind(wx.EVT_COMBOBOX, self.onCombo)

    def onCombo(self, event):
        comboValue = self.combobox.GetValue()
        self.label2.SetLabel('Your language is: ' + comboValue)


class MyApp(wx.App):
    def OnInit(self):
        title = 'Combo Box'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
