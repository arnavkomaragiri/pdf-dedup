import re
import os
import typer
import shutil

from functools import reduce
from tqdm import tqdm
from pypdf import PdfReader
from typing import List, Dict

app = typer.Typer()
whitespace_pattern = re.compile(r'\s+')

def get_pdf_signature(file: str, remove_whitespace: bool = False) -> str:
    if not os.path.exists(file) or not os.path.isfile(file):
        raise ValueError(f"file {file} does not exist")
    reader = PdfReader(file)
    signature = reduce(lambda a, b: a + b, [p.extract_text() for p in reader.pages]).strip()
    if remove_whitespace:
        signature = re.sub(whitespace_pattern, "", signature)
    return signature

@app.command()
def dedup(path: str, unique_dir: str, remove_whitespace: bool = False, verbose: bool = False):
    assert os.path.exists(path), f"input path {path} does not exist"

    if not os.path.exists(unique_dir) or not os.path.isdir(unique_dir):
        os.mkdir(unique_dir)

    paths = []
    if os.path.isfile(path):
        paths = [path]
    else:
        paths = [
            os.path.join(path, p)
            for p in os.listdir(path) if p.endswith('.pdf')
        ]
    
    signatures: Dict[str, List[str]] = {}

    if verbose:
        paths = tqdm(paths, total=len(paths))

    for p in paths:
        sig = get_pdf_signature(p, remove_whitespace=remove_whitespace)
        if sig in signatures:
            if verbose:
                typer.echo(f"found duplicate files: {', '.join([p] + signatures[sig])}")
            signatures[sig] += [p]
        else:
            signatures[sig] = [p]
            shutil.copy2(p, unique_dir)

    # do any post-processing you'd like to here, shouldn't matter too much
    
    if verbose:
        typer.echo(f"found {len(signatures)} unique files")

if __name__ == "__main__":
    app()