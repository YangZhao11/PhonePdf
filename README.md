# Math Books

This repo includes some info on cropping / formatting math PDF books
for reading on Phone / ebook reader type of devices.

## Milne's Course Notes PDF for Phone

The author of Group theory and field and Galois theory book (course notes) from
https://www.jmilne.org/math/CourseNotes/ has published the tex files,
so I made some formatting change and generated PDFs for Phones and Kindle.
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

## Tools

### podofo
podofobox can be used to modify the bounding box of a PDF file. It
works nicely to crop out the margins of some files, so you can have
larger text on an e-reader or tablet device. Something like this would
work:

```
podofobox original.pdf crop.pdf media 5000 5300 34000 58000
```
Unfortunately podofobox does not support different bounding box for
even and odd pages separately.

### pdfcpu
A similar command line to add media bounding box:

```
pdfcpu boxes add -- "media:[50 53 390 633]" original.pdf crop.pdf
```
