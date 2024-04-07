function message(){
    var Name=document.getElementById('name');
    const success=document.getElementById('success');
    const danger=document.getElementById('danger');
    if (Name.value ===''){
    danger.style.display='block';

}
else{
    setTimeout(()=> {
        Name.value='';

    },2000);
    success.style.display='block';
}
setTimeout(()=>{
    danger.style.display='none';
    success.style.display='none';
},4000);
}

function getPrice (item){
    if (message === 'sad'){
        window.open('http://127.0.0.1:5500/templates/result.html','newwindow');
    }
    else if(message === 'happy'){
    window.open('www.google.com','newwindow');
    }
}