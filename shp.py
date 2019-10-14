"""senaps html parser

there is no parsing thing going on actually, we're just removeing links from
html files! this module contains functions needed to crawl a folder, 
replace_links and write the data back to a file.

    - crawl_path()  crawl the given path
    - replace_links()  replace the links with a #
    - write_file()  write some data to a file
    - run()  base function for the module
"""
import os, sys

from bs4 import BeautifulSoup


def crawl_path(folder_name):
    """crawl the given path

    this function will receive a `folder_name` and will try to crawl the whole
    path for all the files which live there. 
    then the function will check if the file ends with `.html` stating that 
    it's a `html` file and we need to parse it. the file's name is then added
    to a list and the whole list is the returned in the end of the function.

    :arg folder_name: str, name of the folder app should crawl for `html` files
    :returns: list of path's of `html` files found in the given directory
    """
    files_list = list()
    for root, dir, files in os.walk(folder_name):
        for _ in files:
            if _.endswith(".html"):
                file_name = os.path.join(root, _)
                files_list.append(file_name)

    return files_list


def replace_links(name):
    """replace the links with a #

    this function will receive a filename, will open it, parse the data and
    then will try to find all the links from the file. we will remove the
    link `url` with a `#` and return the data alongside the name.
    we will check if the link's `href` is starting with  `http`. this will
    match both `http` and `https` links that are going out of our local
    html boundary. there may be other links that aren't starting with `html`
    but we are not worried about that, just yet.
    
    :arg name: str, path/name of a file to be opened and parsed
    :returns: tuple, name of the file and the content of that file
    """
    if not name.endswith("html"):
        raise ValueError("the name should be the full path of a html file")
    with open(name, "r") as tmp_file:
        html = tmp_file.read()
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href.startswith("http"):
            link['href'] = "#"
    return name, str(soup)


def write_file(name, data):
    """write the given data to the given file

    receive a `name` and open the file with that name, then try to write the
    given `data` to it. we will raise an error if the file doesn't exist.

    :arg name: str, path/name of the file to write to
    :arg data: str, the text to be written to the file
    """
    if not os.path.exists(name):
        raise IOError(f"{name} doesn't exist")
    with open(name, "w") as tmp_file:
        tmp_file.write(data)


def run(folder_name):
    files_list = crawl_path(folder_name=folder_name)
    removed_links = list(map(replace_links, files_list))
    list(map(write_file, removed_links))


if __name__ == "__main__":
    folder_name = sys.argv[1]
    run(folder_name)

