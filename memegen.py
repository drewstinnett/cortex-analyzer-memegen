#!/usr/bin/env python
# encoding: utf-8
import sys
import requests
from cortexutils.analyzer import Analyzer


class URLCategoryAnalyzer(Analyzer):

    def summary(self, raw):
        return {'memes': raw['memes']}

    def run(self):
        Analyzer.run(self)

        if self.data_type == 'meme':
            try:
				sys.stderr.write("Data: %s" % self.getData())
				req = requests.get('http://version1.api.memegenerator.net/Generators_Search?q=%s&pageIndex=0&pageSize=5' % self.getData())
				self.report({
                    'memes': req.json()
                })
            except ValueError as e:
                self.unexpectedError(e)
        else:
            self.notSupported()

if __name__ == '__main__':
    URLCategoryAnalyzer().run()
