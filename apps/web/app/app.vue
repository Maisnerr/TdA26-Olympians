<template>
  <div class="container mx-auto max-w-3xl px-4 py-2">
    <pre class="overflow-x-auto font-mono text-sm">
      {{ JSON.stringify(users, null, 2) }}
    </pre>
    <div class="grid gap-6">
      <section class="rounded-lg border p-4">
        <h2 class="mb-2 font-medium">API Status</h2>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
const users = ref(null)

onMounted(async () => {
  const response = await fetch('/api/users')
  users.value = await response.json()
})
</script>
