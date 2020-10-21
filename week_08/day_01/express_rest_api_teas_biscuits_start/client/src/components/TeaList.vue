<template lang="html">
	<div id="tea-list">
		<h2>All the teas!</h2>
		<ul>
			<li v-for="tea in teas">{{ tea.name }} by {{ tea.brand }}</li>
		</ul>
	</div>
</template>

<script>
export default {
	name: "tea-list",
	props: ["teas"]
}
</script>

<style lang="css" scoped>
</style>
