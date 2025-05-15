**Note:**
- In Jupyter, command line arguments (`sys.argv[...]`) are replaced with variables or cell inputs.

- Execute each logic block in order, making sure that all dependencies and I/O paths are set up accordingly.

- Do not change the original logic or sequence; just adapt the way inputs are presented and outputs are handled for the notebook environment.

## Summary Table

| Script Name                  | Main Steps (in order)                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| FPEnhancer.py                | Import → Define enhancer → List .bmp files → Enhance & save images                                     |
| FPExtracter.py               | Import → Define extractor/classes → List .jpg files → Extract minutiae → Save results                  |
| FPHashCalculation.py         | Import → Define hash function → List .jpg files → Calculate hashes → Save to CSV                       |
| HammingDistanceComparison.py | Import → Define distance function → Read hash CSVs → Compute robustness/discrimination → Save to CSV   |
| Threshold.py                 | Import → Define threshold functions → Read Hamming CSVs → Analyze thresholds → Save to CSV             |
| FPOrientationMapExtractor.py | Import → Define orientation functions → List images → Extract/draw orientation maps                    |
