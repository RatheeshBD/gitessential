# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 10:32:30 2023

@author: Hp
"""

class Node:
    def __init__(self,data):
       self.data=data;
       self.next=None;

class SinglyLinkedList:
    def __init__(self):
      self.head=None;
      self.tail=None;
  
    def addNode(self,data):
        newNode=Node(data);

        if(self.head==None):
            self.head=newNode;
            self.tail=newNode;
        else:
            self.tail.next=newNode;
            self.tail=newNode;


    def display(self):
        current=self.head;
        if(self.head==None):
            print("List is empty");
            return;
        print("Nodes of SinglyLinkedList:");
        while(current!=None):
            print(current.data),
            current=current.next;

Slist=SinglyLinkedList();


Slist.addNode(1);
Slist.addNode(2);
Slist.addNode(3);
Slist.addNode(4);

Slist.display();