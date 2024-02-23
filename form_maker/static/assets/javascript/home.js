
document.querySelectorAll('.branch-option').forEach((option) => {
  option.addEventListener('click', (event) => {
    event.preventDefault();
    const branchValue = event.target.dataset.value;
    document.getElementById('branch-input').value = branchValue;
  });
});
