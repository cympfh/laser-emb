import os.path

import fastBPE
import MeCab

from .embed import SentenceEncoder


class Laser:

    def __init__(self):
        dirname = os.path.dirname(__file__)
        mecab = MeCab.Tagger('-Owakati')
        mecab.parse('')
        self.mecab = mecab
        codes_path = os.path.join(dirname, '93langs.fcodes')
        vocab_path = os.path.join(dirname, '93langs.fvocab')
        self.bpe = fastBPE.fastBPE(codes_path, vocab_path)
        model_path = os.path.join(dirname, 'bilstm.93langs.2018-12-26.pt')
        self.enc = SentenceEncoder(model_path)

    def apply(self, sentences, lang=None):
        if lang in ('ja', 'jp', 'jpn'):
            sentences = [self.mecab.parse(sentence).strip() for sentence in sentences]
        sentences = self.bpe.apply(sentences)
        return self.enc.encode_sentences(sentences)
