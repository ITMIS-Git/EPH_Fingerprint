# Evaluation of Perceptual Hash Techniques for Biometric Fingerprint Authentication

### Fingerprint Image Enhancement, Thinning, and Minutiae Extraction Pipeline

This Jupyter notebook implements a pipeline for processing fingerprint images, including:
- **Enhancement** of raw fingerprint images
- **Thinning/Skeletonization** to obtain ridge structures
- **Extraction and visualization of minutiae points**
- In Jupyter, command line arguments (`sys.argv[...]`) are replaced with variables or cell inputs.
- Execute each logic block in order, making sure that all dependencies and I/O paths are set up accordingly.
- Do not change the original logic or sequence; just adapt the way inputs are presented and outputs are handled for the notebook environment.

**Note:** The code in this notebook was taken from source https://github.com/rn1357/PerceptualHashTechniques?tab=readme-ov-file.

## Summary Table

| Script Name                  | Main Steps (in order)                                                                                  |
|------------------------------|--------------------------------------------------------------------------------------------------------|
| FPEnhancer.py                | Import → Define enhancer → List .bmp files → Enhance & save images                                     |
| FPOrientationMapExtractor.py | Import → Define orientation functions → List images → Extract/draw orientation maps                    |
| FPExtracter.py               | Import → Define extractor/classes → List .jpg files → Extract minutiae → Save results                  |
| FPHashCalculation.py         | Import → Define hash function → List .jpg files → Calculate hashes → Save to CSV                       |
| HammingDistanceComparison.py | Import → Define distance function → Read hash CSVs → Compute robustness/discrimination → Save to CSV   |
| Threshold.py                 | Import → Define threshold functions → Read Hamming CSVs → Analyze thresholds → Save to CSV             |

### Fingerprint Perceptual Hashing and Hamming Distance Analysis

This Jupyter notebook implements a pipeline for computing perceptual hashes of fingerprint images using multiple hashing techniques (average_hash, phash, dhash, whash), calculating Hamming distances between genuine and impostor fingerprint sets, and generating probability tables based on Hamming distance thresholds. 

The code automates the process of:

- Reading fingerprint images from specified folders,
- Computing and saving image hashes,
- Calculating pairwise Hamming distances for similarity analysis,
- Producing frequency tables of similarity probabilities at various thresholds.

This notebook is intended for fingerprint verification and image similarity analysis tasks.

**Note:** The code in this notebook was taken from source https://github.com/JohannesBuchner/imagehash.
