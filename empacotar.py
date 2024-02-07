from zipfile import ZipFile

import os
import pathlib

IGNORE = ['.env', '.venv', 'dist', '.git', '.gitignore', 'empacotar.py']


def main():
    dir_dist = pathlib.Path("./dist")
    if not os.path.exists(dir_dist):
        os.makedirs(dir_dist)

    with ZipFile('./dist/suporte-console.zip', 'w') as zip:

        for root, _, files in os.walk("./"):
            pula = False
            for ignore in IGNORE:
                if root[2:].startswith(ignore):
                    pula = True
                    break

            if pula:
                continue

            root_zip = root

            for file in files:
                if file in IGNORE:
                    continue

                zip.write(
                    os.path.join(root, file),
                    os.path.join(root_zip, file)
                )

        # zip.write("./src/__main__.py", "__main__.py")


if __name__ == "__main__":
    main()
