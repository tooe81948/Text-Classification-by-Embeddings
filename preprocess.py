import re
import emoji
from pythainlp import word_tokenize

class preprocess():
    def __init__(self):
        pass

    def replace_url(self,text):
        URL_PATTERN = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}
                          ]+|
                          [^\s()]*?\)|
                          )+(?:
                          [^\s()]*?\)|
                          |[^\s`!()
                          {};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""
        return re.sub(URL_PATTERN, 'xxurl', text)

    def replace_rep(self,text):
        def _replace_rep(m):
            c,cc = m.groups()
            return f'{c}'
            # return f'{c}xxrep'
        re_rep = re.compile(r'(\S)(\1{2,})')
        return re_rep.sub(_replace_rep, text)

    def ungroup_emoji(self,toks):
        res = []
        for tok in toks:
            if emoji.emoji_count(tok) == len(tok):
                for char in tok:
                    res.append(char)
            else:
                res.append(tok)
        return res

    def reWord(self,text):
      replace_word = ' −˜=ðắồ,ö‐—ĩŇŘŤŴŽå/η’;[]\·ႆး$%^&*()_+-~`“”๑๒๓๔฿๕๖๗๘๙↑ʻ–⋅←àìĕ̤ṳ̄нхчйودیëӑɔŋދިވެހބަސްάòفسõøçᓄᒃᑎᑐᑦລາວųāമലയാളംꯃꯤꯇꯩꯂꯣꯟ×éè±!'
      try:
        for idx , data in enumerate(text):
          for i in replace_word:
            data = data.replace( i , '' )
          text[idx] = data
      except:
        for i in replace_word:
            text = text.replace( i , '' )
      return text

    def detect_language(self,text):
        lang, confidence = langid.classify(text)
        return lang

    def process_text(self,text):
        res = text.lower().strip()
        lang = self.detect_language(res)
        if lang == "th":
          res = text.replace("\n","")
          res = self.replace_url(res)
          res = self.reWord(res)
          res = self.replace_rep(res)

          res = [word for word in word_tokenize(res, engine='attacut', join_broken_num=True, keep_whitespace=False) if word and not re.search(pattern=r"\s+", string=word)]
          res = self.ungroup_emoji(res)
        else:
          res = res.split(" ")

        return res

if __name__ in "__main__":
    prepro = Preprocess()
    context = prepro.process_text("")
    print(context)
