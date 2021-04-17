<script>
  export let data = "2 cm/s";
  export let status = "good";

  const colors = {
    good: {backgroundColor: 'rgba(43, 192, 22, 0.2)', borderColor: 'rgb(43, 192, 22)'},
    normal: {backgroundColor: 'rgb(249, 220, 92, 0.2)', borderColor: 'rgb(249, 220, 92)'},
    bad: {backgroundColor: 'rgb(234, 43, 31, 0.2)', borderColor: 'rgb(234, 43, 31)'}
  }
</script>
<div style="
  --backgroundColor: {colors[status].backgroundColor};
  --borderColor: {colors[status].borderColor}">
  <p>{data}</p>
</div>
<style>
  div {
    background: var(--backgroundColor);
    border: 2px solid var(--borderColor);
    width: 50px;
    height: 50px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  p {
    font-size: 12px;
    color: black;
    font-weight: bold;
    margin: 0;
    text-align: center;
  }
</style>