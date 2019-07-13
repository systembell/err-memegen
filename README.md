# Overview

The only meme plugin for errbot seemed rather opinionated, and other bot frameworks seemed to all have dynamic meme generation builtin, so I decided to bring it to errbot. Big ups to @nicolewhite for most of the heavy lifting.

# Installation

`!repos install https://github.com/systembell/err-memegen.git`


# Usage

`!meme help`
```
* Commands:*
* `!meme template_name;top_row;bottom_row` generate a meme
   (NOTE: template_name can also be a URL to an image)
* `!meme templates` View templates
* `!meme help` Shows this menu
```

`!meme templates`  
```
• aag Ancient Aliens Guy  
• ackbar It's A Trap!  
• afraid Afraid to Ask Andy  
...
```

`!meme success;we have;a memebot`

![success we have a memebot](https://memegen.link/success/we_have/a_memebot.jpg "We have a memebot")


## Sources

* https://github.com/jacebrowning/memegen
* https://github.com/nicolewhite/slack-meme
