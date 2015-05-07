def generate_content_HTML(content_title, content_description):
    html_text1 = '''
<div class="content">
    <div class="content_description">
        ''' + content_title
    html_text2 = ''' 
    '''+ content_description
    html_text3 = '''
    </div>
</div>'''
    
    full_html_text = html_text1 + html_text2 + html_text3
    return full_html_text

def get_title(content):
    start_location = content.find('TITLE:')
    end_location = content.find('DESCRIPTION:')
    title = content[start_location+7 : end_location-1]
    return title

def get_description(content):
    start_location = content.find('DESCRIPTION:')
    description = content[start_location+13 :]
    return description

def get_content_by_number(text, content_number):
    counter = 0
    while counter < content_number:
        counter = counter + 1
        next_content_start = text.find('TITLE:')
        next_content_end   = text.find('TITLE:', next_content_start + 1)
        if next_content_end >= 0:
            content = text[next_content_start:next_content_end]
        else:
            next_content_end = len(text)
            content = text[next_content_start:]
        text = text[next_content_end:]
    return content

TEXT = """TITLE: Computers
DESCRIPTION: Computers can be programmed to do anything we want, as long as we can write a program that specifies a specific sequence of instructions.
TITLE: Computer Program
DESCRIPTION: A program is a precise sequence of steps that a computer can follow to do something useful. Web browsers, games, mobile apps, and simple print statements are all examples of computer programs.
TITLE: Programming Language
DESCRIPTION: A programming language is what programmers use to tell a computer what to do. Python is one example of a programming language.
TITLE: Python
DESCRIPTION: Python is a programming language. When you write Python code and press "Run", a Python Interpreter converts the code you wrote as a set of instructions that the computer itself can understand and execute.
TITLE: Grammar
DESCRIPTION: A grammar is a specification of what is "correct" and what is "incorrect." We have to write code that is exactly "correct" according to the Python interpreter, otherwise our code won't run.
TITLE: Python Expressions
DESCRIPTION: A Python "expression" is a legal Python statement. For example: print 1 + 1 is a valid expression, but print 1 + (without a number at the end) is not."""


def generate_all_html(text):
    current_content_number = 1
    content = get_content_by_number(text, current_content_number)
    all_html = ''
    while content != '':
        title = get_title(content)
        description = get_description(content)
        content_html = generate_content_HTML(title, description)
        all_html = all_html + content_html
        current_content_number = current_content_number + 1
        content = get_content_by_number(text, current_content_number)
    return all_html


print generate_all_html(TEXT)