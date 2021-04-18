<script>
  import Card from './Card.svelte';
  let list = ['F1_1_3_1', 'F1_1_3_2', 'F1_1_4_1', 'F1_1_4_2', 'F1_2_3_1', 'F1_2_3_2', 'F2_1_2_2', 'F5_1_2_1', 'F5_1_2_2', 'F5_2_2_1'];
</script>

<main>
  {#each list.slice(0, 2) as el, i}
    <Card name={el} number={i + 1}/>
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