<script>
  export let value;
  export let label;
  export let min;
  export let max;
</script>
<label>
  {label}
  <input class="slider" type="range" bind:value {min} {max}>
  <input class="number" type="number" bind:value>
</label>

<style>
  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  /* Firefox */
  input[type=number] {
    -moz-appearance: textfield;
  }

  label {
    display: flex;
    /*align-items: center;*/
    justify-content: flex-end;
  }

  .slider {
    width: 70%;
    margin: 0;
  }

  .number {
    font-weight: normal;
    width: 50px;
    padding: 0;
    margin: 0 0 0 5px;
  }

</style>