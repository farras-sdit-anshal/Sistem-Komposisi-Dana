let nodeSdit = document.getElementById("c-sdit");
let nodeTkitAe = document.getElementById("c-tkit-ae");
let nodeTkitAnshal = document.getElementById("c-tkit-ans");
let nodeAlbani = document.getElementById("c-albani");
let nodeYayasan = document.getElementById("c-yayasan");
let nodeMiah = document.getElementById("c-miah");
let nodeNuruttauhid = document.getElementById("c-nuruttauhid");

let nodeTableBodyYayasan = document.getElementById("table-body-detail")



let nodeHeader = document.getElementById("header-bar");
let nodeHeaderTabelKomponenDana = document.getElementById("header-table");
const datatablesRekening = document.getElementById('data_tabel_rekening');





function changeData (chart,keys, data){
    chart.data.datasets[0].data = data
    chart.data.labels = keys
    chart.update();
}

function changeTableDetail (obj_table, keys, values){
    length_table = obj_table.data.length
    let rowToRemove = obj_table.body.querySelector("tr");
    // remove all data
    for ( var i = 0 ; i < length_table ; i++){
        obj_table.rows().remove(rowToRemove);
    }

    var formatter = new Intl.NumberFormat('in-ID', {
        style: 'currency',
        currency: 'IDR',
        maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
    });
    for (var j = 0 ; j < values.length ; j++){

        nominal = formatter.format(values[j]).toString()

        obj_table.rows().add([keys[j], nominal])
    }
}

function changeLineChart(lineChart, dates, balance){
    realDates = []
//    convert time stime to js date
    for (const i in dates){
        realDates.push (new Date (dates[i] * 1000).toLocaleDateString())
    }


    lineChart.data.labels = realDates;
    lineChart.data.datasets[0].data = balance;
    lineChart.update();
}


nodeSdit.addEventListener("click",function(event){
    event.preventDefault()
    nodeHeader.innerHTML = "Rekening SDIT Anak Shalih"
    nodeHeaderTabelKomponenDana.innerHTML = "Komponen Dana SDIT Anak Shalih"
    my_values = Object.values(data_38105_sdit)
    my_keys = Object.keys(data_38105_sdit)

    my_sumif_dates = Object.keys(data_sum_if_balance_38105)
    my_sumif_balance = Object.values(data_sum_if_balance_38105)


    changeData(myBarChart,my_keys, my_values);
    changeTableDetail(table_detail, my_keys, my_values)
    changeLineChart(myLineChart, my_sumif_dates, my_sumif_balance)
});

nodeTkitAe.addEventListener("click",function(event){
    event.preventDefault()
    nodeHeader.innerHTML = "Rekening TKIT Aisyah Educare"
    nodeHeaderTabelKomponenDana.innerHTML = "Komponen Dana TKIT Aisyah"
    my_values = Object.values(data_38105_tkit_ae)
    my_keys = Object.keys(data_38105_tkit_ae)
    my_sumif_dates = Object.keys(data_sum_if_balance_38105)
    my_sumif_balance = Object.values(data_sum_if_balance_38105)


    changeData(myBarChart,my_keys, my_values);
    changeTableDetail(table_detail, my_keys, my_values)
    changeLineChart(myLineChart, my_sumif_dates, my_sumif_balance)

});

nodeTkitAnshal.addEventListener("click",function(event){
    event.preventDefault()
    nodeHeader.innerHTML = "Rekening TKIT Anak Shalih"
    nodeHeaderTabelKomponenDana.innerHTML = "Komponen Dana TKIT Anak Shalih"
    my_values = Object.values(data_38105_tkit_ans)
    my_keys = Object.keys(data_38105_tkit_ans)

    my_sumif_dates = Object.keys(data_sum_if_balance_38105)
    my_sumif_balance = Object.values(data_sum_if_balance_38105)

    changeData(myBarChart,my_keys, my_values);
    changeTableDetail(table_detail, my_keys, my_values)
    changeLineChart(myLineChart, my_sumif_dates, my_sumif_balance)

});

nodeYayasan.addEventListener("click",function(event){
    event.preventDefault()
    nodeHeader.innerHTML = "Rekening Yayasan"
    nodeHeaderTabelKomponenDana.innerHTML = "Komponen Dana Yayasan"
    my_values = Object.values(data_3632)
    my_keys = Object.keys(data_3632)

    my_sumif_dates = Object.keys(data_sum_if_balance_3632)
    my_sumif_balance = Object.values(data_sum_if_balance_3632)

    changeData(myBarChart,my_keys, my_values);
    changeTableDetail(table_detail, my_keys, my_values)
    changeLineChart(myLineChart, my_sumif_dates, my_sumif_balance)
});

nodeMiah.addEventListener("click",function(event){
    event.preventDefault()
    nodeHeader.innerHTML = "Rekening MIAH"
    nodeHeaderTabelKomponenDana.innerHTML = "Komponen Dana MIAH"
    my_values = Object.values(data_3633)
    my_keys = Object.keys(data_3633)
    my_sumif_dates = Object.keys(data_sum_if_balance_3633)
    my_sumif_balance = Object.values(data_sum_if_balance_3633)

    changeData(myBarChart,my_keys, my_values);
    changeTableDetail(table_detail, my_keys, my_values)
    changeLineChart(myLineChart, my_sumif_dates, my_sumif_balance)
});

nodeAlbani.addEventListener("click",function(event){
    event.preventDefault()
    nodeHeader.innerHTML = "Rekening Al Bani"
    nodeHeaderTabelKomponenDana.innerHTML = "Komponen Dana Al Bani"
    my_values = Object.values(data_3635)
    my_keys = Object.keys(data_3635)
    my_sumif_dates = Object.keys(data_sum_if_balance_3635)
    my_sumif_balance = Object.values(data_sum_if_balance_3635)

    changeData(myBarChart,my_keys, my_values);
    changeTableDetail(table_detail, my_keys, my_values)
    changeLineChart(myLineChart, my_sumif_dates, my_sumif_balance)
});

nodeNuruttauhid.addEventListener("click",function(event){
    event.preventDefault()
    nodeHeader.innerHTML = "Rekening Nuruttauhid"
    nodeHeaderTabelKomponenDana.innerHTML = "Komponen Dana Nuruttauhid"
    my_values = Object.values(data_3639)
    my_keys = Object.keys(data_3639)
    my_sumif_dates = Object.keys(data_sum_if_balance_3639)
    my_sumif_balance = Object.values(data_sum_if_balance_3639)

    changeData(myBarChart,my_keys, my_values);
    changeTableDetail(table_detail, my_keys, my_values)
    changeLineChart(myLineChart, my_sumif_dates, my_sumif_balance)
});
