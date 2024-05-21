"""
grid sizer
"""


import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size = (600, 500))
        self.SetMinSize(wx.Size(500, 400)) # ajusta tamanho minimo da janela

        panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        self.gridSizer()

    def gridSizer(self):
        # cria um grid de 4 linhas e 4 colunas com espaco de 5 pixels entre
        # gridsizer = wx.GridSizer(4, 4, 5, 5)
        gridsizer = wx.GridSizer(rows=4, cols=4, vgap=5, hgap=5)
        
        # cria botoes em cada grid do painel
        for i in range(1, 17):
            btn = "Btn" + str(i)
            gridsizer.Add(wx.Button(self, label = btn), 0, wx.EXPAND)
            self.SetSizer(gridsizer)
    

class MyApp(wx.App):
    def OnInit(self):
        title = 'Grid Sizer'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True
        

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()