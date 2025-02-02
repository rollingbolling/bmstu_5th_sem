$aux_dir = 'tmp';       # Папка для временных файлов

$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -shell-escape %O %S';

# Если вы используете xelatex
$xelatex = 'xelatex -synctex=1 -interaction=nonstopmode -shell-escape %O %S';

# Если вы используете lualatex
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -shell-escape %O %S';