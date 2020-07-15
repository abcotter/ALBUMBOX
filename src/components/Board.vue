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
				) MiFOTO / &nbsp;
				div(
					class="board-title"
					style="padding-left: 10px;"
				) {{$route.params.boardName}}
			div(
				
			)
				button(
					v-if="!isEditMode"
					class="add-new-memory-button"
					style="margin-right: 5px;"
					@click="toggleEditMode"
				) Edit
				button(
					v-if="isEditMode"
					class="add-new-memory-button"
					style="margin-right: 5px;"
					@click="stopEditMode"
				) Done
				button(
					class="add-new-memory-button"
					@click="enableAddImageModal"
				) Add Memory
		div(
			class="board-body"
		)
			div(
				v-for="image in images"
				:key="image.id"
				class="image-card"
				:class="{ shake : isEditMode }"
			)
				ImageCard(
					:image="image"
				)
				div(
					v-if="isEditMode"
					class="overlay"
					@click="deleteImage(image)"
				)
					ion-icon(
						name="close-circle-outline"
						style="z-index: 3; font-size: 60px; padding-top: 55%;"
					)
		AddImageModal(
			:boardID = "this.$route.params.boardid"
			v-show="showAddImageModal"
			@close="closeModal"
			@add:image="getImages"
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
			isEditMode: false,
			showAddImageModal: false
		};
	},
	// Methods
	methods: {
		closeModal() {
			this.showAddImageModal = false;
		},
		deleteImage($event) {
			console.log($event);
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
		},
		stopEditMode() {
			this.isEditMode = false;
		},
		toggleEditMode() {
			this.isEditMode = true;
		}
	}
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Permanent+Marker");
@import url("https://fonts.googleapis.com/css?family=Cedarville+Cursive");

@keyframes shake {
	0% {
		transform: translate(0.5px, 0.5px) rotate(0deg);
	}
	10% {
		transform: translate(-0.5px, -1px) rotate(-0.5deg);
	}
	20% {
		transform: translate(-1.5px, 0px) rotate(0.5deg);
	}
	30% {
		transform: translate(1.5px, 1px) rotate(0deg);
	}
	40% {
		transform: translate(0.5px, -0.5px) rotate(0.5deg);
	}
	50% {
		transform: translate(-0.5px, 1px) rotate(-0.5deg);
	}
	60% {
		transform: translate(-1.5px, 0.5px) rotate(0deg);
	}
	70% {
		transform: translate(1.5px, 0.5px) rotate(-0.5deg);
	}
	80% {
		transform: translate(-0.5px, -0.5px) rotate(0.5deg);
	}
	90% {
		transform: translate(0.5px, 1px) rotate(0deg);
	}
	100% {
		transform: translate(0.5px, -1px) rotate(-0.5deg);
	}
}

.shake {
	/* Start the shake animation and make the animation last for 0.5 seconds */
	animation: shake 0.8s;

	/* When the animation is finished, start again */
	animation-iteration-count: infinite;
}

.board-main {
	width: 100%;
	height: 100%;
	background-color: rgba(230, 184, 156, 0.6);
	padding-bottom: 30px;
	overflow: scroll;

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
		grid-template-columns: repeat(4, 1fr);
		grid-auto-rows: 30vw;
		grid-gap: 30px;

		.image-card {
			width: 100%;
			height: 100%;
			display: flex;
			flex-direction: column;
			margin-bottom: 30px;
			position: relative;

			.overlay {
				background: #b1182f;
				height: 100%;
				width: 100%;
				opacity: 0;
				z-index: 2;
				position: absolute;
				padding: 0;
				transition: opacity 0.5s;

				&:hover {
					opacity: 0.6;
					transition: opacity 0.5s;
				}
			}
		}
	}
}
</style>