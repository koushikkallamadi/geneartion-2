import re

def clean_file(filepath, start_marker, end_marker=None):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if end_marker:
        # Cut out everything between start_marker and end_marker
        idx1 = content.find(start_marker)
        idx2 = content.find(end_marker)
        if idx1 != -1 and idx2 != -1:
            content = content[:idx1] + content[idx2:]
    else:
        # Cut out everything after start_marker
        idx = content.find(start_marker)
        if idx != -1:
            content = content[:idx]
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Clean Chapter 1
clean_file(
    r'c:\Users\kalla\OneDrive\Desktop\deep dive\Nagarjun_MBA_cahp1.md', 
    '\n> **?? Problem 11:',
    '\n---\n\n## 9. Top 20 Common Exam Mistakes'
)

# Clean Chapter 1 (Glossary at the end)
clean_file(
    r'c:\Users\kalla\OneDrive\Desktop\deep dive\Nagarjun_MBA_cahp1.md', 
    '\n---\n\n## 10. Advanced Mastermind Glossary:'
)

# Clean Chapter 5
clean_file(
    r'c:\Users\kalla\OneDrive\Desktop\deep dive\material_characterization_deep_dive_chap5.md', 
    '\n> **?? Problem 61:',
    '\n---\n\n## 14. Advanced Mastermind Glossary:'
)

# Clean Chapter 5 (Glossary at the end)
clean_file(
    r'c:\Users\kalla\OneDrive\Desktop\deep dive\material_characterization_deep_dive_chap5.md', 
    '\n---\n\n## 14. Advanced Mastermind Glossary:'
)
