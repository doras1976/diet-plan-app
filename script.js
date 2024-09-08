document.getElementById('lifestyle-form').addEventListener('submit', async function(e) {
    e.preventDefault();  // Prevent the form from submitting the traditional way

    const goal = document.getElementById('goal').value;
    const exercise = document.getElementById('exercise').value;
    const diet = document.getElementById('diet').value;

    try {
        const response = await fetch('/api/generate-plan', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ goal, exercise, diet })
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        const data = await response.json();
        document.getElementById('plan-output').innerHTML = `<pre>${data.plan}</pre>`;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('plan-output').innerHTML = 'Error generating the plan. Please try again later.';
    }
});
