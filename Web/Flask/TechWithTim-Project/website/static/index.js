function deleteNote(noteId) {  // fetch send a request
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId})  // request.data
    }).then((_res) => {  // after the request
    window.location.href = '/'  // redirect
    })
}