import RPi.GPIO as IO
from time import sleep

IO.setwarnings(False)
IO.setmode(IO.BOARD)
IO.setup(11,IO.OUT)
IO.setup(12,IO.OUT)
IO.setup(13,IO.OUT)

while 1:
  IO.output(11,IO.HIGH)
  IO.output(12,IO.LOW)
  IO.output(13,IO.LOW)
  print("Red")
  sleep(1)
  IO.output(11,IO.LOW)
  IO.output(12,IO.HIGH)
  IO.output(13,IO.LOW)
  print("Green")
  sleep(1)
  IO.output(11,IO.LOW)
  IO.output(12,IO.LOW)
  IO.output(13,IO.HIGH)
  print("Blue")
  sleep(1)