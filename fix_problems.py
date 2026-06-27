import re

filepath = r'c:\Users\kalla\OneDrive\Desktop\deep dive\material_characterization_deep_dive_chap5.md'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Change the heading
content = content.replace('## 10. Exam Edge: 100 Advanced Solved Numericals', '## 10. Exam Edge: 30 Advanced Solved Numericals')

# Remove the Problem 1-30 placeholder block
placeholder = '> **?? Problem 1-30: [Standard Characterization & Math]**\n> *(Note: Problems 1 through 30 cover standard XRD Bragg\'s Law, Lattice Parameters, Scherrer Equation, WKB Tunneling, De Broglie Wavelength, Enthalpy of Fusion, Mass Stoichiometry, Structure Factors, Ewald Sphere, and Z-contrast calculations as previously detailed).*\n\n'
content = content.replace(placeholder, '')

# Renumber problems 31-60 to 1-30
def replacer(match):
    old_num = int(match.group(1))
    new_num = old_num - 30
    return f'> **?? Problem {new_num}:'

content = re.sub(r'> \*\*?? Problem (\d+):', replacer, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
