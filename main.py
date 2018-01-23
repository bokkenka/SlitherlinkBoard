from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

# Define default colors...
WHITE = [1,1,1,1]
BLACK = [0,0,0,1]
RED = [1,.5,.5,1]
YELLOW = [1,1,.4,1]
GREY = [.9,.9,.9,1]
ERROR = [0,1,0,1]


class MyBoxLayout(BoxLayout):
    pass


class DotButton(Button):
    pass


class NumButton(Button):
    clr = ListProperty(ERROR)

    def resetNumber(self):
        self.text = ' '
    
    def resetColor(self):
        self.clr = WHITE


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
        self.resetAll(self)

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
    clr = ListProperty(ERROR)

    def changeColor(self, line):
        if line.clr == GREY:
            line.clr = BLACK
        elif line.clr == BLACK:
            line.clr = RED
        else:
            line.clr = GREY

    def resetLine(self):
        self.clr = GREY


class HLineButton(Line):
    pass


class VLineButton(Line):
    pass


class SlitherlinkBoardApp(App):
    __version__ = '1.0'
    __author__ = 'NemoM'
    version = StringProperty(__version__)

    title = 'Slitherlink Board'

    size = StringProperty('15sp')
    numlock = BooleanProperty(False)

    def changeNumber(self, btn):
        if self.numlock:
            if btn.clr == YELLOW:
                btn.clr = WHITE
            else:
                btn.clr = YELLOW
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
