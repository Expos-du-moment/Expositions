"""Construit site/ (publié par GitHub Pages) : l'application et sa base d'expositions."""
import pathlib, shutil

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "site"

if __name__ == "__main__":
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(HERE / "app", OUT)
    shutil.copy2(HERE / "data" / "expositions.json", OUT / "expositions.json")
    (OUT / ".nojekyll").write_text("")
    print(f"Expos du moment -> {OUT}")
