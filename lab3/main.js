let btn = document.querySelector('#btn');
let input = document.querySelector('#add');
let holder = document.getElementById("holder")

function delTask(id) {
    let task = document.getElementById(id);
    task.remove();
}

function checkTask(id){
    let task = document.getElementById("task"+id);
    let checkbox = document.getElementById("checkbox"+id);
    if(checkbox.checked) {
        task.style.textDecorationLine = "line-through"
    } else {
        task.style.textDecorationLine =  "none";
    }
}
 
btn.addEventListener('click', () => {
    let txt = input.value;
    if (txt === "") {
        alert('You must write something');
    } else {
        let id = document.getElementById('holder').getElementsByTagName('div').length;
        let task = `<div class="content" id=${id}>
                        <input type="checkbox" class="checkbox" onclick="checkTask('${id}')" id=${"checkbox"+id}> 
                        <p class="task" id=${"task"+id}>${txt}</p> 
                        <img src="https://www.iconsdb.com/icons/preview/red/empty-trash-xxl.png" onclick="delTask('${id}')" class="trash" >
                    </div>`
        holder.insertAdjacentHTML('afterbegin', task);
        input.value = '';
    }
})