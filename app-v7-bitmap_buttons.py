"""
Bitmap Buttons
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
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        # 1. cria os botoes e adiciona imagem bitmap

        # Créditos da imagem: <a href="https://www.flaticon.com/free-icons/copy" title="copy icons">Copy icons created by Catalin Fertu - Flaticon</a>
        imageFile1 = 'assets/copy.png'
        image1 = wx.Image(imageFile1, wx.BITMAP_TYPE_ANY).Rescale(32, 32).ConvertToBitmap()
        self.button1 = wx.BitmapButton(
            self,
            id=1,
            bitmap=image1,
            size=(50, 50 # define tamanho e formato do botao
                # image1.GetWidth() + 40,
                # image1.GetHeight() + 40
            )
        )

        # Créditos da imagem: <a href="https://www.flaticon.com/free-icons/save" title="save icons">Save icons created by Yogi Aprelliyanto - Flaticon</a>
        imageFile2 = 'assets/save.png'
        image2 = wx.Image(imageFile2, wx.BITMAP_TYPE_ANY).Rescale(32, 32).ConvertToBitmap()
        self.button2 = wx.BitmapButton(
            self,
            # id=-1,
            id=2,
            bitmap=image2,
            size=( # define tamanho e formato do botao
                image2.GetWidth() + 100,
                image2.GetHeight() + 40
            )
        )

        # Créditos da imagem: <a href="https://www.flaticon.com/free-icons/folder" title="folder icons">Folder icons created by Freepik - Flaticon</a>
        imageFile3 = 'assets/folder.png'
        image3 = wx.Image(imageFile3, wx.BITMAP_TYPE_ANY).Rescale(32, 32).ConvertToBitmap()
        self.button3 = wx.BitmapButton(
            self,
            # id=-1,
            id=3,
            bitmap=image3,
            size=( # define tamanho e formato do botao
                image3.GetWidth() + 40,
                image3.GetHeight() + 40
            )
        )

        # 2. define o texto que será exibido nos botões

        self.button1.SetLabel('Copy') # label exibido a frente do botao
        self.button2.SetLabel('Save')
        self.button3.SetLabel('Folder')
        self.button1.SetToolTipString("Copy") # passar mouse para mostrar label
        self.button2.SetToolTipString("Save") 
        self.button3.SetToolTipString("Folder")

        # 3. adiciona os eventos aos botoes

        self.button1.Bind(wx.EVT_BUTTON, self.onClicked)
        self.button2.Bind(wx.EVT_BUTTON, self.onClicked)
        self.button3.Bind(wx.EVT_BUTTON, self.onClicked)

        # 4. organiza os três botões lado a lado no layout horizontal, centralizando cada botao e o hbox é adicionado ao layout vertical vbox, centralizando-o verticalmente        

        hbox.Add(self.button1, 0, wx.ALIGN_CENTER)
        hbox.Add(self.button2, 0, wx.ALIGN_CENTER)
        hbox.Add(self.button3, 0, wx.ALIGN_CENTER)
        vbox.Add(hbox, 1, wx.ALIGN_CENTER)
        self.SetSizer(vbox)


    def onClicked(self, event):
        """ Mostra no terminal o nome do botao pressionado """

        btn = event.GetEventObject().GetLabel()
        print('Label of pressed button is:', btn)


class MyApp(wx.App):
    def OnInit(self):
        title = 'Bitmap Buttons'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
