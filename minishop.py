# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:54:58 2019

@author: wanda
"""

from threading import Thread
from queue import Queue
import random
import time

#20 products in my mini shop
product_dict={'food':{'apple':100,
                      'orange':50,
                      'chocolate':20,
                      'bottle water':30,
                      'milk':30,
                      'salt':20},
                  'home':{'bowl':10,
                      'cup':5,
                      'pillow':10,
                      'shampoo':15,
                      'soap':4
                      },
                'toy':{'lego':30,
                     'doll':20,
                     'puzzle':15
                      },
                 'video game':{'mario':10,
                           'sims':5,
                           'minecraft':8,
                           'cooking fever':6,
                           'pacman':4,
                           'plantsvszombies':6} 
                 }
# get the list of all products sold in this shop
product_list=[]
for k,v in product_dict.items():
    for k1,v1 in v.items():
        product_list.append(k1)
        
class Cashier(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue=queue
        
    def run(self):
        while True:
            #Get the work from the queue
            product,num=self.queue.get()
            try:
                if customer_buy(product,num):
                    print("Customer bought {} {} at {} cashier".format(num,product,self.name))
                else:
                    print("Sorry, the purchase could not be completed at cashier {}".format(self.name))
            finally:
                self.queue.task_done()


#buy behavior        
def customer_buy(product,num):
    #customer sprends different time at cashier
    time.sleep(random.choice(range(10)))
    for k,v in product_dict.items():
        if product in v.keys():
            if num<=v[product]:
                v[product]=v[product]-num
                return 1
    return 0

#create a random customer to buy stuffs
def customer():
    return random.choice(product_list),random.choice(range(100))


def main():
    q=Queue()
#cashier_busy=threading.Lock()
    #Create three cashiers thread
    for x in range(3):
        cashier=Cashier(q)
        cashier.daemon=True
        cashier.start()
    
    #put all customers into the queue as a tuple
    for c in range(10):
        q.put(customer())
    
    q.join()
    
if __name__=='__main__':
    main()
