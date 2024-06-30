const apiBaseUrl = 'https://api.sitrix.com';

async function fetchData(endpoint) {
	    try {
		            const response = await fetch(`${apiBaseUrl}/${endpoint}`);
		            if (!response.ok) {
				                throw new Error('Network response was not ok');
				     }
		            const data = await response.json();
		            return data;
		        } catch (error) {
				        console.error('Fetch error:', error);
				        throw error;
				    }
}

async function postData(endpoint, data) {
	    try {
		            const response = await fetch(`${apiBaseUrl}/${endpoint}`, {
				                method: 'POST',
				                headers: {
							                'Content-Type': 'application/json'
							            },
				                body: JSON.stringify(data)
				            });
		            if (!response.ok) {
				                throw new Error('Network response was not ok');
				            }
		            const responseData = await response.json();
		            return responseData;
		        } catch (error) {
				        console.error('Post error:', error);
				        throw error;
				    }
}
