```latex
\mathrm{DELAY} =
\bigl( \mathrm{base}_{SF}
      + \mathrm{perByte}_{SF} \cdot L \bigr)
\cdot
\mathrm{bw\_scale}
\cdot
\mathrm{cr\_scale}
```


```latex
\mathrm{TOA}_{\mathrm{total}} =
\Bigl( \mathrm{base}_{SF}
     + \mathrm{slope}_{SF} \cdot L \Bigr)
\cdot \frac{500{,}000}{B}
\cdot \frac{CR}{8}
\;+\;
(p - 10)\,
\frac{2^{SF}}{B}\cdot 1000
```