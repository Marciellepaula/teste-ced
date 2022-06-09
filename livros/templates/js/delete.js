function deleteLivro(id) {
    Swal.fire({
        title: "Você tem certeza?",
        text: "Você deseja deletar esse livro? essa ação não pode ser desfeita!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sim, deletar!",
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire("Sucesso!", "O arquivo foi deletado.", "success").then(() => {
                document.getElementById(id).submit();
                });
            }
        });
}
