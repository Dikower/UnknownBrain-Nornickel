<script>
  import {url} from "./api";
  import Input from './Input.svelte';
  import Line from './LineChart.svelte';
  import Pie from './PieChart.svelte';
  import Num from './NumChart.svelte';
  import Modal from './Modal.svelte';
  import BigLineChart from 'BigLineChart.svelte';

  export let number = 1;
  let alarm = false;
  let settings = false;
  let info = true;

  let trustSpeed = 4, trustArea = 11, trustLive = 7;
</script>

<Modal bind:open={info}>
  <div class="modal-box">
    <div class="modal-video-box">
      <h1>Камера №{number}</h1>
      <video class="modal-video" width="1200" autoplay muted="muted" loop>
        <source src="{url}/video" type="video/mp4"/>
      </video>
    </div>
    <div class="modal-charts">
      <BigLineChart name="Скорость"/>
      <BigLineChart name="Площадь"/>
      <BigLineChart name="Живучесть"/>
    </div>
  </div>
</Modal>


<div class="component">
  <video class="outer-video" class:red-border={alarm} width="1200" autoplay muted="muted" loop>
    <source src="{url}/video" type="video/mp4"/>
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
        <Input label="Скр." bind:value={trustSpeed}/>
        <Input label="Плд." bind:value={trustArea}/>
        <Input label="Жив." bind:value={trustLive}/>
        <button on:click={_ => settings = false}>Готово</button>
      </div>

    {:else}
      {#each new Array(3) as e}
        <div class="chart-row">
          <Line name="Скорость" status="good"/>
          <Pie status="good"/>
          <Num status="good"/>
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
