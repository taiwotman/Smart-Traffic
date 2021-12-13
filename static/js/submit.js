(function($) {
    $(function() {
        $("select[name=region]").on("change", function() {
            $(this).closest("form")
                .find("input.button_link")
                .prop("disabled", $(this).val() == "#");
        })
            .trigger("change");
    });
})(jQuery);
