inventory = dict()

def addItems():
  gun_names = ['colt', 'beretta', 'glock', 'remington', 'winchester', 'browning', 'smith_wesson', 'walther', 
             'sig_sauer', 'heckler_koch', 'fn_herstal', 'ruger', 'cz', 'kimber', 'springfield', 'taurus', 
             'desert_eagle', 'mossberg', 'kel_tec', 'sako', 'benelli', 'bushmaster', 'stevens', 'steyn', 
             'ar_15', 'm16', 'ak47', 'uzi', 'mp5', 'scar']


  inventory[gun_names[0]] = 800       # colt
  inventory[gun_names[1]] = 750       # beretta
  inventory[gun_names[2]] = 600       # glock
  inventory[gun_names[3]] = 900       # remington
  inventory[gun_names[4]] = 1000      # winchester
  inventory[gun_names[5]] = 850       # browning
  inventory[gun_names[6]] = 950       # smith_wesson
  inventory[gun_names[7]] = 700       # walther
  inventory[gun_names[8]] = 1100      # sig_sauer
  inventory[gun_names[9]] = 1200      # heckler_koch
  inventory[gun_names[10]] = 1400     # fn_herstal
  inventory[gun_names[11]] = 650      # ruger
  inventory[gun_names[12]] = 550      # cz
  inventory[gun_names[13]] = 1300     # kimber
  inventory[gun_names[14]] = 800      # springfield
  inventory[gun_names[15]] = 500      # taurus
  inventory[gun_names[16]] = 1500     # desert_eagle
  inventory[gun_names[17]] = 450      # mossberg
  inventory[gun_names[18]] = 550      # kel_tec
  inventory[gun_names[19]] = 1600     # sako
  inventory[gun_names[20]] = 1700     # benelli
  inventory[gun_names[21]] = 1200     # bushmaster
  inventory[gun_names[22]] = 600      # stevens
  inventory[gun_names[23]] = 1300     # steyr
  inventory[gun_names[24]] = 1100     # ar_15
  inventory[gun_names[25]] = 1800     # m16
  inventory[gun_names[26]] = 900      # ak47
  inventory[gun_names[27]] = 750      # uzi
  inventory[gun_names[28]] = 1000     # mp5
  inventory[gun_names[29]] = 2000     # scar
  user_input = input("Gun name: ")
  print("Price is:", inventory.get(user_input))

addItems()


