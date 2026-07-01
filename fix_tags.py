with open("src/components/AddCardView.tsx", "r") as f:
    lines = f.readlines()

new_lines = []
in_fieldset = False
indent = ""

for line in lines:
    if '<fieldset ' in line:
        # Find the indentation
        indent = line[:line.find('<fieldset ')]
        
    if '</div>' in line and indent != "" and line.startswith(indent + '</div>'):
        # This is the closing tag for the fieldset
        line = line.replace('</div>', '</fieldset>')
        indent = "" # Reset
        
    new_lines.append(line)

with open("src/components/AddCardView.tsx", "w") as f:
    f.writelines(new_lines)
