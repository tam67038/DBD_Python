<template>
  <div>
    <!-- 🔹 FULLSCREEN LOADING -->
      <div v-if="loading" class="overlay">
        <div class="spinner"></div>
        <p>Loading...</p>
      </div>

    <div style="padding: 30px">

      <h2>save PDF</h2>

      <!-- Input -->
      <!-- <input
        v-model="req"
        placeholder="Enter request"
        style="padding:8px; width:250px"
      /> -->

      <!-- Button -->
      <button
        @click="search"
        :disabled="loading"
        style="margin-left:10px; padding:8px"
      >
        Search
      </button>

      <!-- Result -->
      <pre v-if="result">{{ result }}</pre>

    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      req: "",
      result: "",
      loading: false
    }
  },

  methods: {
    async search() {
      // if (!this.req) {
      //   alert("Please enter request")
      //   return
      // }

      try {
        this.loading = true

        const res = await axios.post(
          `http://127.0.0.1:8000/InquirySHL/SavePDF`
        )

        this.result = JSON.stringify(res.data, null, 2)

      } catch (err) {
        console.error(err)
        this.result = "Error calling API"
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style>
  /* 🔹 overlay เต็มจอ */
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.5);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 9999;
  }

  /* 🔹 spinner */
  .spinner {
    width: 60px;
    height: 60px;
    border: 6px solid #ccc;
    border-top: 6px solid white;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg);}
    100% { transform: rotate(360deg);}
  }

  .overlay p {
    color: white;
    margin-top: 15px;
    font-size: 18px;
  }
</style>