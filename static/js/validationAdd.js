const name = document.querySelector('[stu-name]')
const email = document.querySelector('[stu-email]')
const phone = document.querySelector('[stu-phone]')
const btnAdd = document.querySelector('[btn-add]')

btnAdd.addEventListener('click', () =>{
    // email
    if(!email.value)
        email.classList.add('email-req')
    else 
        email.classList.remove('email-req')
        // phone number
    if(!phone.value)
        phone.classList.add('phone-req')
    else{ 
        phone.classList.remove('phone-req')
    }
    if(!name.value)
        name.classList.add('name-req')
    else 
        name.classList.remove('name-req')


})