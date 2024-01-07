from typing import Any
import requests
from dataclasses import dataclass
from typing import *
import random
import os


NColorScheme = ['NPG', 'AAAS', 'NEJM', 'LANCET', 'JAMA', 'JCO', 'UCSCGB', 'D3', 'LOCUSZOOM', 'IGV']


@dataclass
class DefaultColorScheme(object):
    NPG = '"#E64B35FF" "#4DBBD5FF" "#00A087FF" "#3C5488FF" "#F39B7FFF" "#8491B4FF" "#91D1C2FF" "#DC0000FF" "#7E6148FF" "#B09C85FF"'.replace('"', '').split( )
    AAAS = '"#3B4992FF" "#EE0000FF" "#008B45FF" "#631879FF" "#008280FF" "#BB0021FF" "#5F559BFF" "#A20056FF" "#808180FF" "#1B1919FF"'.replace('"', '').split( )
    NEJM = '"#BC3C29FF" "#0072B5FF" "#E18727FF" "#20854EFF" "#7876B1FF" "#6F99ADFF" "#FFDC91FF" "#EE4C97FF"'.replace('"', '').split( )
    LANCET = '"#00468BFF" "#ED0000FF" "#42B540FF" "#0099B4FF" "#925E9FFF" "#FDAF91FF" "#AD002AFF" "#ADB6B6FF" "#1B1919FF"'.replace('"', '').split( )
    JAMA = '"#374E55FF" "#DF8F44FF" "#00A1D5FF" "#B24745FF" "#79AF97FF" "#6A6599FF" "#80796BFF"'.replace('"', '').split( )
    JCO = ' "#0073C2FF" "#EFC000FF" "#868686FF" "#CD534CFF" "#7AA6DCFF" "#003C67FF" "#8F7700FF" "#3B3B3BFF" "#A73030FF" "#4A6990FF"'.replace('"', '').split( )
    UCSCGB = '"#FF0000FF" "#FF9900FF" "#FFCC00FF" "#00FF00FF" "#6699FFFF" "#CC33FFFF" "#99991EFF" "#999999FF" "#FF00CCFF" "#CC0000FF"'.replace('"', '').split( )
    D3 = ' "#1F77B4FF" "#FF7F0EFF" "#2CA02CFF" "#D62728FF" "#9467BDFF" "#8C564BFF" "#E377C2FF" "#7F7F7FFF" "#BCBD22FF" "#17BECFFF"'.replace('"', '').split( )
    LOCUSZOOM = '"#D43F3AFF" "#EEA236FF" "#5CB85CFF" "#46B8DAFF" "#357EBDFF" "#9632B8FF" "#B8B8B8FF"'.replace('"', '').split( )
    IGV = '"#5050FFFF" "#CE3D32FF" "#749B58FF" "#F0E685FF" "#466983FF" "#BA6338FF" "#5DB1DDFF" "#802268FF" "#6BD76BFF" "#D595A7FF"'.replace('"', '').split( )


class ColorScheme:
    def __init__(self, color_scheme: DefaultColorScheme = DefaultColorScheme(), alpha: float = 0.0):
        self.color_scheme = color_scheme
        self.alpha = alpha
        self.__set_alpha()


    def add_alpha_to_hex(self, hex_color: str):
        a_hex = format(int(self.alpha * 255), '02x')
        # 返回带有透明度的颜色代码RGBA
        return f"{hex_color}{a_hex}"
    

    def __set_alpha(self):
       for color in NColorScheme:
            setattr(self.color_scheme, color, [self.add_alpha_to_hex(i) for i in getattr(self.color_scheme, color)])


    @staticmethod
    def get_random_color_from_aicolor() -> list:
        url = 'https://jsuifmbqefnxytqwmaoy.supabase.co/rest/v1/palette?select=*&order=likes.desc'
        res = requests.get(url, headers={
            'Content-Type': 'application/json',
            'Prefer': 'safe',
            'Apikey':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpzdWlmbWJxZWZueHl0cXdtYW95Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2NzcwMjE1ODMsImV4cCI6MTk5MjU5NzU4M30.09YStNMblCJmFgb9BvpbrGEv4vVyePe3zSI7KeVzVTU'

        })
        response_json = res.json()
        color_list = list()
        for i in response_json:
            color_list.append([i['bg'], i['bgFocus'], i['primaryClear'], i['primaryDull'], i['primaryVisible'], i['accentClear'], i['accentDull'], i['clear'], i['dull'], i['duller']])
            
        return random.choice(color_list)


    @staticmethod
    def generate_color_scheme_from_image(img: str) -> list:
        # 从图片中提取颜色
        import colorgram
        
        colors = colorgram.extract(img, 10)
        color_list = list()
        for color in colors:
            color_list.append(color.rgb.hex)
        
        return color_list