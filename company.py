#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: daniellj
"""

class Company:
    def __init__(self, entityStatus, vanityName, Id, industries, foundedOn, website, specialties, staffCountRange):
        self.entityStatus = entityStatus
        self.vanityName = vanityName
        self.Id = Id
        self.industries = industries
        self.foundedOn = foundedOn
        self.website = website
        self.specialties = specialties
        self.staffCountRange = staffCountRange
        