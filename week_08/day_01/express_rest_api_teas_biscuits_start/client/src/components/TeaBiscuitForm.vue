<template lang="html">
	<form v-on:submit.prevent="handleSubmit">
		<label for="name">Name:</label>
		<input type="text" name="name" v-model="name" />

		<label for="brand">Brand:</label>
		<input type="text" name="brand" v-model="brand" />

		<label for="type">Type</label>
		<select name="type" v-model="type">
			<option value="" disabled>Choose...</option>
			<option value="teas">Tea</option>
			<option value="biscuits">Biscuit</option>
		</select>

		<input type="submit" value="Save" />
	</form>
</template>

<script>
import { eventBus } from '../main';
export default {
	name: "tea-biscuit-form",
	data(){
		return {
			name: "",
			brand: "",
			type: ""
		}
	},
	methods: {
		handleSubmit(){

			const url = `http://localhost:3000/api/${this.type}`;
			const payload = {
				name: this.name,
				brand: this.brand
			};

			fetch(url, {
				method: 'POST',
				body: JSON.stringify(payload),
				headers: { 'Content-Type': 'application/json' }
			}).then(response => {
				eventBus.$emit("refresh-data");
				this.name = this.brand = this.type = "";
			});
		}
	}
}
</script>

<style lang="css" scoped>
</style>
