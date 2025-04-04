// Fetch restaurants with filters
async function loadRestaurants(cuisine, maxPrice) {
    let url = '/api/restaurants/';
    if (cuisine || maxPrice) {
        url += `?cuisine=${cuisine || ''}&max_price=${maxPrice || ''}`;
    }
    
    const response = await fetch(url);
    const restaurants = await response.json();
    
    let html = '';
    restaurants.forEach(restaurant => {
        html += `
        <div class="restaurant-card">
            <h3>${restaurant.name}</h3>
            <p>Cuisine: ${restaurant.cuisine} • Price: ${restaurant.price_range}</p>
        </div>
        `;
    });
    
    document.getElementById('restaurants-list').innerHTML = html;
}

// Initial load
loadRestaurants();