
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top. 
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


import pandas as pd
import os
import sys


# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

publications_ref = pd.read_csv("publications.tsv", sep="\t", header=0)
publications_nr = pd.read_csv("publications_nr.tsv", sep="\t", header=0)
publications_jn = pd.read_csv("publications_jn.tsv", sep="\t", header=0)
publications_thesis = pd.read_csv("publications_thesis.tsv", sep="\t", header=0)

# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}


def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:
def publicationPageGenerator(category):
    if category == "ref":
        publications = publications_ref
        collection_cat = """collection: publications"""
    elif category == "nonref":
        publications = publications_nr
        collection_cat = """collection: publications_nr"""
    elif category == "journal":
        publications = publications_jn
        collection_cat = """collection: publications_jn"""
    elif category == "thesis":
        publications = publications_thesis
        collection_cat = """collection: publications_thesis"""
    
    for row, item in publications.iterrows():
        
        md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
        html_filename = str(item.pub_date) + "-" + item.url_slug
        year = item.pub_date[:4]
        
        ## YAML variables
        
        md = "---\ntitle: \""   + item.title + '"\n'
        
        md += collection_cat
        
        md += """\npermalink: /publication/""" + html_filename
        
        if len(str(item.excerpt)) > 5:
            md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"
        
        md += "\ndate: " + str(item.pub_date) 
        
        md += "\nvenue: '" + html_escape(item.venue) + "'"
        
        if len(str(item.paper_url)) > 5:
            md += "\npaperurl: '" + item.paper_url + "'"
        
        md += "\ncitation: '" + html_escape(item.citation) + "'"
        
        md += "\n---"
        
        ## Markdown description for individual page
        if len(str(item.excerpt)) > 5:
            md += "\n**Abstract**   \n" + html_escape(item.excerpt) + "\n"
            
        md += "\n**Recommended citation:**   \n" + item.citation

        if len(str(item.paper_url)) > 5:
            md += "\n\n<a href='" + item.paper_url + "'>Download paper here</a>\n" 
        
        md_filename = os.path.basename(md_filename)
        
        if category == "ref":
            with open("../_publications/" + md_filename, 'w') as f:
                f.write(md)
        elif category == "nonref":
            with open("../_publications_nr/" + md_filename, 'w') as f:
                f.write(md)
        elif category == "journal":
            with open("../_publications_jn/" + md_filename, 'w') as f:
                f.write(md)
        elif category == "thesis":
            with open("../_publications_thesis/" + md_filename, 'w') as f:
                f.write(md)
    
    return None


def main():
    category = sys.argv[1]
    publicationPageGenerator(category)
    return True

if __name__ == '__main__':
    main()
