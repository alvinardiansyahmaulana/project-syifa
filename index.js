const $ = jQuery = require('jquery');
const { spawn } = require('child_process');

$(() => {

    $('#form').on('submit', (e) => {
        e.preventDefault();
        let filePath = $('#file')[0].files[0].path;

        const pythonProcess = spawn('cd process && python -m pipenv run python', ['main.py', filePath], {shell: true});

        pythonProcess.stdout.on('data', (data) => {
            data = data.toString()
            data = JSON.parse(data)

            $.each(data[0], (i, values) => {
                createOptimumDataTable(i)

                $.each(values, (n, value) => {
                    $(`#table_${i}`).append(`
                        <tr>
                            <td>${value}</td>
                        </tr>
                    `)
                })
            })

            $.each(data, (index, values) => {
                let tableName = '';

                switch(index) {
                    case 0:
                        return;
                    case 1:
                        tableName = 'MAX';
                        break;
                    case 2:
                        tableName = 'SUM';
                        break;
                    default:
                        tableName = ''
                        break;
                }
                
                createAdditionalDataTable(index, values.length, tableName)

                $.each(values, (n, value) => {

                    $(`#additional_data_table_${index}`).children().append(`
                        <td>${value}</td>
                    `)
                })
            })
        });

        pythonProcess.stderr.on('data', (data) => {
            console.log(data.toString());
        });

        pythonProcess.on('error', (error) => {
            console.error(error.message)
        });

        pythonProcess.on('close', (code) => {
            console.log('child process exited with code: ', code)
        })

    })

    let createOptimumDataTable = (id) => {
        return $('#optimum_data_table').append(`
            <div class="col">
                <table class="table">
                    <tr>
                        <th>Optimum Data ${id+1}</th>
                    </tr>
                    <tbody id=table_${id}></tbody>
                </table>
            </div>    
        `)
    }

    let createAdditionalDataTable = (id, len, tableName) => {
        return $('#additional_data_table').append(`
            <div class="col">
                <table class="table">
                    <tr>
                        <th colspan=${len}>${tableName} Data ${id}</th>
                    </tr>
                    <tbody id=additional_data_table_${id}>
                        <tr></tr>
                    </tbody>
                </table>
            </div>
        `);
    }
})