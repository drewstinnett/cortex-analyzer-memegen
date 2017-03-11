#!/usr/bin/env python
# encoding: utf-8
import requests
from cortexutils.analyzer import Analyzer


class MemeAnalyzer(Analyzer):

    def summary(self, raw):
        """
        This is the json that's returned in the report
        """
        return {
            'meme_generators': raw['meme_generators'],
            'meme_instances': raw['meme_instances']
            }

    def run(self):
        """
        Run the analysis here
        """
        Analyzer.run(self)

        ## Only do 'meme' types right now
        if self.data_type == 'meme':
            try:

                ## Just get some json, using the user input as the seach query
				generators = requests.get('http://version1.api.memegenerator.net/Generators_Search?q=%s&pageIndex=0&pageSize=5' % self.getData()).json()
				instances = requests.get('http://version1.api.memegenerator.net/Instances_Search?q=%s&pageIndex=0&pageSize=5' % self.getData()).json()

                ## This gets put back to the summary report object
				self.report({
                    'meme_generators': generators,
                    'meme_instances': instances,
                })

            except ValueError as e:
                self.unexpectedError(e)
        else:
            self.notSupported()

if __name__ == '__main__':
    MemeAnalyzer().run()
