<template>
    <div class="m_div">
        <div id='img'>
            <img :src="'http://127.0.0.1:8000/get_img?img=' + i.img">
        </div>
        <div id='name'>{{i.name}}</div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'm_div',
    data(){
        return {
            img:"",
        }
    },
    mounted(){
        axios({
            url: 'http://127.0.0.1:8000/get_img',
            params:{img:this.i.img}
        }).then(res =>{
            this.img = res.data
            console.log(res.data)
        })
    },
    props: ['i']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.m_div{
    width: 550px;
    height: 600px;
}
#name{
    width: 100px;
    height: 100px;
}
img{
    width: 500px;
    height: 500px;
    object-fit: contain;
}
</style>
