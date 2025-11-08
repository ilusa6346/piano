class Slider:
    def __init__(self,x,y,widht,min_val,max_val, step = 1,initial = None,label = '',value_to_text = None):
        self.track_rect = Rect(x,y, widht,6)
        self.handle_radius = 10
        self.min = float(min_val)
        self.max = float(max_val)
        self.step = float(step)
        if initial is not None:
            self.value = float(initial)
        else:
            self.value = float(min_val)    


