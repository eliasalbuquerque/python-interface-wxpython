"""
Box Sizer
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
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.staticText()
        self.staticText1(vbox, hbox)

    def staticText(self):
        label = 'Static text'
        pos = (100, 200)
        self.label = wx.StaticText(self, label=label, pos=pos)
    
    def staticText1(self, vbox, hbox):
        style = wx.ALIGN_CENTER
        label1 = 'Static text 1'
        label2 = 'Static text 2'
        label3 = 'Static text 3'
        label4 = 'Static text 4'

        self.label1 = wx.StaticText(self, label=label1, style=style)
        vbox.Add(self.label1, 0, wx.EXPAND)
        
        self.label2 = wx.StaticText(self, label=label2, style=style)
        vbox.Add(self.label2, 0, wx.EXPAND)
        
        self.label3 = wx.StaticText(self, label=label3, style=style)
        hbox.Add(self.label3, 0, wx.EXPAND)
        hbox.AddSpacer(10) # adiciona espaco entre os labels

        self.label4 = wx.StaticText(self, label=label4, style=style)
        hbox.Add(self.label4, 0, wx.EXPAND)

        # coloca os labels 3 e 4 dentro do alinhamento vertical
        # vbox.Add(hbox) # adiciona o hbox dentro do espaco vertical
        # vbox.Add(hbox, 1, wx.ALL, 20) # adiciona espaco em todos os lados
        # vbox.Add(hbox, 1, wx.LEFT | wx.RIGHT, 10) # adiciona espaco na esq e dir, o numero 1 indica que todo o espaco da vertical sera ocupado
        vbox.Add(hbox, 0, wx.LEFT | wx.RIGHT, 10) # adiciona espaco na esq e dir
        self.SetSizer(vbox)
    

class MyApp(wx.App):
    def OnInit(self):
        title = 'Box Sizer'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True
        

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()