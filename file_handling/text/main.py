def read_file(filename):
    file = open(filename, "r",encoding='utf-8')
    content = file.read()
    print(content)
    file.close()
    return content

# content = read_file("krish.txt")

def write_file(filename):
    file=open(filename, "w",encoding='utf-8')
    content=file.write("""A playboy billionaire by day, Bruce Wayne’s double life affords him the comfort of a life without financial worry, 
               a loyal butler-turned-guardian and the perfect base of operations in the ancient network of caves
               beneath his family’s sprawling estate. By night, however, 
               he sheds all pretense, dons his iconic scalloped cape and pointed cowl and takes to the shadowy streets,
               skies and rooftops of Gotham City.He is vengeance. He is the night. He is Batman.""")
    print(content)
    file.close()
   

# content=write_file("krish.txt")

def append_file(filename):
    file=open(filename,'a',encoding='UTF-8')
    content=file.write("""Batman prides himself on being prepared for any emergency. He’s devised various fail-safes and 
                       plans for any number of potential doomsday scenarios. As the sometime leader of the Justice League 
                       and the patriarch of the Batman Family, he’s more than ready to take on whatever the universe throws at him. 
                       Armed with a utility belt full of Batarangs, a Batsuit loaded with cutting-edge technology and his own hair-trigger 
                       reflexes, Batman is ready to strike fear into the hearts of criminals everywhere.""")
    file.close()
    print(content)

content=append_file("krish.txt")

def truncate(filename):
    file=open(filename,"w")
    file.close()
    
# truncate("krish.txt")