from reporter import header
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Generator:
    def __init__(self, json_path, xls_path, md_path):
        self.json_path = json_path
        self.xls_path = xls_path
        self.md_path = md_path
        
        with open(json_path, "r") as in_file:
            self.reloaded = json.load(in_file)
    
        self.series = pd.read_excel(xls_path).set_index("année").transpose().dropna(how="all", axis=1)

    def create_graph(self):
        self.series.plot(y=['PIB'])
        plt.savefig('graph.png')

    
    def create_markdown(self):
        var_md = header.create_header(self.reloaded) + "\n\n![a graph](graph.png)\n"
        
        with open(self.md_path, 'w', encoding='utf-8') as out_file:
            out_file.write(var_md)