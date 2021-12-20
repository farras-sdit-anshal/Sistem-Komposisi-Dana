var table_fpk_running = ""
window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const table_fpk_running = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(table_fpk_running);
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


