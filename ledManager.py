import board
import neopixel
import time
from rpi_ws281x import *
import time
import sys
import threading

# LED strip configuration:
LED_COUNT      = 95      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

class ledManager(object):
	def __init__(self):
		self.strand = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
		self.strand.begin()
		self.set_led_off()
		self.led_status = "Off"

		print('led Manager Activated')

	def set_led_off(self):
		"""
			Turn off all LEDs
		"""
		for i in range(self.strand.numPixels()):
			self.strand.setPixelColor(i, Color(0, 0, 0))
		self.strand.show()
		self.led_status = "Off"

	def set_led_blue(self):
		"""
			Turn LEDS to Blue
		"""
		for i in range(self.strand.numPixels()):
			self.strand.setPixelColor(i, Color(0, 0, 255))
		self.strand.show()
		self.led_status = "Blue"

	def set_led_red(self):
		"""
			Turn LEDS to Red
		"""
		for i in range(self.strand.numPixels()):
			self.strand.setPixelColor(i, Color(255, 0, 0))
		self.strand.show()
		self.led_status = "Red"

	def set_led_green(self):
		"""
			Turn LEDS to Green
		"""
		for i in range(self.strand.numPixels()):
			self.strand.setPixelColor(i, Color(0, 255, 0))
		self.strand.show()
		self.led_status = "Green"

	def set_led_on(self):
		"""
			Turn LEDs to Blue by default
		"""
		self.set_led_blue()
