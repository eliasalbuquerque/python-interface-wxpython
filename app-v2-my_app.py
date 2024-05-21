import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title)

        # Cria um painel para conter os widgets
        self.panel = wx.Panel(self)

        # Cria os widgets
        self.create_text_ctrl()
        self.create_button()

        # Cria o sizer e organiza os widgets
        self.organize_widgets()

        # Ajusta a dimensão mínima da janela
        self.set_min_size()

        # Ajusta o tamanho da janela e centraliza
        self.fit_and_center()

        # Traz o botão para frente do campo de preenchimento
        self.button.Raise()

    def create_text_ctrl(self):
        self.text_ctrl = wx.TextCtrl(self.panel)

    def create_button(self):
        self.button = wx.Button(self.panel, label="Clique aqui")

    def organize_widgets(self):
        # Cria um sizer para organizar os widgets
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Adiciona o botão ao sizer com uma borda e sem expansão
        sizer.Add(self.button, 0, wx.ALL | wx.ALIGN_CENTER, 10)  # 10 pixels de borda em todos os lados

        # Adiciona um espaço vazio para separar o campo de preenchimento do botão
        sizer.AddSpacer(10)  # Adiciona 10 pixels de espaço vazio

        # Adiciona o campo de preenchimento ao sizer com uma borda e sem expansão
        sizer.Add(self.text_ctrl, 0, wx.ALL | wx.ALIGN_CENTER, 10)  # 10 pixels de borda em todos os lados

        # Define o sizer no painel
        self.panel.SetSizer(sizer)

        # Centraliza os widgets no painel
        sizer.Fit(self.panel)
        self.panel.Layout()

    def set_min_size(self):
        # Define a dimensão mínima da janela
        self.SetMinSize(wx.Size(500, 400))  # Largura mínima de 500 e altura mínima de 400

    def fit_and_center(self):
        # Ajusta o tamanho da janela para que os widgets sejam visíveis
        self.Fit()

        # Centraliza a janela na tela
        self.Centre()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title="Preenchimento")
    frame.Show()
    app.MainLoop()