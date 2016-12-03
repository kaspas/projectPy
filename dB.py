#!/usr/bin/python

Items=[]
task=[[]]
    def get_item(position):
        return list[position]
    def set_item(item):
        Items.insert(len(Items),item)
        task[len(Items)-1]=[]
    def set_task(position,item):
        task[position].insert(len(task[position]),item)
    def get_task(position): 
        return task[position]

