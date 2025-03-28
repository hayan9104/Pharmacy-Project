// Basic JavaScript for interactive elements
document.addEventListener('DOMContentLoaded', function() {
    // Filter button functionality
    const filterBtns = document.querySelectorAll('.filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });
    
    // Price range slider
    const priceRange = document.getElementById('priceRange');
    const priceValue = document.getElementById('priceValue');
    if(priceRange && priceValue) {
        priceRange.addEventListener('input', function() {
            priceValue.textContent = `₹${this.value}`;
        });
    }
    
    // Product quantity selector
    const minusBtns = document.querySelectorAll('.quantity-btn.minus');
    const plusBtns = document.querySelectorAll('.quantity-btn.plus');
    
    minusBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const input = this.nextElementSibling;
            let value = parseInt(input.value);
            if(value > input.min) {
                input.value = value - 1;
            }
        });
    });
    
    plusBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const input = this.previousElementSibling;
            let value = parseInt(input.value);
            if(value < input.max) {
                input.value = value + 1;
            }
        });
    });
});

// Cart and Wishlist functionality
let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
let wishlistItems = JSON.parse(localStorage.getItem('wishlistItems')) || [];

// Update cart and wishlist counts
function updateCounts() {
    const cartCount = document.querySelector('.cart-count');
    const wishlistCount = document.querySelector('.wishlist-count');
    
    if (cartCount) {
        cartCount.textContent = cartItems.reduce((total, item) => total + item.quantity, 0);
    }
    if (wishlistCount) {
        wishlistCount.textContent = wishlistItems.length;
    }
}

// Show notification
function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Toggle wishlist functionality
function toggleWishlist(productId) {
    const productCard = document.querySelector(`.product-card[data-product-id="${productId}"]`);
    if (!productCard) return;

    const wishlistIcon = productCard.querySelector('.wishlist-icon i');
    const isInWishlist = wishlistItems.some(item => item.id === productId);

    if (isInWishlist) {
        wishlistItems = wishlistItems.filter(item => item.id !== productId);
        wishlistIcon.classList.remove('fas');
        wishlistIcon.classList.add('far');
        showNotification('Product removed from wishlist!');
    } else {
        const product = {
            id: productId,
            name: productCard.querySelector('h3').textContent,
            brand: productCard.querySelector('.brand').textContent,
            price: parseFloat(productCard.querySelector('.current-price').textContent.replace('₹', '')),
            image: productCard.querySelector('.product-img img').src
        };
        wishlistItems.push(product);
        wishlistIcon.classList.remove('far');
        wishlistIcon.classList.add('fas');
        showNotification('Product added to wishlist!');
    }

    localStorage.setItem('wishlistItems', JSON.stringify(wishlistItems));
    updateCounts();
}

// Add to cart functionality
function addToCart(product) {
    const existingItem = cartItems.find(item => item.id === product.id);
    
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cartItems.push({ ...product, quantity: 1 });
    }
    
    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    updateCounts();
    showNotification('Product added to cart!');
    updateProductCardUI(product.id);
}

// Update product card UI
function updateProductCardUI(productId) {
    const productCard = document.querySelector(`.product-card[data-product-id="${productId}"]`);
    if (!productCard) return;

    const addToCartBtn = productCard.querySelector('.add-to-cart-btn');
    const quantityControls = productCard.querySelector('.quantity-controls');
    const quantityDisplay = productCard.querySelector('.quantity-display');
    
    const cartItem = cartItems.find(item => item.id === productId);
    
    if (cartItem) {
        addToCartBtn.style.display = 'none';
        quantityControls.style.display = 'flex';
        quantityDisplay.textContent = cartItem.quantity;
    } else {
        addToCartBtn.style.display = 'block';
        quantityControls.style.display = 'none';
    }
}

// Update quantity functionality
function updateQuantity(productId, change) {
    const cartItem = cartItems.find(item => item.id === productId);
    
    if (cartItem) {
        cartItem.quantity += change;
        
        if (cartItem.quantity <= 0) {
            cartItems = cartItems.filter(item => item.id !== productId);
        }
        
        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        updateCounts();
        updateProductCardUI(productId);
        showNotification(change > 0 ? 'Product added to cart!' : 'Product removed from cart!');
    }
}

// Initialize counts and UI on page load
document.addEventListener('DOMContentLoaded', function() {
    updateCounts();
    
    // Add event listeners to all "Add to Cart" buttons
    document.querySelectorAll('.add-to-cart-btn').forEach(button => {
        button.addEventListener('click', function() {
            const productCard = this.closest('.product-card');
            const product = {
                id: productCard.dataset.productId,
                name: productCard.querySelector('h3').textContent,
                brand: productCard.querySelector('.brand').textContent,
                price: parseFloat(productCard.querySelector('.current-price').textContent.replace('₹', '')),
                image: productCard.querySelector('.product-img img').src
            };
            addToCart(product);
        });
    });

    // Add event listeners to quantity controls
    document.querySelectorAll('.quantity-btn').forEach(button => {
        button.addEventListener('click', function() {
            const productCard = this.closest('.product-card');
            const productId = productCard.dataset.productId;
            const change = this.classList.contains('plus') ? 1 : -1;
            updateQuantity(productId, change);
        });
    });

    // Add event listeners to wishlist icons
    document.querySelectorAll('.wishlist-icon').forEach(icon => {
        icon.addEventListener('click', function() {
            const productCard = this.closest('.product-card');
            const productId = productCard.dataset.productId;
            toggleWishlist(productId);
        });
    });

    // Initialize product card UI for items in cart and wishlist
    cartItems.forEach(item => {
        updateProductCardUI(item.id);
    });

    // Initialize wishlist icons
    wishlistItems.forEach(item => {
        const productCard = document.querySelector(`.product-card[data-product-id="${item.id}"]`);
        if (productCard) {
            const wishlistIcon = productCard.querySelector('.wishlist-icon i');
            wishlistIcon.classList.remove('far');
            wishlistIcon.classList.add('fas');
        }
    });
});

