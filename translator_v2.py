import re
import pdb
import sys


import config
from misc import gen_paragraph, md2html_pars, md2html_notes  

# html_head (title, title)
# html_tab_head
# html_tab xLoop (h2-tag, h2-tag, h2-tag, h2-name)
# html_tail

if len(sys.argv) < 3:
    print("Error: provide the filenames, <input>.md and <output>.html")
title = sys.argv[3] if len(sys.argv) == 4 else "No Title"

## HTML: Stating the code
# html = config.top_html.format(title, title)

# Sample input
with open(sys.argv[1], "r") as file:
    lines = file.readlines()

# Variables to hold data
h1s = []
h1 = None
h2s = []
current_h2 = None
current_h3 = None
intro_text = []
current_level = None

ptr_s = 0
ptr_f = 0
for idx, line in enumerate(lines):
    if line.startswith("# "):
        ptr_s = idx
        break

# html += f'''
#     <div class="container">
#         <div class="tab-content" id="pills-tabContent">
#     '''
html = f'''
    <div class="container">
        <div class="tab-content" id="pills-tabContent">
    '''


while (ptr_f < len(lines)-1):
    ptr_f = ptr_s + 1
    # print("Starting the loop: ", ptr_s, ptr_f)
    while (ptr_f < len(lines)) and (not lines[ptr_f].startswith("# ")):
        ptr_f += 1
    h1 = None
    h2s = []
    current_h2 = None
    current_h3 = None
    intro_text = []
    current_level = None

    print("Done with counting: ", ptr_s, ptr_f)
    # Process lines
    for line in lines[ptr_s:ptr_f]:
        line = line.strip()
        # print("." + line)
        # if not line:
        #     continue
    
        if line.startswith("# "):
            h1 = line[2:]
            h1s.append(h1)
    
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
    # <div class="container">
    # <div class="tab-content" id="pills-tabContent">

    # html += f'''
    #         <div
    #             class="tab-pane fade show active"
    #             id="pills-bank"
    #             role="tabpanel"
    #             aria-labelledby="pills-bank-tab"
    #             tabindex="0">
    #             <section>
    #                 <div class="tab-title">
    #                     <h2>{h1}</h2>
    #                 </div>
    # 
    #                 <div class="tab-outlines">
    # '''
    h1_id = h1.replace(" ", "-").lower()
    show_status = "show active" if len(h1s)==1 else ""
    html += config.html_tab.format(show_status, h1_id, h1_id, h1)
    icons = [
        "mdi-bank", "mdi-account-cash", "mdi-cash-fast",
        "mdi-credit-card", "mdi-checkbook"
    ]
    
    for idx, h2 in enumerate(h2s):
        sec_id = re.sub(r'[^a-z0-9]', '', h2['title'].lower())
        # html += f'''
        #                 <a class="outline" href="#secid{secid}">
        #                     <i class="iconify" data-icon="{icons[idx % len(icons)]}"></i>
        #                     <h2 class="h6">{h2['title']}</h2>
        #                 </a>
        # '''
        
        html += f'''
                        <a class="outline" href="#secid{sec_id}">
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
                </div>
    '''
    print("Done with this Tab")
    ptr_s = ptr_f

html_ = config.html_head.format(title, title)
html_ += config.html_tab_nav_head

# The first one should be active
_h1_id = h1s[0].replace(" ", "-").lower()
html_ += config.html_tab_nav.format("active", _h1_id,_h1_id, _h1_id, h1s[0]) 

for _h1 in h1s[1:]:
    _h1_id = _h1.replace(" ", "-").lower()
    html_ += config.html_tab_nav.format(" ", _h1_id,_h1_id, _h1_id, _h1) 
html_ += config.html_tab_nav_tail

html_ += html 

html_ += '''
            </section>
        </div>
    </div>
</div>
'''
html_ += config.tail_text
with open(sys.argv[2], "w") as output_file:
    output_file.write(html_)
