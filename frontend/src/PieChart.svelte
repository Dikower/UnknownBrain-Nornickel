<script>
  import Doughnut from "svelte-chartjs/src/Doughnut.svelte"

  export let status = "good";
  export let percent = 90;
  const colors = {
    good: 'rgb(34, 191, 47)',
    normal: 'rgb(245, 171, 0)',
    bad: 'rgb(234, 43, 31)'
  }
  $: data = {
    datasets: [{
      label: '%',
      percent: percent,
      backgroundColor: [colors[status]],
      borderWidth: 1

    }]
  }
  const plugins = [{
    beforeInit: (chart) => {
      const dataset = chart.data.datasets[0];
      chart.data.labels = [dataset.label];
      dataset.data = [dataset.percent, 100 - dataset.percent];
    }
  },
    {
      beforeDraw: (chart) => {
        var width = chart.chart.width,
          height = chart.chart.height,
          ctx = chart.chart.ctx;
        ctx.restore();
        // var fontSize = (height / 150).toFixed(2);
        // ctx.font = fontSize + "em sans-serif";
        ctx.font = "11px sans-serif"
        ctx.fillStyle = "black";
        ctx.textBaseline = "middle";
        var text = chart.data.datasets[0].percent + "%",
          textX = Math.round((width - ctx.measureText(text).width) / 2),
          textY = height / 2;
        ctx.fillText(text, textX, textY);
        ctx.save();
      }
    }
  ];
  const options = {
    animation: false,
    maintainAspectRatio: false,
    cutoutPercentage: 85,
    rotation: Math.PI / 2,
    legend: {
      display: false,
    },
    tooltips: {enabled: false},
    hover: {mode: null},
  }
</script>

{#key data}
  <div class="wrapper">
    <Doughnut {data} {plugins} {options}/>
  </div>
{/key}

<style>
  .wrapper {
    width: 45px;
    height: 45px;
    padding: 2px;
  }
</style>