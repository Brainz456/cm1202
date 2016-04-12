# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:29:37 2016

@author: c1533095
"""

class student:
    def __init__(self, StudentID, Name, Results, Password, ModulesEnrolled):
        self.StudentID = str(StudentID)
        self.Name = str(Name)
        self.Results = Results
        self.Password = str(Password)
        self.ModulesEnrolled = ModulesEnrolled
    def __str__(self):
        return "StudentID: %s, Name: %s, Results: %s, Modules Enrolled: %s" % (self.StudentID, self.Name, self.Results, self.ModulesEnrolled)
