# Math Books

## Milne's Course Notes PDF for Phone

This repo contains 2 course notes from
https://www.jmilne.org/math/CourseNotes/, formatted for phone screens.
All the credit and goes to the original author. I might have
introduced formatting problems, so please check the official PDF if
you encounter one.

- [Group Theory](https://github.com/YangZhao11/PhonePdf/releases/download/202301/GT.pdf)
- [Field and Galois Theory](https://github.com/YangZhao11/PhonePdf/releases/download/202301/FT.pdf)

The following adjustments are made:

- PDF size adjusted for phone screen
- Adjusted font to be more like sans-serif, for screen reading
- Shrank some diagrams
- Long formulas were broke into multiple lines.

### Licence

The oringinal source is released under Creative Commons CC BY-NC-SA
4.0 licence.

## Hatcher's Algebraic Topology
`AT_index.info` contains index for Hatcher's [Algebraic Topology](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html)
book. Use the following command to add this index to the pdf file:

```
gs -sDEVICE=pdfwrite -q -dBATCH -dNOPAUSE \
  -sOutputFile=AT_indexed.pdf AT_index.info -f AT.pdf
```

## Fulton's Algebraic Curves
PDF can be cropped using this command:
```
pdfcrop -bbox-even "140 105 540 700" -bbox-odd "80 105 480 700" CurveBook.pdf
```

We also have a `CurveBook_index.info` file to add index to this pdf
```
gs -sDEVICE=pdfwrite -q -dBATCH -dNOPAUSE \
  -sOutputFile=CurveBook_indexed.pdf CurveBook_index.info \
  -f CurveBook.pdf
```
