#Q 5
import pickle 
import datetime
import time
import random

example_dict = { 1:"I love those who can smile in trouble Leonardo da Vinci"
                ,2:"Time means a lot to me because, you see, I, too, am also a learner and am often lost in the joy of forever developing and simplifying. If you love life, do not waste time, for time is what life is made up of. Bruce Lee"
                ,3:"Life is what happens when you\'re busy making other plans. John Lennon"
                ,4:"It is better to be hated for what you are than to be loved for what you are not. Andre Gide"
                ,5:"Dost thou love life? Then do not squander time, for that is the stuff life is made of. Benjamin Franklin"
                ,6:"Life is like playing a violin in public and learning the instrument as one goes on. Samuel Butler"
                ,7:"In the end, it is not the years in your life that count. It is the life in your years. Abraham Lincoln"}

pickle_out = open("dict.pickle","wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()

pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)



print "Date : " + datetime.datetime.now().strftime("%y-%m-%d")
print "Time : " + datetime.datetime.now().strftime("%H:%M")

print "#################################################################################################################"
print " "*(100/2) + "Today's quote"

for i in range(4):
    print "#"+" "*111+"#"

print " "*3 + str(example_dict[random.randint(1,7)])
for i in range(4):
    print "#"+" "*111+"#"
    
print "#################################################################################################################"

