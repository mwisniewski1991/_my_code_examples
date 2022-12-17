from os import chdir
from pathlib import Path

def main_basic() -> None:
    print('-- -- --')
    print(f'Current directory: {Path.cwd()}')
    print(f'Home directory: {Path.home()}')

    path: Path = Path(r'D:\_data.web\__roadmap') 
    print(f'Path existed?:{path.exists()}')

    path: Path = Path(r'D:\_data.web\__roadmap') / "Python" / "Standard Libraries"
    print(f'Path existed?:{path.exists()}')

    with Path(r'D:\_data.web\__roadmap') / "Python" / "Standard Libraries" / "Pathlib" / "settings.yaml" as file:
        print('Read text')
        print(file.read_text())

def main_advanced() -> None:
    print('-- -- --')
    with Path("settings.yaml") as path:
        print('File text')
        print(path.read_text())

        print(f'Resolve: {path.resolve()}') #absolute path

        full_path = path.resolve()
        print(f'Parent: {full_path.parent}')
        print(f'Grand Parent: {full_path.parent.parent}')
        print(f'Path name: {full_path.name}')
        print(f'Path name no extension: {full_path.stem}')

def main_advanced_is_sth() -> None:
    print('-- -- --')
    with Path("settings.yaml") as file_path:
        full_path = file_path.resolve()
        print(f'Is folder {full_path.is_dir()}')
        print(f'Is file {full_path.is_file()}')

def main_creating_file() -> None:
    print('-- -- --')
    new_file: Path =  Path.cwd() / "new_file.txt"
    print(f'Path cwd: {new_file}')
    print(f'Is exists?: {new_file.exists()}')

    new_file.touch()
    new_file.write_text("Text")
    print(f'Is exists?: {new_file.exists()}')

    new_file.unlink() #removing file
    print(f'Is exists?: {new_file.exists()}')


def main_creating_directory() -> None:
    print('-- -- --')
    new_dir: Path = Path.cwd() / "new_dir"

    new_dir.mkdir()

    # print(f'Old Path cwd: {Path.cwd()}')
    # chdir(new_dir) #changing working directory
    # print(f'New Path cwd: {Path.cwd()}')

    new_dir.rmdir()
    

if __name__ == "__main__":
    main_basic()
    main_advanced()
    main_advanced_is_sth()
    main_creating_file()
    main_creating_directory()