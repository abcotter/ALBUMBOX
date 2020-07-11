<template lang="pug">
	div(
		class="main"
	)
		div(
			class="header"
		)
			div(
				class="title"
			) POSTCARD
		div(
			class="body"
		)
			div(
				v-for="image in images"
				:key="image"
				class="image-card"
			)
				ImageCard(
					:image="image"
				)
</template>

<script>
import ImageCard from "./ImageCard.vue";

const testData = Array.from(Array(10).keys());

export default {
	components: {
		ImageCard
	},
	data() {
		return {
			images: testData
		};
	}
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Permanent+Marker");

.main {
	width: 100%;
	height: 100%;
	background-color: rgba(230, 184, 156, 0.6);
	overflow-x: hidden;

	.header {
		width: 100%;
		height: 40px;
		background-color: rgba(230, 184, 156, 0.7);
		display: flex;
		padding: 10px 25px 10px 25px;
		justify-content: space-between;

		.title {
			vertical-align: middle;
			font-size: 30px;
			font-weight: 600;
			font-family: "Permanent Marker";
		}
	}

	.body {
		width: 100%;
		height: 100%;
		display: flex;
		flex-flow: row wrap;
		padding: 10px;
		margin-left: 8px; /* Adjustment for the gutter */
		overflow-y: scroll;

		.image-card {
			width: 30%;
			height: 500px;
			background-color: #efefef;
			margin: 0 8px 8px 0; /* Some gutter */
		}
	}
}
</style>