import re
import string


def text_analyzer(*str_text):
    """
        This function counts the number of upper characters, lower characters,
        punctuations (listed below) and spaces in a given text.

        punctuations characters : "!#$%&'(),-./:;<=>?@[]^_`{|}~
    """

    total_args = len(str_text)
    if total_args > 1:
        print('ERROR')
        return
    if total_args == 1:
        evaluate_str = str_text[0]
    else:
        print('What is the text to analyze?')
        evaluate_str = input()
    spaces = len(re.findall('[ \t\n\r\f\v]', evaluate_str))
    str_len = len(evaluate_str)
    uppers = len(re.findall('[A-Z]', evaluate_str))
    lowers = len(re.findall('[a-z]', evaluate_str))
    punct = len(re.findall(r"[\"!#$%&'(),-./:;<=>?@[\]^_`{|}~]", evaluate_str))
    result = f"""The text contains {str_len} characters:
    \n- {uppers} upper letters
    \n- {lowers} lower letters
    \n- {punct} punctuation marks
    \n- {spaces} spaces"""
    print(result)
