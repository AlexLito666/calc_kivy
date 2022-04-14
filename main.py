from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
Window.size = (400, 500) 



class MyApp(App):
    def build(self):
        
        layout_box = BoxLayout(orientation="vertical")
        layout_grid = GridLayout(cols = 4, rows = 5)
        btn1 = Button(text = "C", background_color = (230, 230, 230, .8), color = (72, 206, 255), font_size =25)
        btn2 = Button(text = "/", background_color = (230, 230, 230, .8), color = (72, 206, 255), font_size =25)
        btn3 = Button(text = "X", background_color = (230, 230, 230, .8), color = (72, 206, 255), font_size =25)
        btn4 = Button(text = "=", background_color = (230, 230, 230, .8), color = (72, 206, 255), font_size =25)
        btn5 = Button(text = "7", background_color = (250, 250, 250), color = (0,0,0), font_size =25)
        btn6 = Button(text = "8", background_color = (250, 250, 250), color = (0,0,0), font_size =25)
        btn7 = Button(text = "9", background_color = (250, 250, 250), color = (0,0,0), font_size =25)
        btn8 = Button(text = "-", background_color = (230, 230, 230, .8), color = (72, 206, 255), font_size =25)
        btn9 = Button(text = "4", background_color = (250, 250, 250), color = (0,0,0), font_size =25)
        btn10 = Button(text = "5", background_color = (250, 250, 250), color = (0,0,0), font_size =25)
        btn11 = Button(text = "6", background_color = (250, 250, 250), color = (0,0,0), font_size =25)
        btn12 = Button(text = "+", background_color = (230, 230, 230, .8), color = (72, 206, 255), font_size =25)
        btn13 = Button(text = "1", background_color = (250, 250, 250), color = (0,0,0), font_size =25)
        btn14 = Button(text = "2", background_color = (250, 250, 250), color = (0,0,0), font_size =25)
        btn15 = Button(text = "3", background_color = (250, 250, 250), color = (0,0,0), font_size =25)
        btn16 = Button(text = "0", background_color = (250, 250, 250), color = (0,0,0), font_size =25)


        txt_input = TextInput(multiline=False, size_hint =(1, .15), font_size = 40, base_direction ="rtl")

        layout_grid.add_widget(btn1)
        layout_grid.add_widget(btn2)
        layout_grid.add_widget( btn3)
        layout_grid.add_widget(btn4)
        layout_grid.add_widget(btn5)
        layout_grid.add_widget( btn6)
        layout_grid.add_widget(btn7)
        layout_grid.add_widget(btn8)
        layout_grid.add_widget( btn9)
        layout_grid.add_widget(btn10)
        layout_grid.add_widget(btn11)
        layout_grid.add_widget( btn12)
        layout_grid.add_widget( btn13)
        layout_grid.add_widget(btn14)
        layout_grid.add_widget(btn15)
        layout_grid.add_widget( btn16)


        layout_box.add_widget(txt_input)
        layout_box.add_widget(layout_grid)

        return layout_box

MyApp().run()