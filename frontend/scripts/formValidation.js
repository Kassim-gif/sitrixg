document.addEventListener('DOMContentLoaded', function() {
	    const form = document.querySelector('form');
	    form.addEventListener('submit', function(e) {
		            const email = form.querySelector('input[name="email"]').value;
		            if (!isValidEmail(email)) {
				                e.preventDefault();
				                alert('Please enter a valid email address.');
				            }
		        });
});

function isValidEmail(email) {
	    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	    return regex.test(email);
}

