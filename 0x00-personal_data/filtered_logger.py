#!/usr/bin/env python3

'''
function that return log message obfuscated
'''

def filter_datum(fields, redaction, message, separator):
    '''
    function that return log message obfuscated
    '''
    for field in fields:
        message = message.replace(field + separator, field + separator + redaction + separator)
    return (message)
    