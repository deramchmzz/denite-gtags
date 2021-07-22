import os
import sys

sys.path.insert(1, os.path.dirname(__file__))
from denite_gtags import TagsBase  # pylint: disable=locally-disabled, wrong-import-position

from denite import util

class Source(TagsBase):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'gtags_ref'
        self.kind = 'file'

    def get_search_flags(self):
        return [['-rs', '--result=ctags-mod']]

    def convert_to_candidates(self, tags):
        candidates = []
        for tag in tags:
            path, line, text = self._parse_tag(tag)
            col = text.find(text) - 1
            candidates.append({
                'word': '{0}:{1};{2}'.format(util.abspath(self.vim, path), line, text),
                'action__path': path,
                'action__line': line,
                'action__text': text,
                'action__col': col
            })
        return candidates
