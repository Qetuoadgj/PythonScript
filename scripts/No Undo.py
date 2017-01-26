# -*- coding: utf-8 -*-

# Delete the undo history.
editor.emptyUndoBuffer()

# Remember the current position in the undo history as the position at which the document was saved.
# editor.setSavePoint()

# Save the document.
notepad.save()

# Turn the undo recorder back on.
editor.setUndoCollection(1)
