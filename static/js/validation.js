const email = document.querySelector('[email]')
const password = document.querySelector('[password]')
const btn_submit = document.querySelector('[submit-btn]')

btn_submit.addEventListener('click', () =>{
    if(!email.value)
        email.classList.add('email-req')
    else 
        email.classList.remove('email-req')
    if(!password.value)
        password.classList.add('password-req')
    else 
        password.classList.remove('password-req')
})

