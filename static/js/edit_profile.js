const inputs = document.querySelectorAll('.dis_input')
const edit_btn = document.getElementById('edit_btn')
const edit_save = document.getElementById('save_btn')
const edit_cancle = document.getElementById('cancle_btn')

const enb_input = (eles)=>{
    eles.forEach((ele)=>{
        ele.disabled = false
        ele.classList.remove('dis_input')
    })
}

const dis_input = (eles)=>{
    eles.forEach((ele)=>{
        ele.disabled = true
        ele.classList.add('dis_input')
    })
}

edit_btn.addEventListener('click', ()=>{
    edit_save.style.display = 'block'
    edit_cancle.style.display = 'block'
    enb_input(inputs)
})

edit_save.addEventListener('click', ()=>{

})

edit_cancle.addEventListener('click', ()=>{
    edit_save.style.display = 'none'
    edit_cancle.style.display = 'none'
    dis_input(inputs)
})