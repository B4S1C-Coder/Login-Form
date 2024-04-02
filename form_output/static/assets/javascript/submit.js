const form = document.getElementById("dataForm");
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      console.log("Form submitted");
      const formData = new FormData(form);
      submitFormData(formData);
    });
    
    async function submitFormData(formData) {

      // const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      // const data = Object.fromEntries(formData.entries());
      // const jsonData = JSON.stringify(data);
      try {
        const response = await fetch("submit", {
          method: "POST",
          body: formData
        });
        } catch (error) {
          console.error('Error during form submission:', error);
          throw error;
        }
        return response.json();
      }