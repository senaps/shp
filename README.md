# SHP [Senaps HTML Parser] [havent tested it yet]

this is a small code that I had to write while at work! what this does is
it'll receive a folder name, crawl it to find all the `html` files within
it, check the links in each `html` file and if that link is going out to
the internet, replace it.
this was part of our static site generator thing where we download a
website, replace the links and it's totally ready to be used or served
as a static site

## How to install

to install the project, will there is no installation yet! so one could
get away with just installing `bs4` and then run the code in good old
fashion python script running way! I have placed the `bs4` in the
requirements.txt file, so it's easier to install the deps.

    pip3 install -r requirements.txt
    python3 shp.py <file_name>

although it seems pretty okay, I recommend to install the `bs4` package
on a virtualenv.

    virtualenv -p /usr/bin/python3.7 env
    source env/bin/activate
    pip3 install -r requirements.txt
    python3 shp.py <file_name>


# TODO:

- [ ] setup file and make it a whole package
- [ ] multi folder thing
- [ ] add exception handling
- [ ] logging maybe?
- [ ] threads and multiprocess?