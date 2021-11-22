// Set new default font family and font color to mimic Bootstrap's default styling


// Bar Chart Example
var ctx = document.getElementById("myBarChart");

const labels = ["SPP","Biaya Kegiatan Satu Tahun","Ekstrakulikuler","Dompet Pendidikan Tetap","Dompet Pendidikan TIdak Tetap","Infaq","Infrastruktur","SPP","Biaya Kegiatan Satu Tahun","Ekstrakulikuler","Dompet Pendidikan Tetap","Dompet Pendidikan TIdak Tetap","Infaq","Infrastruktur"];
const data = {
  labels: labels,
  datasets: [{
    data: [65, 59, 180, 81, 56, 55, 40,65, 59, 180, 81, 56, 55, 40],
    fill: false,
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(75, 192, 192, 0.2)'
    ],
    borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(75, 192, 192, 0.2)'
    ],
    borderWidth: 1
  }]
};



const dataDua = {
  labels: labels,
  datasets: [{
    data: [650, 59, 180, 821, 16, 255, 440,655, 559, 80, 81, 556, 515, 471],
    fill: false,
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(75, 192, 192, 0.2)'
    ],
    borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(75, 192, 192, 0.2)'
    ],
    borderWidth: 1
  }]
};


var myBarChart = new Chart(ctx, {
  type: 'bar',
  data: data,
  options: {
    indexAxis: 'y', // x atau y, y menjadi horizontal bar
    plugins: {
        title: {
            display: true,
            text: 'Komposisi dana'
        },
        legend: {
            display: false
            }
        },
    scales: {
        yAxis: {
            min: 0,
            ticks: {
                display: true,
                padding: 30
            }
        }
    }
  }

});
