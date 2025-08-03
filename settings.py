import os
from dotenv import load_dotenv
#BOT FILES

load_dotenv()
bot_token = os.getenv('DISCORD_TOKEN')
# notion_pmc_token = os.getenv('PMC_KEY')

commands_table_name = "tables/commands.tsv"
user_levels_table_name = "tables/user_levels.tsv"
log_file = "corvibot.log"
error_file = "somethingbroke.log"
#prefixfile = "prefixes.json"

#BOT SETTINGS
default_status = "PokeyManz RPG"

#POKEYMANZ DATA FILES

audiencesave = "save/audiences.json"
spotlightsave = "save/spotlights.json"

#HARDCODED LINKS
character_sheet = "https://docs.google.com/spreadsheets/d/158iI4LCpfS4AGjV5EshHkbKUD4GxogJCiwZCV6QzJ5s/edit#gid=295914024"
bug_image = "https://raw.githubusercontent.com/gskbladez/meddyexe/master/virusart/bug.png"
invite_link = ""
# notion_pmc_id = ""
bugreport_image = "https://raw.githubusercontent.com/gskbladez/meddyexe/master/virusart/bug.png"
bugreport_channel_id = 1401570913404719138
admin_guild = 1401569514797273141

#CUSTOM EMOJI SUPPORT
source_guild_id = 1401569514797273141
custom_emojis = {"instant": r"<:instant:892170110465363969>", "cost": r"<:cost:892170110364680202>",
                 "roll": r"<:roll:892170110377295934>", "underflow": r"<:underflow:901995743752106064>",
                 "KissRaffi": r"<:KissRaffi:911806713496223775>", "HappyRaffi": r"<a:HappyRaffi:911806713890476032>", "devilish": r"👿"}

# /home/bladez/update-proggers

#NETBATTLER CONSTANTS