
(function(){
  const btn=document.querySelector('.menu-button');
  const nav=document.querySelector('.nav-links');
  if(btn&&nav){btn.addEventListener('click',()=>{const open=nav.classList.toggle('open');btn.setAttribute('aria-expanded',String(open));});document.addEventListener('keydown',e=>{if(e.key==='Escape'){nav.classList.remove('open');btn.setAttribute('aria-expanded','false');}});}
  document.querySelectorAll('[data-year]').forEach(el=>el.textContent=new Date().getFullYear());
  document.querySelectorAll('[data-product-form]').forEach(form=>{
    const radios=[...form.querySelectorAll('input[name="plan"]')];
    const release=form.querySelector('[name="release"]');
    const duration=form.querySelector('[data-selected-duration]');
    const price=form.querySelector('[data-selected-price]');
    const edition=form.querySelector('[data-selected-release]');
    const link=form.querySelector('[data-order-link]');
    const product=form.dataset.product;
    function update(){
      const selected=radios.find(r=>r.checked)||radios[0];
      duration.textContent=selected.dataset.duration;
      price.textContent='USD '+selected.dataset.price;
      edition.textContent=release.value;
      const subject=`Purchase inquiry: ${product} - ${selected.dataset.duration} - ${release.value}`;
      const body=`Hello Allofwind Digital,%0D%0A%0D%0AI would like to confirm availability for:%0D%0AProduct: ${product}%0D%0ATerm: ${selected.dataset.duration}%0D%0ARelease: ${release.value}%0D%0APrice shown: USD ${selected.dataset.price}%0D%0A%0D%0APlease confirm eligibility, delivery, and next steps.`;
      link.href=`mailto:contact@webdailylifetyles.com?subject=${encodeURIComponent(subject)}&body=${body}`;
    }
    radios.forEach(r=>r.addEventListener('change',update));release.addEventListener('change',update);update();
  });
})();
