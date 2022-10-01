const setIsEditFormBtn = document.getElementById('setIsEditForm')
const editForm = document.getElementById('editForm')
const infosBox = document.getElementById('infosBox')
const cancelEditFormBtn = document.getElementById('cancelFormBtn')
const isEditAvatarBtn = document.getElementById('changeAvatarBtn')
const avatarInput = document.getElementById('id_avatar')
const professionalAccountInput = document.getElementById('id_is_a_proffessional_account')
const professionalAccountLabel = document.querySelector('label[for="id_is_a_proffessional_account"]')
const avatarProfile = document.getElementById('avatarProfile')
avatarInput.removeAttribute('required')

if(professionalAccountInput.checked){
    professionalAccountLabel.classList.add('checked')
}else{
    professionalAccountLabel.classList.remove('checked')
}
setIsEditFormBtn.addEventListener('click', () => {
    infosBox.classList.add('hidden')
    editForm.classList.remove('hidden')
    isEditAvatarBtn.classList.remove('hidden')
})

cancelEditFormBtn.addEventListener('click', () => {
    editForm.classList.add('hidden')
    isEditAvatarBtn.classList.add('hidden')
    infosBox.classList.remove('hidden')
})

avatarInput.addEventListener('change', (e) => {
    const url = URL.createObjectURL(e.target.files[0])
    avatarProfile.setAttribute('src', url)
})

professionalAccountInput.parentNode.classList.add('check')
professionalAccountInput.addEventListener('change', (e) => {
    if(e.target.checked){
        professionalAccountLabel.classList.add('checked')
    }else{
        professionalAccountLabel.classList.remove('checked')
    }
})