class CustomNotesManager():
    def create_note(self,content,tags):
        if not content : 
            raise ValueError("content must be present")
        
        note = self.model(content=content)
        note.save(using= self._db)
        return note