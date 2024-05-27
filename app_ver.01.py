import wx
# import wx.grid as grid


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 500))
        self.SetMinSize(wx.Size(520, 430))  # ajusta tamanho minimo da janela
        self.SetMaxSize(wx.Size(1200, 650))  # ajusta tamanho máximo da janela

        # Inicializar o painel
        self.panel = MyPanel(self)

    def closeProgram(self):
        self.Close()


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        # 1. Areas do layout

        # Layouts do painel principal (MyPanel)
        vbox = wx.BoxSizer(wx.VERTICAL)  # Para organizar os widgets
        hbox = wx.BoxSizer(wx.HORIZONTAL)  # Para organizar os grupos de botões

        # Painel para alocar os widgets da aplicacao (painel branco)
        widgetArea = wx.Panel(self)
        widgetAreaSizer = wx.BoxSizer(wx.VERTICAL)
        widgetArea.SetBackgroundColour('white')  # Definir a cor do painel

        # Painel para alocar widgets da area superior do painel branco
        verticalTop = wx.Panel(widgetArea)
        verticalTopSizer = wx.BoxSizer(wx.HORIZONTAL)

        # Painel para alocar widgets da area inferior do painel branco
        verticalBotton = wx.Panel(widgetArea)
        verticalBottonSizer = wx.BoxSizer(wx.HORIZONTAL)

        # 2. Widgets

        # Widgets do painel principal (self = MyPanel)

        # static text
        self.staticText = wx.StaticText(
            self, label='This is a Static Text', style=wx.ALIGN_CENTER)

        # ok / cancel buttons
        okButton = wx.Button(self, wx.ID_OK, "&OK")
        cancelButton = wx.Button(self, wx.ID_CANCEL, "&Cancel")

        # organizar botões OK/Cancel com StdDialogButtonSizer
        btnStdSizer = wx.StdDialogButtonSizer()
        btnStdSizer.AddButton(okButton)
        btnStdSizer.AddButton(cancelButton)
        btnStdSizer.Realize()

        # Divisor
        # staticLine = wx.StaticLine(self, style=wx.LI_HORIZONTAL)

        # Widgets do Vertical Top
        """ 
        1. cria static box
        2. cria o sizer e vincula com o static box
        2. cria os widgets
        3. add widgets ao sizer
        4. add sizer a area do painel 
        """

        # buttons
        sbButtons = wx.StaticBox(verticalTop, label='Buttons')
        buttonsSizer = wx.StaticBoxSizer(sbButtons, wx.VERTICAL)

        btn1 = wx.Button(verticalTop, label='Button 1')
        btn2 = wx.Button(verticalTop, label='Button 2')
        btn3 = wx.Button(verticalTop, label='Button 3')

        buttonsSizer.Add(btn1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        buttonsSizer.Add(btn2, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        buttonsSizer.Add(btn3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        verticalTopSizer.Add(buttonsSizer, 1, wx.EXPAND | wx.ALL, 5)

        # bitmap buttons
        sbBitmapButtons = wx.StaticBox(verticalTop, label='Bitmap Buttons')
        bitmapButtonsSizer = wx.StaticBoxSizer(sbBitmapButtons)

        imageFile1 = 'assets/copy.png'
        imageFile2 = 'assets/save.png'
        imageFile3 = 'assets/folder.png'

        image1 = wx.Image(imageFile1, wx.BITMAP_TYPE_ANY).Rescale(
            32, 32).ConvertToBitmap()
        image2 = wx.Image(imageFile2, wx.BITMAP_TYPE_ANY).Rescale(
            32, 32).ConvertToBitmap()
        image3 = wx.Image(imageFile3, wx.BITMAP_TYPE_ANY).Rescale(
            32, 32).ConvertToBitmap()

        bitmapBtn1 = wx.BitmapButton(verticalTop, bitmap=image1, size=(50, 50))
        bitmapBtn2 = wx.BitmapButton(verticalTop, bitmap=image2, size=(50, 50))
        bitmapBtn3 = wx.BitmapButton(verticalTop, bitmap=image3, size=(50, 50))

        bitmapBtn1.SetLabel('Copy')  # label exibido a frente do botao
        bitmapBtn2.SetLabel('Save')
        bitmapBtn3.SetLabel('Folder')

        bitmapBtn1.SetToolTip("Copy")  # passar mouse para mostrar label
        bitmapBtn2.SetToolTip("Save")
        bitmapBtn3.SetToolTip("Folder")

        bitmapButtonsSizer.Add(bitmapBtn1, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        bitmapButtonsSizer.Add(bitmapBtn2, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        bitmapButtonsSizer.Add(bitmapBtn3, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        verticalTopSizer.Add(bitmapButtonsSizer, 1, wx.EXPAND | wx.ALL, 5)

        # toggle button
        sbToggleButtons = wx.StaticBox(verticalTop, label='Toggle Button')
        toggleButtonsSizer = wx.StaticBoxSizer(sbToggleButtons, wx.VERTICAL)

        toggleBtn = wx.ToggleButton(verticalTop, label='Click to ON')

        toggleButtonsSizer.Add(toggleBtn, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        verticalTopSizer.Add(toggleButtonsSizer, 1, wx.EXPAND | wx.ALL, 5)

        # Widgets do Vertical Botton
        """ 
        1. cria static box
        2. cria o sizer e vincula com o static box
        2. cria os widgets
        3. add widgets ao sizer
        4. add sizer a area do painel 
        """

        # checkbox
        sbCheckBox = wx.StaticBox(verticalBotton, label='Check Box')
        checkBoxSizer = wx.StaticBoxSizer(sbCheckBox, wx.VERTICAL)

        checkBox1 = wx.CheckBox(verticalBotton, label='Cat')
        checkBox2 = wx.CheckBox(verticalBotton, label='Dog')
        checkBox3 = wx.CheckBox(verticalBotton, label='Rat')

        checkBoxSizer.Add(checkBox1, 0, wx.ALL, 5)
        checkBoxSizer.Add(checkBox2, 0, wx.ALL, 5)
        checkBoxSizer.Add(checkBox3, 0, wx.ALL, 5)

        self.checkBoxes = []  # para contar quanto foram selecionados
        self.checkBoxes.append(checkBox1)
        self.checkBoxes.append(checkBox2)
        self.checkBoxes.append(checkBox3)

        verticalBottonSizer.Add(checkBoxSizer, 1, wx.EXPAND | wx.ALL, 5)

        # radio buttons
        sbRadioButtons = wx.StaticBox(verticalBotton, label='Radio Buttons')
        radioButtonsSizer = wx.StaticBoxSizer(sbRadioButtons, wx.VERTICAL)

        radioButton1 = wx.RadioButton(verticalBotton, label='Fox')
        radioButton2 = wx.RadioButton(verticalBotton, label='Owl')
        radioButton3 = wx.RadioButton(verticalBotton, label='Bee')

        radioButtonsSizer.Add(radioButton1, 0, wx.ALL, 5)
        radioButtonsSizer.Add(radioButton2, 0, wx.ALL, 5)
        radioButtonsSizer.Add(radioButton3, 0, wx.ALL, 5)

        verticalBottonSizer.Add(radioButtonsSizer, 1, wx.EXPAND | wx.ALL, 5)

        # message box
        sbMessageButtons = wx.StaticBox(
            verticalBotton, label='Message Buttons')
        messageButtonsSizer = wx.StaticBoxSizer(sbMessageButtons, wx.VERTICAL)

        messageButton1 = wx.Button(verticalBotton, label='Info Message')
        messageButton2 = wx.Button(verticalBotton, label='Warning Message')
        messageButton3 = wx.Button(verticalBotton, label='Error Message')

        messageButtonsSizer.Add(messageButton1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        messageButtonsSizer.Add(messageButton2, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        messageButtonsSizer.Add(messageButton3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        verticalBottonSizer.Add(messageButtonsSizer, 1, wx.EXPAND | wx.ALL, 5)

        # qestion buttons
        sbQuestionButtons = wx.StaticBox(
            verticalBotton, label='Question Buttons')
        questionButtonsSizer = wx.StaticBoxSizer(
            sbQuestionButtons, wx.VERTICAL)

        questionButton1 = wx.Button(verticalBotton, label='Question Dialog')
        questionButton2 = wx.Button(
            verticalBotton, label='Confirmation Dialog')

        questionButtonsSizer.Add(
            questionButton1, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        questionButtonsSizer.Add(
            questionButton2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        verticalBottonSizer.Add(questionButtonsSizer, 1, wx.EXPAND | wx.ALL, 5)

        # 4. Layout

        # Paineis individuais: definindo os layouts de cada painel vertical
        verticalBotton.SetSizer(verticalBottonSizer)
        verticalTop.SetSizer(verticalTopSizer)

        # Painel conteiner: add Vertical TOP / BOTTON na area dos widgets (painel branco)
        widgetAreaSizer.Add(verticalTop, 1, wx.EXPAND | wx.ALL, 5)
        widgetAreaSizer.Add(verticalBotton, 1, wx.EXPAND | wx.ALL, 5)
        widgetArea.SetSizer(widgetAreaSizer)

        # Painel principal: add static text, area dos widgets e botoes infer. no painel principal
        vbox.Add(self.staticText, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        vbox.Add(widgetArea, 1, wx.ALL | wx.EXPAND, 10)
        vbox.Add(btnStdSizer, 0, wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, 10)

        # Fecha o layout
        self.SetSizer(vbox)

        # Eventos
        self.Bind(wx.EVT_BUTTON, self.onOK, okButton)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelButton)

        self.Bind(wx.EVT_BUTTON, self.onButton, btn1)
        self.Bind(wx.EVT_BUTTON, self.onButton, btn2)
        self.Bind(wx.EVT_BUTTON, self.onButton, btn3)

        self.Bind(wx.EVT_BUTTON, self.onBitmapButton, bitmapBtn1)
        self.Bind(wx.EVT_BUTTON, self.onBitmapButton, bitmapBtn2)
        self.Bind(wx.EVT_BUTTON, self.onBitmapButton, bitmapBtn3)

        self.Bind(wx.EVT_TOGGLEBUTTON, self.onToggleClick, toggleBtn)

        self.Bind(wx.EVT_CHECKBOX, self.onChecked, checkBox1)
        self.Bind(wx.EVT_CHECKBOX, self.onChecked, checkBox2)
        self.Bind(wx.EVT_CHECKBOX, self.onChecked, checkBox3)

        self.Bind(wx.EVT_RADIOBUTTON, self.onRadioButton, radioButton1)
        self.Bind(wx.EVT_RADIOBUTTON, self.onRadioButton, radioButton2)
        self.Bind(wx.EVT_RADIOBUTTON, self.onRadioButton, radioButton3)

        self.Bind(wx.EVT_BUTTON, self.onInfoButton, messageButton1)
        self.Bind(wx.EVT_BUTTON, self.onWarningButton, messageButton2)
        self.Bind(wx.EVT_BUTTON, self.onErrorButton, messageButton3)

        self.Bind(wx.EVT_BUTTON, self.onQuestionDialog, questionButton1)
        self.Bind(wx.EVT_BUTTON, self.onConfirmationDialog, questionButton2)

    def onConfirmationDialog(self, event):
        dialog = wx.MessageDialog(
            # None,
            self,
            message='Confirm that you want to close the application:',
            caption='Confirm Action',
            style=wx.OK | wx.CANCEL | wx.ICON_EXCLAMATION)
        result = dialog.ShowModal()

        if result == wx.ID_OK:
            self.GetParent().closeProgram()
        else:
            self.staticText.SetLabelText('This is a Static Text')

    def onQuestionDialog(self, event):
        dialog = wx.MessageDialog(
            self,
            message='Are you sure you want to close?',
            caption='Question Action',
            style=wx.YES_NO | wx.ICON_QUESTION
        )
        result = dialog.ShowModal()

        if result == wx.ID_YES:
            self.GetParent().closeProgram()
        else:
            self.staticText.SetLabelText('This is a Static Text')

    def onErrorButton(self, event):
        wx.MessageBox('Message box ERROR icon', 'Dialog',
                      wx.OK | wx.ICON_ERROR)
        self.staticText.SetLabelText('This is a Static Text')

    def onWarningButton(self, event):
        wx.MessageBox('Message box WARNING icon', 'Dialog',
                      wx.OK | wx.ICON_WARNING)
        self.staticText.SetLabelText('This is a Static Text')

    def onInfoButton(self, event):
        wx.MessageBox('Message box INFO icon', 'Dialog',
                      wx.OK | wx.ICON_INFORMATION)
        self.staticText.SetLabelText('This is a Static Text')

    def onRadioButton(self, event):
        rb = event.GetEventObject().GetLabel()
        newLabel = 'You selected the radio button: ' + str(rb)
        self.staticText.SetLabelText(newLabel)

    def onChecked(self, event):
        selected = sum(cb.GetValue() for cb in self.checkBoxes)
        newLabel = str(selected) + ' checkbox(es) selected'
        self.staticText.SetLabelText(newLabel)

    def onToggleClick(self, event):
        self.state = event.GetEventObject().GetValue()
        if self.state == True:
            self.staticText.SetLabel('Toggle button set ON')
            self.staticText.Refresh()
            event.GetEventObject().SetLabel('Click to OFF')
        else:
            self.staticText.SetLabel('Toggle button set OFF')
            self.staticText.Refresh()
            event.GetEventObject().SetLabel('Click to ON')

    def onBitmapButton(self, event):
        labelBtn = event.GetEventObject().GetLabel()
        newLabel = labelBtn + ' button'
        self.staticText.SetLabelText(newLabel)

    def onButton(self, event):
        labelBtn = event.GetEventObject().GetLabel()
        newLabel = labelBtn + ' was clicked'
        self.staticText.SetLabelText(newLabel)

    def onCancel(self, event):
        self.GetParent().closeProgram()

    def onOK(self, event):
        self.staticText.SetLabelText('This is a Static Text')


class MyApp(wx.App):
    def OnInit(self):
        # Inicializar o frame com um título
        self.frame = MyFrame(
            parent=None, title="wxPython Desenvolvimento - Ver.01")
        self.frame.Show()
        return True


# Ponto de entrada da aplicação
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
