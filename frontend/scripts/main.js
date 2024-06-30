document.addEventListener('DOMContentLoaded', function() {
	    console.log('Sitrix app initialized.');
 document.querySelectorAll('nav ul li a').forEach(anchor => {
	         anchor.addEventListener('click', function(e) {
			             e.preventDefault();
			             const targetId = this.getAttribute('href').substring(1);
			             document.getElementById(targetId).scrollIntoView({ behavior: 'smooth' });
			         });
	     });
});
