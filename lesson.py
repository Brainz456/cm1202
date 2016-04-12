# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:20:10 2016

@author: c1533095
"""
class lesson:
    def __init__(self, LessonID, LessonMaterials, ImageReferences, ModuleID):
        self.LessonID = str(LessonID)
        self.LessonMaterials = []
        self.ImageReferences = []
        self.ModuleID = int(ModuleID)
        
    def __str__(self):
        return "LessonID: %s, ModuleID: %s" % (self.LessonID, self.ModuleID)
        
    def Take_Test(TestID, StudentID):
        #list
        pass
    
    def Display_Learning_Materials(ImageReferences):
        #image here
        pass
    
