class BaseApp:
    help = 'base app help'
    name = 'base app'
    
    def entry_point(self):
        self._run()

    def _run(self):
        self.what_is_love()

    def what_is_love(self):
        value = input('What is love?\n\n')
        print(value)
