"""
write_bout_the_script_and_what_the_main_focus_of_that
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


class MyApp(wx.App):
    def OnInit(self):
        title = 'Name_title_window'
        self.frame = MyFrame(parent=None, title=title)
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
