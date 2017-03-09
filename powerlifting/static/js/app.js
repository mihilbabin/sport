$(document).ready(function () {
  $('.button-collapse').sideNav();
  $('.carousel.carousel-slider').carousel({fullWidth: true});
  setInterval(function(){
    $('.carousel').carousel('next');
  }, 5000);
  $('select').material_select();
  makeActive();
});

function makeActive() {
  var current = location.pathname;
  if (current !== '/') {
    $('#nav_list li a').each(function(){
        var $this = $(this);
        if ($this.attr('href').indexOf(current) !== -1 || current.startsWith($this.attr('href')) ){
            $this.parent().addClass('active');
        }
    });
  }
}
