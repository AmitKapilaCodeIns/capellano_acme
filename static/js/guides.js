const editButtons = document.getElementsByClassName("btn-edit");

const holeForm = document.getElementById("holeForm");
const submitButton = document.getElementById("submitButton");

// Form fields for editing hole guides
const holeText = document.getElementById("id_guide");
console.log(holeText);
console.log("Hello from guides.js");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated guide's ID upon click.
* - Fetches the content of the corresponding guide.
* - Populates the `guideText` input/textarea with the guide's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit/{guide_id}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let holeId = e.target.getAttribute("hole_id");

    let holeContent = document.getElementById(`hole${holeId}`).innerText;

    holeText.value = holeContent;

    // Update form fields with the retrieved content
    submitButton.innerText = "Update";
    holeForm.setAttribute("action", `edit/${holeId}`);
  });
}