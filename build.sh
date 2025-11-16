set -eu
APP=single_page_python
STATIC_DIR="src/$APP/static"
if [ -d $STATIC_DIR ] ; then
  rm $STATIC_DIR/*  || echo "No files found in static folder"
else
  mkdir $STATIC_DIR
fi

NPM_DEPS="\
    bootstrap/dist/js/bootstrap.bundle.min.js \
    bootstrap/dist/css/bootstrap.min.css \
    bootstrap/dist/css/bootstrap.min.map"

echo "Install npm dependencies"
npm ci
for dep in $NPM_DEPS
do
  SRC="node_modules/$dep"
  echo "Copy $SRC to $STATIC_DIR"
  cp  $SRC $STATIC_DIR
done

echo "Install python dependencies"
python -m pip install -e '.[dev]'

echo "Building python wheel"
python -m build
