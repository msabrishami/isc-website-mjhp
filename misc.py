# By M. Saeed Abrishami
# ISC Information Portal Project 
# Misc. functions 

import re

def gen_paragraph(par, style):
    if style in ["h1", "h2"]:
        res = f'''
            <p>{par}</p>
            '''

    elif style == "h3":
        res = f'''
            <p class="ms-3">{par}</p>
            '''

    return res

def md2html_pars(pars, style):
    res = ""
    in_list = False
    in_note = False
    if isinstance(pars, str):
        pars = ["".join(pars)]
    for line in pars:
		# bold and italic 
        line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
        line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)

        # Note boxes
        if line.strip() == "```":
            if in_note:
                res += '</div>\n'
                in_note = False
            else:
                if in_list:     # just ad hoc modification
                    res += '</ul>\n'
                    in_list = False
                res += '<div class="alert alert-primary" role="alert">\n'
                in_note = True
            continue


        # itemized list, the line starts with '*'
        if line.startswith('*'):
            if not in_list:
                res += '<ul>\n'
                in_list = True
            res  += f'<li>{line[1:].strip()}</li>\n'
        else:
            if in_list:
                res += '</ul>\n'
                in_list = False
			
			# based on style paragraph can be different
            if in_note:
                res+= line
            elif style in ["h1", "h2"]:
                res += f'<p>{line}</p>\n'
            elif style in ["h3"]:
                res += f'<p class="ms-3">{line}</p>\n'
            else:
                print("Warning: paragraph with unknown style!")
                res += f'<p>{line}</p>\n'
                
    if in_list:
        res += '</ul>'
    if in_note: 
        res += '</div>\n'  
    
    return res

def md2html_notes(notes):
    res = ""
    for note in notes:
        res += '''
                <!-- ======= Note ======= -->
                <div class="alert alert-primary" role="alert">
                    {note}
                </div>
        '''
    return res 


