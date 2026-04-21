from random import randint

from PIL import Image


def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)


def render_ves(ves_source, width):
  parsed_width = _safe_int(width, 640)
  commands = _parse_ves_source(ves_source)

  if not commands:
    fallback_height = max(round(parsed_width * 0.625), 1)
    return Image.new('RGB', (max(parsed_width, 1), fallback_height), (255, 255, 255))

  _, _, source_width, source_height = commands[0]
  if source_width <= 0 or source_height <= 0:
    raise ValueError('Neplatna velkost platna vo VES hlavicke.')

  target_width = max(parsed_width, 1)
  target_height = max(round(source_height * (target_width / source_width)), 1)
  img = Image.new('RGB', (target_width, target_height), (255, 255, 255))

  scale_x = target_width / source_width
  scale_y = target_height / source_height

  for command in commands[1:]:
    operation = command[0]
    args = command[1:]

    if operation == "CLEAR":
      FILL_RECT(img, (0, 0), (target_width, target_height), _parse_color(args[0]))
    elif operation == "FILL_CIRCLE":
      center = _scale_point(args[0], args[1], scale_x, scale_y)
      radius = _scale_scalar(args[2], scale_x, scale_y)
      FILL_CIRCLE(img, center, radius, _parse_color(args[3]))
    elif operation == "FILL_RECT":
      point = _scale_point(args[0], args[1], scale_x, scale_y)
      size = _scale_size(args[2], args[3], scale_x, scale_y)
      FILL_RECT(img, point, size, _parse_color(args[4]))
    elif operation == "FILL_TRIANGLE":
      a = _scale_point(args[0], args[1], scale_x, scale_y)
      b = _scale_point(args[2], args[3], scale_x, scale_y)
      c = _scale_point(args[4], args[5], scale_x, scale_y)
      FILL_TRIANGLE(img, a, b, c, _parse_color(args[6]))
    elif operation == "CIRCLE":
      center = _scale_point(args[0], args[1], scale_x, scale_y)
      radius = _scale_scalar(args[2], scale_x, scale_y)
      thickness = max(_scale_thickness(args[3], scale_x, scale_y), 1)
      CIRCLE(img, center, radius, thickness, _parse_color(args[4]))
    elif operation == "RECT":
      point = _scale_point(args[0], args[1], scale_x, scale_y)
      size = _scale_size(args[2], args[3], scale_x, scale_y)
      thickness = max(_scale_thickness(args[4], scale_x, scale_y), 1)
      RECT(img, point, size, thickness, _parse_color(args[5]))
    elif operation == "TRIANGLE":
      a = _scale_point(args[0], args[1], scale_x, scale_y)
      b = _scale_point(args[2], args[3], scale_x, scale_y)
      c = _scale_point(args[4], args[5], scale_x, scale_y)
      thickness = max(_scale_thickness(args[6], scale_x, scale_y), 1)
      TRIANGLE(img, a, b, c, thickness, _parse_color(args[7]))
    elif operation == "LINE":
      a = _scale_point(args[0], args[1], scale_x, scale_y)
      b = _scale_point(args[2], args[3], scale_x, scale_y)
      thickness = max(_scale_thickness(args[4], scale_x, scale_y), 1)
      LINE(img, a, b, thickness, _parse_color(args[5]))

  return img


def get_line_pixels(img, A, B):
  pixels = []
  width, height = img.size

  if A[0] == B[0]:
    if A[1] > B[1]:
      A, B = B, A
    for y in range(A[1], B[1] + 1):
      x = A[0]
      if not (x < 0 or y < 0 or x >= width or y >= height):
        pixels.append((x, y))
  elif A[1] == B[1]:
    if A[0] > B[0]:
      A, B = B, A
    for x in range(A[0], B[0] + 1):
      y = A[1]
      if not (x < 0 or y < 0 or x >= width or y >= height):
        pixels.append((x, y))
  else:
    if A[0] > B[0]:
      A, B = B, A
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dy / dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
        x = int((y - A[1] + (dy / dx) * A[0]) * (dx / dy))
        if not (x < 0 or y < 0 or x >= width or y >= height):
          pixels.append((x, y))
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
        y = int((B[1] - A[1]) / (B[0] - A[0]) * (x - A[0]) + A[1])
        if not (x < 0 or y < 0 or x >= width or y >= height):
          pixels.append((x, y))

  return pixels


def draw_line(img, A, B, color):
  width, height = img.size

  if A[0] == B[0]:
    if A[1] > B[1]:
      A, B = B, A
    for y in range(A[1], B[1] + 1):
      x = A[0]
      if not (x < 0 or y < 0 or x >= width or y >= height):
        img.putpixel((x, y), color)
  elif A[1] == B[1]:
    if A[0] > B[0]:
      A, B = B, A
    for x in range(A[0], B[0] + 1):
      y = A[1]
      if not (x < 0 or y < 0 or x >= width or y >= height):
        img.putpixel((x, y), color)
  else:
    if A[0] > B[0]:
      A, B = B, A
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dy / dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
        x = int((y - A[1] + (dy / dx) * A[0]) * (dx / dy))
        if not (x < 0 or y < 0 or x >= width or y >= height):
          img.putpixel((x, y), color)
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
        y = int((B[1] - A[1]) / (B[0] - A[0]) * (x - A[0]) + A[1])
        if not (x < 0 or y < 0 or x >= width or y >= height):
          img.putpixel((x, y), color)


def FILL_CIRCLE(img, S, r, colour):
  for x in range(0, int(r / 2 ** (1 / 2)) + 1):
    y = int((r ** 2 - x ** 2) ** (1 / 2))
    draw_line(img, (x + S[0], y + S[1]), (x + S[0], -y + S[1]), colour)
    draw_line(img, (y + S[0], x + S[1]), (y + S[0], -x + S[1]), colour)
    draw_line(img, (-x + S[0], -y + S[1]), (-x + S[0], y + S[1]), colour)
    draw_line(img, (-y + S[0], -x + S[1]), (-y + S[0], x + S[1]), colour)


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

  for x, y in pixels:
    if y > ymax or y < ymin:
      continue
    if x < xmin[y]:
      xmin[y] = x
    if x > xmax[y]:
      xmax[y] = x

  for y in range(ymin, ymax + 1):
    if xmin[y] <= xmax[y]:
      draw_line(img, (xmin[y], y), (xmax[y], y), colour)


def FILL_RECT(img, A, B, colour):
  ax, ay = A
  width, height = B
  bx, by = ax + width, ay + height

  if ax < bx and ay > by:
    ay, by = by, ay
  elif ax > bx and ay > by:
    ax, bx = bx, ax
    ay, by = by, ay
  elif ax > bx and ay < by:
    ax, bx = bx, ax

  for x in range(ax, bx):
    for y in range(ay, by):
      if not (x < 0 or y < 0 or x >= img.width or y >= img.height):
        img.putpixel((x, y), colour)


def LINE(img, A, B, thickness, colour):
  radius = max(round(thickness / 2), 1)
  for point in get_line_pixels(img, A, B):
    FILL_CIRCLE(img, point, radius, colour)


def TRIANGLE(img, A, B, C, thickness, colour):
  LINE(img, A, B, thickness, colour)
  LINE(img, A, C, thickness, colour)
  LINE(img, B, C, thickness, colour)


def RECT(img, A, B, thickness, colour):
  ax, ay = A
  w, h = B
  bx, by = ax + w, ay + h

  if ax > bx:
    ax, bx = bx, ax
  if ay > by:
    ay, by = by, ay

  LINE(img, (ax, ay), (bx, ay), thickness, colour)
  LINE(img, (bx, ay), (bx, by), thickness, colour)
  LINE(img, (ax, ay), (ax, by), thickness, colour)
  LINE(img, (ax, by), (bx, by), thickness, colour)


def CIRCLE(img, S, r, thickness, colour):
  for x in range(0, int(r / (2 ** 0.5)) + 1):
    y = int((r ** 2 - x ** 2) ** 0.5)
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
      sucet += 10 * 16 ** exp
    elif i == "B":
      sucet += 11 * 16 ** exp
    elif i == "C":
      sucet += 12 * 16 ** exp
    elif i == "D":
      sucet += 13 * 16 ** exp
    elif i == "E":
      sucet += 14 * 16 ** exp
    elif i == "F":
      sucet += 15 * 16 ** exp
    else:
      sucet += int(i) * 16 ** exp
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


def _safe_int(value, default):
  try:
    return int(value)
  except (TypeError, ValueError):
    return default


def _parse_ves_source(ves_source):
  if ves_source is None:
    raise ValueError("VES subor chyba.")

  commands = []
  lines = []
  for raw_line in ves_source.splitlines():
    line = raw_line.strip()
    if not line or line.startswith("#"):
      continue
    lines.append(line)

  if not lines:
    return commands

  header = lines[0].split()
  if len(header) != 4 or header[0] != "VES" or header[1] != "v1.0":
    raise ValueError("VES subor musi zacinat hlavickou: VES v1.0 sirka vyska")

  try:
    commands.append(("VES", "v1.0", int(header[2]), int(header[3])))
  except ValueError as error:
    raise ValueError("Sirka a vyska vo VES hlavicke musia byt cisla.") from error

  command_specs = {
    "CLEAR": (1,),
    "FILL_CIRCLE": (4,),
    "FILL_RECT": (5,),
    "FILL_TRIANGLE": (7,),
    "CIRCLE": (4, 5),
    "RECT": (5, 6),
    "TRIANGLE": (7, 8),
    "LINE": (4, 6),
  }

  for line in lines[1:]:
    parts = line.split()
    operation = parts[0]
    allowed_args = command_specs.get(operation)

    if allowed_args is None:
      raise ValueError(f"Nepodporovany prikaz: {operation}")
    if len(parts) - 1 not in allowed_args:
      raise ValueError(f"Prikaz {operation} ma zly pocet argumentov.")

    commands.append(tuple(_normalize_command(parts)))

  return commands


def _normalize_command(parts):
  operation = parts[0]

  if operation == "LINE" and len(parts) == 6:
    return parts
  if operation == "LINE" and len(parts) == 5:
    return parts[:-1] + ["1", parts[-1]]

  if operation in {"CIRCLE", "RECT", "TRIANGLE"} and len(parts) in {6, 7, 9}:
    return parts
  if operation in {"CIRCLE", "RECT", "TRIANGLE"}:
    return parts[:-1] + ["1", parts[-1]]

  return parts


def _scale_point(x, y, scale_x, scale_y):
  return (round(int(x) * scale_x), round(int(y) * scale_y))


def _scale_size(width, height, scale_x, scale_y):
  return (round(int(width) * scale_x), round(int(height) * scale_y))


def _scale_scalar(value, scale_x, scale_y):
  return max(round(int(value) * ((scale_x + scale_y) / 2)), 1)


def _scale_thickness(value, scale_x, scale_y):
  return _scale_scalar(value, scale_x, scale_y)


def _parse_color(value):
  if not isinstance(value, str) or len(value) != 7 or not value.startswith("#"):
    raise ValueError(f"Neplatna farba: {value}")
  return hex2dec_color(value.upper())
