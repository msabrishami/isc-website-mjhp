# By M. Saeed Abrishami
# ISC Information Portal Project 
# Misc. functions 

import re
import pdb


all_icons = {
        "financial": [],
        "arrival": [],
        }

all_icons["financial"] = ["mdi-bank", "mdi-account-cash", "mdi-cash-fast", 
        "mdi-credit-card", "mdi-checkbook"]

all_icons["arrival"] = ["mdi-notebook", "mdi-shield-home", "mdi-shield-sun",
        "mdi-plane-car", "mdi-list-box"]

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

def gen_table(table):

    # print(table)
    header = table.split("</tr>")[0].split("<tr>")[1]
    header = [x.replace("<td>", "") for x in header[:-5].split("</td>")]

    html = '''
<!-- ======= Table ======= -->
<div class="table-responsive">
    <table class="table table-bordered">
        <thead>
            <tr>\n''' 
    for col in header:
        html+= f'''\t\t\t\t<th scope="col">{col}</th>\n'''
    html += "\t\t\t</tr>\n"
    html += "\t\t</thead>\n"
    html += "\t\t<tbody>\n"
    body = [x[4:] for x in table.split("</tr>")[1:-1]]
    for row in body:
        html += "\t\t\t<tr>\n"
        items = row.split("</td>")
        for item in items[:-1]:
            html += "\t\t\t\t" + item + "</td>\n"
        # html += "\t\t\t\t" + row.replace("</td>", "</td>\n")
        html += "\t\t\t</tr>\n"

    html += "\t\t</tbody>\n"
    html += "\t</table>\n"
    html += "</div>\n"
    return html




def md2html_pars(pars, style):
    res = ""
    in_list = False
    in_note = False
    in_table = False
    table_str = ""

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

        if line.strip() == "<table>":
            in_table = True
            in_note = False
            in_list = False
            table_str += line
            continue
        elif line.strip() == "</table>":
            in_table = False
            table_str += line
            res += gen_table(table_str)
            table_str = ""
            continue
        elif in_table:
            table_str += line
            continue

        # itemized list, the line starts with '*'
        if line.startswith('*'):
            if not in_list:
                res += '\n<ul>\n'
                in_list = True
            res  += f'\t<li>{line[1:].strip()}</li>\n'
        else:
            if in_list:
                res += '</ul>\n'
                in_list = False
			
			# based on style paragraph can be different
            if in_note:
                res+= line
            elif in_table: 
                res+= line
            elif style in ["h1", "h2"]:
                res += f'\t\t\t<p>{line}</p>\n'
            elif style in ["h3"]:
                res += f'\t\t<p class="ms-3">{line}</p>\n'
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


