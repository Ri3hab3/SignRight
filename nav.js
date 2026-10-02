/* SignRight — nav dropdown controller.
   CSS :hover alone closed the panel the instant the cursor slipped out of the
   item's box, which happens on any diagonal travel toward the panel's outer
   edge. A short grace period on close makes that harmless. Also adds
   click-to-toggle, Escape and outside-click. Pure CSS :hover stays as the
   no-JS fallback. */
(function () {
  if (window.__srNavReady) return;
  window.__srNavReady = true;

  var CLOSE_DELAY = 300;

  function init() {
    var items = [].filter.call(
      document.querySelectorAll('.nav-item'),
      function (it) { return it.querySelector('.nav-tab') && it.querySelector('.nav-panel'); }
    );
    if (!items.length) return;

    var timer = null;

    function cancel() {
      if (timer) { clearTimeout(timer); timer = null; }
    }

    function closeAll() {
      cancel();
      items.forEach(function (it) {
        it.classList.remove('open');
        it.querySelector('.nav-tab').setAttribute('aria-expanded', 'false');
      });
    }

    function open(item) {
      cancel();
      items.forEach(function (it) {
        var on = it === item;
        it.classList.toggle('open', on);
        it.querySelector('.nav-tab').setAttribute('aria-expanded', on ? 'true' : 'false');
      });
    }

    function scheduleClose() {
      cancel();
      timer = setTimeout(closeAll, CLOSE_DELAY);
    }

    items.forEach(function (item) {
      var tab = item.querySelector('.nav-tab');
      tab.setAttribute('aria-haspopup', 'true');
      tab.setAttribute('aria-expanded', 'false');

      item.addEventListener('mouseenter', function () { open(item); });
      item.addEventListener('mouseleave', scheduleClose);

      // Keeps the panel alive while the cursor is inside it, even if a stray
      // sample lands in a rounded corner or on the border.
      item.addEventListener('mousemove', cancel);

      tab.addEventListener('click', function (e) {
        e.preventDefault();
        if (item.classList.contains('open')) closeAll(); else open(item);
      });

      item.addEventListener('focusin', function () { open(item); });
      item.addEventListener('focusout', function (e) {
        if (!item.contains(e.relatedTarget)) scheduleClose();
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeAll();
    });

    document.addEventListener('click', function (e) {
      if (!e.target.closest || !e.target.closest('.nav-item')) closeAll();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
