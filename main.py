from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class MyBoxLayout(BoxLayout):
    pass


class DotButton(Button):
    pass


class NumButton(Button):
    src = StringProperty('resources/white.png')

    def resetNumber(self):
        self.text = ' '
    
    def resetColor(self):
        self.src = 'resources/white.png'



class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.gamecols = 7
        self.cols = self.gamecols * 2 + 1
        self.gamerows = 7
        for row in range(self.gamerows):
            self.dotRow()
            self.numRow()
        self.dotRow()

    def dotRow(self):
        for col in range(self.gamecols):
            self.add_widget(DotButton())
            self.add_widget(HLineButton())
        self.add_widget(DotButton())

    def numRow(self):
        for col in range(self.gamecols):
            self.add_widget(VLineButton())
            self.add_widget(NumButton())
        self.add_widget(VLineButton())

    def resetLines(self, grid):
        for child in grid.children:
            if 'Line' in str(type(child)):
                child.resetLine()

    def resetAll(self, grid):
        for child in grid.children:
            if 'Line' in str(type(child)):
                child.resetLine()
            elif 'Num' in str(type(child)):
                child.resetNumber()
                child.resetColor()
    
    def resetColor(self, grid):
        for child in grid.children:
            if 'Num' in str(type(child)):
                child.resetColor()


class Line(Button):
    src = StringProperty('resources/grey.png')

    def changeColor(self, line):
        if line.src == 'resources/grey.png':
            line.src = 'resources/black.png'
        elif line.src == 'resources/black.png':
            line.src = 'resources/red.png'
        else:
            line.src = 'resources/grey.png'

    def resetLine(self):
        self.src = 'resources/grey.png'


class HLineButton(Line):
    pass


class VLineButton(Line):
    pass


class SlitherlinkBoardApp(App):
    __version__ = '005'
    __author__ = 'NemoM'
    version = StringProperty(__version__)

    title = 'Slitherlink Board'

    size = StringProperty('15sp')
    numlock = BooleanProperty(False)

    def changeNumber(self, btn):
        if self.numlock:
            if btn.src == 'resources/yellow.png':
                btn.src = 'resources/white.png'
            else:
                btn.src = 'resources/yellow.png'
        else:
            if btn.text == '3':
                btn.text = '0'
            elif btn.text == '2':
                btn.text = '3'
            elif btn.text == '1':
                btn.text = '2'
            elif btn.text == '0':
                btn.text = ' '
            else:
                btn.text = '1'



if __name__ == '__main__':
    SlitherlinkBoardApp().run()
