import wx

class HelloFrame(wx.Frame):
    """ Um Hello World mais robusto """

    def __init__(self, *args, **kw):
        # garantir que o __init__ será chamado
        super(HelloFrame, self).__init__(*args, **kw)

        # criar o frame do painel
        painel = wx.Panel(self)

        # colocar e configurar o texto
        texto = wx.StaticText(painel, label='Hello World')
        fonte = texto.GetFont()
        fonte.PointSize += 10
        fonte = fonte.Bold()
        texto.SetFont(fonte)

        # criar o tamanho para gerenciar o layout dos widgets filhos
        tamanho = wx.BoxSizer(wx.VERTICAL)
        tamanho.Add(texto, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        painel.SetSizer(tamanho)

        # criar uma barra de menu
        self.makeMenuBar()

        # criar uma barra de status
        self.CreateStatusBar()
        self.SetStatusText('Primeira interface com wxPython!')

    def makeMenuBar(self):
        """ 
        Uma barra de menu composta por itens de menu.
        Esse metodo constroi um conjunto de menus e cria links para serem 
        chamados quando clicados
        """

        # criar um menu 'arquivo' com Olá e Sair como itens
        menuArquivo = wx.Menu()

        # criar o menu Olá e definir um label para ele
        # - o '\t' define um comando de teclado que aciona o mesmo evento
        itemOla = menuArquivo.Append(-1, '&Olá!\tCtrl-O')
        menuArquivo.AppendSeparator()

        # criar o menu Sair, nesse caso nao precisa criar um label por ser um 
        # ID padrão da biblioteca 'ID_EXIT'
        # itemSair = menuArquivo.Append(wx.ID_EXIT) # item de menu padrao simples
        itemSair = menuArquivo.Append(wx.ID_EXIT, '&Sair\tCtrl+Q') # adiciona o atalho e o label para o item de menu

        # criar o menu 'ajuda' com o item 'sobre'
        menuAjuda = wx.Menu()
        itemSobre = menuAjuda.Append(wx.ID_ABOUT)

        # criar a barra do menu e incluir os menus
        # o '&' define que a proxima letra é o 'mnemonic' para o item menu
        barraMenu = wx.MenuBar()
        barraMenu.Append(menuArquivo, '&Arquivo')
        barraMenu.Append(menuAjuda, 'Aju&da')

        # colocar a barra de menu no frame
        self.SetMenuBar(barraMenu)

        # associe uma função manipuladora ao evento EVT_MENU para cada um dos 
        # itens de menu. Isso significa que quando esse item de menu for 
        # ativado, a função de manipulador associada será chamada.
        self.Bind(wx.EVT_MENU, self.OnHello, itemOla)
        self.Bind(wx.EVT_MENU, self.OnExit, itemSair)
        self.Bind(wx.EVT_MENU, self.OnAbout, itemSobre)

    # associando os itens aos eventos correspondentes
    def OnExit(self, event):
        """ fecha o frame terminando a aplicacao """
        self.Close(True)

    def OnHello(self, event):
        """ diz ola para o usuario """

        # wx.MessageBox('Hello World com wxPython') # caixa de mensagem simples
        wx.MessageBox('Hello World com wxPython', 
        'Arquivo - Hello World 2',
        wx.OK|wx.ICON_INFORMATION) # com titulo na caixa de mensagem

    def OnAbout(self, event):
        """ mostra um dialogo Sobre """

        # abre a caixa de mensagem com o texto (1) e titulo na caixa (2)
        wx.MessageBox('Este é um exemplo de Hello World', 
        'Sobre - Hello World 2', 
        wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    app = wx.App()
    frame = HelloFrame(None, title='Hello World 2')
    frame.Show()
    app.MainLoop()