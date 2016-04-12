# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:29:37 2016

@author: c1533095
"""

class lecturer:
    def __init__(self, LecturerID, Name, Password, ModulesTeaching):
        self.LecturerID = int(LecturerID)
        self.Name = str(Name)
        self.Password = str(Password)
        self.ModulesTeaching = ModulesTeaching
    def __str__(self):
        return "LecturerID: %s, Name: %s, Results: %s, Modules Enrolled: %s" % (self.LecturerID, self.Name, self.Results, self.ModulesTeaching)
