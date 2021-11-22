let nodeSdit = document.getElementById("c-sdit");


function changeData (chart,data){
    chart.data = data;
    chart.update();
}

nodeSdit.addEventListener("click",function(){
    changeData(myBarChart,dataDua);
});
