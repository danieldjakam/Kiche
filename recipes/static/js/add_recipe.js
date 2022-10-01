const nextBtn = document.querySelector('button.add_recipe')

// All inputs
const inputs = document.querySelectorAll('input.required')
const nameInput = document.querySelector('input#id_name')
const descInput = document.querySelector('input#description')
const nbrePlatesInput = document.querySelector('input#id_nbre_of_plates')
const timePreparationInput = document.querySelector('input#id_time_preparation')
const timeCuissonInput = document.querySelector('input#id_time_cuisson')
const isPrivateInput = document.querySelector('input#id_is_private')
const isPublicInput = document.querySelector('input#id_is_public')
const recipe_picture = document.getElementById('recipe_picture')
const id_picture = document.getElementById('id_picture')
 
let form_is_fill = false

const myFunc = () => {
    console.log(form_is_fill);
    if (form_is_fill) {
        nextBtn.classList.remove('disabled')
    }
}


const name = nameInput.value;
const nbrePlates = nbrePlatesInput.value
const timepreparation = timePreparationInput.value

console.log(timepreparation);

if (name === '') {
    nextBtn.classList.add('disabled')
}
else if(nbrePlates === '' || parseInt(nbrePlates) <= 0){
    nextBtn.classList.add('disabled')
}
else if(timepreparation === '' || parseInt(timepreparation) <= 0){
    nextBtn.classList.add('disabled')
}
else{
    nextBtn.classList.remove('disabled')
    nextBtn.classList.add('approved')
    const nextBtnApproved = document.querySelector('button.add_recipe.approved')

    nextBtnApproved.addEventListener('click', (e) => {
        window.location.assign('?action=finish&name='+name)
    })
}

inputs.forEach(input => {
    input.addEventListener('keyup', () => {
        const name = nameInput.value;
        const nbrePlates = nbrePlatesInput.value
        const timepreparation = timePreparationInput.value

        console.log(timepreparation);

        if (name === '') {
            nextBtn.classList.add('disabled')
        }
        else if(nbrePlates === '' || parseInt(nbrePlates) <= 0){
            nextBtn.classList.add('disabled')
        }
        else if(timepreparation === '' || parseInt(timepreparation) <= 0){
            nextBtn.classList.add('disabled')
        }
        else{
            nextBtn.classList.remove('disabled')
            nextBtn.classList.add('approved')
            const nextBtnApproved = document.querySelector('button.add_recipe.approved')

            nextBtnApproved.addEventListener('click', (e) => {
                window.location.assign('?action=finish&name='+name)
            })
        }

    })
})
    
id_picture.addEventListener('change', (e) => {
    const url = URL.createObjectURL(e.target.files[0])
    recipe_picture.setAttribute('src', url)
})