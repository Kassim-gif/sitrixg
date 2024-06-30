function typeEffect(element, speed) {
	    const text = element.innerHTML;
	    element.innerHTML = '';
	    let i = 0;
	    const timer = setInterval(() => {
		            if (i < text.length) {
				                element.append(text.charAt(i));
				                i++;
				            } else {
						                clearInterval(timer);
						            }
		        }, speed);
}

document.addEventListener('DOMContentLoaded', function() {
	    const element = document.querySelector('.type-effect');
	    if (element) {
		            typeEffect(element, 100);
		        }
});

