set -eu
APP=single_page_python
NPM_DEST="src/$APP/npm"
if [ -d $NPM_DEST ] ; then
  rm $NPM_DEST/*  || echo "No files found in static folder"
else
  mkdir $NPM_DEST
fi

NPM_FILES="\
    bootstrap/dist/js/bootstrap.bundle.min.js \
    bootstrap/dist/css/bootstrap.min.css \

echo "Install npm dependencies"
npm ci
for dep in $NPM_FILES
do
  SRC="node_modules/$dep"
  echo "Copy $SRC to $NPM_DEST"
  cp  $SRC $NPM_DEST
done

echo "Install python dependencies"
python -m pip install -e '.[dev]'

echo "Building python wheel"
python -m build
