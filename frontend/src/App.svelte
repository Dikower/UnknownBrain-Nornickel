<script>
  import Card from './Card.svelte';
  // const ws = new WebSocket("ws://localhost:8000/ws");
  // let list = [];
  // ws.onmessage = function (event) {
  //   let content = event.data;
  //   console.log(content);
  //   list = list.concat(content);
  // }
  import {onMount} from 'svelte'
  import {writable} from 'svelte/store'


  // setInterval(() => {
  //   dataLine.datasets[0].data.push(1)
  //   dataLine.datasets[1].data.push(1)
  //   console.log($dataLine)
  // }, 1000)
</script>

<main>
<!--    <button on:click={_ => ws.send('Hello')}>Send</button>-->
  {#each [...Array(10).keys()] as el}
    <Card number={el + 1}/>
  {/each}
</main>

<style>
  :root {
    /*background: #888888;*/
    background: whitesmoke;
  }

  /*main {*/
  /*  display: flex;*/
  /*  align-content: center;*/
  /*  justify-content: center;*/
  /*  height: 300px;*/
  /*}*/

  main {
    display: grid;
    /*grid-template-columns: repeat(5, auto);*/
    grid-template-columns: repeat(5, 264px);
    gap: 20px 10px;
    justify-content: center;
    padding: 1em;
    max-width: 1440px;
    margin: 0 auto;
  }

  /*h1 {*/
  /*  color: #ff3e00;*/
  /*  text-transform: uppercase;*/
  /*  font-size: 4em;*/
  /*  font-weight: 100;*/
  /*}*/

</style>