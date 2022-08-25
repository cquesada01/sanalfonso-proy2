function showMessageAlert(message,category ){
    Swal.fire({
        icon: category,
        title: message,
        text: message
      })
}