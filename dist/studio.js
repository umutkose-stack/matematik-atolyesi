const fmt = new Intl.NumberFormat('tr-TR', {maximumFractionDigits: 2});
function padovan(n) {
  const p = {0:0, 1:0, 2:1};
  for (let i=3; i<=n; i++) p[i]=p[i-2]+p[i-3];
  for (let i=-1; i>=n; i--) p[i]=p[i+3]-p[i+1];
  return p[n];
}
const lab = document.querySelector('[data-lab]');
if (lab) {
  const result = lab.querySelector('output');
  function render() {
    const values = [...lab.querySelectorAll('input')].map(input => {
      input.nextElementSibling.textContent = fmt.format(input.valueAsNumber);
      return input.valueAsNumber;
    });
    if (lab.dataset.lab === 'padovan') {
      const n = values[0];
      result.textContent = 'P(' + n + ') = ' + padovan(n);
    } else if (lab.dataset.lab === 'dogum') {
      const n = values[0];
      let q = 1;
      for (let k=0; k<n; k++) q *= (365-k)/365;
      result.textContent = n + ' kişide en az iki kişinin doğum gününün aynı olma olasılığı yaklaşık %' + fmt.format((1-q)*100) + '.';
    } else {
      const [a,b] = values;
      result.textContent = 'Girdiler iki katına çıktığında üretim ' + fmt.format(2 ** (a+b)) + ' katına çıkar. Üslerin toplamı ' + fmt.format(a+b) + '.';
    }
  }
  lab.addEventListener('input',render);
  render();
}
