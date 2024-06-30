document.addEventListener('DOMContentLoaded', function() {
	    const elements = document.querySelectorAll('.animate-on-scroll');
	    const observer = new IntersectionObserver(entries => {
		            entries.forEach(entry => {
				                if (entry.isIntersecting) {
							                entry.target.classList.add('animated');
							            } else {
									                    entry.target.classList.remove('animated');
									                }
				            });
		        });

	    elements.forEach(element => {
		            observer.observe(element);
		        });
});

