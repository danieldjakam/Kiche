const jumpForm = document.getElementById('jumpForm');
const jumpFormInput = document.getElementById('jumpFormInput');
const jumpFormIcon = document.getElementById('jumpFormIcon');
const addDropdown = document.getElementById('add_dropdown');
const profileDropdown = document.getElementById('profile_dropdown');
const addDropdownOn = document.getElementById('add_dropdown_on');
const profileDropdownOn = document.getElementById('profile_dropdown_on');
const page = document.getElementById('view');
const navbar = document.getElementById('navbar');

let search = '';
let isAddChoices = false;
let isProfileChoices = false;

const activateAddDropdown = () => {
    addDropdown.classList.remove('hidden');
    isAddChoices = !isAddChoices
}

const deactivateAddDropdown = () => {
    alert('d')
    addDropdown.classList.add('hidden')
    console.log(addDropdown);
}

const activateProfileDropdwon = () => {
    profileDropdown.classList.remove('hidden')
    isProfileChoices = !isProfileChoices
}

const deactivateProfileDropdwon = () => {
    profileDropdown.classList.add('hidden')
}
const handleSubmit = (e) => {
    e.preventDefault();
    alert(search)
}

jumpForm.addEventListener('submit', handleSubmit)
jumpFormInput.addEventListener('change', (e) => {search = e.target.value})
jumpFormIcon.addEventListener('click', handleSubmit)

page.addEventListener('click', () => {
    deactivateAddDropdown;
    deactivateProfileDropdwon;
})
navbar.addEventListener('click', () => {
    deactivateAddDropdown;
    deactivateProfileDropdwon;
})
addDropdownOn.addEventListener('click', activateAddDropdown)
profileDropdownOn.addEventListener('click', activateProfileDropdwon)