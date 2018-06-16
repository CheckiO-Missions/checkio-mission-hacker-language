init_code = """
if not "HackerLanguage" in USER_GLOBAL:
    raise NotImplementedError("Where is 'HackerLanguage'?")
HackerLanguage = USER_GLOBAL['HackerLanguage']
"""

run_test = """
RET['code_result'] = {}
"""


def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. First": [
        prepare_test(middle_code='''message = HackerLanguage()
message.write('secrit')
message.delete(2)
message.write('et')''',
                     test="message.send()",
                     answer="111001111001011100011111001011001011110100")
    ],
    "2. Second": [
        prepare_test(middle_code='''message = HackerLanguage()
message.write('Remember: 21.07.2018')
message.write(' at 11:11AM')
message.delete(1)
message.delete(1)''',
                     test="message.send()",
                      answer="10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:11")
    ],
    "3. Third": [
        prepare_test(middle_code='''message = HackerLanguage()
message.write('Hi man')
message.delete(3)
message.write('dude!')''',
                     test="message.send()",
                     answer="1001000110100110000001100100111010111001001100101!")
    ],
    "4. Fourth": [
        prepare_test(middle_code='''message = HackerLanguage()
message.write('need some drugs?')''',
                     test="message.send()",
                     answer="110111011001011100101110010010000001110011110111111011011100101100000011001001110010111010111001111110011?")
    ],
    "5. Fifth": [
        prepare_test(middle_code='''message = HackerLanguage()
message.delete(10)
message.write('I need more % and $ from this deal!')''',
                     test="message.send()",
                     answer="100100110000001101110110010111001011100100100000011011011101111111001011001011000000%10000001100001110111011001001000000$100000011001101110010110111111011011000000111010011010001101001111001110000001100100110010111000011101100!")
    ],
    "6. Sixth": [
        prepare_test(middle_code="message = HackerLanguage()",
                     test="message.read('11001011101101110000111010011101100')",
                     answer="email")
    ],
    "7. Seventh": [
        prepare_test(middle_code="message = HackerLanguage()",
                     test="message.read('10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101')",
                     answer="My email is mr.robot@gmail.com")
    ],
    "8. Eighth": [
        prepare_test(middle_code="message = HackerLanguage()",
                     test="message.read('10010001100001111011011001011000000111100111011111110101111001010000001100101111011011001011110010100000011000101100101110010111011101000000110100111011101000000111010011010001100101100000010010101100001111000011000011101110?..')",
                     answer="Have your ever been in the Japan?..")
    ],
    "9. Ninth": [
        prepare_test(middle_code="message = HackerLanguage()",
                     test="message.read('...110000111011101100100100000011000111101111110010011001011000000110110011010011101011110010110000001101000110010111011001101100!')",
                     answer="...and code like hell!")
    ],
    "10. Tenth": [
        prepare_test(middle_code="message = HackerLanguage()",
                     test="message.read('1001001100000011000011101101100000011101001101001111001011001011100100...')",
                     answer="I am tired...")
    ]

}
