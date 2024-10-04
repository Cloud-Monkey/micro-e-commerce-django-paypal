// Edit and update review
const editButton = document.getElementById("btn-edit");
const reviewText = document.getElementById("id_body");
const reviewRating = document.getElementById("id_rating");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

editButton && editButton.addEventListener("click", (e) => {
    const id = e.target.getAttribute("review_id");
    const body = e.target.getAttribute("review_body");
    const rating = e.target.getAttribute("review_rating");

    reviewText.value = body;
    reviewRating.value = rating;
    submitButton.innerText = "Update";
    reviewForm.style = "margin-top: 1.3em;";
    reviewForm.setAttribute("action", `edit_review/${id}`);
});

// Delete review
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("review_id");
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
}
