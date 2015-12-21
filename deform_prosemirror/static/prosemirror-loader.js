(function($) {
  "use strict";

  // Deform JS integration
  // deform.addCallback('${oid}', function(oid) {
  //
  //});

  // Called before form save
  // $().bind('form.pre.serialize', function(event, $form, options) {
  //  tinyMCE.triggerSave();
  // });

  $(".prosemirror").each(function() {
    var pm = new ProseMirror({
      place: this,
      doc: content,
      docFormat: "markdown",
      tooltipMenu: true
    })
    pm.focus()
  });

})(jQuery);