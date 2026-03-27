// Custom JavaScript for Orchid Elegant

// Add to Cart AJAX Function
function addToCart(productId, quantity = 1) {
    const csrftoken = getCookie('csrftoken');
    
    $.ajax({
        url: '/add-to-cart/',
        type: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        data: JSON.stringify({
            product_id: productId,
            quantity: quantity
        }),
        contentType: 'application/json',
        success: function(response) {
            if (response.success) {
                showNotification(response.message, 'success');
                updateCartCount(response.cart_count);
            } else {
                showNotification(response.message, 'error');
            }
        },
        error: function() {
            showNotification('Error adding to cart', 'error');
        }
    });
}

// Update Cart Item
function updateCartItem(itemId, quantity) {
    const csrftoken = getCookie('csrftoken');
    
    $.ajax({
        url: '/update-cart/',
        type: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        data: JSON.stringify({
            item_id: itemId,
            quantity: quantity
        }),
        contentType: 'application/json',
        success: function(response) {
            if (response.success) {
                updateCartItemDisplay(itemId, response.item_total);
                updateCartTotal(response.cart_total);
                updateCartCount(response.cart_count);
            }
        }
    });
}

// Remove from Cart
function removeFromCart(itemId) {
    const csrftoken = getCookie('csrftoken');
    
    $.ajax({
        url: `/remove-from-cart/${itemId}/`,
        type: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function(response) {
            if (response.success) {
                $(`#cart-item-${itemId}`).fadeOut(300, function() {
                    $(this).remove();
                    updateCartTotal(response.cart_total);
                    updateCartCount(response.cart_count);
                    
                    if ($('.cart-item').length === 0) {
                        $('#cart-table').html('<div class="text-center p-5"><i class="fas fa-shopping-cart fa-3x mb-3"></i><h3>Your cart is empty</h3><a href="/products/" class="btn btn-primary mt-3">Continue Shopping</a></div>');
                    }
                });
            }
        }
    });
}

// Update Cart Count in Header
function updateCartCount(count) {
    $('.cart-count').text(count);
    if (count === 0) {
        $('.cart-count').hide();
    } else {
        $('.cart-count').show();
    }
}

// Update Cart Item Display
function updateCartItemDisplay(itemId, itemTotal) {
    $(`#item-total-${itemId}`).text('$' + itemTotal.toFixed(2));
}

// Update Cart Total
function updateCartTotal(cartTotal) {
    $('#cart-total').text('$' + cartTotal.toFixed(2));
    $('#subtotal').text('$' + cartTotal.toFixed(2));
    $('#final-total').text('$' + cartTotal.toFixed(2));
}

// Show Notification
function showNotification(message, type) {
    const notification = $(`
        <div class="toast-notification alert alert-${type === 'success' ? 'success' : 'danger'}">
            <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i>
            ${message}
        </div>
    `);
    
    $('body').append(notification);
    
    setTimeout(() => {
        notification.fadeOut(300, function() {
            $(this).remove();
        });
    }, 3000);
}

// Get Cookie Function
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Quantity Input Handlers
$(document).ready(function() {
    // Handle quantity increase
    $('.increase-qty').click(function() {
        const input = $(this).siblings('.quantity-input');
        let value = parseInt(input.val());
        value = isNaN(value) ? 1 : value + 1;
        input.val(value).trigger('change');
    });
    
    // Handle quantity decrease
    $('.decrease-qty').click(function() {
        const input = $(this).siblings('.quantity-input');
        let value = parseInt(input.val());
        value = isNaN(value) ? 1 : Math.max(1, value - 1);
        input.val(value).trigger('change');
    });
    
    // Handle quantity change
    $('.quantity-input').on('change', function() {
        const itemId = $(this).data('item-id');
        const quantity = parseInt($(this).val());
        if (quantity > 0) {
            updateCartItem(itemId, quantity);
        }
    });
    
    // Add to cart button handler
    $('.add-to-cart-btn').click(function() {
        const productId = $(this).data('product-id');
        const quantity = $(this).data('quantity') || 1;
        addToCart(productId, quantity);
    });
    
    // Remove from cart button handler
    $('.remove-item').click(function() {
        const itemId = $(this).data('item-id');
        if (confirm('Are you sure you want to remove this item?')) {
            removeFromCart(itemId);
        }
    });
    
    // Search form submission
    $('#search-form').submit(function(e) {
        e.preventDefault();
        const searchTerm = $('#search-input').val();
        if (searchTerm) {
            window.location.href = `/products/?search=${encodeURIComponent(searchTerm)}`;
        }
    });
    
    // Product filtering
    $('.filter-btn').click(function() {
        const category = $(this).data('category');
        if (category) {
            window.location.href = `/products/?category=${category}`;
        } else {
            window.location.href = '/products/';
        }
    });
    
    // Smooth scroll
    $('a[href*="#"]').click(function(e) {
        if (this.hash !== '') {
            e.preventDefault();
            const hash = this.hash;
            $('html, body').animate({
                scrollTop: $(hash).offset().top - 70
            }, 800);
        }
    });
    
    // Back to top button
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
    
    $('#back-to-top').click(function() {
        $('html, body').animate({scrollTop: 0}, 800);
        return false;
    });
    
    // Form validation
    $('form').on('submit', function(e) {
        if ($(this).hasClass('needs-validation')) {
            if (this.checkValidity() === false) {
                e.preventDefault();
                e.stopPropagation();
            }
            $(this).addClass('was-validated');
        }
    });
    
    // Load more products (pagination)
    let page = 1;
    $('#load-more').click(function() {
        page++;
        const url = `/products/?page=${page}`;
        $.get(url, function(data) {
            const newProducts = $(data).find('.product-card');
            if (newProducts.length > 0) {
                $('#products-container').append(newProducts);
            } else {
                $('#load-more').hide();
            }
        });
    });
});

// Product Image Gallery
function initProductGallery() {
    $('.thumb-image').click(function() {
        const newImage = $(this).attr('src');
        $('#main-product-image').attr('src', newImage);
        $('.thumb-image').removeClass('active');
        $(this).addClass('active');
    });
}

// Add to Cart Animation
function animateAddToCart(button) {
    const cartIcon = $('.cart-icon');
    const productCard = button.closest('.product-card');
    const clone = productCard.find('.product-image img').clone();
    
    clone.css({
        position: 'absolute',
        width: '50px',
        height: '50px',
        borderRadius: '50%',
        top: button.offset().top,
        left: button.offset().left,
        zIndex: 9999
    });
    
    $('body').append(clone);
    
    clone.animate({
        top: cartIcon.offset().top,
        left: cartIcon.offset().left,
        width: '20px',
        height: '20px',
        opacity: 0.5
    }, 500, function() {
        $(this).remove();
        cartIcon.css('animation', 'bounce 0.5s');
        setTimeout(() => {
            cartIcon.css('animation', '');
        }, 500);
    });
}