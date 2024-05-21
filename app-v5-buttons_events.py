"""
Buttons and events
"""


import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        self.SetMinSize(wx.Size(500, 400))  # ajusta tamanho minimo da janela

        panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        """"
        Cria botoes e acoes para os mesmos
        """
        super(MyPanel, self).__init__(parent)
        
        # cria o que?
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        vboxSizer = wx.BoxSizer(wx.VERTICAL)
        hboxSizer = wx.BoxSizer(wx.HORIZONTAL)

        # adiciona texto estatico
        self.labelText = wx.StaticText(self, label="Buttons", style=wx.ALIGN_CENTER)
        vboxSizer.Add(self.labelText, 0, wx.EXPAND)

        # adiciona o botao
        self.btn = wx.Button(self, label='Click me')
        btnSizer.Add(self.btn, 0)
        self.btn.Bind(wx.EVT_BUTTON, self.onClickMe) # adiciona o evento

        vboxSizer.Add(btnSizer)
        self.SetSizer(vboxSizer)

    def onClickMe(self, event):
        self.labelText.SetLabelText('Text has been changed')

class MyApp(wx.App):
    def OnInit(self):
        title = 'Buttons Events'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
