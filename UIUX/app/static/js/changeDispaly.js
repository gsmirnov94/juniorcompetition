function changeDisplay() {
    let type = document.getElementById('type_mutator').value;
    if(type == 1){
        console.log('OF');
        $.ajax({
            success: () => {
                formfile = "<div id='div-form' class='file-input'><label for='file' id='file-label'>Файл: </label>\n" +
                    "            <input id='file' name='file' required type='file'>\n" +
                    "            <span class='button'>Choose</span>\n" +
                    "            <label class='label' data-js-label>No file selected</label>\n" +
                    "        </div>";
                document.getElementById('post-file').innerHTML=formfile;
                let inputs = document.querySelectorAll('.file-input');
                for(let i = 0, len = inputs.length; i < len; i++) {
                  customInput(inputs[i])
                }
                function customInput (el) {
                  const fileInput = el.querySelector('[type="file"]');
                  const label = el.querySelector('[data-js-label]');
                  console.log('OK')
                  fileInput.onchange =
                  fileInput.onmouseout = function () {
                    if (!fileInput.value) return;

                    var value = fileInput.value.replace(/^.*[\\\/]/, '');
                    el.className += ' -chosen';
                    label.innerText = value
                  }
                }
            }
        })
    }
    else{
        console.log('OF');
        $.ajax({
            success: () => {
                document.getElementById('div-form').remove();
            }
        })
    }
}