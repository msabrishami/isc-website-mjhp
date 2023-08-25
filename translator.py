import re
import config
import pdb
import sys

html = config.top_html
# condition to check argv is given - TODO 
if len(sys.argv != 3):
    print("Error: provide the filenames, <input>.md and <output>.html")

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


# Sample input
with open(sys.argv[1], "r") as file:
    lines = file.readlines()

# Variables to hold data
h1 = None
h2s = []
current_h2 = None
current_h3 = None
intro_text = []
current_level = None

# Process lines
for line in lines:
    line = line.strip()
    # if not line:
    #     continue

    if line.startswith("# "):
        h1 = line[2:]

    elif line.startswith("## "):
        if current_h2:
            if current_h3:
                current_h2['h3s'].append(current_h3)
                current_h3 = None
            h2s.append(current_h2)
        
        current_h2 = {'title': line[3:], 'h3s': [], 'paragraphs': []}
        current_level = 'h2'

    elif line.startswith("### "):
        if current_h3:
            current_h2['h3s'].append(current_h3)
        current_h3 = {'title': line[4:], 'paragraphs': []}
        current_level = 'h3'
    # elif line.startswith("```"):
    #     if in_note_box:
    #         in_note_box = False
    #         current_h2['notes'].append(' '.join(note_content))
    #         note_content = []
    #     else:
    #         in_note_box = True

    # elif line and in_note_box:
    #     note_content.append(line)
    elif line:
        if current_level == 'h3':
            current_h3['paragraphs'].append(line)
        elif current_level == 'h2':
            current_h2['paragraphs'].append(line)
        else: # this is the intro for h1 right before any h2
            intro_text.append(line)

if current_h2:
    if current_h3:
        current_h2['h3s'].append(current_h3)
    h2s.append(current_h2)

# Generate HTML
html += f'''
<div class="container">
    <div class="tab-content" id="pills-tabContent">
        <div
            class="tab-pane fade show active"
            id="pills-bank"
            role="tabpanel"
            aria-labelledby="pills-bank-tab"
            tabindex="0">
            <section>
                <div class="tab-title">
                    <h2>{h1}</h2>
                </div>

                <div class="tab-outlines">
'''

icons = [
    "mdi-bank", "mdi-account-cash", "mdi-cash-fast",
    "mdi-credit-card", "mdi-checkbook"
]

for idx, h2 in enumerate(h2s):
    secid = re.sub(r'[^a-z0-9]', '', h2['title'].lower())
    html += f'''
                    <a class="outline" href="#secid{secid}">
                        <i class="iconify" data-icon="{icons[idx % len(icons)]}"></i>
                        <h2 class="h6">{h2['title']}</h2>
                    </a>
    '''

# Main Content
html += '''
                </div>
'''

for paragraph in intro_text:
    html += f'''
                <p>{paragraph}</p>
    '''
html += '''
         </section>
         <!-- End of First Section  -->
'''

for h2 in h2s:
    secid = re.sub(r'[^a-z0-9]', '', h2['title'].lower())
    # creating the h2 linked to the outline
    html += f'''
                <section id="secid{secid}">
					<div class="title-lvl2">
						<div class="outline">
							<i class="iconify" data-icon="mdi-bank"></i>
							<h2 class="h4">{h2['title']}</h2>
						</div>
					</div>	
    '''
    
    # creating the intro below h2 
    html += md2html_pars(h2['paragraphs'], "h2")
    # html += md2html_notes(h2['notes'])
    # for paragraph in h2['paragraphs']:
    #     print("." + paragraph)
    #     html += gen_paragraph(paragraph, 'h2')

    # creating the h3s within this h2
    for h3 in h2['h3s']:
        html += f'''
                    <h5>{h3['title']}</h5>
        '''
        # html += gen_paragraph(h3['paragraph'], 'h3')
        html += md2html_pars(h3['paragraphs'], 'h3')

    html += '''
                </section>
    '''

html += '''
            </section>
        </div>
    </div>
</div>
'''
html += config.tail_text
with open(sys.argv[2], "w") as output_file:
    output_file.write(html)
