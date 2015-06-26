from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter

class EverNoteServe():

	dev_token = ''
	client = None

	def __init__(self):
		self.client = EvernoteClient(token=self.dev_token)

	def getNotes(self):
		noteStore = self.client.get_note_store()
		notefilter = NoteFilter()
		notes = noteStore.findNotes(notefilter, 0, 100)
		for note in notes.notes:
			print note.guid
			noteInfo = noteStore.getNote(self.dev_token, note.guid, True, False, False, False)
			
			print note.title
			print noteInfo.content


if __name__ == '__main__':
	everSer = EverNoteServe()
	everSer.getNotes()
