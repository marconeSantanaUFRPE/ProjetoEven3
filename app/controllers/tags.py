
from flask import render_template

def verificaTagsTextoPlanilha(tags,tagsdaPlanilha):
    
    for x in tags:
        if x not in tagsdaPlanilha:
            return False
                                