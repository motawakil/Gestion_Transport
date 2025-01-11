    
document.addEventListener('DOMContentLoaded', () => {
    const menuItems = document.querySelectorAll('.menu-item');
    const currentPath = window.location.pathname; // Get the current path of the page

    // Highlight the menu item that matches the current path
    menuItems.forEach(item => {
        if (item.getAttribute('href') === currentPath) {
            item.classList.add('active');
        }

        // Add animations for hover
        item.addEventListener('mouseenter', () => {
            item.classList.add('animate__pulse');
        });

        item.addEventListener('mouseleave', () => {
            item.classList.remove('animate__pulse');
        });

        // Set active class on click
        item.addEventListener('click', () => {
            menuItems.forEach(menuItem => menuItem.classList.remove('active'));
            item.classList.add('active');
        });
    });
});
