#  Biblioteca para normalização, tokenização e steemmer dos textos
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import word_tokenize
nltk.download('punkt')
from stop_words import get_stop_words

class ajustandoDados():

    # Removendo espaços em branco antes e depois das senteças, e caracteres especiais
    def remove_misc1(data,column):
        column1 = str(column)
        # remover espaço antes e depois dos comentários:
        data[column1] = data[column1].str.strip()

        # remover caracteres especiais:
        data[column1] = data[column1].str.lower()
        #data[column1] = data[column1].str.replace(r"#[A-Za-z0-9_]+", 'xuserx', regex=True)
        data[column1] = data[column1].str.replace(r'http\S+', 'xurlx', regex=True)
        #data[column1] = data[column1].str.replace(r"@[A-Za-z0-9_]+", 'xuserx', regex=True)
        data[column1] = data[column1].str.replace(r'\n+', ' ',regex=True)
        #data[column1] = data[column1].str.replace(r'[^\w\s]','', regex = True)
        #data[column1] = data[column1].str.replace(r'''b['|"]+RT @[\w_]+:''', '', regex=True)
        data[column1] = data[column1].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        
        # print(df.apenas_texto)

        return data

    # Remove stopwords
    def remove_stopwords(text):
        stop_words = set(stopwords.words('portuguese'))
        words = word_tokenize(text)
        return [x for x in words if x not in stop_words]

    def lemmatize_word(text):
        wordnet = WordNetLemmatizer()
        return " ".join([wordnet.lemmatize(word) for word in text])

    # Remoce hashtag e users
    def remove_user_hash(data,column):
        column1 = str(column)
        data[column1] = data[column1].str.replace(r"@[A-Za-z0-9_]+", 'xuserx', regex=True)
        data[column1] = data[column1].str.replace(r"#[A-Za-z0-9_]+", 'xhashtagx', regex=True)