<script>
  import {url} from "./api";
  import Input from './Input.svelte';
  import Line from './LineChart.svelte';
  import Pie from './PieChart.svelte';
  import Num from './NumChart.svelte';
  import Modal from './Modal.svelte';
  import BigLineChart from 'BigLineChart.svelte';

  export let number = 1;
  export let name = 'F1_1_3_1'
  const ws = new WebSocket(`ws://localhost:8000/ws/${name}`);
  let dataArea = [];
  let dataSpeed = [];
  let dataStability = [];
  ws.onmessage = function (event) {
    let content = JSON.parse(event.data);
    let {stability, speed, area} = content;
    stability *= 10;
    dataArea = [area].concat(dataArea);
    dataSpeed = [speed].concat(dataSpeed);
    dataStability = [stability].concat(dataStability);
  }

  let alarm = false;
  let settings = false;
  let info = false;
  // let src = `${url}/video/${name}`;
  let src = `${url}/static/raw/${name}.mp4`;
  let srcProc = `${url}/static/processed/${name}.mp4`;
  let counter = 0;
  let trustSpeed = 230, trustArea = 1880, trustLive = 8;
  const speedScatter = 20, areaScatter = 200, liveScatter = 4;
  let speedPercent = 100, areaPercent = 100, livePercent = 100;
  let speedStatus = 'good', areaStatus = 'good', liveStatus = 'good';
  let dataLst;
  $: {
    speedPercent = Math.floor(speedScatter / (Math.abs(dataSpeed[0] - trustSpeed) + 1) * 100);
    areaPercent = Math.floor(areaScatter / (Math.abs(dataArea[0] - trustArea) + 1) * 100);
    livePercent = Math.floor(liveScatter / (Math.abs(dataStability[0] - trustLive) + 1) * 100);

    if (speedPercent > 100) {
      speedPercent = 100;
    }
    if (areaPercent > 100) {
      areaPercent = 100;
    }
    if (livePercent > 100) {
      livePercent = 100;
    }

    if (speedPercent > 85) {
      speedStatus = 'good';
    } else if (60 < speedPercent && speedPercent < 85) {
      speedStatus = 'normal';
      counter++;
    } else {
      speedStatus = 'bad'
      counter += 2;
    }

    if (areaPercent > 85) {
      areaStatus = 'good';
    } else if (60 < areaPercent && areaPercent < 85) {
      areaStatus = 'normal';
      counter++
    } else {
      areaStatus = 'bad'
      counter += 2;
    }

    if (livePercent > 85) {
      liveStatus = 'good';
    } else if (60 < livePercent && livePercent < 85) {
      liveStatus = 'normal';
      counter++;
    } else {
      liveStatus = 'bad'
      counter += 2;
    }

    if (counter >= 4) {
      alarm = true;
    } else {
      alarm = false;
    }
    dataLst = [
      {
        name: "Скорость",
        measure: "px/s",
        data: dataSpeed,
        status: speedStatus,
        percent: speedPercent,
        last: Math.floor(dataSpeed[0])
      },
      {
        name: "Площадь",
        measure: "px",
        data: dataArea,
        status: areaStatus,
        percent: areaPercent,
        last: Math.floor(dataArea[0])
      },
      {
        name: "Стабильность",
        measure: "st",
        data: dataStability,
        status: liveStatus,
        percent: livePercent,
        last: Math.floor(dataStability[0])
      },
    ];
  }

</script>

<Modal bind:open={info}>
  <div class="modal-box">
    <div class="modal-video-box">
      <h1>Камера №{number}</h1>
      <video class="modal-video" width="1200" autoplay muted="muted" loop>
        <source src={srcProc} type="video/mp4"/>
      </video>
    </div>
    <div class="modal-charts">
      {#each dataLst as {data, name, status}}
        <BigLineChart {data} {name} {status}/>
      {/each}
    </div>
  </div>
</Modal>


<div class="component">
  <video class:red-border={alarm} class="outer-video" width="1200" autoplay muted="muted" loop>
    <source {src} type="video/mp4"/>
  </video>
  <div class="top-row">
    <p class="number">№{number}</p>

    <div class="button-block">
      <button class:active-button={settings} on:click={_ => settings = !settings}>
        <img src="icons/settings.svg" alt="settings">
      </button>
      <button on:click={_ => info = true}>
        <img src="icons/information.svg" alt="info">
      </button>
    </div>
  </div>
  <div class="chart-box">
    {#if settings}
      <div class="settings-block">
        <Input label="Скр." bind:value={trustSpeed} min={2000} max={30000}/>
        <Input label="Плд." bind:value={trustArea} min={1800} max={2000}/>
        <Input label="Жив." bind:value={trustLive} min={1} max={20}/>
        <button on:click={_ => settings = false}>Готово</button>
      </div>

    {:else}
      {#each dataLst as {name, data, status, percent, measure, last}}
        <div class="chart-row">
          <Line {data} {name} {status}/>
          <Pie {status} {percent}/>
          <Num {status} {last} {measure}/>
        </div>
      {/each}
    {/if}
  </div>
</div>

<style>
  img {
    width: 15px;
  }

  h1 {
    color: #333333;
    margin-top: 0;
  }

  .modal-video-box {
    margin-top: 30px;
  }

  .modal-box {
    display: flex;
    width: 1200px;
    height: 700px;
    justify-content: space-evenly;
    margin-right: 20px;
  }

  .modal-charts {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .active-button {
    background: #cccccc;
  }

  button {
    margin-bottom: 0;
    display: flex;
    padding: 10px 10px;
    margin-left: 5px;
    background: transparent;
    border-radius: 10px;
  }

  .settings-block {
    height: 70%;
    margin-top: 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
  }

  .button-block {
    display: flex;
    justify-content: space-between;
  }

  .top-row {
    width: 93%;
    height: 60px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;

  }

  .number {
    font-weight: bold;
    font-size: 20px;
    /*padding: 0;*/
    margin: 10px 0;

  }

  .component {
    width: 240px;
    height: 500px;
    background: white;
    padding: 5px;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    box-shadow: 5px 5px 20px 1px rgba(10, 10, 10, 0.1);
    /*justify-content: center;*/
  }

  .red-border {
    border-color: red;
  }

  .outer-video {
    width: 220px;
    height: 165px;
    border-radius: 15px;
    border: 7px solid #666666;
  }

  .modal-video {
    width: 600px;
  }

  .chart-box {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
  }

  .chart-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
</style>
