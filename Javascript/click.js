document.addEventListener('DOMContentLoaded', function(event) {
	const theNumber =  document.getElementById('theNumber');                                  
	const buttonAdd =  document.getElementById('buttonAdd');                                  
	const buttonMinus =  document.getElementById('buttonMinus');
	let clicks = 0;

	buttonAdd.addEventListener('click', function() {
		clicks++;
		theNumber.innerHTML = 'Clicked ' + clicks + ' times!';
	});

	buttonMinus.addEventListener('click', function() {
		clicks--;
		theNumber.innerHTML = 'Clicked ' + clicks + ' times!';
	});
});


