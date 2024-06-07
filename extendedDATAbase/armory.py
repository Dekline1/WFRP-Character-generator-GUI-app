armour = {
    "Leather": {
        "Leather Skullcap": {"Cost": "3 gc", "Encumbrance": "-", "Location": "Head", "Armour points": 1, "Availability": "Common"},
        "Leather Jerkin": {"Cost": "6 gc", "Encumbrance": "40", "Location": "Body", "Armour points": 1, "Availability": "Common"},
        "Leather Leggings": {"Cost": "10 gc", "Encumbrance": "20", "Location": "Legs", "Armour points": 1, "Availability": "Common"},
        "Leather Jack": {"Cost": "12 gc", "Encumbrance": "50", "Location": "Body, Arms", "Armour points": 1, "Availability": "Common"},
        "Full Leather Armour": {"Cost": "25 gc", "Encumbrance": "80", "Location": "All", "Armour points": 1, "Availability": "Average"}
    },
    "Chain": {
        "Chain Shirt": {"Cost": "60 gc", "Encumbrance": "60", "Location": "Body", "Armour points": 2, "Availability": "Average"},
        "Mail Coif": {"Cost": "20 gc", "Encumbrance": "30", "Location": "Head", "Armour points": 2, "Availability": "Average"},
        "Sleeved Mail Shirt": {"Cost": "95 gc", "Encumbrance": "80", "Location": "Body, Arms", "Armour points": 2, "Availability": "Average"},
        "Mail Coat": {"Cost": "75 gc", "Encumbrance": "80", "Location": "Body, Legs", "Armour points": 2, "Availability": "Average"},
        "Sleeved Mail Coat": {"Cost": "130 gc", "Encumbrance": "100", "Location": "Body, Arms, Legs", "Armour points": 2, "Availability": "Average"},
        "Mail Leggings": {"Cost": "20 gc", "Encumbrance": "40", "Location": "Legs", "Armour points": 2, "Availability": "Scarce"},
        "Full Mail Armour": {"Cost": "170 gc", "Encumbrance": "210", "Location": "All", "Armour points": 3, "Availability": "Scarce"}
    },
    "Plate": {
        "Plate Helmet": {"Cost": "30 gc", "Encumbrance": "40", "Location": "Head", "Armour points": 2, "Availability": "Scarce"},
        "Breastplate": {"Cost": "70 gc", "Encumbrance": "75", "Location": "Body", "Armour points": 2, "Availability": "Scarce"},
        "Plate Bracers": {"Cost": "60 gc", "Encumbrance": "30", "Location": "Arms", "Armour points": 2, "Availability": "Scarce"},
        "Plate Leggings": {"Cost": "70 gc", "Encumbrance": "40", "Location": "Legs", "Armour points": 2, "Availability": "Scarce"},
        "Full Plate Armour": {"Cost": "400 gc", "Encumbrance": "395", "Location": "All", "Armour points": 5, "Availability": "Rare"}
    }
}

melee_weapons = {
    "Buckler": {"Cost": "2 gc", "Encumbrance": "10", "Group": "Parrying", "Damage": "Strength Bonus 4", "Qualities": "Balanced, Defensive, Pummelling", "Availability": "Average"},
    "Dagger": {"Cost": "1 gc", "Encumbrance": "10", "Group": "Ordinary", "Damage": "Strength Bonus-3", "Qualities": "None", "Availability": "Common"},
    "Demilance (Cavalry Spear)": {"Cost": "20 gc", "Encumbrance": "75", "Group": "Cavalry", "Damage": "Strength Bonus", "Qualities": "Fast, Impact, Tiring", "Availability": "Scarce"},
    "Flail*": {"Cost": "15 gc", "Encumbrance": "95", "Group": "Flail", "Damage": "Strength Bonus+1", "Qualities": "Impact, Tiring", "Availability": "Scarce"},
    "Foil": {"Cost": "18 gc", "Encumbrance": "40", "Group": "Fencing", "Damage": "Strength Bonus-2", "Qualities": "Fast, Precise", "Availability": "Rare"},
    "Gauntlet/Knuckle-duster": {"Cost": "1 gc", "Encumbrance": "1", "Group": "Ordinary", "Damage": "Strength Bonus-3", "Qualities": "Pummelling", "Availability": "Common"},
    "Great Weapon": {"Cost": "20 gc", "Encumbrance": "200", "Group": "Two-handed", "Damage": "Strength Bonus", "Qualities": "Impact, Slow", "Availability": "Average"},
    "Halberd*": {"Cost": "15 gc", "Encumbrance": "175", "Group": "Two-handed", "Damage": "Strength Bonus", "Qualities": "Special", "Availability": "Common"},
    "Hand Weapon (sword etc)": {"Cost": "10 gc", "Encumbrance": "50", "Group": "Ordinary", "Damage": "SE", "Qualities": "None", "Availability": "Common"},
    "Improvised": {"Cost": "-", "Encumbrance": "35", "Group": "Ordinary", "Damage": "Strength Bonus-4", "Qualities": "None", "Availability": "-"},
    "Lance": {"Cost": "15 gc", "Encumbrance": "100", "Group": "Cavalry", "Damage": "Strength Bonus+1", "Qualities": "Fast, Impact, Tiring", "Availability": "Rare"},
    "Main Gauche": {"Cost": "4 gc", "Encumbrance": "15", "Group": "Parrying", "Damage": "Strength Bonus-3", "Qualities": "Balanced, Defensive", "Availability": "Scarce"},
    "Morning Star": {"Cost": "15 gc", "Encumbrance": "60", "Group": "Flail", "Damage": "Strength Bonus", "Qualities": "Impact, Tiring", "Availability": "Scarce"},
    "Quarter Staff": {"Cost": "3 $", "Encumbrance": "50", "Group": "Ordinary", "Damage": "Strength Bonus-2", "Qualities": "Defensive, Pummelling", "Availability": "Plentiful"},
    "Rapier": {"Cost": "18 gc", "Encumbrance": "40", "Group": "Fencing", "Damage": "Strength Bonus-1", "Qualities": "Fast", "Availability": "Scarce"},
    "Shield": {"Cost": "10 gc", "Encumbrance": "50", "Group": "Ordinary", "Damage": "Strength Bonus-2", "Qualities": "Defensive, Special", "Availability": "Common"},
    "Spear": {"Cost": "10 gc", "Encumbrance": "50", "Group": "Ordinary", "Damage": "Strength Bonus", "Qualities": "Fast", "Availability": "Common"},
    "Sword-breaker": {"Cost": "5 gc", "Encumbrance": "40", "Group": "Parrying", "Damage": "Strength Bonus-3", "Qualities": "Balanced, Special", "Availability": "Scarce"},
    "Unarmed": {"Cost": "-", "Encumbrance": "-", "Group": "Ordinary", "Damage": "Strength Bonus-4", "Qualities": "Special", "Availability": "-"}
}

missile_weapons = {
    "Blunderbuss": {"Cost": "70 gc", "Encumbrance": 50, "Group": "Gunpowder", "Damage": 3, "Range": "32/-", "Reload": "3 Full/6 Full", "Qualities": ["Shrapnel", "Unreliable"], "Availability": "Scarce"},
    "Bola": {"Cost": "7s", "Encumbrance": 20, "Group": "Entangling", "Damage": 1, "Range": "8/16", "Reload": "Half", "Qualities": ["Snare"], "Availability": "Scarce"},
    "Bow": {"Cost": "10 gc", "Encumbrance": 80, "Group": "Ordinary", "Damage": 3, "Range": "24/48", "Reload": "Half", "Qualities": [], "Availability": "Common"},
    "Crossbow": {"Cost": "25 gc", "Encumbrance": 120, "Group": "Ordinary", "Damage": 4, "Range": "30/60", "Reload": "Full", "Qualities": [], "Availability": "Average"},
    "Crossbow Pistol": {"Cost": "35 gc", "Encumbrance": 23, "Group": "Crossbow", "Damage": 4, "Range": "8/16", "Reload": "Full", "Qualities": [], "Availability": "Rare"},
    "Elfbow": {"Cost": "70 gc", "Encumbrance": "T", "Group": "Longbow", "Damage": 3, "Range": "36/72", "Reload": "Half", "Qualities": ["Armour Piercing"], "Availability": "Very Rare"},
    "Firearm": {"Cost": "300 gc", "Encumbrance": 30, "Group": "Gunpowder", "Damage": 4, "Range": "24/48", "Reload": "2 Full", "Qualities": ["Impact", "Unreliable"], "Availability": "Very Rare"},
    "Hochland Long Rifle": {"Cost": "450 gc", "Encumbrance": 70, "Group": "Engineer", "Damage": 4, "Range": "48/96", "Reload": "2 Full", "Qualities": ["Impact", "Unreliable"], "Availability": "Very Rare"},
    "Improvised": {"Cost": "—", "Encumbrance": 10, "Group": "Ordinary", "Damage": "SB—4", "Range": "6/—", "Reload": "Half", "Qualities": [], "Availability": "—"},
    "Javelin": {"Cost": "25s", "Encumbrance": 30, "Group": "Ordinary", "Damage": "SB-1", "Range": "8/16", "Reload": "Half", "Qualities": [], "Availability": "Average"},
    "Lasso": {"Cost": "1 gc", "Encumbrance": 10, "Group": "Entangling", "Damage": "n/a", "Range": "8/—", "Reload": "Half", "Qualities": ["Snare"], "Availability": "Plentiful"},
    "Longbow": {"Cost": "15 gc", "Encumbrance": 90, "Group": "Longbow", "Damage": 3, "Range": "30/60", "Reload": "Half", "Qualities": ["Armour Piercing"], "Availability": "Average"},
    "Net": {"Cost": "3 gc", "Encumbrance": 60, "Group": "Entangling", "Damage": "n/a", "Range": "4/8", "Reload": "Full", "Qualities": ["Snare"], "Availability": "Plentiful"},
    "Pistol": {"Cost": "200 gc", "Encumbrance": 25, "Group": "Gunpowder", "Damage": 4, "Range": "8/16", "Reload": "2 Full", "Qualities": ["Impact", "Unreliable"], "Availability": "Very Rare"},
    "Repeater Crossbow": {"Cost": "100 gc", "Encumbrance": 150, "Group": "Crossbow", "Damage": 2, "Range": "16/32", "Reload": "Free", "Qualities": ["Special"], "Availability": "Very Rare"},
    "Repeater Firearm": {"Cost": "600 gc", "Encumbrance": 30, "Group": "Engineer", "Damage": 4, "Range": "24/48", "Reload": "Free", "Qualities": ["Experimental", "Special"], "Availability": "Very Rare"},
    "Repeater Pistol": {"Cost": "400 gc", "Encumbrance": 25, "Group": "Engineer", "Damage": 4, "Range": "8/16", "Reload": "Free", "Qualities": ["Experimental", "Special"], "Availability": "Very Rare"},
    "Shortbow": {"Cost": "7 gc", "Encumbrance": 75, "Group": "Ordinary", "Damage": 3, "Range": "16/32", "Reload": "Half", "Qualities": [], "Availability": "Common"},
    "Sling": {"Cost": "4 gc", "Encumbrance": 10, "Group": "Sling", "Damage": 3, "Range": "16/32", "Reload": "Half", "Qualities": [], "Availability": "Common"},
    "Spear": {"Cost": "10 gc", "Encumbrance": 50, "Group": "Ordinary", "Damage": "SB", "Range": "8/-", "Reload": "Half", "Qualities": [], "Availability": "Common"},
    "Staff Sling": {"Cost": "6 gc", "Encumbrance": 50, "Group": "Sling", "Damage": 4, "Range": "24/48", "Reload": "Full", "Qualities": [], "Availability": "Rare"},
    "Throwing Axe/Hammer": {"Cost": "5 gc", "Encumbrance": 40, "Group": "Throwing", "Damage": "SB-2", "Range": "8/-", "Reload": "Half", "Qualities": [], "Availability": "Average"},
    "Throwing Dagger/Star": {"Cost": "3 gc", "Encumbrance": 10, "Group": "Throwing", "Damage": "SB-3", "Range": "6/12", "Reload": "Half", "Qualities": [], "Availability": "Common"},
    "Whip": {"Cost": "2 gc", "Encumbrance": 5, "Group": "Entangling", "Damage": "SB-4", "Range": "6/-", "Reload": "Half", "Qualities": ["Snare"], "Availability": "Average"}
}

ammunition = {
    "Arrows (5)": {"Cost": "1s", "Encumbrance": 10, "Availability": "Common"},
    "Bolts (5)": {"Cost": "1s", "Encumbrance": 10, "Availability": "Average"},
    "Firearm Shot (10)": {"Cost": "1s", "Encumbrance": 10, "Availability": "Rare"},
    "Gunpowder (per shot)": {"Cost": "3s", "Encumbrance": 1, "Availability": "Very Rare"}
}







