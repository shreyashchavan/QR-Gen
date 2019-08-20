import pyqrcode 
from pyqrcode import QRCode  
s = print('input your website name : ')
use = input()
url = pyqrcode.create(use)  
url.svg("myqr.svg", scale = 8)