<template lang="pug">
	div(
		class="main"
	)
		div(
			class="header"
		)
			div(
				style="display: flex;"
			)
				div(
					class="title"
				) POSTCARD /
				div(
					class="title"
				) &nbsp; Summer 2020{{boardName}}
		div(
			class="board-body"
		)
			div(
				v-for="image in images"
				:key="image"
				class="image-card"
			)
				ImageCard(
					:image="image"
				)
				div(
					class="image-date"
				) Date
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
@import url("https://fonts.googleapis.com/css?family=Cedarville+Cursive");

.main {
	width: 100%;
	height: 100%;
	background-color: rgba(230, 184, 156, 0.6);
	padding-bottom: 30px;

	.header {
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

	.board-body {
		height: 100%;
		padding: 30px;
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		grid-auto-rows: 40vw;
		grid-gap: 30px;
		overflow: scroll;

		.image-card {
			width: 100%;
			height: 100%;
			background-color: #efefef;
			display: flex;
			flex-direction: column;
		}

		.image-date {
			height: 30px;
			font-size: 20px;
			font-family: "Permanent Marker";
			padding-bottom: 30px;
		}
	}
}
</style>