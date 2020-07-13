<template lang="pug">
	div(
		class="board-main"
	)
		div(
			class="board-header"
		)
			div(
				style="display: flex;"
			)
				div(
					class="board-title home"
					@click="$router.push('/')"
				) POSTCARD / &nbsp;
				div(
					class="board-title"
					style="padding-left: 10px;"
				) {{$route.params.boardName}}
			button(
				class="add-new-memory-button"
				@click="enableAddImageModal"
			) Add Memory
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
		AddImageModal(
			v-show="showAddImageModal"
			@close="closeModal"
		)
</template>

<script>
import axios from "axios";
import ImageCard from "./ImageCard.vue";
import AddImageModal from "./AddImageModal.vue";

export default {
	components: {
		AddImageModal,
		ImageCard
	},
	//lifehooks
	mounted() {
		this.getImages();
	},
	// Data
	data() {
		return {
			images: null,
			showAddImageModal: false
		};
	},
	// Methods
	methods: {
		closeModal() {
			this.showAddImageModal = false;
		},
		enableAddImageModal() {
			this.showAddImageModal = true;
		},
		getImages() {
			let boardId = this.$route.params.boardid;
			axios
				.get(`${this.$apiURL}getBoardImages`, {
					params: {
						boardId
					}
				})
				.then(response => {
					this.images = response.data;
				});
		}
	}
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Permanent+Marker");
@import url("https://fonts.googleapis.com/css?family=Cedarville+Cursive");

.board-main {
	width: 100%;
	height: 100%;
	background-color: rgba(230, 184, 156, 0.6);
	padding-bottom: 30px;

	.board-header {
		height: 40px;
		background-color: rgba(230, 184, 156, 1);
		display: flex;
		padding: 10px 25px 10px 25px;
		justify-content: space-between;

		.board-title {
			vertical-align: middle;
			font-size: 30px;
			font-weight: 600;
			font-family: "Permanent Marker";
		}

		.add-new-memory-button {
			width: 150px;
			height: 30px;
			background-color: #904e55;
			color: #efefef;
			font-size: 13px;
			font-weight: 600;
			border-radius: 5px;
			border: none;
			margin-top: 5px;

			&:hover {
				width: 151px;
				height: 31px;
				background-color: #843f55;
				cursor: pointer;
			}
		}

		.home:hover {
			cursor: pointer;
		}
	}

	.board-body {
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
			margin-bottom: 30px;
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