def strip_html(html):

    should_read = True

    text = ""

    for char in html:
        if char == "<":
            should_read = False
        
        if should_read:
            text += char
        
        if char == ">":
            should_read = True

    return text

html_example = """
<b>hello</b>
World
<i>Italic</i>
"""

print(strip_html(html=html_example))