<script>
  import Line from "svelte-chartjs/src/Line.svelte"

  export let name = 'Скорость';
  export let data = [0, 0, 0, 11, 9, 17, 13];
  export let status = "good";

  const colors = {
    good: {backgroundColor: 'rgba(43, 192, 22, 0.2)', borderColor: 'rgb(43, 192, 22)'},
    normal: {backgroundColor: 'rgb(245, 171, 0, 0.2)', borderColor: 'rgb(245, 171, 0)'},
    bad: {backgroundColor: 'rgb(234, 43, 31, 0.2)', borderColor: 'rgb(234, 43, 31)'}
  }
  const options = {
    animation: false,
    legend: {
      display: false,
    },
    scales: {
      xAxes: [{
        ticks: {
          fontSize: 10,
          fontColor: 'lightgrey'
        }
      }],
      yAxes: [{
        ticks: {
          beginAtZero: true,
          fontSize: 10,
          fontColor: 'lightgrey',
          maxTicksLimit: 10,
          padding: 25,
        }
      }]
    },
    tooltips: {
      backgroundColor: '#1e90ff'
    }
  }
  let drawData;
  $: {
    data = data.slice(0, 20);
    drawData = {
      labels: ['5s', '10s', '15s', '20s', '25s', '30s', '35s', '40s', '45s', '50s', '55s', '60s'],
      datasets: [{
        data: data,
        tension: 0.0,
        borderColor: colors[status].borderColor,
        backgroundColor: colors[status].backgroundColor,
        pointRadius: 3,
        borderWidth: 2
      }]
    };
  }

</script>

<div class="wrapper">
  <p>{name}</p>
  {#key data}
    <Line data={drawData} {options}/>
  {/key}
</div>

<style>
  .wrapper {
    width: 400px;
  }

  p {
    position: relative;
    top: 20px;
    left: 20px;
    padding: 0;
    margin: 0;
    color: #4A4A4A;
    font-size: 20px;
  }
</style>