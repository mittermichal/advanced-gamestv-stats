# Greatshot
Demo analysis, cutting, video rendering for IdTech3 games mainly Wolfenstein: Enemy Territory
[![Discord](https://img.shields.io/discord/546291405404897290?label=discord)](https://discord.gg/p59kWdF)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=BRRRFPT7N9NP6&currency_code=EUR&source=url)
## what it can do:
- cut demos (dm_84/tv_84) -> dm_84
- export demos (dm_84/tv_84) to json and analyze it to output:
	- hit regions (headshots) counter
	- fast consecutive kills <img src="/app/static/excellent.png" height="25" width="25"/> [example](https://streamable.com/a5tx7)
	- consecutive headshots - [example](https://streamable.com/e4ogi)
	- revive stats
- download ETTV demo (tv_84) from [gamestv.org](http://gamestv.org)
- render demo to video and publish it - [example](https://streamable.com/2d77)
- link highlights and statistics in comments of gamestv match
- render highlights from gamestv match
- add player name + flag to highlight [example](https://streamable.com/zn7r4)

## what it could do in future:
- create database of players with statistics
- visualize timeline of match
- retrieve true damage stats when its bugged to 0
- support other IdTech3 games/mods: RTCW, Quake3, ...

This project uses  [hannes's](http://www.crossfire.nu/user/view/id/6710) modified [Tech3 Demo API - 0.1](http://www.crossfire.nu/news/4632/tech3-demo-api-01) to cut and export demos.
It was modified to be able to cut [ETTV](http://wolfwiki.anime.net/index.php/ETTV:Viewer%27s_Guide) demo with selected player's POV. My modification: [Tech3 Demo API](https://github.com/mittermichal/Anders.Gaming.LibTech3)
