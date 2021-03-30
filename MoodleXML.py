

def MoodleXML(cat, qg, n=10):
  xml = f"""<?xml version="1.0" ?>
<quiz>
<question type="category">
<category>
<text>$course$/{cat}</text>
</category></question>
"""
  for i in range(1,n):
    q = qg(i)
    qa = q['answer']
    qt = q['text']
    if isinstance(qa,list):
      # Multiple
      xml = xml + f"""<question type="multichoice">
<name><text>{cat + '#' + format(i, '03d')}</text></name>
<questiontext format="html"><text><![CDATA[{qt}]]></text></questiontext>"""
      for j in range(0, len(qa)-1):
        xml = xml + f'''<answer fraction="{ '100' if j==0 else '0'}">
<text><![CDATA[{qa[j]}]]></text>
</answer>'''
      xml = xml + '''<shuffleanswers>1</shuffleanswers>
<single>true</single>
<answernumbering>abc</answernumbering>'''
    elif qa is None:
      # Essay
      xml = xml + f'''<question type="essay">
<name>
  <text>{cat + '#' + format(i, '03d')}</text>
</name>
<questiontext format="html">
  <text><![CDATA[<p>{qt}</p>]]></text>
</questiontext>
<defaultgrade>1.0</defaultgrade>
<generalfeedback format="html"><text/></generalfeedback>
<penalty>0.1000000</penalty>
<hidden>0</hidden>
<responserequired>1</responserequired>
<responseformat>noinline</responseformat>
<responsefieldlines>15</responsefieldlines>
<attachments>1</attachments>
<attachmentsrequired>1</attachmentsrequired>
<graderinfo format="html"><text/></graderinfo>
<responsetemplate format="html"><text/></responsetemplate>'''
    elif isinstance(qa, (int, float)):
      # Numeric
      xml = xml + f'''<question type="numerical">
<name><text>{cat + '#' + format(i, '03d')}</text></name>
<questiontext format="html"><text><![CDATA[{qt}]]></text></questiontext>'''
      xml = xml + f'''<answer fraction="100">
<text><![CDATA[{qa}]]></text>
</answer>'''
    else:
      # Short
      xml = xml + f'''<question type="shortanswer">
<name><text>{cat + '#' + format(i, '03d')}</text></name>
<questiontext format="html"><text><![CDATA[{qt}]]></text></questiontext>'''
      xml = xml + f'''<answer fraction="100">
<text><![CDATA[{qa}]]></text>
</answer>'''
    xml = xml + '</question>'
  xml = xml + '</quiz>'
  return xml


