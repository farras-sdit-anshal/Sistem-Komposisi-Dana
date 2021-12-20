// Set new default font family and font color to mimic Bootstrap's default styling

const bgColor = [
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
    ]

var chartConsolidation = document.getElementById("myBarChartConsolidation");

const dataConsolidation = {
  labels: ["Posisi Kas"],
  datasets: [{
    label: 'SDIT Anak Shalih Bogor',
    data: [data_sum_38105_sdit],
    fill: false,
    backgroundColor: 'rgba(255, 159, 64, 0.2)',
    borderRadius: 10,
    borderWidth: 1,
    stack: 'Stack 0',
  },
  {
    label: 'TKIT Aisyah Educare',
    data: [data_sum_38105_tkit_ae],
    fill: false,
    backgroundColor: 'rgba(75, 192, 192, 0.2)',
    borderRadius: 10,
    borderWidth: 1,
    stack: 'Stack 0',
  },
  {
    label: 'TKIT Anak Shalih',
    data: [data_sum_38105_tkit_ans],
    fill: false,
    backgroundColor: 'rgba(255, 99, 132, 0.2)',
    borderRadius: 10,
    borderWidth: 1,
    stack: 'Stack 0',
  },
  {
    label: "Ma'had Al Bani",
    data: [data_sum_3635],
    fill: false,
    backgroundColor: '#0dcaf0',
    borderRadius: 10,
    borderWidth: 1,
    stack: 'Bank 1220003635',
  },
  {
    label: 'Yayasan',
    data: [data_sum_3632],
    fill: false,
    backgroundColor: '#6610f2',
    borderRadius: 10,
    borderWidth: 1,
    stack: 'Bank 1220003632',
  },
  {
    label: 'Masjid Imam Ahmad bin Hanbal',
    data: [data_sum_3633],
    fill: false,
    backgroundColor: '#dc3545',
    borderRadius: 10,
    borderWidth: 1,
    stack: '1220003635',
  },
  {
    label: 'Masjid Nuruttauhid',
    data: [data_sum_3639],
    fill: false,
    backgroundColor: '#0d6efd',
    borderRadius: 10,
    borderWidth: 1,
    stack: '1210103639',
  }]
};

var myBarChartConsolidation = new Chart(chartConsolidation, {
  type: 'bar',
  data: dataConsolidation,
  options: {
    indexAxis: 'x', // x atau y, y menjadi horizontal bar
    plugins: {
        title: {
            display: true,
            text: 'Posisi Kas Konsolidasi'
        },
        legend: {
            display: true,
            position: "bottom"
            }
        },
    scales: {
      x: {
        stacked: true,
      },
      y: {
        stacked: true
      }
    }
  }

});
