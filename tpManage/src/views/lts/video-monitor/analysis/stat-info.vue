<template>
  <div class="main" style="padding:10px;">
    <!--工具条-->
    <el-row :span="24" class="toolbar">
      <el-col :span="8">
        <el-select v-model="db_file" clearable placeholder="请选择" style="width: 98%">
          <el-option-group
            v-for="group in db_file_options"
            :key="group.label"
            :label="group.label">
            <el-option
              v-for="item in group.options"
              :key="item.value"
              :label="group.label+' - '+item.label"
              :value="item.value">
            </el-option>
          </el-option-group>
        </el-select>
      </el-col>
      <el-col :span="6">
        <el-date-picker
          v-model="dateTime"
          type="datetimerange"
          :picker-options="pickerOptions"
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          value-format="yyyy-MM-dd HH:mm:ss"
          align="right">
        </el-date-picker>
      </el-col>
      <el-col :span="6">
        <el-button type="primary" @click="handleLoadDB">加载</el-button>
      </el-col>
    </el-row>

    <!--数据统计分析-->
    <el-container>
      <el-main v-loading="dbLoading" element-loading-background="rgba(0, 0, 0, 0.5)">
        <div style="padding-top: 10px" >
          <LineChart ref="line_chart_one" />
         </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>

import LineChart from '@/views/lts/video-monitor/analysis/components/LineChart'
import LineGradientY from '@/views/lts/video-monitor/analysis/components/LineGradientY'
import { getDBList, getStatInfoList } from "@/api/lts/video-monitor/analysis";

export default {
  name: 'StatInfo',
  components: { LineChart, LineGradientY },
  data() {
    return {
      pickerOptions: {
          shortcuts: [{
            text: '最近一小时',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000);
              picker.$emit('pick', [start, end]);
            }
          },{
            text: '最近一天',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24);
              picker.$emit('pick', [start, end]);
            }
          },{
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
      dateTime: [
        // new Date(new Date().getTime() - 3600 * 1000 * 24),//默认开始时间
        // new Date(
        //   new Date().getFullYear(),
        //   new Date().getMonth(),
        //   new Date().getDate(),
        //   new Date().getHours(),
        //   new Date().getMinutes()
        // ), // 默认结束时间
      ],
      db_file_options: [],
      db_file: '',

      dbLoading: false,
      dataList: [],
      total: 0,
      page: 1,
      page_size: 10**11,
      page_count: 0,
    }
  },
  created() {
  },
  mounted() {
    this.fetchData()
  },
  methods: {
    // 获取ENV列表
    fetchData() {
      getDBList({}).then(response => {
        const { msg, code } = response
        if (code === 2) {
          this.db_file_options = response.data
        } else {
          this.$message.error({
            message: msg,
            center: true
          })
        }
      })
    },

    getStatDateTime: function(objInfo) {
      return objInfo['datetime'];
    },
    getStatOPS: function(objInfo) {
      return objInfo['ops'];
    },
    getStatElapsed: function(objInfo) {
      return objInfo['elapsed_avg'];
    },
    getObjQsize: function(objInfo) {
      return objInfo['queue_size_avg'];
    },
    handleLoadDB() {
      this.dbLoading = true
      const params = {
        page: this.page,
        page_size: this.page_size,
        datetime__gte: this.dateTime[0],
        datetime__lte: this.dateTime[1],
        db_path: this.db_file
      }
      getStatInfoList(params).then(response => {
        const { msg, code } = response
        this.dbLoading = false
        if (code === 2) {
          this.total = response.data.count
          this.dataList = response.data.data.list
          const dataList = this.dataList
          this.$message.success({
            message: "数据库加载成功！",
            center: true
          })
          const xData = dataList.map(this.getStatDateTime)
          const yDataOPS = dataList.map(this.getStatOPS)
          const yDataElapsed = dataList.map(this.getStatElapsed)
          this.$refs.line_chart_one.initChart("统计信息", ["OPS", "时延"], xData, [yDataOPS, yDataElapsed])
        } else {
          this.dbLoading = false
          this.$message.error({
            message: msg,
            center: true
          })
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  ::v-deep .loading-div {
    width: 100%;
    position: absolute;
  }
  ::v-deep .el-drawer__body {
    overflow: auto;
  }
  ::v-deep .demo-drawer__content {
    margin-bottom: 2px;
    padding: 10px 20px 20px;
    overflow: auto;
  }
  ::v-deep .demo-drawer__footer{
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 0;
    border-top: 1px solid #e8e8e8;
    padding: 10px 16px;
    text-align: center;
    background-color: white;
  }
</style>
