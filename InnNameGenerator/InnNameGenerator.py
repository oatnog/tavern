from flask import Flask
from flask import render_template
from flask import jsonify

import random

app = Flask(__name__)

bonuses = dict(A=['Fighter Attractor', 'Greater daily chance for a hero of this type to enter Tavern'],
               B=['Mage Attractor', 'Greater daily chance for a hero of this type to enter Tavern'],
               C=['Rogue Attractor', 'Greater daily chance for a hero of this type to enter Tavern'],
               D=['Healer Attractor', 'Greater daily chance for a hero of this type to enter Tavern'],
               E=['Ally-Stores', 'Ally who provides a weekly shopping bonus'],
               F=['Ally-Furniture', 'Ally who provides a weekly shopping bonus'],
               GB=['Group Bonding bonus', 'Provides a bonus during brawl event for this outcome'],
               PR=['Personal Reputation bonus', 'Provides a bonus during brawl event for this outcome']
)

starternouns = {'Sage': 'A', 'Wheel': 'A', 'Stone': 'A', 'Dragon': 'A', 'Needle': 'B', 'Spice': 'B', 'Goat': 'B',
         'Cutpurse': 'B', 'Boar': 'C', 'Thimble': 'C', 'Violin': 'C', 'Manticore': 'C', 'Fiddle': 'D', 'Loaf': 'D',
         'Vest': 'D', 'Hobgoblin': 'D', 'Thistle': 'E', 'Rust Monster': 'E', 'Anvil': 'E', 'Shadow': 'E'}

finishernouns = {'Biscuit': 'F', 'Quill': 'F', 'Yak': 'F', 'Thicket': 'F', 'Oliphant': 'A', 'Mill': 'B', 'Crab': 'C',
                 'Nymph': 'D', 'Cleric': 'E', 'Door': 'F', 'Rose': 'A', 'Eel': 'B', 'Candle': 'C', 'Wolf': 'D',
                 'Harp': 'E', 'Whirlpool': 'F', 'Sword': 'A', 'Axe': 'B', 'Inkwell': 'C', 'Zebra': 'D'}

gerund = {
    'Cavorting': 'GB',
    'Bellowing': 'PR',
    'Humming': 'A',
    'Staggering': 'B',
    'Sneaking': 'C',
    'Hopping': 'D',
    'Skipping': 'GB',
    'Sloshing': 'PR',
    'Meandering': 'A',
    'Striking': 'B',
    'Slipping': 'C',
    'Mincing': 'D',
    'Galumphing': 'GB',
    'Bragging': 'PR',
    'Jabbering': 'A',
    'Pulsing': 'B',
    'Scrying': 'C',
    'Mumbling': 'D',
    'Relaxing': 'GB',
    'Brewing': 'PR',
    }

noun_for_gerund = {
    'Pony':'GB',
    'Sailor': 'PR',
    'Mermaid': 'A',
    'Troll': 'B',
    'Knight': 'C',
    'Dragon': 'D',
    'Hero': 'GB',
    'Wizard': 'PR',
    'Hound': 'A',
    'Bard': 'B',
    'Soldier': 'C',
    'King': 'D',
    'Queen': 'GB',
    'Tower': 'PR',
    'Monk': 'A',
    'Cup': 'B',
    'Dwarf': 'C',
    'Castle': 'D',
    'Jester': 'GB',
    'Salamander': 'PR',
}


@app.route('/')
def noun_n_noun():
    inn_name = random.choice(list(starternouns)) + " & " + random.choice(list(finishernouns))
    return render_template('inn_name.html', inn_name=inn_name)

def gerunding_noun():
    inn_name = random.choice(gerund)


@app.route('/starter_n')  # "Noun & Noun"
def snouns_json():
    return jsonify(starternouns)

@app.route('/finisher_n')
def fnouns_json():
    return jsonify(finishernouns)

@app.route('/gerund')
def gerunds_json():
    return jsonify(gerund)

@app.route('/gerund_n')
def gnouns_json():
    return jsonify(noun_for_gerund)


if __name__ == '__main__':
    app.debug = True
    app.run()
