class FilterModule():
    def filters(self):
        return {
            'surround_by_quotes': self.surround_by_quotes
        }

    def surround_by_quotes(self, a_list):
        return ['"%s"' % an_element for an_element in a_list]