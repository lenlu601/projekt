# VES Renderer

Single-page aplikacia postavena na `HTML + CSS + JavaScript + Flask`.

Pouzivatel:
- vlozi obsah `.ves` suboru do textoveho pola,
- alebo klikne na jednu z pripravenych vzoriek,
- stlaci tlacidlo a backend vrati PNG obrazok.

## Spustenie lokalne

Vsetko rob v tomto repozitari na svojom branche, napr. `rebeka_vzorky`, aby si nemenila `master`.

### Windows PowerShell

Ak je projekt v OneDrive priecinku a `python -m venv .venv` zlyha, pouzi samostatne virtualne prostredie mimo projektu:

```powershell
C:\Users\rebek\venvs\aplikacia-rebeka_vzorky\Scripts\Activate.ps1
python gympel\main.py
```

Ak to prostredie este neexistuje, vytvoris ho takto:

```powershell
py -m venv C:\Users\rebek\venvs\aplikacia-rebeka_vzorky
C:\Users\rebek\venvs\aplikacia-rebeka_vzorky\Scripts\python.exe -m pip install -r requirements.txt
```

Potom otvor v prehliadaci:

```text
http://127.0.0.1:5000
```

## Git workflow

Ak chces poslat zmeny spoluziakom:

```powershell
git checkout rebeka_vzorky
git add .
git commit -m "Pridane vzorky a GUI pre VES renderer"
git push -u origin rebeka_vzorky
```

Potom na GitHube vytvor Pull Request z `rebeka_vzorky` do cielovej vetvy.
