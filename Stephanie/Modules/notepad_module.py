from Stephanie.Modules.base_module import BaseModule
import Stephanie.globals as glob
import os

class NotepadModule(BaseModule):
    def __init__(self, *args):
        super().__init__(*args)
        print("inited")

    def write_note(self):
        note_text=""
        self.assistant.say("Should I save or append these notes?")
        note_filename = str(self.assistant.listen().decipher()).lower()
        if "save as" in note_filename:
            note_filename = note_filename[note_filename.rindex("save as ")+8:]
            note_mode = 'xt'
            self.assistant.say("Notes will be saved as, "+note_filename+". Starting transcription.")
        elif "append to" in note_filename:
            note_filename = note_filename[note_filename.rindex("append to ")+10:]
            note_mode = 'at'
            note_text += " \n"
            self.assistant.say("Notes will be appended to , "+note_filename+". Starting transcription.")
        else:
            note_filename = "ScrapBook"
            note_mode = 'at'
            note_text += " \n"
            self.assistant.say("Notes will be appended to the scrapbook. Starting transcription.")
        
        
        note_response = True
        
        while note_response:
            note_text += str(self.assistant.listen().decipher())
            self.assistant.say("Noted. Would you like to continue?")
            note_response = str(self.assistant.listen().decipher()).lower() in glob.affirmative
            
        self.assistant.say("Transcription complete.")
        
        punctuation = ["semicolon", ':',
                       "newline", '\n',
                       "new line", '\n']
        
        for i in range(len(punctuation)-1):
            note_text = note_text.replace(punctuation[i], punctuation[i+1])
        
        path = os.path.expanduser("~\Documents\AssistantNotes\ ").strip()
        try: os.makedirs(path)
        except: pass
        try:
            note = open(path + note_filename+".txt", note_mode)
            note.write(note_text)
            note.close
            self.assistant.say("Note has been saved as, "+note_filename+".txt")
        except:
            self.assistant.say("An error occured while saving the note. Redirecting text to console.")        
            print(note_text)