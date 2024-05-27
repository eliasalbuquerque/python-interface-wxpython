"""
Question Dialog
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
        widgetSizer = wx.BoxSizer(wx.VERTICAL)
        widgetPanel = wx.Panel(self)


        self.button = wx.Button(widgetPanel, label='Open Question Dialog')
        self.Bind(wx.EVT_BUTTON, self.questionDialog, self.button)

        self.button2 = wx.Button(widgetPanel, label='Open Confirmation Dialog')
        self.Bind(wx.EVT_BUTTON, self.confirmationDialog, self.button2)


        widgetSizer.Add(self.button)
        widgetSizer.Add(self.button2, 0, wx.TOP, 20)
        widgetPanel.SetSizer(widgetSizer)

        vbox.Add(widgetPanel, 0, wx.ALL, 100)
        self.SetSizer(vbox)

    def questionDialog(self, event):
        dialog = wx.MessageDialog(
            # None, 
            self, 
            message='Are you sure you want to close?', 
            caption='Question', 
            style=wx.YES_NO | wx.ICON_QUESTION)
        """ Opções para style:
            Botões:
                wx.YES_NO
                wx.YES_DEFAULT
                wx.NO_DEFAULT
                wx.OK
                wx.OK_DEFAULT
                wx.CANCEL
                wx.CANCEL_DEFAULT
                wx.YES_NO | wx.CANCEL (com três botões)
            Ícones:
                wx.ICON_EXCLAMATION (exclamação)
                wx.ICON_ERROR (erro)
                wx.ICON_INFORMATION (informação)
                wx.ICON_QUESTION (pergunta)
                wx.ICON_WARNING (aviso)"""
        result = dialog.ShowModal()

        if result == wx.ID_YES:
            print('Yes, close the app')
            self.GetParent().Close(True)
        else:
            print('No, the app still open')

    def confirmationDialog(self, event):
        dialog = wx.MessageDialog(
            # None, 
            self, 
            message='Do you want to proceed with this action?', 
            caption='Confirm Action', 
            style=wx.OK | wx.CANCEL | wx.ICON_EXCLAMATION)
        result = dialog.ShowModal()

        if result == wx.ID_OK:
            print('Ok, close the app')
            self.GetParent().Close(True)
        else:
            print('Cancel action')



class MyApp(wx.App):
    def OnInit(self):
        title = 'Question Dialog'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
