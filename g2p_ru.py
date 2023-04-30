class Consonant:
    def __init__(self, nh=None, dh=None, vh=None, ns=None, ds=None, vs=None):
        self.forms = dict(
            # normal, deaf and voiced x soft and hard
            n_hard=nh, d_hard=dh, v_hard=vh, n_soft=ns, d_soft=ds, v_soft=vs
        )


class Vocal:
    def __init__(self, c1=None, c2=None, c3=None, c4=None, c5=None, c6=None, c7=None, c8=None):
        self.forms = dict(
            case1=c1, case2=c2, case3=c3, case4=c4, case5=c5, case6=c6, case7=c7, case8=c8
        )


class Phonetics:
    def __init__(self):
        self.vocals_phonemes = {'U0', 'U', 'O0', 'O', 'A0', 'A', 'E0', 'E', 'Y0', 'Y', 'I0', 'I',
                                'U0l', 'Ul', 'O0l', 'Ol', 'A0l', 'Al', 'E0l', 'El', 'Y0l', 'Yl', 'I0l', 'Il'}

        self.voiced_weak_phonemes = {'J0', 'V0', 'V', 'N0', 'N', 'L0', 'L', 'M0', 'M', 'R0', 'R',
                                     'J0l', 'V0l', 'Vl', 'N0l', 'Nl', 'L0l', 'Ll', 'M0l', 'Ml', 'R0l', 'Rl'}

        self.voiced_strong_phonemes = {'B', 'B0', 'G', 'G0', 'D', 'D0', 'Z', 'Z0', 'ZH', 'ZH0',
                                       'GH', 'GH0', 'DZ', 'DZ0', 'DZH', 'DZH0',
                                       'Bl', 'B0l', 'Gl', 'G0l', 'Dl', 'D0l', 'Zl', 'Z0l', 'ZHl', 'ZH0l',
                                       'GHl', 'GH0l', 'DZl', 'DZ0l', 'DZHl', 'DZH0l'}

        self.deaf_phonemes = {'K', 'K0', 'P', 'P0', 'S', 'S0', 'T', 'T0', 'F', 'F0', 'KH', 'KH0',
                              'TS', 'TS0', 'TSH', 'TSH0', 'SH', 'SH0',
                              'Kl', 'K0l', 'Pl', 'P0l', 'Sl', 'S0l', 'Tl', 'T0l', 'Fl', 'F0l', 'KHl', 'KH0l',
                              'TSl', 'TS0l', 'TSHl', 'TSH0l', 'SHl', 'SH0l'}

        self.russian_phonemes_set = self.vocals_phonemes | self.voiced_weak_phonemes |\
                                    self.voiced_strong_phonemes | self.deaf_phonemes | {'sil'}

        self.all_russian_letters = {'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
                                    'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
                                    'я', 'h', 'z', 'j', 'g', 'd', 't', 'x', 's'}

        self.hard_and_soft_signs = {'ъ', 'ь'}

        self.vocals = {'а', 'о', 'у', 'э', 'ы', 'и', 'я', 'ё', 'ю', 'е', 'а+', 'о+', 'у+', 'э+', 'ы+', 'и+', 'я+',
                       'ё+', 'ю+', 'е+'}

        self.double_vocals = {'е', 'ё', 'ю', 'я', 'е+', 'ё+', 'ю+', 'я+'}

        # назвать получше
        self.gen_vocals_hard = {'ъ', 'а', 'о', 'у', 'э', 'ы', 'а+', 'о+', 'у+', 'э+', 'ы+'}
        self.gen_vocals_soft = {'ь', 'я', 'ё', 'ю', 'е', 'и', 'я+', 'ё+', 'ю+', 'е+', 'и+'}

        self.consonants = {'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц',
                           'ч', 'ш', 'щ', 'h', 'z', 'j', 'g', 'd', 't', 'x', 's'}

        # парные по звонкости согласные
        self.pair_consonants = {'б', 'в', 'г', 'д', 'ж', 'з', 'к', 'п', 'с', 'т', 'ф', 'ш', 'h', 'х',
                                'z', 'ц', 'j', 'ч', 'g', 'щ'}

        self.hardsoft_consonants = {'б', 'в', 'г', 'д', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'h', 'х'}
        self.hard_consonants = {'ж', 'ш', 'ц', 'x', 's', 'z'}
        self.soft_consonants = {'й', 'ч', 'щ', 'g', 'j', 'd', 't'}



class ModernMode(Phonetics):
    def __init__(self):
        Phonetics.__init__(self)
        self.TableG2P = {
            'й': Consonant('J0', 'J0', 'J0', 'J0', 'J0', 'J0'),

            'л': Consonant('L', 'L', 'L', 'L0', 'L0', 'L0'),
            'м': Consonant('M', 'M', 'M', 'M0', 'M0', 'M0'),
            'н': Consonant('N', 'N', 'N', 'N0', 'N0', 'N0'),
            'р': Consonant('R', 'R', 'R', 'R0', 'R0', 'R0'),

            'б': Consonant('B', 'P', 'B', 'B0', 'P0', 'B0'),
            'п': Consonant('P', 'P', 'B', 'P0', 'P0', 'B0'),

            'в': Consonant('V', 'F', 'V', 'V0', 'F0', 'V0'),
            'ф': Consonant('F', 'F', 'V', 'F0', 'F0', 'V0'),

            'г': Consonant('G', 'K', 'G', 'G0', 'K0', 'G0'),
            'к': Consonant('K', 'K', 'G', 'K0', 'K0', 'G0'),

            'h': Consonant('GH', 'KH', 'GH', 'GH0', 'KH0', 'GH0'),  # боh, аhа, буhалте
            'х': Consonant('KH', 'KH', 'GH', 'KH0', 'KH0', 'GH0'),

            'д': Consonant('D', 'T', 'D', 'D0', 'T0', 'D0'),
            'т': Consonant('T', 'T', 'D', 'T0', 'T0', 'D0'),

            'з': Consonant('Z', 'S', 'Z', 'Z0', 'S0', 'Z0'),
            'с': Consonant('S', 'S', 'Z', 'S0', 'S0', 'Z0'),

            'ж': Consonant('ZH', 'SH', 'ZH', 'ZH', 'SH', 'ZH'),
            'ш': Consonant('SH', 'SH', 'ZH', 'SH', 'SH', 'ZH'),

            'z': Consonant('DZ', 'TS', 'DZ', 'DZ', 'TS', 'DZ'),  # zета, Zагоев
            'ц': Consonant('TS', 'TS', 'DZ', 'TS', 'TS', 'DZ'),

            'j': Consonant('DZH0', 'TSH0', 'DZH0', 'DZH0', 'TSH0', 'DZH0'),
            'ч': Consonant('TSH0', 'TSH0', 'DZH0', 'TSH0', 'TSH0', 'DZH0'),

            'g': Consonant('ZH0', 'SH0', 'ZH0', 'ZH0', 'SH0', 'ZH0'),  # доggи, приеggа
            'щ': Consonant('SH0', 'SH0', 'ZH0', 'SH0', 'SH0', 'ZH0'),

            'd': Consonant('DZ0', 'TS0', 'DZ0', 'DZ0', 'TS0', 'DZ0'),  # Dюба
            't': Consonant('TS0', 'TS0', 'DZ0', 'TS0', 'TS0', 'DZ0'),

            'x': Consonant('DZH', 'TSH', 'DZH', 'DZH', 'TSH', 'DZH'),  # маxонг, Xек
            's': Consonant('TSH', 'TSH', 'DZH', 'TSH', 'TSH', 'DZH'),  # поsтанники

            # считаем, что J0 уже добавили, где нужно
            'ё+': Vocal('O0', 'O0', 'O0', 'O0', 'O0', 'O0', 'O0', 'O0'),
            'ю+': Vocal('U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0'),
            'я+': Vocal('A0', 'A0', 'A0', 'A0', 'A0', 'A0', 'A0', 'A0'),
            'е+': Vocal('E0', 'E0', 'E0', 'E0', 'E0', 'E0', 'E0', 'E0'),

            'о+': Vocal('O0', 'O0', 'O0', 'O0', 'O0', 'O0', 'O0', 'O0'),
            'у+': Vocal('U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0'),
            'а+': Vocal('A0', 'A0', 'A0', 'A0', 'A0', 'A0', 'A0', 'A0'),
            'э+': Vocal('E0', 'E0', 'E0', 'E0', 'E0', 'E0', 'E0', 'E0'),
            'ы+': Vocal('Y0', 'Y0', 'Y0', 'Y0', 'Y0', 'Y0', 'Y0', 'Y0'),
            'и+': Vocal('I0', 'I0', 'I0', 'I0', 'Y0', 'Y0', 'I0', 'I0'),

            'ё': Vocal('O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'),
            'ю': Vocal('U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'),
            'я': Vocal('A', 'I', 'A', 'I', 'A', 'Y', 'A', 'I'),
            'е': Vocal('I', 'I', 'I', 'I', 'Y', 'Y', 'I', 'I'),

            'о': Vocal('A', 'A', 'A', 'I', 'A', 'A', 'A', 'A'),
            'у': Vocal('U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'),
            'а': Vocal('A', 'A', 'A', 'I', 'A', 'A', 'A', 'A'),
            'э': Vocal('Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'),
            'ы': Vocal('Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'),
            'и': Vocal('I', 'I', 'I', 'I', 'Y', 'Y', 'I', 'I')
        }

    def rule_27(self, letters_list: list, next_phoneme: str, cur_pos: int) -> str:
        case = ''
        if letters_list[cur_pos] == 'н':
            if next_phoneme in {'J0', 'TSH0', 'SH0', 'DZH0', 'ZH0', 'D0', 'T0', 'Z0', 'S0'}:
                case = 'n_soft'
        elif letters_list[cur_pos] in {'с', 'з'}:
            if next_phoneme in {'D0', 'Z0'}:
                case = 'v_soft'
            elif next_phoneme in {'T0', 'S0'}:
                case = 'd_soft'
            elif next_phoneme in {'N0'}:
                case = 'n_soft'
        return case


class ClassicMode(Phonetics):
    def __init__(self):
        Phonetics.__init__(self)
        self.TableG2P = {
            'й': Consonant('J0', 'J0', 'J0', 'J0', 'J0', 'J0'),

            'л': Consonant('L', 'L', 'L', 'L0', 'L0', 'L0'),
            'м': Consonant('M', 'M', 'M', 'M0', 'M0', 'M0'),
            'н': Consonant('N', 'N', 'N', 'N0', 'N0', 'N0'),
            'р': Consonant('R', 'R', 'R', 'R0', 'R0', 'R0'),

            'б': Consonant('B', 'P', 'B', 'B0', 'P0', 'B0'),
            'п': Consonant('P', 'P', 'B', 'P0', 'P0', 'B0'),

            'в': Consonant('V', 'F', 'V', 'V0', 'F0', 'V0'),
            'ф': Consonant('F', 'F', 'V', 'F0', 'F0', 'V0'),

            'г': Consonant('G', 'K', 'G', 'G0', 'K0', 'G0'),
            'к': Consonant('K', 'K', 'G', 'K0', 'K0', 'G0'),

            'h': Consonant('GH', 'KH', 'GH', 'GH0', 'KH0', 'GH0'),  # боh, аhа, буhалтер
            'х': Consonant('KH', 'KH', 'GH', 'KH0', 'KH0', 'GH0'),

            'д': Consonant('D', 'T', 'D', 'D0', 'T0', 'D0'),
            'т': Consonant('T', 'T', 'D', 'T0', 'T0', 'D0'),

            'з': Consonant('Z', 'S', 'Z', 'Z0', 'S0', 'Z0'),
            'с': Consonant('S', 'S', 'Z', 'S0', 'S0', 'Z0'),

            'ж': Consonant('ZH', 'SH', 'ZH', 'ZH', 'SH', 'ZH'),
            'ш': Consonant('SH', 'SH', 'ZH', 'SH', 'SH', 'ZH'),

            'z': Consonant('DZ', 'TS', 'DZ', 'DZ', 'TS', 'DZ'),  # zета, Zагоев
            'ц': Consonant('TS', 'TS', 'DZ', 'TS', 'TS', 'DZ'),

            'j': Consonant('DZH0', 'TSH0', 'DZH0', 'DZH0', 'TSH0', 'DZH0'),
            'ч': Consonant('TSH0', 'TSH0', 'DZH0', 'TSH0', 'TSH0', 'DZH0'),

            'g': Consonant('ZH0', 'SH0', 'ZH0', 'ZH0', 'SH0', 'ZH0'),  # доggи, приеggать
            'щ': Consonant('SH0', 'SH0', 'ZH0', 'SH0', 'SH0', 'ZH0'),

            'd': Consonant('DZ0', 'TS0', 'DZ0', 'DZ0', 'TS0', 'DZ0'),  # Dюба
            't': Consonant('TS0', 'TS0', 'DZ0', 'TS0', 'TS0', 'DZ0'),

            'x': Consonant('DZH', 'TSH', 'DZH', 'DZH', 'TSH', 'DZH'),  # маxонг, лоxия
            's': Consonant('TSH', 'TSH', 'DZH', 'TSH', 'TSH', 'DZH'),  # поsтанники

            # считаем, что J0 уже добавили, где нужно
            'ё+': Vocal('O0', 'O0', 'O0', 'O0', 'O0', 'O0', 'O0', 'O0'),
            'ю+': Vocal('U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0'),
            'я+': Vocal('A0', 'A0', 'A0', 'A0', 'A0', 'A0', 'A0', 'A0'),
            'е+': Vocal('E0', 'E0', 'E0', 'E0', 'E0', 'E0', 'E0', 'E0'),

            'о+': Vocal('O0', 'O0', 'O0', 'O0', 'O0', 'O0', 'O0', 'O0'),
            'у+': Vocal('U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0'),
            'а+': Vocal('A0', 'A0', 'A0', 'A0', 'A0', 'A0', 'A0', 'A0'),
            'э+': Vocal('E0', 'E0', 'E0', 'E0', 'E0', 'E0', 'E0', 'E0'),
            'ы+': Vocal('Y0', 'Y0', 'Y0', 'Y0', 'Y0', 'Y0', 'Y0', 'Y0'),
            'и+': Vocal('I0', 'I0', 'I0', 'I0', 'Y0', 'Y0', 'I0', 'I0'),

            'ё': Vocal('O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'),
            'ю': Vocal('U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'),
            'я': Vocal('A', 'I', 'A', 'I', 'A', 'Y', 'A', 'I'),
            'е': Vocal('I', 'I', 'I', 'I', 'Y', 'Y', 'I', 'I'),

            'о': Vocal('A', 'A', 'A', 'I', 'A', 'A', 'A', 'A'),
            'у': Vocal('U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'),
            'а': Vocal('A', 'A', 'A', 'I', 'A', 'A', 'A', 'A'),
            'э': Vocal('Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'),
            'ы': Vocal('Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'),
            'и': Vocal('I', 'I', 'I', 'I', 'Y', 'Y', 'I', 'I')
        }

    def rule_27(self, letters_list: list, next_phoneme: str, cur_pos: int) -> str:
        case = ''
        if letters_list[cur_pos] == 'н':
            if next_phoneme in {'J0', 'TSH0', 'SH0', 'DZH0', 'ZH0', 'D0', 'T0', 'Z0', 'S0', 'L0', 'M0', 'P0', 'B0', 'V0', 'F0', 'N0'}:
                case = 'n_soft'
        elif letters_list[cur_pos] in {'т', 'с', 'д', 'з', 'п', 'б', 'в', 'ф'}:
            if next_phoneme in {'D0', 'Z0', 'B0'}:
                case = 'v_soft'
            elif next_phoneme in {'T0', 'S0', 'P0'}:
                case = 'd_soft'
            elif next_phoneme in {'N0', 'L0', 'M0', 'V0', 'F0'}:
                case = 'n_soft'
        return case











import codecs
import copy
import json
import os
import re
import warnings
import urllib.request
import urllib.parse
import lxml.html
import itertools
import dawg_python as dawg
import logging


class Accentor:
    def __init__(self, mode='one', debug='no', exception_for_unknown=False, use_wiki=True):
        if debug == 'no':
            logging.basicConfig()
        else:
            logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger()
        self.logger.debug('Setting up the Accentor...')
        self.mode = mode
        self.__all_russian_letters = {'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
                                      'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
                                      'я'}
        self.__russian_vowels = {'а', 'о', 'у', 'э', 'ы', 'и', 'я', 'ё', 'ю', 'е'}
        self.exception_for_unknown = exception_for_unknown
        self.use_wiki = use_wiki
        self.__homonyms = None
        self.__simple_words_dawg = None
        self.__function_words = None
        self.__new_homonyms = {}
        self.__new_simple_words = set()
        self.__bad_words = []
        self.__re_for_morphosplit = re.compile(r'[\,\s\|]+', re.U)
        self.__re_for_morphotag = re.compile(r'^(\w+|\w+[\-\=]\w+)$', re.U)
        assert mode in ('one', 'many'), 'Set either "one" or "many" variant mode!'
        assert debug in ('yes', 'no'), 'Set either "yes" or "no" variant mode!'
        homograph_dictionary_name = os.path.join(os.path.dirname(__file__), 'data', 'homographs.json')
        assert os.path.isfile(homograph_dictionary_name), f'File `{homograph_dictionary_name}` does not exist!'
        simple_words_dawg_name = os.path.join(os.path.dirname(__file__), 'data', 'simple_words.dawg')
        assert os.path.isfile(simple_words_dawg_name), f'File `{simple_words_dawg_name}` does not exist!'
        function_words_name = os.path.join(os.path.dirname(__file__), 'data', 'Function_words.json')
        assert os.path.isfile(function_words_name), f'File `{function_words_name}` does not exist!'
        data = None
        try:
            d = dawg.IntDAWG()
            self.__simple_words_dawg = d.load(simple_words_dawg_name)
            ###
            with codecs.open(homograph_dictionary_name, mode='r', encoding='utf-8', errors='ignore') as fp:
                data = json.load(fp)
            error_message_homographs = f'File `{homograph_dictionary_name}` contains incorrect data!'
            assert isinstance(data, dict), error_message_homographs
            self.__homonyms = dict()
            for cur_wordform in data:
                assert self.check_source_wordform(cur_wordform), \
                    error_message_homographs + f' Word `{cur_wordform}` is inadmissible!'
                assert (cur_wordform not in self.__homonyms) and (cur_wordform.lower() not in self.__simple_words_dawg), \
                    error_message_homographs + f' Word `{cur_wordform}` is repeated!'
                assert isinstance(data[cur_wordform], dict), \
                    error_message_homographs + f' Word `{cur_wordform}` has incorrect description of accents!'
                for cur_key in data[cur_wordform]:
                    assert self.check_morphotag(cur_key), \
                        error_message_homographs + f' Word `{cur_wordform}` has incorrect description of accents!'
                    assert self.check_accented_wordform(data[cur_wordform][cur_key]), \
                        error_message_homographs + f' Word `{cur_wordform}` has incorrect description of accents!'
                values = [data[cur_wordform][it] for it in data[cur_wordform]]
                self.__homonyms[cur_wordform] = copy.deepcopy(data[cur_wordform])
            ###
            self.__function_words = None
            with codecs.open(function_words_name, mode='r', encoding='utf-8', errors='ignore') as fp:
                function_words = json.load(fp)
            error_message_function_words = f'File `{function_words_name}` contains incorrect data!'
            assert isinstance(function_words, list), error_message_function_words
            assert isinstance(function_words[0], str), error_message_function_words
            self.__function_words = function_words
        finally:
            if data is not None:
                del data

    def __del__(self):
        if self.__homonyms is not None:
            del self.__homonyms
        if self.__simple_words_dawg is not None:
            del self.__simple_words_dawg
        del self.__all_russian_letters
        del self.__russian_vowels
        del self.__re_for_morphosplit
        del self.__re_for_morphotag
        del self.__new_homonyms
        del self.__new_simple_words
        del self.__bad_words
        del self.__function_words

    def get_correct_omograph_wiki(self, root_text, cur_word, morphotag='X'):
        '''
        Разбор омографии.
        Использование морфологической информации о 
        слове для их разграничения.
        '''
        langs = root_text.split('<hr />')
        #print('hello?')
        root = None
        for lang in langs:
            #print(lang)
            head_pos = lang.find('<h2><span class="mw-headline" id="Russian">Russian</span>')
            if head_pos != -1:
                root = lxml.html.document_fromstring(lang[head_pos:])
        if root == None:
            #print(':^(')
            return []
        good_headers = []
        shallow_vars = set()
        results = set()
        for header in root.findall('.//*[@class="mw-headline"]'):
            #print(cur_word, morphotag)
            if header.text_content() in ['Noun', 'Verb', 'Adjective', 'Adverb', 'Conjunction', 'Determiner', 'Interjection',
    'Morpheme', 'Numeral', 'Particle', 'Predicative', 'Preposition', 'Pronoun']:
                good_headers.append(header.text_content())
                acc_word = header.getparent().getnext()
                while acc_word.tag != 'p':
                    acc_word = acc_word.getnext()
                #print(acc_word)
                result = []
                hyphen = 0
                for part in acc_word.find_class('Cyrl headword'):
                    result += [part.text_content()]
                    if part.text_content().find('-') != -1:
                        hyphen = 1
                #print(result)
                if (hyphen == 1) or (len(result) == 1):
                    result = ''.join(result)
                else:
                    continue
                if result.replace('ё', 'е́').find('') != -1:
                    shallow_vars.add(result)
                if header.text_content()[0] == morphotag[0]:
                    #print('The tags are equal')
                    if header.text_content()[0] == 'N':
                        gramm_info = acc_word.getnext()
                        if gramm_info.text_content().find('of') != -1:
                            for variant in gramm_info.find_class('form-of-definition'):
                                info = variant.findall('a')
                                #print(variant.text_content())
                                try:
                                    if info[0].text_content()[0] == 'p':
                                        case = 'l'
                                    else:
                                        case = info[0].text_content()[0]
                                    #print(case)
                                    number = info[1].text_content()[0]
                                    #print(number + case, morphotag)
                                    if case == morphotag[morphotag.find('Case=') + 5].lower():
                                        results.add(result)
                                except IndexError:
                                    continue
                        else:
                            if morphotag[morphotag.find('Case=') + 5].lower() == 'n':
                                results.add(result)
                    elif header.text_content()[0] == 'V':
                        gramm_info = acc_word.getnext()
                        if morphotag.find('Mood=Inf') != -1:
                            results.add(result)
                            #print('Wut',morphotag, results)
                        for variant in gramm_info.find_class('form-of-definition'):
                            #print(variant.text_content())
                            t = 0
                            if (variant.text_content().find('indicative') != -1) and (morphotag.find('Mood=Ind') != -1):                          
                                if ((variant.text_content().find('future') != -1) or (variant.text_content().find('present') != -1)) and (morphotag.find('Tense=Notpast') != -1):
                                    #print('I should be here')
                                    results.add(result)
                                    #print(1, results)
                                elif (variant.text_content().find('past') != -1) and (morphotag.find('Tense=Past') != -1):
                                    results.add(result)
                                    #print(2, results)
                            elif (variant.text_content().find('imperative') != -1) and (morphotag.find('Mood=Imp') != -1):
                                results.add(result)
                    else:
                        results.add(result)
            elif (header.text_content()[0] == 'D') and (morphotag.find('PRON') != -1):
                acc_word = header.getparent().getnext()
                result = ''
                for part in acc_word.find_class('Cyrl headword'):
                    result += part.text_content()
                results.add(result)
            elif (header.text_content().lower().find(morphotag.split()[0].lower()) != -1):
                acc_word = header.getparent().getnext()
                result = ''
                for part in acc_word.find_class('Cyrl headword'):
                    result += part.text_content()
                results.add(result)
        #print(shallow_vars)
        if len(list(shallow_vars)) == 1:
            if list(shallow_vars)[0].replace('ё', 'е+').replace('', '') == cur_word:
                return [list(shallow_vars)[0].replace('ё', 'ё+').replace('', '+').replace('', '+')]
        #print(results)
        if len(list(results)) != 1:
            return []
        best_results = [variant.replace('', '+') for variant in results]
        return list(best_results)

    def get_simple_form_wiki(self, root_text, form):
        '''
        Непосредственное нахождение релевантной формы
        и ударение без морфологической информации.
        '''
        root = lxml.html.document_fromstring(root_text)
        rel_forms = set()
        for header in root.findall('.//*[@class="Cyrl headword"][@lang="ru"]'):
            header_text = header.text_content().replace('ё', 'е́')
            header_text_best = header.text_content().replace('ё', 'ё+').replace('', '+')
            if header_text.replace('', '') == form:
                if header_text.find('') != -1:
                    rel_forms.add(header_text_best)
        for mention in root.findall('.//i[@class="Cyrl mention"][@lang="ru"]'):
            mention_text = mention.text_content().replace('ё', 'е́')
            mention_text_best = mention.text_content().replace('ё', 'ё+').replace('', '+')
            if mention_text.replace('', '') == form:
                if mention_text.replace('ё', 'е́').find('') != -1:
                    rel_forms.add(mention_text_best)
        for mention in root.findall('.//b[@class="Cyrl"][@lang="ru"]'):
            mention_text = mention.text_content().replace('ё', 'е́')
            mention_text_best = mention.text_content().replace('ё', 'ё+').replace('', '+')
            if mention_text.replace('', '') == form:
                if mention_text.replace('ё', 'е́').find('') != -1:
                    rel_forms.add(mention_text_best)
            elif mention_text.find('(') != -1:
                if mention_text.replace('', '').find(form) != -1:
                    if mention_text.find('') != -1:
                        rel_forms.add(mention_text_best[mention_text.replace('', '').find(form):])
                elif re.sub(r'[\(\)́]', '', mention_text) == form:
                    rel_forms.add(re.sub(r'[\(\)]', '', mention_text_best))
        for target in root.xpath('.//span[@class="Cyrl"][@lang="ru"]'):
            one_form = target.text_content()
            if one_form.replace('ё', 'е́').replace('', '') == form:
                if one_form.replace('ё', 'е́').find('') != -1:
                    rel_forms.add(one_form.replace('ё', 'ё́').replace('', '+'))
        results = list(rel_forms)
        if len(results) == 2:
            if results[0].replace('ё', 'е') == results[1].replace('ё', 'е'):
                rel_forms = set()
                for var in results:
                    if var.find('ё') != -1:
                        rel_forms.add(var)
        return list(rel_forms)

    def load_wiki_page(self, cur_form):
        if not self.use_wiki:
            if self.exception_for_unknown:
                raise ValueError(f'Word `{cur_form}` is unknown!')
            return
        query = urllib.parse.urlencode({ 'title' : cur_form })
        try:
            http_exception_type = urllib.error.HTTPError
        except:
            http_exception_type = urllib.request.HTTPError
        try:
            with urllib.request.urlopen(f'https://en.wiktionary.org/w/index.php?{query}&#printable=yes') as f:
                root_text = f.read().decode('utf-8')
                return root_text
        except http_exception_type:
            return

    def do_accents(self, source_phrase_and_morphotags: list) -> list:
        self.logger.debug('Checking the source phrase...')
        error_message = f'`{source_phrase_and_morphotags}`: the phrase should be of a "list of lists" format!\nExample: [["word1","morphotag1"], ["word2","morphotag2"]] or [["word1"], ["word2"]]'
        assert isinstance(source_phrase_and_morphotags, list), error_message
        try:
            assert isinstance(source_phrase_and_morphotags[0], list), error_message
        except IndexError:
            assert len(source_phrase_and_morphotags) > 0, 'Source phrase is empty!'
        try:
            source_phrase, morphotags_of_phrase = list(zip(*source_phrase_and_morphotags))
        except (ValueError, TypeError):
            source_phrase = list(zip(*source_phrase_and_morphotags))[0]
            morphotags_of_phrase = None
        for pair in source_phrase_and_morphotags:
            assert len(pair) == len(source_phrase_and_morphotags[0]), \
                f"`{' '.join(source_phrase)}`: morphotags do not correspond to words!"
        prepared_phrase = []
        for cur_word in source_phrase:
            assert len(cur_word.strip()) > 0, f'`{source_phrase}`: this phrase is wrong!'
            prepared_phrase.append(cur_word.strip().lower())
        if morphotags_of_phrase is not None:
            assert len(prepared_phrase) == len(morphotags_of_phrase), \
                f"`{' '.join(source_phrase)}`: morphotags do not correspond to words!"
        assert len(prepared_phrase) > 0, 'Source phrase is empty!'
        try:
            res = self.__do_accents(prepared_phrase, morphotags_of_phrase)
        except Exception as e:
            err_msg = str(e)
            ok = False
            res = []
            for modified_phrase in self.__generate_phrases_with_jo(prepared_phrase, []):
                try:
                    res = self.__do_accents(modified_phrase, morphotags_of_phrase)
                    ok = True
                except Exception as e:
                    ok = False
                    err_msg = str(e)
                if ok:
                    break
            if not ok:
                raise ValueError(err_msg)
        return res

    def check_source_wordform(self, checked: str) -> bool:
        if len(checked.strip()) == 0:
            return False
        res = len(self.__all_russian_letters | {'-'}) \
              == len((self.__all_russian_letters | {'-'}) | set(checked.lower()))
        if not res:
            return False
        if '-' not in checked:
            return True
        for cur_part in checked.split('-'):
            if len(cur_part) == 0:
                res = False
                break
        return res

    def check_accented_wordform(self, checked: str) -> bool:
        if len(checked.strip()) == 0:
            return False
        res = len(self.__all_russian_letters | {'-', '+'}) \
              == len((self.__all_russian_letters | {'-', '+'}) | set(checked.lower()))
        if not res:
            return False
        if '-' in checked:
            parts = list()
            for cur_part in checked.split('-'):
                parts.append(cur_part.lower().strip())
        else:
            parts = [checked.lower().strip()]
        for cur_part in parts:
            filtered_part = ''.join(list(filter(lambda c: c != '+', cur_part)))
            if len(filtered_part) == 0:
                res = False
                break
        return res

    def check_morphotag(self, morphotag: str) -> bool:
        if len(morphotag.strip()) == 0:
            return False
        if morphotag.isdigit():
            return True
        ind1 = morphotag.find('(')
        ind2 = morphotag.find(')')
        if (ind1 < 0) and (ind2 < 0):
            ok = len(morphotag.strip()) > 0
        else:
            if (ind1 >= 0) and (ind1 >= ind2):
                ok = False
            elif len(morphotag[:ind1].strip()) == 0:
                ok = False
            elif len(morphotag[(ind1 + 1):ind2].strip()) == 0:
                ok = False
            elif not morphotag[(ind1 + 1):ind2].strip().isdigit():
                ok = False
            else:
                ok = (len(morphotag[(ind2 + 1):].strip()) == 0)
        if ok:
            if ind1 < 0:
                ind1 = len(morphotag)
            for cur_part in self.__re_for_morphosplit.split(morphotag[:ind1].strip()):
                if len(cur_part.strip()) == 0:
                    ok = False
                    break
                if cur_part.strip().isdigit():
                    ok = False
                    break
                search_res = self.__re_for_morphotag.search(cur_part.strip())
                if search_res is None:
                    ok = False
                    break
                if (search_res.start() < 0) or (search_res.end() < 0):
                    ok = False
                    break
        return ok

    def calculate_morpho_similarity(self, morphotags_1: str, morphotags_2: str) -> float:
        if morphotags_1.isdigit() or morphotags_2.isdigit():
            return 0.0
        prepared_morpotags_1 = set(filter(
            lambda a: len(a) > 0,
            map(lambda b: b.strip(), self.__re_for_morphosplit.split(morphotags_1))
        ))
        prepared_morpotags_2 = set(filter(
            lambda a: len(a) > 0,
            map(lambda b: b.strip(), self.__re_for_morphosplit.split(morphotags_2))
        ))
        if (len(prepared_morpotags_1) == 0) and (len(prepared_morpotags_2) == 0):
            return 0.0
        return len(prepared_morpotags_1 & prepared_morpotags_2) / len(prepared_morpotags_1 | prepared_morpotags_2)

    def prepare_morphotag(self, source_morphotag: str) -> str:
        ind1 = source_morphotag.find('(')
        ind2 = source_morphotag.find(')')
        if ind1 < 0:
            if ind2 >= 0:
                res = source_morphotag[:ind2].strip()
            else:
                res = source_morphotag.strip()
        else:
            if ind2 >= 0:
                res = source_morphotag[:(ind2 if ind2 < ind1 else ind1)].strip()
            else:
                res = source_morphotag[:ind1].strip()
        return res

    def get_new_dics(self):
        return self.__new_homonyms, sorted(list(self.__new_simple_words))

    def get_bad_words(self):
        return self.__bad_words

    def __generate_phrases_with_jo(self, old_phrase, new_phrase):
        if len(old_phrase) == 0:
            yield new_phrase
        else:
            found_pos = old_phrase[0].find('е')
            while found_pos >= 0:
                new_word = old_phrase[0][:found_pos] + 'ё' + old_phrase[0][(found_pos + 1):]
                yield from self.__generate_phrases_with_jo(old_phrase[1:], new_phrase + [new_word])
                found_pos = old_phrase[0].find('е', found_pos + 1)
            yield from self.__generate_phrases_with_jo(old_phrase[1:], new_phrase + [old_phrase[0]])

    def __do_accents(self, words_list: list, morphotags_list: list=None) -> list:
        n = len(words_list)
        if morphotags_list is not None:
            assert n == len(morphotags_list), 'Morphotags do not correspond to words!'
        if n < 1:
            return []
        cur_token = words_list[0].lower()
        warn = ''
        if '+' in cur_token:
            accented_wordforms = [cur_token]
            accented_wordforms_many = [cur_token]
        else:
            accented_wordforms = []
            accented_wordforms_many = []
            separate_tokens = [cur_token] + cur_token.split('-')
            for i, cur_word in enumerate(separate_tokens):
                vowels_counter = 0
                for cur in cur_word:
                    if cur in self.__russian_vowels:
                        vowels_counter += 1
                if (cur_word in self.__function_words) or (vowels_counter == 0) or (('-' + cur_word) in self.__function_words) or ((cur_word + '-') in self.__function_words):
                    self.logger.debug(f'The word `{cur_word}` is in the list of function words')
                    accented_wordforms += [cur_word]
                    accented_wordforms_many.append([cur_word])
                elif vowels_counter == 1:
                    self.logger.debug(f'The word `{cur_word}` has one vowel: accented automatically')
                    cur_vowel = list(set(cur_word) & self.__russian_vowels)[0]
                    pos = cur_word.find(cur_vowel)
                    try:
                        accented_wordforms += [cur_word[:(pos+1)] + '+' + cur_word[(pos+1):]]
                        accented_wordforms_many.append([cur_word[:(pos+1)] + '+' + cur_word[(pos+1):]])
                    except IndexError:
                        accented_wordforms += [cur_word[:pos] + '+']
                        accented_wordforms_many.append([cur_word[:pos] + '+'])
                elif cur_word in self.__simple_words_dawg:
                    self.logger.debug(f'The word `{cur_word}` is in the dictionary of simple words')
                    accented_wordform = cur_word[:self.__simple_words_dawg[cur_word]] + '+' + cur_word[self.__simple_words_dawg[cur_word]:]
                    accented_wordforms += [accented_wordform]
                    accented_wordforms_many.append([accented_wordform])
                elif cur_word in self.__homonyms:
                    self.logger.debug(f'The word `{cur_word}` is in the dictionary of homonyms')
                    if (morphotags_list is None) or morphotags_list[0].isdigit():
                        accented_wordforms += [cur_word]
                        accented_wordforms_many.append(sorted([self.__homonyms[cur_word][it] for it in self.__homonyms[cur_word]]))
                        warn = 'many'
                    else:
                        best_ind = -1
                        best_similarity = 0.0
                        morpho_variants = list(self.__homonyms[cur_word].keys())
                        for ind in range(len(morpho_variants)):
                            similarity = self.calculate_morpho_similarity(morpho_variants[ind], morphotags_list[0])
                            if similarity > best_similarity:
                                best_similarity = similarity
                                best_ind = ind
                        if best_ind >= 0:
                            accented_wordforms += [self.__homonyms[cur_word][morpho_variants[best_ind]]]
                            accented_wordforms_many.append([self.__homonyms[cur_word][morpho_variants[best_ind]]])
                        else:
                            root_text = self.load_wiki_page(cur_word)
                            if root_text != None:
                                #print('am I even here?')
                                cur_accented_wordforms = sorted(self.get_correct_omograph_wiki(root_text, cur_word, morphotags_list[0]))
                                if len(cur_accented_wordforms) == 1:
                                    accented_wordforms += [cur_accented_wordforms[0]]
                                    accented_wordforms_many.append([cur_accented_wordforms[0]])
                                    self.__new_homonyms[cur_word] = {morphotags_list[0] : cur_accented_wordforms[0]}
                                elif len(cur_accented_wordforms) > 1:
                                    accented_wordforms += [cur_word]
                                    accented_wordforms_many.append([cur_accented_wordforms])
                                    warn = 'many'
                                else:
                                    accented_wordforms += [cur_word]
                                    accented_wordforms_many.append(sorted([self.__homonyms[cur_word][it] for it in self.__homonyms[cur_word]]))
                                    warn = 'many'
                            else:
                                accented_wordforms += [cur_word]
                                accented_wordforms_many.append(sorted([self.__homonyms[cur_word][it] for it in self.__homonyms[cur_word]]))
                                warn = 'many'
                else:
                    self.logger.debug(f'The word `{cur_word}` was not found in any of the dictionaries\nTrying to parse wictionary page...')
                    root_text = self.load_wiki_page(cur_word)
                    if root_text != None:
                        cur_accented_wordforms = sorted(self.get_simple_form_wiki(root_text, cur_word))
                        if len(cur_accented_wordforms) == 1:
                            accented_wordforms += [cur_accented_wordforms[0]]
                            accented_wordforms_many.append([cur_accented_wordforms[0]])
                            self.__new_simple_words.add(cur_accented_wordforms[0])
                        elif len(cur_accented_wordforms) == 0:
                            accented_wordforms += [cur_word]
                            accented_wordforms_many.append([cur_word])
                            warn = 'no'
                        else:
                            cur_accented_wordforms = sorted(self.get_correct_omograph_wiki(root_text, cur_word, morphotags_list[0]))
                            if len(cur_accented_wordforms) == 1:
                                accented_wordforms += [cur_accented_wordforms[0]]
                                accented_wordforms_many.append([cur_accented_wordforms[0]])
                                self.__new_homonyms[cur_word] = {morphotags_list[0] : cur_accented_wordforms[0]}
                            else:
                                accented_wordforms += [cur_word]
                                accented_wordforms_many.append(sorted([self.__homonyms[cur_word][it] for it in self.__homonyms[cur_word]]))
                                warn = 'many'

                    else:
                        accented_wordforms += [cur_word]
                        accented_wordforms_many.append([cur_word])
                        warn = 'no'
                if i == 0:
                    if (accented_wordforms[0].find('+') != -1) or (len(separate_tokens) == 2):
                        break
                    else:
                        accented_wordforms = []
        if (len(accented_wordforms) != 1) or (len(accented_wordforms_many) != 1):
            accented_wordforms = ['-'.join(accented_wordforms)]
            new_accented_wordforms_many = []
            for combination in list(itertools.product(*accented_wordforms_many[1:])):
                new_accented_wordforms_many.append('-'.join(combination))
            accented_wordforms_many = new_accented_wordforms_many
        else:
            accented_wordforms = [accented_wordforms[0]]
            accented_wordforms_many = accented_wordforms_many[0]
        if cur_token in accented_wordforms:
            accented_wordforms = [accented_wordforms[accented_wordforms.index(cur_token)]]
            if warn != '':
                if warn == 'many':
                    err_msg = f'Word `{cur_token}` has too many accent variants!'
                else:  # warn == 'no':
                    err_msg = f'Word `{cur_token}` is unknown!'
                if self.exception_for_unknown:
                    raise ValueError(err_msg)
                self.__bad_words.append(cur_token)
                warnings.warn(err_msg)
        accented_phrases = []
        if n > 1:
            if self.mode == 'one':
                for vt in self.__do_accents(words_list[1:], None if morphotags_list is None else morphotags_list[1:]):
                    accented_phrases.append([accented_wordforms[0]] + vt)
            else:
                for cur_accent in accented_wordforms_many:
                    for vt in self.__do_accents(words_list[1:], None if morphotags_list is None else morphotags_list[1:]):
                        accented_phrases.append([cur_accent] + vt)
        else:
            if self.mode == 'one':
                accented_phrases.append([accented_wordforms[0]])
            else:
                for cur_accent in accented_wordforms_many:
                    accented_phrases.append([cur_accent])
        return accented_phrases

class RulesForGraphemes:
    def __init__(self, users_mode: str='Classic'):
        if users_mode == 'Modern':
            UsersMode = ModernMode
        else:
            UsersMode = ClassicMode

        self.mode = UsersMode()

    def apply_rule_for_vocals(self, letters_list: list, cur_pos: int) -> list:
        new_phonemes_list = list()
        case = 0
        if cur_pos == 0:
            if letters_list[cur_pos] in self.mode.double_vocals:
                new_phonemes_list.append('J0')
            if cur_pos + 1 >= len(letters_list):
                case = 1
            else:
                case = 2
        elif letters_list[cur_pos - 1] in self.mode.hard_and_soft_signs:
            if letters_list[cur_pos] in self.mode.gen_vocals_soft | {'о', 'о+'}:
                new_phonemes_list.append('J0')
            if cur_pos + 1 >= len(letters_list):
                case = 1
            else:
                case = 2
        elif letters_list[cur_pos - 1] in self.mode.vocals:
            if letters_list[cur_pos] in self.mode.double_vocals:
                new_phonemes_list.append('J0')
            if cur_pos + 1 >= len(letters_list):
                case = 1
            else:
                case = 2
        elif letters_list[cur_pos - 1] in self.mode.soft_consonants:
            if cur_pos + 1 >= len(letters_list):
                case = 3
            else:
                case = 4
        elif letters_list[cur_pos - 1] in self.mode.hard_consonants:
            if cur_pos + 1 >= len(letters_list):
                case = 5
            else:
                case = 6
        elif letters_list[cur_pos - 1] in self.mode.hardsoft_consonants:
            if cur_pos + 1 >= len(letters_list):
                case = 7
            else:
                case = 8
        else:
            assert 0 == 1, "Incorrect word! " + ''.join(letters_list)
        new_phonemes_list.append(self.mode.TableG2P[letters_list[cur_pos]].forms['case' + str(case)])
        return new_phonemes_list

    def apply_rule_for_consonants(self, letters_list: list, next_phoneme: str, cur_pos: int) -> list:
        new_phonemes_list = list()
        n = len(letters_list)
        # твердость / мягкость
        if cur_pos < n - 1 and letters_list[cur_pos + 1] in self.mode.gen_vocals_soft:
            hardsoft = 'soft'
        else:
            hardsoft = 'hard'
        if letters_list[-1] in self.mode.hard_and_soft_signs:
            n -= 1
        # конец слова
        if cur_pos == n - 1:
            if next_phoneme == 'sil':
                voice = 'd'
            elif next_phoneme in self.mode.deaf_phonemes:
                voice = 'd'
            elif next_phoneme in self.mode.voiced_weak_phonemes:
                voice = 'd'
            elif next_phoneme in self.mode.voiced_strong_phonemes:
                voice = 'v'
            elif next_phoneme in self.mode.vocals_phonemes:
                voice = 'd'
            else:
                voice = ''
                assert 0 == 1, "Incorrect word! " + ' '.join(letters_list)
            case = voice + '_' + hardsoft
        # внутри слова
        else:
            case = self.mode.rule_27(letters_list, next_phoneme, cur_pos)
            if len(case) == 0:
                if next_phoneme == 'sil':
                    voice = ''
                    assert 0 == 1, "Incorrect word! " + ' '.join(letters_list)
                elif next_phoneme in self.mode.deaf_phonemes:
                    voice = 'd'
                elif next_phoneme in self.mode.voiced_weak_phonemes:
                    voice = 'n'
                elif next_phoneme in self.mode.voiced_strong_phonemes:
                    voice = 'v'
                elif next_phoneme in self.mode.vocals_phonemes:
                    voice = 'n'
                else:
                    voice = ''
                    assert 0 == 1, "Incorrect word! " + ' '.join(letters_list)
                case = voice + '_' + hardsoft
        new_phonemes_list.append(self.mode.TableG2P[letters_list[cur_pos]].forms[case])
        return new_phonemes_list

class Transcription:
    def __init__(self, raise_exceptions: bool=False, batch_size: int=64, verbose: bool=False,
                 use_wiki: bool=False):
        self.__preprocessor = Preprocessor(batch_size=batch_size)
        self.__accentor = Accentor(exception_for_unknown=raise_exceptions, use_wiki=use_wiki)
        self.__g2p = Grapheme2Phoneme(exception_for_nonaccented=raise_exceptions)
        self.verbose = verbose

    def transcribe(self, texts: list):
        all_words_and_tags = self.__preprocessor.preprocessing(texts)
        if self.verbose:
            print('All texts have been preprocessed...')
        n_texts = len(texts)
        n_data_parts = 100
        part_size = n_texts // n_data_parts
        while (part_size * n_data_parts) < n_texts:
            part_size += 1
        data_counter = 0
        part_counter = 0
        total_result = []
        for cur_words_and_tags in all_words_and_tags:
            try:
                accented_text = self.__accentor.do_accents(cur_words_and_tags)
            except:
                accented_text = []
            if len(accented_text) > 0:
                tmp = ' '.join(accented_text[0])
                tmp = ' ' + tmp
                phonetic_words = tmp.split(' <sil>')
                try:
                    result = []
                    for phonetic_word in phonetic_words:
                        if len(phonetic_word) != 0:
                            phonemes = self.__g2p.phrase_to_phonemes(phonetic_word)
                            result.append(phonemes)
                except:
                    result = []
            else:
                result = []
            total_result.append(result)
            data_counter += 1
            if (part_size > 0) and self.verbose:
                if (data_counter % part_size) == 0:
                    part_counter += 1
                    print(f'{part_counter}% of texts have been processed...')
        if (part_counter < n_data_parts) and self.verbose:
            print('100% of texts have been processed...')
        return total_result

import codecs
import os
import re
import warnings



class Grapheme2Phoneme(RulesForGraphemes):
    def __init__(self, users_mode='Modern', exception_for_nonaccented=False):
        RulesForGraphemes.__init__(self, users_mode)
        self.exception_for_nonaccented = exception_for_nonaccented

        self.__re_for_phrase_split = None

        self.__silence_name = 'sil'

        #self.__function_words_1 = {'без', 'безо', 'близ', 'в', 'во', 'вне', 'для', 'до', 'за', 'из', 'изо', 'к', 'ко',
        #                           'меж', 'на', 'над', 'о', 'об', 'обо', 'от', 'ото', 'по', 'под', 'подо', 'пред',
        #                           'предо', 'перед', 'при', 'про', 'с', 'со', 'у', 'чрез', 'через', 'не', 'ни', 'из-за',
        #                           'из-подо', 'из-под', 'а-ля', 'по-над', 'по-за'}

        self.__function_words_1 = {'без', 'близ', 'в', 'из', 'меж', 'над', 'об', 'под', 'пред', 'перед', 'чрез', 'через',
                                   'из-под', 'по-над'}

        self.__function_words_2 = {'бы', 'б', 'де', 'ли', 'же', '-то', '-ка', '-либо', '-нибудь', '-таки'}

        self.__exclusions_dictionary = None
        exclusions_dictionary_name = os.path.join(os.path.dirname(__file__), 'Phonetic_Exclusions.txt')
        assert os.path.isfile(exclusions_dictionary_name), \
            f'File `{exclusions_dictionary_name}` does not exist!'
        self.__exclusions_dictionary = self.load_exclusions_dictionary(exclusions_dictionary_name)
        self.__re_for_phrase_split = re.compile(r'[\s\-]+', re.U)

    @property
    def russian_letters(self) -> list:
        return sorted(list(self.mode.all_russian_letters))

    @property
    def russian_phonemes(self) -> list:
        return sorted(list(self.mode.russian_phonemes_set))

    @property
    def silence_name(self) -> str:
        return self.__silence_name

    def load_exclusions_dictionary(self, file_name: str) -> dict:
        words_and_words = dict()
        with codecs.open(file_name, mode='r', encoding='utf-8', errors='ignore') as dictionary_file:
            cur_line = dictionary_file.readline()
            cur_line_index = 1
            while len(cur_line):
                error_message = f"File `{file_name}`, line {cur_line_index}: description of this word and its transformation is " \
                                "incorrect!"
                prepared_line = cur_line.strip()
                if len(prepared_line):
                    words_of_line = prepared_line.lower().split()
                    nwords = len(words_of_line)
                    assert nwords == 2, error_message
                    word_original, word_transformed = words_of_line
                    assert any([c in (self.mode.all_russian_letters | {'-', '+'}) for c in word_original]), error_message
                    assert any([c in (self.mode.all_russian_letters | {'-', '+'}) for c in word_transformed]), error_message
                    assert len(word_original) > 0 and len(word_transformed) > 0, error_message
                    words_and_words[word_original] = word_transformed
                cur_line = dictionary_file.readline()
                cur_line_index += 1
        return words_and_words

    def check_word(self, checked_word: str):
        assert len(checked_word) > 0, 'Checked word is empty string!'
        assert all([c in (self.mode.all_russian_letters | {'+', '-'}) for c in checked_word.lower()]), \
            f'`{checked_word}`: this word contains inadmissible characters!'
        assert len(list(filter(lambda c: c in self.mode.all_russian_letters, checked_word.lower()))) > 0, \
            f'`{checked_word}`: this word is incorrect!'

    def check_phrase(self, checked_phrase: str):
        assert len(checked_phrase) > 0, 'Checked phrase is empty string!'
        assert all([c in (self.mode.all_russian_letters | {' ', '+', '-'} | {'s', 'i', 'l'})
                    for c in checked_phrase.lower()]), \
            f'`{checked_phrase}`: this phrase contains inadmissible characters!'
        # for cur_word in self.__re_for_phrase_split.split(checked_phrase.lower()):
        # assert (len(list(filter(lambda c: c in self.all_russian_letters, cur_word))) > 0) \
        #      or (cur_word.lower() == 'sil'), f'`{checked_phrase}`: this phrase is incorrect!'

    def word_to_phonemes(self, source_word: str, next_phoneme: str = 'sil') -> list:
        self.check_word(source_word)
        error_message = f'`{source_word}`: this word is incorrect!'
        prepared_word = source_word.lower()
        if prepared_word in self.__exclusions_dictionary:
            prepared_word = self.__exclusions_dictionary[prepared_word]
        if '+' not in prepared_word:
            counter = len(prepared_word) - len(re.sub(r'[аоуэыияёею]', '', prepared_word))
            if counter > 1:
                if self.exception_for_nonaccented:
                    raise ValueError(f'`{source_word}`: the accent for this word is unknown!')
                warnings.warn(f'`{source_word}`: the accent for this word is unknown!')
        if prepared_word in self.__exclusions_dictionary:
            prepared_word = self.__exclusions_dictionary[prepared_word]
        prepared_word = prepared_word.replace('\'', '')
        if '-' in prepared_word:
            if (not self.in_function_words_1(prepared_word)) and (not self.in_function_words_2(prepared_word)):
                word_parts = list(filter(lambda a: len(a) > 0, map(lambda b: b.strip(), prepared_word.split('-'))))
                assert len(word_parts) > 0, error_message
                prepared_word_parts = [word_parts[0]]
                for cur_part in word_parts[1:]:
                    if self.in_function_words_1('-' + cur_part) or self.in_function_words_2('-' + cur_part):
                        prepared_word_parts.append('-' + cur_part)
                    else:
                        prepared_word_parts.append(cur_part)
                return self.phrase_to_phonemes(' '.join(prepared_word_parts))
            prepared_word = self.__remove_character(prepared_word, '-')
        letters_list = self.__word_to_letters_list(self.__prepare_word(prepared_word))
        n = len(letters_list)
        assert n > 0, error_message
        ind = n - 1
        # начинаем формировать транскрипцию
        transcription = list()
        while ind >= 0:
            if ind >= 0 and letters_list[ind] in self.mode.hard_and_soft_signs:
                ind -= 1
                continue
            if letters_list[ind] in self.mode.vocals:
                new_phonemes = self.apply_rule_for_vocals(letters_list, ind)
            else:
                assert letters_list[ind] in self.mode.consonants, error_message
                new_phonemes = self.apply_rule_for_consonants(letters_list, next_phoneme, ind)
            ind -= 1
            transcription = new_phonemes + transcription
            next_phoneme = new_phonemes[0]
        assert len(transcription) > 0, f'`{source_word}`: this word cannot be transcribed!'
        return self.__remove_long_phonemes(self.__remove_repeats_from_transcription(transcription))

    def phrase_to_phonemes(self, source_phrase: str) -> list:
        error_message = f'`{source_phrase}`: this phrase is incorrect!'
        source_phrase = source_phrase.lower().replace('-', ' ')
        source_phrase = re.sub('[^a-zйцукенгшщзхъфывапролджэячсмитьбюё+ ]', '', source_phrase)
        self.check_phrase(source_phrase)
        words_in_phrase = source_phrase.split()
        l = len(words_in_phrase)
        for i in range(l):
            if words_in_phrase[i] in self.__exclusions_dictionary:
                words_in_phrase[i] = self.__exclusions_dictionary[words_in_phrase[i]]
            words_in_phrase[i] = self.__prepare_word(words_in_phrase[i])
        # формируем псевдослова, объединяя предлоги со стоящими после них словами
        new_words = list()
        cur_word = ''
        last_letter = ''
        for i in range(0, l):
            clear_word = words_in_phrase[i].replace('+', '')
            to_append = (i == l - 1) or (clear_word not in self.__function_words_1)
            if words_in_phrase[i][0] == 'и':
                if last_letter not in (self.mode.vocals | {'ь', ''} | self.mode.soft_consonants):
                    words_in_phrase[i] = 'ы' + words_in_phrase[i][1:]
            if words_in_phrase[i][0] in self.mode.double_vocals:
                words_in_phrase[i] = 'ъ' + words_in_phrase[i]
            cur_word += words_in_phrase[i]
            if to_append:
                new_words.append(cur_word)
                cur_word = ''
            last_letter = clear_word[-1]
        # разбираем фразу
        next_phoneme = 'sil'
        phrase_transcription = []
        for i in range(len(new_words) - 1, -1, -1):
            new_transcription = self.word_to_phonemes(new_words[i], next_phoneme)
            new_transcription = self.__remove_repeats_from_transcription(new_transcription)
            new_transcription = self.__remove_long_phonemes(new_transcription)
            phrase_transcription = [new_transcription] + phrase_transcription
            next_phoneme = new_transcription[0]
        final_transcription = list()
        for word_transcription in phrase_transcription:
            final_transcription += word_transcription
        final_transcription = self.__remove_repeats_from_transcription(final_transcription, full=False)
        final_transcription = self.__remove_long_phonemes(final_transcription)
        return final_transcription

    def in_function_words_1(self, source_word: str) -> bool:
        return self.__remove_character(source_word, '+').lower() in self.__function_words_1

    def in_function_words_2(self, source_word: str) -> bool:
        return self.__remove_character(source_word, '+').lower() in self.__function_words_2

    def __remove_character(self, source_word: str, removed_char: str) -> str:
        return ''.join(list(filter(lambda a: a != removed_char, source_word.lower())))

    def __prepare_word(self, cur_word: str) -> str:
        prepared_word = cur_word.lower().strip()
        replace_pairs = [('стн', 'сн'), ('стл', 'сл'), ('нтг', 'нг'), ('здн', 'зн'), ('здц', 'зц'),
                         ('ндц', 'нц'), ('рдц', 'рц'), ('ндш', 'нш'), ('гдт', 'гт'), ('лнц', 'нц'),
                         ]
        if (len(prepared_word) > 2 and prepared_word[-3:] == 'его') or \
                (len(prepared_word) > 3 and prepared_word[-3:] == 'ого') or \
                (len(prepared_word) > 3 and prepared_word[-4:] in {'о+го', 'е+го'}):
            prepared_word = prepared_word[:-2] + 'ва'
        elif len(prepared_word) > 2 and prepared_word[-3:] == 'тся':
            prepared_word = prepared_word[:-3] + 'ца'
        elif len(prepared_word) > 3 and prepared_word[-4:] == 'ться':
            prepared_word = prepared_word[:-4] + 'ца'
        for repl_from, repl_to in replace_pairs:
            prepared_word = prepared_word.replace(repl_from, repl_to)
        return prepared_word

    def __word_to_letters_list(self, cur_word: str) -> list:
        vocal_letters = set(filter(lambda letter: not letter.endswith('+'), self.mode.vocals))
        error_message = f"`{cur_word}`: this word is incorrect!"
        letters_list = list()
        new_letter = ''
        for ind in range(len(cur_word)):
            if cur_word[ind] == '+':
                assert new_letter in vocal_letters, error_message
                new_letter += cur_word[ind]
            else:
                assert cur_word[ind] in self.mode.all_russian_letters, error_message
                if len(new_letter):
                    letters_list.append(new_letter)
                new_letter = cur_word[ind]
        if len(new_letter):
            letters_list.append(new_letter)
        del vocal_letters
        return letters_list

    def __remove_repeats_from_transcription(self, source_transcription: list, full: bool=True) -> list:
        def equal(s_l: str, s_r: str) -> bool:
            s_l_ = re.sub(r'[l]', '', s_l)
            s_r_ = re.sub(r'[l]', '', s_r)
            ans = s_l_ == s_r_
            return ans

        def equal_almost(s_l: str, s_r: str) -> bool:
            s_l_ = re.sub(r'[l]', '', s_l)
            s_r_ = re.sub(r'[0l]', '', s_r)
            ans = s_l_ == s_r_
            return ans

        phomene_pairs = {('Z', 'ZH'): 'ZH',
                         ('Z', 'ZH0'): 'ZH0', ('Z0', 'ZH0'): 'ZH0',

                         ('D', 'Z'): 'DZ', ('D', 'DZ'): 'DZ',
                         ('D', 'Z0'): 'DZ0', ('D0', 'Z0'): 'DZ0', ('D', 'DZ0'): 'DZ0', ('D0', 'DZ0'): 'DZ0',

                         ('D', 'ZH'): 'DZH', ('D', 'DZH'): 'DZH',
                         ('D', 'ZH0'): 'DZ0', ('D0', 'ZH0'): 'DZH0', ('D', 'DZH0'): 'DZH0', ('D0', 'DZH0'): 'DZH0',

                         ('T', 'S'): 'TS', ('T', 'TS'): 'TS',
                         ('T', 'S0'): 'TS0', ('T0', 'S0'): 'TS0', ('T', 'TS0'): 'TS0', ('T0', 'TS0'): 'TS0',

                         ('T', 'SH'): 'TSH', ('T', 'TSH'): 'TSH',
                         ('T', 'SH0'): 'TSH0', ('T0', 'SH0'): 'TSH0', ('T', 'TSH0'): 'TSH0', ('T0', 'TSH0'): 'TSH0',

                         ('S', 'SH'): 'SH',
                         ('S', 'TSH0'): 'SH0', ('SH', 'TSH0'): 'SH0',
                         }

        def conjugate(s_l: str, s_r: str) -> str:
            s_l_ = re.sub(r'[l]', '', s_l)
            s_r_ = re.sub(r'[l]', '', s_r)
            ans = phomene_pairs[(s_l_, s_r_)] if (s_l_, s_r_) in phomene_pairs else ''
            return ans

        prepared_transcription = list()
        previous_phoneme = ''
        if full:
            for current_phoneme in source_transcription:
                if equal(previous_phoneme, current_phoneme):
                    #  1st case: S0 S0 -> S0l
                    prepared_transcription[-1] = current_phoneme + 'l'
                elif equal_almost(previous_phoneme, current_phoneme):
                    #  2nd case: S S0 -> S0l
                    prepared_transcription[-1] = current_phoneme + 'l'
                else:
                    conj = conjugate(previous_phoneme, current_phoneme)
                    if len(conj) > 0:
                        #  3rd case: S SH -> SHl
                        prepared_transcription[-1] = conj
                    else:
                        prepared_transcription.append(current_phoneme)
                previous_phoneme = prepared_transcription[-1]
        else:
            for current_phoneme in source_transcription:
                if equal(previous_phoneme, current_phoneme):
                    #  1st case: S0 S0 -> S0l
                    prepared_transcription[-1] = current_phoneme + 'l'
                elif equal_almost(previous_phoneme, current_phoneme):
                    #  2nd case: S S0 -> S0l
                    prepared_transcription[-1] = current_phoneme + 'l'
                else:
                    prepared_transcription.append(current_phoneme)
                previous_phoneme = prepared_transcription[-1]
        return prepared_transcription

    def __remove_long_phonemes(self, source_transcription: list) -> list:

        def postprocess_phoneme(src):
            if (len(src) > 1) and (src.endswith('l')):
                return src[:-1]
            return src

        n = len(source_transcription)
        if n == 0:
            return []
        new_transcription = [postprocess_phoneme(source_transcription[0])]
        for idx in range(1, n):
            new_phoneme = postprocess_phoneme(source_transcription[idx])
            if new_phoneme != new_transcription[-1]:
                new_transcription.append(new_phoneme)
        return list(filter(lambda it: len(it) > 0, new_transcription))



from re import sub

from rnnmorph.predictor import RNNMorphPredictor


class Preprocessor():

    def __init__(self, batch_size=1):
        self.batch_size = batch_size
        self.predictor = RNNMorphPredictor(language="ru")

    def __del__(self):
        if hasattr(self, 'predictor'):
            del self.predictor

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.predictor = self.predictor
        return result

    def __deepcopy__(self, memodict={}):
        cls = self.__class__
        result = cls.__new__(cls)
        result.predictor = self.predictor
        return result

    def gettags(self, texts):
        if not isinstance(texts, list):
            raise ValueError(f'Expected `{type([1, 2])}`, but got `{type(texts)}`.')
        if len(texts) == 0:
            return []
        all_phonetic_phrases = []
        all_phrases_for_rnnmorph = []
        for cur_text in texts:
            list_of_phonetic_phrases = [cur.strip() for cur in ' '.join(cur_text).split('<sil>')]
            united_phrase_for_rnnmorph = []
            for phonetic_phrase in list_of_phonetic_phrases:
                if len(phonetic_phrase) > 0:
                    united_phrase_for_rnnmorph += phonetic_phrase.split()
            if len(united_phrase_for_rnnmorph) > 0:
                all_phrases_for_rnnmorph.append(united_phrase_for_rnnmorph)
                all_phonetic_phrases.append(list_of_phonetic_phrases)
            else:
                all_phonetic_phrases.append([])
        if len(all_phrases_for_rnnmorph) > 0:
            all_forms = self.predictor.predict_sentences(all_phrases_for_rnnmorph, batch_size=self.batch_size)
        else:
            all_forms = []
        all_words_and_tags = []
        phrase_ind = 0
        for cur in all_phonetic_phrases:
            words_and_tags = [['<sil>', 'SIL _']]
            if len(cur) > 0:
                token_ind = 0
                for phonetic_phrase in cur:
                    if len(phonetic_phrase) > 0:
                        n = len(phonetic_phrase.split(' '))
                        analysis = all_forms[phrase_ind][token_ind:(token_ind + n)]
                        for word in analysis:
                            word_and_tag = []
                            word_and_tag.append(word.word)
                            word_and_tag.append(word.pos + ' ' + word.tag)
                            words_and_tags.append(word_and_tag)
                        words_and_tags.append(['<sil>', 'SIL _'])
                        token_ind += n
                phrase_ind += 1
            all_words_and_tags.append(words_and_tags)
        return all_words_and_tags

    def preprocessing(self, texts):

        def prepare(src):
            dst = sub('[\.\,\?\!\(\);:]+', ' <sil>', src.lower())
            dst = sub(' [–-] |\n', ' <sil> ', dst)
            dst = sub('\s{2,}', ' ', dst)
            dst = sub('^\s|(?<!\w)[\\\/@#~¬`£€\$%\^\&\*–_=+\'\"\|«»–-]+', '', dst)
            return dst.strip().split(' ')

        words_and_tags = self.gettags([prepare(cur) for cur in texts])
        return words_and_tags





