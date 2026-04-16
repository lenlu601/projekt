from PIL import Image
from random import randint


def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)

def render_ves():
  width = 640
  height = 400
  img = Image.new('RGB', (width, height), (255,255,255))
  farba = random_color()
  for x in range(200, 401):
    for y in range(100, 201):
      img.putpixel((x, y), farba)
  return img
  
def get_line_pixels(img, A, B):
  pixels = []
  width, height = img.size
  if A[0] == B[0]:
    if A[1] > B[1]:
        A,B=B,A
    for y in range(A[1], B[1] + 1):
      x= A[0]
      if not (x < 0 or y < 0 or x >= width or y >= height):
        pixels.append((x, y))
  elif A[1] == B[1]:
    if A[0] > B[0]:
        A,B=B,A
    for x in range(A[0], B[0] + 1):
      y = A[1]
      if not (x < 0 or y < 0 or x >= width or y >= height):
        pixels.append((x, y))
  else:
    if A[0] > B[0]:
        A,B=B,A
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dy/dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
        x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
        if not (x < 0 or y < 0 or x >= width or y >= height):
          pixels.append((x, y))
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
        y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
        if not (x < 0 or y < 0 or x >= width or y >= height):
          pixels.append((x, y))
  return pixels
def draw_line(img,A,B,color):
  width, height = img.size
  if A[0] == B[0]:
    if A[1] > B[1]:
        A,B=B,A
    for y in range(A[1], B[1] + 1):
      x= A[0]
      if not (x < 0 or y < 0 or x >= width or y >= height):
        img.putpixel((x, y), color)
  elif A[1] == B[1]:
    if A[0] > B[0]:
        A,B=B,A
    for x in range(A[0], B[0] + 1):
      y = A[1]
      if not (x < 0 or y < 0 or x >= width or y >= height):
        img.putpixel((x, y), color)
  else:
    if A[0] > B[0]:
        A,B=B,A
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dy/dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
        x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
        if not (x < 0 or y < 0 or x >= width or y >= height):
          img.putpixel((x, y), color)
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
        y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
        if not (x < 0 or y < 0 or x >= width or y >= height):
          img.putpixel((x, y), color)
def FILL_CIRCLE(img, S, r, colour):
  for x in range(0, int(r/2**(1/2)) + 1):
      y = int((r**2 - x**2)**(1/2))
      draw_line(img, (x + S[0], y + S[1]), (x + S[0], -y + S[1]), colour)
      draw_line(img, (y + S[0], x + S[1]), (y + S[0], -x + S[1]), colour)
      draw_line(img, (-x + S[0], -y + S[1]), (-x + S[0], y + S[1]), colour)
      draw_line(img, (-y + S[0], -x + S[1]), (-y + S[0], x + S[1]), colour)
def distance(A, B): #A (5,1) B(4, 2)
  Ax, Ay = A
  Bx, By = B
  return

def FILL_TRIANGLE(img, A, B, C, colour):
  ymin = min(A[1], B[1], C[1])
  ymax = max(A[1], B[1], C[1])

  if ymin < 0:
    ymin = 0
  if ymax >= img.height:
    ymax = img.height - 1

  pixels = get_line_pixels(img, A, B) + get_line_pixels(img, B, C) + get_line_pixels(img, C, A)

  xmin = [img.width] * (ymax + 1)
  xmax = [-1] * (ymax + 1)

  for p in pixels:
    x,y = p

    if y > ymax or y < ymin:
      continue

    if x < xmin[y]:
      xmin[y] = x
    if x > xmax[y]:
      xmax[y] = x

  for y in range(ymin, ymax + 1):
    if xmin[y] <= xmax[y]:
      draw_line(img, (xmin[y], y), (xmax[y], y), colour)


def FILL_RECT(img,A,B,colour):
  ax, ay = A
  width, height = B
  bx, by = ax + width, ay + height

  if ax < bx and ay > by:
    ay, by = by, ay
    for x in range(ax, bx):
      for y in range(ay, by):
        img.putpixel((x, y), colour)
  elif ax < bx and ay < by:
    for x in range(ax, bx):
      for y in range(ay, by):
        img.putpixel((x, y), colour)

  elif ax > bx and ay > by:
    ax, bx = bx, ax
    ay, by = by, ay
    for x in range(ax, bx):
      for y in range(ay, by):
        img.putpixel((x, y), colour)
  elif ax > bx and ay < by:
    ax, bx = bx, ax
    for x in range(ax, bx):
      for y in range(ay, by):
        img.putpixel((x, y), colour)
def LINE(img, A, B, thickness, colour):
  for X in get_line_pixels(img, A, B):
    FILL_CIRCLE(img, X, thickness / 2, colour)
def TRIANGLE(img,A,B,C,thickness,colour):
  LINE(img, A, B,thickness,colour)
  LINE(img, A, C,thickness, colour)
  LINE(img, B, C,thickness,colour)
def RECT(img, A, B, thickness, colour):
  ax, ay = A
  w, h = B
  bx, by = ax + w, ay + h

  if ax < bx and ay < by:
    LINE(img, (ax, ay), (bx, ay), thickness, colour)
    LINE(img, (bx, ay), (bx, by), thickness, colour)
    LINE(img, (ax, ay), (ax, by), thickness, colour)
    LINE(img, (ax, by), (bx, by), thickness, colour)
  elif ax < bx and ay > by:
    LINE(img, (ax, ay), (bx, ay), thickness, colour)
    LINE(img, (bx, ay), (bx, by), thickness, colour)
    LINE(img, (ax, ay), (ax, by), thickness, colour)
    LINE(img, (ax, by), (bx, by), thickness, colour)

  elif ax > bx and ay < by:
    ax, bx = bx, ax
    LINE(img, (ax, ay), (bx, ay), thickness, colour)
    LINE(img, (bx, ay), (bx, by), thickness, colour)
    LINE(img, (ax, ay), (ax, by), thickness, colour)
    LINE(img, (ax, by), (bx, by), thickness, colour)
  elif ax > bx and ay > by:
    ax, bx = bx, ax
    LINE(img, (ax, ay), (bx, ay), thickness, colour)
    LINE(img, (bx, ay), (bx, by), thickness, colour)
    LINE(img, (ax, ay), (ax, by), thickness, colour)
    LINE(img, (ax, by), (bx, by), thickness, colour)
def draw_pixel(img, X, farba):
  width, heigh = img.size
  x, y = X
  if not (x < 0 or y < 0 or x >= width or y >= height):
    img.putpixel(X, farba)
def CIRCLE(img, S, r, thickness, colour):
  A=S
  for x in range(0, int(r / (2**0.5)) + 1):
    y = int((r**2 - x**2)**0.5)
    FILL_CIRCLE(img, (x + S[0], y + S[1]), thickness, colour)
    FILL_CIRCLE(img, (y + S[0], x + S[1]), thickness, colour)
    FILL_CIRCLE(img, (y + S[0], -x + S[1]), thickness, colour)
    FILL_CIRCLE(img, (x + S[0], -y + S[1]), thickness, colour)
    FILL_CIRCLE(img, (-x + S[0], -y + S[1]), thickness, colour)
    FILL_CIRCLE(img, (-y + S[0], -x + S[1]), thickness, colour)
    FILL_CIRCLE(img, (-y + S[0], x + S[1]), thickness, colour)
    FILL_CIRCLE(img, (-x + S[0], y + S[1]), thickness, colour)
def dec2hex(cislo):
  a = ""
  while cislo > 0:
    zvysok = cislo % 16

    if zvysok == 10:
      zvysok = "A"
    elif zvysok == 11:
      zvysok = "B"
    elif zvysok == 12:
      zvysok = "C"
    elif zvysok == 13:
      zvysok = "D"
    elif zvysok == 14:
      zvysok = "E"
    elif zvysok == 15:
      zvysok = "F"

    a += str(zvysok)
    cislo = cislo // 16
  return a[::-1]

def hex2dec(cislo):
  cislo = cislo[::-1]
  sucet = 0
  exp = 0
  for i in cislo:
    if i == "A":
      sucet += 10 * 16**exp
    elif i == "B":
      sucet += 11 * 16**exp
    elif i == "C":
      sucet += 12 * 16**exp
    elif i == "D":
      sucet += 13 * 16**exp
    elif i == "E":
      sucet += 14 * 16**exp
    elif i == "F":
      sucet += 15 * 16**exp
    else:
      sucet += int(i) * 16**exp
    exp += 1
  return sucet

def dec2hex_color(color):
  red, green, blue = color
  r = dec2hex(red)
  if len(r) < 2:
    r = "0" + r
  g = dec2hex(green)
  if len(g) < 2:
    g = "0" + g
  b = dec2hex(blue)
  if len(b) < 2:
    b = "0" + b
  return f"#{r}{g}{b}"

def hex2dec_color(color):
  r = color[1:3]
  g = color[3:5]
  b = color[5:]
  return hex2dec(r), hex2dec(g), hex2dec(b)
def load_file_content(file):
  pole = []
  with open(file, "r") as f:
    for riadok in f:
      pole.append(riadok.split(" "))
  return pole
def kontrola(file):
  pole=load_file_content(file)
  if (pole[0][0]) != "VES":
    print("chyba formátu")
    return False
  elif (pole[0][1]) != "v1.0":
    print("error(zlá verzia)")
    return False
  else:
    return True
def picture(file):
  pole=load_file_content(file)
  if width/height != (int(pole[0][2]))/int((pole[0][3])):
    print("zadal si zle rozlisenie")
  else:
    pass
  from PIL import Image
  color = "white"
  img = Image.new("RGB", (width,height), color)
  for x in range(0,len(pole)):
    y=pole[x][0]
    if y=="CLEAR":
      FILL_RECT(img,(0,0),(width,height),hex2dec_color(pole[x][1].strip()))
    elif y=="FILL_CIRCLE":
      S=[int((int(pole[x][1]))*(width/(int(pole[0][2])))),int((int(pole[x][2]))*(height/(int(pole[0][3]))))]
      FILL_CIRCLE(img,S,(int(pole[x][3])*(width/(int(pole[0][2])))),hex2dec_color(pole[x][4].strip()))
    elif y=="FILL_RECT":
      A=[int((int(pole[x][1]))*(width/(int(pole[0][2])))),int((int(pole[x][2]))*(height/(int(pole[0][3]))))]
      B=[int((int(pole[x][3]))*(width/(int(pole[0][2])))),int((int(pole[x][4]))*(height/(int(pole[0][3]))))]
      FILL_RECT(img,A,B,hex2dec_color(pole[x][5].strip()))
    elif y=="FILL_TRIANGLE":
      A=[int((int(pole[x][1]))*(width/(int(pole[0][2])))),int((int(pole[x][2]))*(height/(int(pole[0][3]))))]
      B=[int((int(pole[x][3]))*(width/(int(pole[0][2])))),int((int(pole[x][4]))*(height/(int(pole[0][3]))))]
      C=[int((int(pole[x][5]))*(width/(int(pole[0][2])))),int((int(pole[x][6]))*(height/(int(pole[0][3]))))]
      FILL_TRIANGLE(img,A,B,C,hex2dec_color(pole[x][7].strip()))
    elif y=="CIRCLE":
      S=[int((int(pole[x][1]))*(width/(int(pole[0][2])))),int((int(pole[x][2]))*(height/(int(pole[0][3]))))]
      CIRCLE(img,S,int(int(pole[x][3])*(width/(int(pole[0][2])))),(int(pole[x][4])),hex2dec_color(pole[x][5].strip()))
    elif y=="RECT":
      A=[int((int(pole[x][1]))*(width/(int(pole[0][2])))),int((int(pole[x][2]))*(height/(int(pole[0][3]))))]
      B=[int((int(pole[x][3]))*(width/(int(pole[0][2])))),int((int(pole[x][4]))*(height/(int(pole[0][3]))))]
      RECT(img,A,B,int(int(pole[x][5])*(width/(int(pole[0][2])))),hex2dec_color(pole[x][6].strip()))
    elif y=="TRIANGLE":
      A=[int((int(pole[x][1]))*(width/(int(pole[0][2])))),int((int(pole[x][2]))*(height/(int(pole[0][3]))))]
      B=[int((int(pole[x][3]))*(width/(int(pole[0][2])))),int((int(pole[x][4]))*(height/(int(pole[0][3]))))]
      C=[int((int(pole[x][5]))*(width/(int(pole[0][2])))),int((int(pole[x][6]))*(height/(int(pole[0][3]))))]
      TRIANGLE(img,A,B,C,int(int(pole[x][7])*(width/(int(pole[0][2])))),hex2dec_color(pole[x][8].strip()))
    elif y=="LINE":
      A=[int((int(pole[x][1]))*(width/(int(pole[0][2])))),int((int(pole[x][2]))*(height/(int(pole[0][3]))))]
      B=[int((int(pole[x][3]))*(width/(int(pole[0][2])))),int((int(pole[x][4]))*(height/(int(pole[0][3]))))]
      LINE(img,A,B,int(int(pole[x][5])*(width/(int(pole[0][2])))),hex2dec_color(pole[x][6].strip()))
    else:
      pass

  display(img)
