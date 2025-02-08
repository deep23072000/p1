let arr = ["pink","black","red","orange","green"];
const show = ()=>{
    for(let i=0;i<arr.length;i++){
       document.getElementById(`div${i}`).style.backgroundColor = arr[i]
    }
}

let c ='';
function colorpick(colorpick1){
    c = c+colorpick1;
    document.getElementById('selectedcolor').style.backgroundColor = colorpick1;
}

function final(){
      let store = Math.random();
      let amul = store*arr.length;
      let afloor = Math.floor(amul);
      let ind = arr[afloor];
      console.log(afloor);
      document.getElementById('div5').style.backgroundColor = ind ;

      if(ind === c){
        alert("paise double ho gaye")
      }
      else{
        alert("paise doob gaye")
      }

}

// function s(){

// }