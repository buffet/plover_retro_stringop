# plover_retro_stringop

Call arbirary code on the last n words!
This is inheritly unsafe and horrible, yay!

Complaints go to **[[redacted]]@[[redacted]].com**.

### Usage

`{:retro_stringop:N:EXPR}`, where `N` is the number of words (backwards) to work on and `EXPR` is the expression that constitutes the new text.
This has `text` as the entire string and `words` as an array of the individual words (already stripped, use `raw_words` for words including the spaces).

`{:retro_stringop_sh:N:EXPR}` does the same stuff, but calls `/bin/sh`, and provides the text as `TEXT` env var.

### Examples

- `{:retro_stringop:1:"(" + text + ")"}`: surround last word in parenthesis
- `{:retro_stringop:2:"(" + text + ")"}`: surround last two words in parenthesis
- `{:retro_stringop_sh:1:echo "$TEXT" | tee some-file.txt}`: log last word to some-file.txt (tee is used here to so that the word doesn't get deleted)
- `{:retro_stringop:1:text[::-1]}`: reverse the last word
- `{:retro_stringop_sh:1:cat "$TEXT"}`: read the last word as a filename, and read that file, replacing the filename with the content
- `{:retro_stringop:3:"".join([w.lower().capitalize() for w in words])}`: PascalCase the last 3 words
