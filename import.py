import feedparser
import html2markdown 
import os
from jinja2 import Template

MD_TEMPLATE = \
"""Title: {{title.replace("\n", " ")}}
Date: {{publish_date}}
Modified: {{update_date}}
Category: misc
Tags: {{tag_str}}
Slug: {{path[1:].replace('.html', '')}}
Authors: Seth Gottlieb

{{content}}

"""

if __name__ == "__main__":
    blog_data = feedparser.parse("feed.atom")
    template = Template(MD_TEMPLATE)

    for entry in blog_data["entries"]:
        status = entry["blogger_status"]
        content_type = entry["blogger_type"]
        
        if status == "LIVE" and content_type == "POST":
            context = {}
            context["path"] = entry["blogger_filename"]
            context["title"] = entry["title"]
            context["publish_date"] = entry["published"]
            context["update_date"] = entry["updated"]
            if len(entry["content"]) > 1:
                print("more than one content")
            context["content"] = html2markdown.convert(entry["content"][0]["value"])

            if "tags" in entry.keys():
                context["tag_str"] = ", ".join([tag["term"] for tag in entry["tags"]])
                
        file_path = "content/" + context["path"].replace(".html", ".md")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(template.render(**context))