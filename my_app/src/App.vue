<template>
  <div>
    <div id='body'>
      <m_div v-for="i in data" :key="i.name" :i="i"></m_div>
      <!-- <m_div :img="data[0].img"></m_div>
      <m_div :img="data[1].img"></m_div> -->
    </div>
    <div id='bottom'>
      <button>页码</button>
    </div>
  </div>
</template>

<script>
import m_div from './components/m_div'
import axios from 'axios'

export default {
  name: 'App',
  data(){
    return {
      data:[],
    }
  },
  created(){
    axios({
      url: 'http://127.0.0.1:8000/get_movies'
    }).then(res =>{
      console.log(res)
      this.data = res.data/*  */
    })
  },
  components: {
    m_div,
  }
  
}
</script>

<style>
.m_div{
  width: 200px;
  height: 200px;
  float:left;
}
#body{
}
#bottom{
  height: 40px;
  text-align: center;
  clear:both;
}
</style>
