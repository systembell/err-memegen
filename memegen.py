import os
import re
from errbot import BotPlugin, botcmd, arg_botcmd, webhook
import requests
from urllib.parse import unquote_plus, quote


class GenerateMeme():

    def __init__(self):
        self.BASE_URL = "https://memegen.link"
        self.template_info = self.get_template_info()
        self.valid_templates = self.get_valid_templates()
        self.template_list = self.get_template_list()

    def get_valid_templates(self):
        return [x[0] for x in self.template_info]

    def get_template_info(self):
        template = requests.get(self.BASE_URL + "/api/templates/").json()

        data = []

        for description, api_link in template.items():
            alias = api_link.split("/api/templates/")[1]
            link = "https://memegen.link/{}/your-text/goes-here.jpg".format(alias)

            data.append((alias, description, link))

        return sorted(data, key=lambda x: x[0])

    def get_template_list(self):
        help = ""
        for alias, description, example_link in self.template_info:
            help += '- `{}` {}\n'.format(alias, description)
        return help

    def build_url(self, template, top, bottom, alt=None):
        path = "/{0}/{1}/{2}.jpg".format(template, top or '_', bottom or '_')

        if alt:
            path += "?alt={}".format(alt)

        url = self.BASE_URL + path.replace(" ", "_")

        return url

    def bad_template(self, template):
        return ("Template `%s` doesn't exist. "
                "Type `/meme templates` to see valid templates "
                "or provide your own as a URL." % template)

    def help(self):
        return "\n".join([
            "**> Commands:**",
            "* `!meme template_name;top_row;bottom_row` generate a meme",
            "    (NOTE: template_name can also be a URL to an image)",
            "* `!meme templates` View templates",
            "* `!meme help` Shows this menu"
        ])


    def image_exists(path):
        if path.split("://")[0] not in ["http", "https"]:
            return False

        r = requests.head(path)
        return r.ok

class MemeGen(BotPlugin):
    @botcmd(split_args_with=";")
    def meme(self, mess, args):


        memegen = GenerateMeme()

        print(args)
        print(args[0])
        text = args[0]

        if text.lower() in ("help", ""):
            return memegen.help()

        if text.lower() == "templates":
            return memegen.template_list

        template, top, bottom = args
        top = top.replace('?', '~q').replace('%', '~p').replace('#', '~h').replace('/', '~s')
        bottom = bottom.replace('?', '~q').replace('%', '~p').replace('#', '~h').replace('/', '~s')
        if template in memegen.valid_templates:
            meme_url = memegen.build_url(template, top, bottom)
            return meme_url
        elif GenerateMeme.image_exists(template):
            meme_url = memegen.build_url("custom", top, bottom, template)
            return meme_url
        else:
            return memegen.bad_template(template)