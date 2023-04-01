const deleteButton = document.querySelectorAll('.delete');

deleteButton.forEach(button=>{
    button.addEventListener('click',()=>{
        studentId = button.getAttribute('id');
        if (confirm('Are you sure you want to delete this student?'))
            location.href='/delete/' + studentId;
    })
})