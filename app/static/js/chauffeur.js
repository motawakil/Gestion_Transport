
document.addEventListener("DOMContentLoaded", function () {
    const pageToStep = {
        "reservation": 1,
        "vehicule": 2,
        "chauffeur": 3,
        "confirmation": 4
    };

    const currentPage = document.body.dataset.page;
    const progressSteps = document.querySelectorAll(".progress-step");

    if (pageToStep[currentPage]) {
        const currentStep = pageToStep[currentPage];

        progressSteps.forEach((step, index) => {
            const stepIndex = index + 1;

            if (stepIndex < currentStep) {
                step.classList.add("completed");
            } else if (stepIndex === currentStep) {
                step.classList.add("active");
            }
        });
    }
});

function navigateTo(page) {
    // Update the URL for redirection
    const routes = {
        "vehicule": "{{ url_for('main.vehicule') }}",
        "chauffeur": "{{ url_for('main.chauffeur') }}",
        "confirmation": "{{ url_for('main.vehicule') }}"
    };
    window.location.href = routes[page];
}
