    # """
    # >>> search_for(['coin', 'crown', 'key'], 'key')
    # True
    # >>> search_for([], 'key')
    # False
    # >>> search_for(['coin', 'crown', 'key'], 'dagger')
    # False
    # >>> box = ['coin', 'coin', 'silver coin', 'silver key', 'needle', 'golden crown',
    # ...        ['coin', 'coin', 'coin'],
    # ...        'diamond',
    # ...        'small diamond',
    # ...        ['coin'],
    # ...        ['potion of healing', 'scroll'],
    # ...        ['golden key']]
    # >>> search_for(box, 'coin')
    # True
    # >>> search_for(box, 'silver crown')
    # False
    # >>> search_for(box, 'small diamond')
    # True
    # >>> search_for(box, 'potion of healing')
    # True
    # >>> search_for(box, 'potion of fear')
    # False
    # >>> search_for(box, 'potion')
    # False
    # >>> search_for(box, 'healing')
    # False
    # """