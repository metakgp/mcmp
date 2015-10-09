from __future__ import print_function
import json

prof_details = json.load(open('./prof_details.json','r'))

txt_list = []
start = "xxxx"
end = "yyyy"
for prof in prof_details[:50]:
    prof = dict(prof)
    prof["field"] = "| ".join(prof["field"])
    prof_txt = """xxxx
'''User:Kakashi/%(name)s'''
{{Infobox Professor
| department = %(dept)s
| research_areas = {{ubl| %(field)s}}
| year_joined = %(year)s
}}
yyyy
"""
    prof_txt = prof_txt % prof
    txt_list.append(prof_txt)

txt = "".join(txt_list)
print(txt)
