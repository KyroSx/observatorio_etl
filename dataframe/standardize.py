import re

def t_parenthesis(cell):
    return cell.replace('(', '').replace(')', '')

def t_comma(cell):
    return cell.replace('.', '').replace(',', '.')

def standardize(cell):    
    value = ''
    regexs = {
        'correct': re.compile(r'^\d*\.?\d*$'),
        'hyphen': re.compile(r'^\-$'),
        'comma': re.compile(r'^\d*\.?\d*\,?\d*$'),
        'parenthesis': re.compile(r'^\(\d*\.?\d*\,?\d*\)$')
    }
    
    if regexs['correct'].match(cell):
        value = cell
    elif regexs['hyphen'].match(cell):
        value = '0'
    elif regexs['comma'].match(cell):
        value = t_comma(cell)
    elif regexs['parenthesis'].match(cell):
        value = t_parenthesis(cell)
        value = t_comma(value)
    
    return float(value)
    

