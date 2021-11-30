window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
});

var table_detail = ""
window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesRekening = document.getElementById('data_tabel_rekening');

    console.log (data_tabel_rekening)
    if (datatablesRekening) {
        table_detail = new simpleDatatables.DataTable(datatablesRekening);
    }
});
