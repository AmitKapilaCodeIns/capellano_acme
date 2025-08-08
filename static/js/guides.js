const editButtons = document.getElementsByClassName("btn-edit");

const holeForm = document.getElementById("holeForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Form fields for editing hole guides
const formNumber = document.getElementById("id_hole_number");
const formName = document.getElementById("id_name");
const formPar = document.getElementById("id_par");
const formYardage = document.getElementById("id_yardage");
const formSI = document.getElementById("id_stroke_index");
const formText = document.getElementById("id_guide");


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

    // Get content from hidden span elements
    let holeNum = document.getElementById(`hole-num-${holeId}`).innerText;
    let holeName = document.getElementById(`hole-name-${holeId}`).innerText;
    let par = document.getElementById(`hole-par-${holeId}`).innerText;
    let yardage = document.getElementById(`hole-yardage-${holeId}`).innerText;
    let strokeIndex = document.getElementById(`hole-si-${holeId}`).innerText;
    

    // Set form fields with the retrieved content
    formNumber.value = holeNum;
    formName.value = holeName;
    formPar.value = par;
    formYardage.value = yardage;
    formSI.value = strokeIndex;

    let holeContent = document.getElementById(`hole${holeId}`).innerText;

    formText.value = holeContent;

    // Update form fields with the retrieved content
    submitButton.innerText = "Update";
    holeForm.setAttribute("action", `edit/${holeId}/`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific hole guide.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let holeId = e.target.getAttribute("hole_id");
    deleteConfirm.href = `delete_hole_guide/${holeId}`;
    deleteModal.show();
  });
}