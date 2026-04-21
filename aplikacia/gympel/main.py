from io import BytesIO
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
PACKAGES_DIR = BASE_DIR / '.packages'

if PACKAGES_DIR.is_dir():
  sys.path.insert(0, str(PACKAGES_DIR))

from flask import Flask, abort, request, send_file, send_from_directory

try:
  from .ves import render_ves
except ImportError:
  from ves import render_ves

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
PUBLIC_DIR = BASE_DIR / 'public'
SAMPLES_DIR = PUBLIC_DIR / 'samples'


def serve_pil_image(img):
  """
    Tato funkcia umozni obrazok z kniznice PIL ulozit do virtualneho suboru v pamati a ten subor potom vratit ako HTTP odpoved
  """
  img_io = BytesIO()
  img.save(img_io, 'PNG', quality=70)
  img_io.seek(0)
  return send_file(img_io, mimetype='image/png')



@app.route('/sample/<name>')
def sample(name):
  sample_file = SAMPLES_DIR / f'{name}.txt'
  if not sample_file.is_file():
    abort(404, description='Pozadovana ukazka neexistuje.')

  return send_from_directory(SAMPLES_DIR, sample_file.name, mimetype='text/plain')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  """
    Tato funkcia bude odpovedat na vsetky ostatne HTTP poziadavky, pre ktore nemame specialnu funkciu. Bude hladat subory v priecinku public.
  """
  if (len(path) == 0): # ak nezadany ziaden subor, teda cesta / chceme index.html
    return send_from_directory(PUBLIC_DIR, 'index.html')

  return send_from_directory(PUBLIC_DIR, path)


@app.route('/render', methods=['post'])
def render():
  """
    Tato funkcia dostane v HTTP poziadavke zdrojovy kod pre VES a pozadovanu sirku, vyrenderuje obrazok a vrati ho ako HTTP odpoved
  """
  ves = request.form.get('ves', '') # nacitanie hodnoty ktoru sme dostali v poziadavke
  width = request.form.get('width', 640) # nacitanie hodnoty ktoru sme dostali v poziadavke

  try:
    img = render_ves(ves, width)
  except ValueError as error:
    return str(error), 400

  return serve_pil_image(img) # vratime vyrenderovany obrazok ako png


if __name__ == '__main__':
  app.run(debug=True)
