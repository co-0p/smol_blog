# Aggressively Small Blog

This is the c0_0p.io website and blog. Lots to do!

The `build.py` script will take the files located in `src` and subdirectories and generate recursively the final .html files inside the `build` directory. Any html file that is not called `template.html` will end up as an output file nested inside any and all of it's parent `template.html` files.

The `<replace/>` tag inside the `template.html` files is replaced recursively either with depper `template.html` files or the final content html files/

## To Build Site
Run `python build.py` from the root project directory. You must do this after every change.

## To View Site
- Either open the built html files in the browser (links may be broken)
- Or `cd build` and run `python3 -m http.server 8000` to view pages with working links

