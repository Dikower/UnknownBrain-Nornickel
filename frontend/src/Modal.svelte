<script>
  export let open = true;
  import {fade, fly} from 'svelte/transition';
  let component;
</script>

{#if open}
  <div bind:this={component}
       on:click={event => event.target === component ? open = false : undefined}
       class="background" transition:fade>
    <div class="window" transition:fly={{y: -20}}>
      <button class="cancel-button" on:click={() => open = false}>
        <svg width=32 height=32>
          <line x1=2 y1=2 x2=14 y2=14></line>
          <line x1=2 y1=14 x2=14 y2=2></line>
        </svg>
      </button>
      <div class="content">
        <slot/>
      </div>
    </div>
  </div>
{/if}

<style>
  .background {
    z-index: 1;
    position: fixed;
    top:0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .window {
    width: 40%;
    min-width: 300px;
    max-width: 600px;
    padding-bottom: 20px;
    background: #eae8e9;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-bottom: 300px;
  }
  .cancel-button {
    width: 32px;
    height: 32px;
    margin-top: 5px;
    margin-right: 5px;
    background: transparent;
    border-color: transparent;
    cursor: pointer;
  }
  .content {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  line {
    stroke: #333333;
  }

</style>