document.getElementById('generate-quote').addEventListener('click', function() {
    console.log('Button clicked');
    fetch('/api/quote/random')
        .then(response => response.json())
        .then(data => {
            console.log('Quote fetched:', data);
            document.getElementById('quote-display').innerText = data.quote;
        })
        .catch(error => {
            console.error('Error fetching the quote:', error);
        });
});
