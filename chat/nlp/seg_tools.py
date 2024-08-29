from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.constants import TEXT
import jieba
from typing import Any, Text, Dict, List

class JiebaTokenizer(Tokenizer):
    provides = [TEXT]

    def tokenize(self, message: Message, attribute: Text) -> List[Token]:
        text = message.get(attribute)
        tokens = jieba.lcut(text)
        running_offset = 0
        return [
            Token(t, running_offset)
            for t in tokens
            for running_offset in range(running_offset, len(t) + running_offset)
        ]