(function($) {
  "use strict"

  $(".truncate-text-multiline").each(function(idx, element){
    let options = {'height': 100};
    new Dotdotdot(element, options);
  });

})(jQuery);
