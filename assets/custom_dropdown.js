// Custom JavaScript to update dropdown placeholders based on selection count
document.addEventListener('DOMContentLoaded', function() {

    // Function to update dropdown placeholder
    function updateDropdownPlaceholder(dropdownId, defaultPlaceholder) {
        const observer = new MutationObserver(function(mutations) {
            try {
                const dropdown = document.getElementById(dropdownId);
                if (!dropdown) return;

                // Find the control div and placeholder
                const control = dropdown.querySelector('.Select-control');
                if (!control) return;

                const placeholderDiv = control.querySelector('.Select-placeholder');
                const multiValueWrapper = control.querySelector('.Select-multi-value-wrapper');

                if (!placeholderDiv) return;

                // Count selected values
                let count = 0;
                if (multiValueWrapper) {
                    const selectedValues = multiValueWrapper.querySelectorAll('.Select-value');
                    count = selectedValues.length;
                }

                // Update placeholder text
                if (count > 0) {
                    const text = count === 1 ? '1 selected' : count + ' selected';
                    placeholderDiv.textContent = text;
                    placeholderDiv.style.display = 'block';
                    placeholderDiv.style.opacity = '1';
                } else {
                    placeholderDiv.textContent = defaultPlaceholder;
                }
            } catch (error) {
                console.log('Error updating dropdown:', error);
            }
        });

        // Start observing with a longer delay to ensure Dash is ready
        setTimeout(function() {
            observer.observe(document.body, {
                childList: true,
                subtree: true,
                attributes: true,
                attributeFilter: ['class', 'style']
            });

            // Trigger initial update
            const dropdown = document.getElementById(dropdownId);
            if (dropdown) {
                const event = new Event('change');
                dropdown.dispatchEvent(event);
            }
        }, 500);
    }

    // Monitor all filter dropdowns with staggered initialization
    setTimeout(function() {
        updateDropdownPlaceholder('filter-industry', 'Select industries...');
        updateDropdownPlaceholder('filter-cloud', 'Select cloud platforms...');
        updateDropdownPlaceholder('filter-region', 'Select regions...');
        updateDropdownPlaceholder('filter-optimization', 'Select optimization types...');
        updateDropdownPlaceholder('filter-license', 'Select license systems...');
    }, 1500);
});
