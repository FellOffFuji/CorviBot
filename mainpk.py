import discord
import random
import settings
import pandas as pd
import numpy as np
import re

from maincommon import clean_args
from maincommon import send_query_msg
from maincommon import find_value_in_table
from maincommon import cc_color_dictionary

from maincommon import bot, commands_dict, errlog

MAX_QUERY = 5
PROBABLY_INFINITE = 99 # don't know when we'll ever need this, but..

help_categories = {"Lookups": ':mag: **Lookups**',
                  "Rollers": ':game_die: **Rollers**',
                  "Helpers": ':thumbsup: **Helpers**',
                  "Reminders (Base)": ':information_source: **Reminders (Base)**',
                  "Reminders (Optional)": ':trophy: **Reminders (Advanced Content)**',
                  "Safety Tools": ':shield: **Safety Tools**'}

@bot.tree.command(name='action', description=commands_dict['action'])
async def action(interaction: discord.Interaction):

    trainer_info = {
        "Name": "Wixom",
        "Trainer Types": ["Water", "Steel"],
        "Heart": 'd4',
        "Tactics": 'd4',
        "Research": 'd4',
        "Fitness": 'd4'
    }

    pokemon_info = {
        "Species": "CorviKnight",
        "Nickname": "not progbot",
        "Type": ["Flying", "Steel"],
        "Toughness": 4,
        "Wounds": 0,
        "Mastery": 0,
        "Status": "OK"
    }

    embed = discord.Embed(title="Action Panel", color=discord.Color.blue())

    embed.add_field(
        name="Trainer Info",
        value=(
            f"**Name:** {trainer_info['Name']}\n"
            f"**Trainer Types:** {trainer_info['Trainer Types'][0]}, {trainer_info['Trainer Types'][1]}\n"
            f"**Heart:** {trainer_info['Heart']}\n"
            f"**Tactics:** {trainer_info['Tactics']}\n"
            f"**Research:** {trainer_info['Research']}\n"
            f"**Fitness:** {trainer_info['Fitness']}"
        ),
        inline=False
    )

    embed.add_field(
        name="Pokémon Info",
        value=(
            f"**Species:** {pokemon_info['Species']}\n"
            f"**Nickname:** {pokemon_info['Nickname']}\n"
            f"**Type:** {pokemon_info['Type'][0]}, {pokemon_info['Type'][1]}\n"
            f"**Toughness:** {pokemon_info['Toughness']}\n"
            f"**Wounds:** {pokemon_info['Wounds']}\n"
            f"**Mastery:** {pokemon_info['Mastery']}\n"
            f"**Status:** {pokemon_info['Status']}"
        ),
        inline=False
    )

    class ActionButtons(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label="Roll", style=discord.ButtonStyle.primary)
        async def roll_button(self, interaction_button: discord.Interaction, button: discord.ui.Button):
            await interaction_button.response.send_message("You rolled!", ephemeral=True)

        @discord.ui.button(label="Call Action", style=discord.ButtonStyle.primary)
        async def call_button(self, interaction_button: discord.Interaction, button: discord.ui.Button):
            await interaction_button.response.send_message("Action called!", ephemeral=True)

        @discord.ui.button(label="Invoke", style=discord.ButtonStyle.primary)
        async def invoke_button(self, interaction_button: discord.Interaction, button: discord.ui.Button):
            await interaction_button.response.send_message("You invoke'd!", ephemeral=True)

        @discord.ui.button(label="Forfeit Turn", style=discord.ButtonStyle.primary)
        async def forfeit_button(self, interaction_button: discord.Interaction, button: discord.ui.Button):
            await interaction_button.response.send_message("You forfeited your turn.", ephemeral=True)

        @discord.ui.button(label="SOS", style=discord.ButtonStyle.danger)
        async def forfeit_button(self, interaction_button: discord.Interaction, button: discord.ui.Button):
            await interaction_button.response.send_message("todo.", ephemeral=True)


    await interaction.response.send_message(embed=embed, view=ActionButtons())