// Chart.js initialization
    const ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
        labels: ['Vitamin A', 'Vitamin B12', 'Vitamin C', 'Vitamnin D'],
        datasets: [{
            label: 'Example Dataset',
            data: [12, 19, 3, 5],
            backgroundColor: ['#bb3e00', '#f7ad45', '#657c6a', '#79ADDC'],
            borderWidth: 1
        }]
        },
        options: {
        responsive: true,
        scales: {
            y: {
            beginAtZero: true
            }
        }
        }
    });

    const ctx2 = document.getElementById('myChart2').getContext('2d');
    new Chart(ctx2, {
        type: 'doughnut',
        data: {
            labels: ['Calcium', 'Magnesium', 'Potassium', 'Iron'],
            datasets: [{
                label: 'Another Dataset',
                data: [8, 14, 9, 6],
                backgroundColor: ['#bb3e00', '#f7ad45', '#657c6a', '#79ADDC'],
                borderWidth: 1,
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    })

    const ctx3 = document.getElementById('myChart3').getContext('2d');
    new Chart(ctx3, {
        type: 'pie',
        data: {
            labels: ['Consumed', 'Remaining'],
            datasets: [{
                data: [6,4],
                backgroundColor: ['#79ADDC', '#bb3e00'],
                borderWidth: 0,
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    })

    // Toggle menu function for small screens
    function toggleMenu() {
        const menu = document.getElementById('menuList');
        menu.style.display = (menu.style.display === 'none' || menu.style.display === '') ? 'block' : 'none';
    }

    function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");

    const video = document.getElementById("bitaminLogo");
    const source = video.querySelector("source");
    const isDarkMode = document.body.classList.contains("dark-mode");

    source.src = isDarkMode ? "bitamin_logo_dk.mp4" : "bitamin_logo_lt.mp4";
    video.load();
    video.playbackRate = 0.75;
    video.play();

    // Toggle icon
    const icon = document.getElementById("darkModeBtn").querySelector("i");
    icon.className = isDarkMode ? "fas fa-sun" : "fas fa-moon";
}
