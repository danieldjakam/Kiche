const recipe_picture = document.getElementById('recipe_picture')
const id_picture = document.getElementById('id_picture')

id_picture.addEventListener('change', (e) => {
    const url = URL.createObjectURL(e.target.files[0])
    recipe_picture.setAttribute('src', url)
})