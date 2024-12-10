from pathlib import Path

def get_text(path_to_file: Path):
    with open(path_to_file) as fp:
        text = fp.read()
    return text

def main()->None:
    path_to_file = Path("books","frankenstein.txt")
    print(get_text(path_to_file))
    
if __name__=="__main__":
    main()
