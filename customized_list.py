class CustomList(list):
    def remove_if_exist(self,d):
        try:
            self.remove(d)
        except ValueError:
            pass