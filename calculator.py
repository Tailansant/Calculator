import flet as ft
from flet import colors
from decimal import Decimal

buttons = [
    {'operator': 'AC','source': colors.BLACK,'bottom': colors.BLUE_GREY_100},
    {'operator': '±','source': colors.BLACK,'bottom': colors.BLUE_GREY_100},
    {'operator': '%','source': colors.BLACK,'bottom': colors.BLUE_GREY_100},
    {'operator': '/','source': colors.WHITE,'bottom': colors.ORANGE},
    {'operator': '7','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '8','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '9','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '*','source': colors.WHITE,'bottom': colors.ORANGE},
    {'operator': '4','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '5','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '6','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '-','source': colors.WHITE,'bottom': colors.ORANGE},
    {'operator': '1','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '2','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '3','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '+','source': colors.WHITE,'bottom': colors.ORANGE},
    {'operator': '0','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '.','source': colors.WHITE,'bottom': colors.WHITE24},
    {'operator': '=','source': colors.WHITE,'bottom': colors.ORANGE},
]

def main_function(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 390
    page.title = 'Calculator'
    page.window_always_on_top = True
    
    result = ft.Text(value='0', color=colors.WHITE, size=20)
    
    def calculate(operator, actual_value):
        try:
            
            value = eval(actual_value)
            
            if operator == '%':
                value = value / 100
            
            elif operator == '±':
                value =- value
        except:
            return '--'
        
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        
        return format(value, f'.{digits}f')
    
    def select(event):
        actual_value = result.value if result.value not in ('0','--') else ''
        value = event.control.content.value
        
        if value.isdigit():
            value = actual_value + value
            
        elif value == 'AC':
            value = '0'
            
        else:
            if actual_value and actual_value[-1] in ('/','*','-','+','.'):
                actual_value = actual_value[:-1]
                
            value = actual_value + value
            
            if value[-1] in ('=','%', '±'):
                value = calculate(operator=value[-1], actual_value= actual_value)
                
        result.value = value
        result.update()
    
    display = ft.Row(
        width = 300,
        controls = [result],
        alignment= 'end'
    )
    
    button = [ft.Container(
        content = ft.Text(value= button['operator'], color= button['source']),
        width= 50,
        height= 50,
        bgcolor= button['bottom'],
        border_radius= 100,
        alignment= ft.alignment.center,
        on_click= select
    )  for button in buttons ]
    
    keybord = ft.Row(
        width= 250,
        wrap = True,
        controls = button,
        alignment = 'end',
    )
    
    page.add(display, keybord,)
    
    
    
ft.app(target= main_function)

