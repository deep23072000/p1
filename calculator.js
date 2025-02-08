let store = '';

function cal(vijay){
    store = store+vijay;
    console.log(store);
    document.getElementById('show').innerHTML = store;
    
}

function calculate(){
    document.getElementById('show').innerHTML = eval(store);
    store = eval(store);
    store = store.toString()
}

function allclear(){
    store = "";
    document.getElementById('show').innerHTML = store;

}
function del(){
   let len = store.length
   console.log(len)
   store = store.slice(0,len-1)
   document.getElementById('show').innerHTML = store;

}