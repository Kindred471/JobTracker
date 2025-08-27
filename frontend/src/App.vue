<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center p-6">
    <h1 class="text-2xl font-bold mb-6">🎯 投递进程记录</h1>

    <div class="w-full max-w-5xl bg-white shadow rounded-xl overflow-hidden relative">

      <table class="w-full">
        <thead class="bg-gray-200 text-left">
          <tr>
            <th class="p-3">公司</th>
            <th class="p-3">官网</th>
            <th class="p-3">岗位</th>
            <th class="p-3">状态</th>
            <th class="p-3">投递日期</th>
            <th class="p-3">操作</th>
          </tr>
        </thead>
        <tbody>
          <!-- 表格顶部新增行 -->
          <tr class="bg-gray-50 border-b">
            <td class="p-2">
              <input v-model="newJob.company" placeholder="公司名称" class="w-full border rounded px-2 py-1" />
            </td>
            <td class="p-2">
              <input v-model="newJob.website" placeholder="公司官网" class="w-full border rounded px-2 py-1" />
            </td>
            <td class="p-2">
              <input v-model="newJob.position" placeholder="岗位名称" class="w-full border rounded px-2 py-1" />
            </td>
            <td class="p-2">
              <select v-model="newJob.status" class="w-full border rounded px-3 py-1">
                <option value="投递中">投递</option>
                <option value="已面试">面试</option>
                <option value="Offer">Offer</option>
                <option value="被拒">被拒</option>
              </select>
            </td>
            <td class="p-2">
              <input type="date" v-model="newJob.date" class="w-full border rounded px-2 py-1" />
            </td>
            <td class="p-2">
              <button @click="addJob" class="px-3 py-1 bg-green-600 text-white rounded hover:bg-green-700">
                添加
              </button>
            </td>
          </tr>

          <!-- 已有记录 -->
          <tr v-for="job in jobs" :key="job.id" class="border-b">
            <td class="p-3">
              <input v-model="job.company" @blur="updateJob(job)" class="w-full border rounded px-2 py-1" />
            </td>
            <td class="p-3">
              <input v-model="job.website" @blur="updateJob(job)" class="w-full border rounded px-2 py-1" />
              <div class="mt-1">
                <a
                  v-if="job.website"
                  :href="job.website"
                  target="_blank"
                  class="text-blue-600 hover:underline text-sm"
                >
                  访问官网
                </a>
              </div>
            </td>
            <td class="p-3">
              <input v-model="job.position" @blur="updateJob(job)" class="w-full border rounded px-2 py-1" />
            </td>
            <td class="p-3">
              <select
                v-model="job.status"
                @change="updateJob(job)"
                :class="{
                  'text-yellow-600': job.status === '投递中',
                  'text-purple-600': job.status === '已面试',
                  'text-green-600': job.status === 'Offer',
                  'text-red-600': job.status === '被拒'
                }"
                class="w-full border rounded px-3 py-1"
              >
                <option value="投递中">投递</option>
                <option value="已面试">面试</option>
                <option value="Offer">Offer</option>
                <option value="被拒">被拒</option>
              </select>
            </td>
            <td class="p-3">
              <input type="date" v-model="job.date" @blur="updateJob(job)" class="w-full border rounded px-2 py-1" />
            </td>
            <td class="p-3">
              <button
                @click="deleteJob(job.id)"
                class="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600"
              >
                删除
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const jobs = ref([])

const newJob = ref({ company: '', website: '', position: '', status: '投递中', date: '' })

// 获取所有记录
const fetchJobs = async () => {
  const res = await axios.get('/api/jobs')
  jobs.value = res.data
}

// 新增记录
const addJob = async () => {
  if (!newJob.value.company || !newJob.value.position || !newJob.value.date) return
  const res = await axios.post('/api/jobs', newJob.value)
  jobs.value.unshift(res.data) // 直接使用后端返回的新对象
  newJob.value = { company: '', website: '', position: '', status: '投递中', date: '' }
}


// 更新记录
const updateJob = async (job) => {
  await axios.put(`/api/jobs/${job.id}`, job)
}

// 删除记录
const deleteJob = async (id) => {
  await axios.delete(`/api/jobs/${id}`)
  jobs.value = jobs.value.filter(j => j.id !== id)
}

onMounted(fetchJobs)
</script>
