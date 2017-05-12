# main.py
import pyb
import upcd8544
from machine import SPI,Pin 

def main():
    lcd_5110.lcd_write_string('MicroPython',10,1)

    lcd_5110.lcd_write_chinese("物",18,3)
    lcd_5110.lcd_write_chinese("联",34,3)
    lcd_5110.lcd_write_chinese("网",50,3)

    pyb.delay(1000)

if __name__ == '__main__':
    SPI = pyb.SPI(1) #DIN=>X8-MOSI/CLK=>X6-SCK
    RST    = pyb.Pin('X1')
    CE     = pyb.Pin('X2')
    DC     = pyb.Pin('X3')
    LIGHT  = pyb.Pin('X4')
    lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
    while(1):
     main()
