class Hcl_list_exception(Exception):
    def __init__(self,mes):
        self.message=mes
        super().__init__(self.message)


