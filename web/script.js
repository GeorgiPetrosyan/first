document.getElementById('submitButton').addEventListener('click', function() {
    const inputField = document.getElementById('inputField');
    const resultText = document.getElementById('resultText');
    resultText.textContent = `Вы ввели: ${inputField.value}`;
});
