root = bespoke.get_root() + 48
scale = bespoke.get_scale()

def on_pulse():
   step = bespoke.get_step(8)
   this.play_note(random.choice(scale) + root, walk([110,30,60,30],step), 1.0/16)
   
def walk(list, step):
   return list[step % len(list)] 