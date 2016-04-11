# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:29:37 2016

@author: c1533095
"""

class module:
    def __init__(self, ModuleID, Name, ModuleCode):
        self.ModuleID = int(ModuleID)
        self.Name = str(Name)
        self.ModuleCode = int(ModuleCode)
        
    def __str__(self):
        return "ModuleID: %d, Name: %s, ModuleCode: %s" % (self.ModuleID, self.Name, self.ModuleCode)
        
     def Take_Test(TestID, StudentID):
        #list
        pass
    def View_Lessons(ModuleID, LessonID):
        #display
        pass