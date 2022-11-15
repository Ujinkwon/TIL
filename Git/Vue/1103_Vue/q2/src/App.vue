<template>
  <div id="app">
    <h1>SSAFY 상담 예약 시스템</h1>
    <div class="page" style="display: flex;">
      <div style="padding: 0px 30px; flex: 2;">
        <h2 style="padding-bottom: 23px;">예약 페이지</h2>
      <div style="margin-bottom: 30px">
        <h3 style="margin-bottom: 30px;">선생님 선택</h3>
        <button class="t-eric tbox" @click="tselect" :class="{tselectBox: eric}" style="padding: 10px 25px; margin-right: 10px;">Eric</button>
        <button class="t-tony tbox" @click="tselect" :class="{tselectBox: tony}" style="padding: 10px 25px; margin-left: 10px;">Tony</button>
      </div>
      <hr style="background:darkblue; height:1px; border:0;">
      <div style="margin-bottom: 50px">
        <h3>시간 선택</h3>
        <span v-for="(time, index) in times" :key="index">
          <button class="time" @click="select" style="padding: 10px;" v-bind:class="{selectBox: selected.includes(time), box: !selected.includes(time)}">{{ time }}</button>
          <br v-show="(index+1) % 10 === 0">
        </span>
      </div>
    </div>
    <div style="padding: 0px 30px; background-color: #658dc63d; flex: 2;">
      <h2 style="padding-bottom: 23px;">상담 신청 현황</h2>
      <div style="margin-bottom:50px">
        <h3>상담 선생님</h3>
        <span>{{ teacher }}</span>
        <hr style="background:darkblue; height:1px; border:0;">
      </div>
      <div>
        <h3>예약 현황</h3>
        <span v-for="stime in selected" :key="stime" style="margin: 5px;"> {{ stime }} </span>
        <hr style="background:darkblue; height:1px; border:0;">
        <img src="./assets/ssafy-logo.png" alt="" style="padding-top: 70px">
      </div>
    </div>
  </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },

  data: function() {
    return {
      times: [
  "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
  "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
  "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
],
      selected: [],
      eric: false,
      tony: false,
      teacher: '',
    }
  },
  
  methods: {
    select: function(event) {
      const index = this.selected.indexOf(event.target.innerText)
      console.log(index)

      if (index > -1) {
        this.selected.splice(index, 1)
      }
      else if (this.selected.length < 5) {
        this.selected.push(event.target.innerText)
      }
      else {
        alert('5타임까지만 신청할 수 있습니다.')
      }
    },

    tselect: function(event) {
      console.log(event.target.innerText)
      this.teacher = event.target.innerText
      if (event.target.innerText === 'Tony') {
        this.tony = true
        this.eric = false
      }
      else {
        this.eric = true
        this.tony = false
      }
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.box {
      border: 1px solid white;
      background-color: white;
      color: #84898C;
}
.tbox {
      border: 1px solid darkblue;
      background-color: white;
}
.tselectBox {
      border: 1px solid darkblue;
      background-color: #658dc63d;
      color: #0F4C81;
}
.selectBox {
      border: 1px solid #658dc63d;
      background-color: #658dc63d;
      color: #0F4C81;
    }
.page {
      box-shadow: 2px 2px 2px 2px lightgray;
}

.t-tony:hover, 
.t-eric:hover {
  background-color: #658dc63d;
}

.time:hover {
  background-color: #658dc63d;
}

</style>
