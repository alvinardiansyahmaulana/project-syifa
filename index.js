const $ = jQuery = require('jquery');
const { data } = require('jquery');
const { PythonShell } = require('python-shell');

$(() => {

    $('#form').on('submit', (e) => {
        e.preventDefault();
        let options = {
            mode: 'text',
            args: [$('#test').val()]
        };
    
    
        console.log(options.args[0])
        PythonShell.run('./process/main.py', options, (error, result) => {
            if (error) throw error;

            let data = JSON.parse(result[0])
            console.log(data);
            
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
                if (index < 1) return

                createAdditionalDataTable(index, values.length)

                $.each(values, (n, value) => {

                    $(`#additional_data_table_${index}`).children().append(`
                        <td>${value}</td>
                    `)
                })
            })
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

    let createAdditionalDataTable = (id, len) => {
        return $('#additional_data_table').append(`
            <div class="col">
                <table class="table">
                    <tr>
                        <th colspan=${len}>Additionl Data ${id}</th>
                    </tr>
                    <tbody id=additional_data_table_${id}>
                        <tr></tr>
                    </tbody>
                </table>
            </div>
        `);
    }
})