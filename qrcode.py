import pyqrcode 
from pyqrcode import QRCode  
s = print('input your Website link or Prpfile URL : ')
use = input()
url = pyqrcode.create(use)  
url.svg("myqr.svg", scale = 8)
