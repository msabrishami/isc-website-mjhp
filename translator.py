import re
import config

html = config.top_html

# Sample input
with open("input.md", "r") as file:
    lines = file.readlines()

# Variables to hold data
h1 = None
h2s = []
current_h2 = None
current_h3 = None
intro_text = []

# Process lines
for line in lines:
    line = line.strip()

    if line.startswith("# "):
        h1 = line[2:]
    elif line.startswith("## "):
        if current_h2:
            h2s.append(current_h2)
        current_h2 = {'title': line[3:], 'h3s': [], 'paragraphs': []}
    elif line.startswith("### "):
        if current_h3:
            current_h2['h3s'].append(current_h3)
        current_h3 = {'title': line[4:], 'paragraph': None}
    elif line.startswith("```"):
        pass  # If notes are needed for HTML generation, process here
    elif line and current_h2:
        if current_h3:
            current_h3['paragraph'] = line
            current_h2['h3s'].append(current_h3)
            current_h3 = None
        else:
            current_h2['paragraphs'].append(line)
    elif line and not current_h2:  # Introduction text after H1 and before first H2
        intro_text.append(line)

if current_h2:
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


import pdb
pdb.set_trace()
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
    html += f'''
                <section id="secid{secid}">
					<div class="title-lvl2">
						<div class="outline">
							<i class="iconify" data-icon="mdi-bank"></i>
							<h2 class="h4">{h2['title']}</h2>
						</div>
					</div>	
    '''
    for paragraph in h2['paragraphs']:
        html += f'''
                    <p>{paragraph}</p>
        '''
    for h3 in h2['h3s']:
        html += f'''
                    <h5>{h3['title']}</h5>
                    <p class="ms-3">{h3['paragraph']}</p>
        '''

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
with open("output.html", "w") as output_file:
    output_file.write(html)
