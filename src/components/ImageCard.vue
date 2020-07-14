<template lang='pug'>
	div(
		class="postcard-wrapper"
	)
		img(
			class="image"
			:src="image.imageURL"
		)
		
</template>

<script>
export default {
	props: ["image"]
};
</script>

<style lang="scss">
.postcard-wrapper {
	width: 100%;
	height: 100%;
	display: flex;
	padding-top: 15px;
	justify-content: center;
	background-color: #efefef;

	.image {
		width: 90%;
		height: 90%;
		background-color: #000000;
		object-fit: cover;
	}
}
</style>