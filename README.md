# LASER-embeddings for 日本語/英語

An interface for [facebookresearch/LASER](https://github.com/facebookresearch/LASER)

## Requirements

- mecab
    - Install `https://github.com/taku910/mecab`
    - and `mecab-python3`
- fastBPE
    - Install `https://github.com/glample/fastBPE`
    - and run `pip install .` (Python binding)

## Install

Run `make install`.
The models are downloaded from LASER's repository.

## Usage

```
In [1]: import laserEmb

In [2]: laser = laserEmb.Laser()
Loading vocabulary from .../laserEmb/93langs.fvocab ...
Read 2369862597 words (73636 unique) from vocabulary file.
Loading codes from .../laserEmb/93langs.fcodes ...
Read 50000 codes from the codes file.

In [3]: laser.apply(['こんにちわ'], lang='ja')
Out[3]:
array([[ 0.00085875,  0.00056912, -0.00141654, ...,  0.00085222,
        -0.00292836, -0.00184826]], dtype=float32)

In [4]: laser.apply(['Hi'], lang='en')
Out[4]:
array([[ 1.5956871e-02, -4.5510857e-05,  2.1781763e-03, ...,
         9.3557676e-03, -2.5163505e-03,  2.2534702e-02]], dtype=float32)
```
