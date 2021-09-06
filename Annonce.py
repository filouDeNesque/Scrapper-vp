class Annonce:
    def __init(self, title, price, desc, link):
        self.title = title
        self.price = price
        self.desc = desc
        self.link = link


    def toString(self):
        print('Title : '+ self.title)
        print('Price : '+ self.price)
        print('Desc : '+ self.desc)
        print('Link : '+ self.link)
