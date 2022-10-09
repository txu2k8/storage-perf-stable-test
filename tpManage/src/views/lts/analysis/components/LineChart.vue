<template>
  <div id="echart-line" :style="{width: '100%', height: '500%'}"></div>
</template>

<script>
import * as echarts from "echarts";

export default {
  name: "LineChart",
  methods:{
    initChart(title, legend_nameArr,xData,yDataArr) {
      let getChart = echarts.init(document.getElementById('echart-line'));
      const option = {
        tooltip: {
          trigger: 'axis'
        },
        title: {
          left: 'center',
          text: title
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: 'none'
            },
            restore: {},
            saveAsImage: {}
          }
        },
        dataZoom: [
          {
            type: 'inside',
            start: 0,
            end: 100
          },
          {
            start: 0,
            end: 100
          }
        ],
        legend: {
          data: legend_nameArr,
          left: 10
        },
        grid: { //调整图表上下左右位置
          top: '12%',
          left: '3%',
          right: '3%',
          bottom: 50,
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
            name: legend_nameArr[0],
            type: 'line',
            data: yDataArr[0]
          },
          {
            name: legend_nameArr[1],
            type: 'line',
            smooth: true,
            data: yDataArr[1]
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
