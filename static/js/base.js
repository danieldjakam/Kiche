const themeChoices = document.querySelectorAll('#theme_choice')
const themesChecker = document.querySelectorAll('#theme_checker')
const langChoices = document.querySelectorAll('#lang_choice')

themesChecker.forEach((el) => {
    if (localStorage.getItem('theme') === el.dataset.theme) {
        el.checked = true
    }
})

if(localStorage.getItem('lang') !== null && ['fr', 'en', 'es', 'de'].includes(localStorage.getItem('lang'))){
    const directions = window.location.pathname.split('/');
    const lan = directions[1];
    if (lan !== localStorage.getItem('lang')) {
        directions[1] = localStorage.getItem('lang')
        const path = directions.join('/')
        window.location.replace(path)
    }
}

themeChoices.forEach(el => {
    if (localStorage.getItem('theme') === el.dataset.theme) {
        el.classList.add('checked')
    }
})

const checkCorrectChoiceBox = (theme) => {
    themeChoices.forEach(el => {
        el.classList.remove('checked')
    })
    themeChoices.forEach(el => {
        if (theme === el.dataset.theme) {
            el.classList.add('checked')
        }
    })
}

if(localStorage.theme === undefined || localStorage.theme === 'sync'){
    const date = new Date().getHours();
    if (date < 21) {
        document.body.classList.remove('dark_mode')
    }else{
        document.body.classList.add('dark_mode')
    }
}
else if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark_mode')
    checkCorrectChoiceBox(localStorage.getItem('theme'))
}else{
    checkCorrectChoiceBox(localStorage.getItem('theme'))
}

themeChoices.forEach(el => {
    el.addEventListener('click', (e) => {
        const theme = e.target.dataset.theme;
        if (theme === 'sync') {
            localStorage.setItem('theme', 'sync')
            const date = new Date().getHours();
            if (date < 21) {
                document.body.classList.remove('dark_mode')
            }else{
                document.body.classList.add('dark_mode')
            }
        }else if(theme === 'ligth'){
            document.body.classList.remove('dark_mode')
            localStorage.setItem('theme', 'ligth')
        }
        else{ 
            document.body.classList.add('dark_mode')
            localStorage.setItem('theme', 'dark')
        }
        checkCorrectChoiceBox(theme)
        const checkbox = document.querySelector('#theme_checker[data-theme="'+ theme +'"]')
        checkbox.checked = true
    } )
})

langChoices.forEach(choice => {
    choice.addEventListener('click', (e) => {
        e.preventDefault();
        const lang = e.target.dataset.language;
        localStorage.setItem('lang', lang);
        window.location.replace('/'+lang+'/accounts/settings')
    })
})