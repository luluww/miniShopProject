# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:54:58 2019

@author: wanda
"""

import threading
from queue import Queue
import random

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
                           'plantsvszombies':6
                     } 
             }
             
# get the list of all products sold in this shop
product_list=[]
for k,v in product_dict.items():
    for k1,v1 in v.items():
        product_list.append(k1)

#buy behavior        
def customer_buy(product,num):
    with cashier_busy:
        for k,v in product_dict.items():
            if product in v.keys():
                if num<=v[product]:
                    v[product]=v[product]-num
                    return 1
        return 0

#create a random customer to buy stuffs
def customer():
    return random.choice(product_list),random.choice(range(100))

def cashier():
    while True:
        product,num=q.get()
        if customer_buy(product,num):
            print("a customer bought %s %s at # %s cashier."%(num,product,threading.current_thread().name))
        else:
            print("sorry, the purchase could not be completed! at %s"%(threading.current_thread().name))
        q.task_done()

cashier_busy=threading.Lock()

q=Queue()
  
#create three threads to represent three cashiers
for i in range(10):
    t=threading.Thread(target=cashier)
    t.daemon=True
    t.start()
    
#create 10 customers
for c in range(10):
    q.put(customer())

q.join()
        