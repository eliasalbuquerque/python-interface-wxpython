import wx

# criar o objeto da aplicacao
app = wx.App()

# criar o frame
frame = wx.Frame(None, title='Hello World')

# mostrar o frame
frame.Show()

# colocar a janela em loop
app.MainLoop()
