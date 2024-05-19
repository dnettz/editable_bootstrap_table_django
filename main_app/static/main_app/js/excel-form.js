const tableData = [
    { 'item_name': '', 'item_qnty': '', 'item_price': '' },
    { 'item_name': '', 'item_qnty': '', 'item_price': '' },
    { 'item_name': '', 'item_qnty': '', 'item_price': '' },
    { 'item_name': '', 'item_qnty': '', 'item_price': '' },
    { 'item_name': '', 'item_qnty': '', 'item_price': '' },
    { 'item_name': '', 'item_qnty': '', 'item_price': '' },
    { 'item_name': '', 'item_qnty': '', 'item_price': '' },
    { 'item_name': '', 'item_qnty': '', 'item_price': '' },
]

function createTable(container, data) {
    const table = document.createElement('table');
    table.id = 'excel-table';
    table.className = 'w-100 table table-bordered';
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    ['ITEM NAME', 'ITEM QNTY', 'ITEM PRICE'].forEach(headerText => {
        const th = document.createElement('th');
        th.textContent = headerText;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    thead.style.whiteSpace = 'nowrap';
    table.appendChild(thead);
    const tbody = document.createElement('tbody');
    data.forEach(rowData => {
        const row = document.createElement('tr');
        Object.entries(rowData).forEach(([key, value]) => {
            const cell = document.createElement('td');
            cell.setAttribute('data-field', key);
            cell.style.whiteSpace = 'nowrap';
            cell.textContent = value;
            cell.contentEditable = true;
            row.appendChild(cell);
        });
        tbody.appendChild(row);
    });
    table.appendChild(tbody);

    container.appendChild(table);
};

const excelFormContainer = document.getElementById('excel-form');
createTable(excelFormContainer, tableData);