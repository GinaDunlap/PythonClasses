class Top:
    def __init__(self, style, sleeve_length, color):
        self.style = style
        self.sleeve_length = sleeve_length
        self.color = color
        self.is_discounted = False
        self.style = []
    
    def on_sale(self):
        self.is_discounted = True

    def add_style(self,style):
        self.styles.append(style)

ginas_top = Top("Blouse","Short_Sleeve","Pink")
troys_top = Top("Tee", "Long_Sleeve", "Black")

ginas_top.on_sale()
print(ginas_top.is_discounted)
print(troys_top.is_discounted)
