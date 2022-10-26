<template>
  <div id="echart-line-gradient-y" :style="{width: '100%', height: '200%'}"></div>
</template>

<script>
import * as echarts from "echarts";

export default {
  name: "LineGradientY",
  methods:{
    initChart(name,xData,yData) {
      let getChart = echarts.init(document.getElementById('echart-line-gradient-y'));
      const option = {
          // Make gradient line here
        visualMap: [
          {
            show: false,
            type: 'continuous',
            seriesIndex: 0,
            // min: 0,
            max: 1
          }
        ],
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          data: [name],
          bottom: '0%'
        },
        grid: { //调整图表上下左右位置
          top: '10%',
          left: '3%',
          right: '8%',
          bottom: '10%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: xData
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: name,
            type: 'line',
            showSymbol: false,
            stack: '总量',
            data: yData
          },
        ]
      };

      getChart.setOption(option);
      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        getChart.resize();
      });
    },
  }
}
</script>

<style scoped>

</style>
