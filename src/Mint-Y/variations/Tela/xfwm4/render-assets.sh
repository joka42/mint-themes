#! /bin/bash

INKSCAPE="inkscape"
OPTIPNG="optipng"

SRC_FILE="assets.svg"
ASSETS_DIR="."

INDEX="assets.txt"

# check command avalibility
has_command() {
  "$1" -v $1 > /dev/null 2>&1
}

mkdir -p $ASSETS_DIR

for i in `cat $INDEX`
do
if ! [ -f $ASSETS_DIR/$i.png ]; then
    echo Rendering $ASSETS_DIR/$i.png

    $INKSCAPE --export-id=$i \
              --export-id-only \
              --export-png=$ASSETS_DIR/$i.png $SRC_FILE >/dev/null
    $OPTIPNG -o7 --quiet $ASSETS_DIR/$i.png
fi
done
exit 0
