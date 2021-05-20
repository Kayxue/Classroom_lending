import $ from "jquery"

$(() => {
    $(document).on("ready", (eve) => {
        $(document).find("div").addClass("test")
    })
})

