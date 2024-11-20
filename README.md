# PDF Deduper
Just a PDF deduper.

## Usage:
### Installation:
If using Poetry:
```bash
poetry install
```
If using other venv:
```bash
pip install -r requirements.txt
```

### Running Deduplication
The template to use this script is as such:
```bash
python pdf_dedup/dedup.py \
    [INSERT SOURCE FILE/DIR] \
    [INSERT OUTPUT UNIQUE FILE DIR] 
    [--remove-whitespace if removing whitespaces before comparing] \
    [--verbose if you want cool logs]
```
An example usage could be:
```bash
python pdf_dedup/dedup.py files/ unique_files --remove-whitespace --verbose
```

## Support:
If you want help with this either text/call me or figure it out yourself. It's one script, it cant be that hard.