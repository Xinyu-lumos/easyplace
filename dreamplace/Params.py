##
# @file   Params.py
# @author Yibo Lin
# @date   Apr 2018
# @brief  User parameters
#

import os
import sys
import json 
import math 
from collections import OrderedDict
import pdb

class Params:
    """
    @brief Parameter class
    """
    def __init__(self):
        """
        @brief initialization
        """
        # os.path.join 是 Python 中 os.path 模块提供的一个函数，用于 智能拼接文件路径
        filename = os.path.join(os.path.dirname(__file__), 'params.json')
        print (filename)
        self.__dict__ = {}
        params_dict = {}
        # json.load() 函数用于将文件中的 JSON 格式数据解析为 Python 对象
        # object_pairs_hook=OrderedDict 指定使用 有序字典（OrderedDict）存储 JSON 数据中的键值对。
        with open(filename, "r") as f:
            params_dict = json.load(f, object_pairs_hook=OrderedDict)

        for key, value in params_dict.items():
            if 'default' in value: 
                self.__dict__[key] = value['default']
            else:
                self.__dict__[key] = None
        self.__dict__['params_dict'] = params_dict

    def printWelcome(self):
        """
        @brief print welcome message
        """
        content = "Hello, welcome to easyPlace!"
        print(content)

    def printHelp(self):
        content = "Hello, welcome to easyPlace!"
        print(content)


    def toJson(self):
        """
        @brief convert to json
        """
        data = {}
        for key, value in self.__dict__.items():
            if key != 'params_dict': 
                data[key] = value
        return data

    def fromJson(self, data):
        """
        @brief load form json
        """
        for key, value in data.items(): 
            self.__dict__[key] = value

    def dump(self, filename):
        """
        @brief dump to json file
        """
        with open(filename, 'w') as f:
            json.dump(self.toJson(), f)

    def load(self, filename):
        """
        @brief load from json file
        """
        with open(filename, 'r') as f:
            self.fromJson(json.load(f))

    def __str__(self):
        """
        @brief string
        """
        return str(self.toJson())

    def __repr__(self):
        """
        @brief print
        """
        return self.__str__()

    def design_name(self):
        """
        @brief speculate the design name for dumping out intermediate solutions 
        """
        if self.aux_input: 
            design_name = os.path.basename(self.aux_input).replace(".aux", "").replace(".AUX", "")
        elif self.verilog_input:
            design_name = os.path.basename(self.verilog_input).replace(".v", "").replace(".V", "")
        elif self.def_input: 
            design_name = os.path.basename(self.def_input).replace(".def", "").replace(".DEF", "")
        return design_name 

    def solution_file_suffix(self): 
        """
        @brief speculate placement solution file suffix 
        """
        if self.def_input is not None and os.path.exists(self.def_input): # LEF/DEF 
            return "def"
        else: # Bookshelf
            return "pl"
