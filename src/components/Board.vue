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
				) ALBUMBOX / &nbsp;
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
					v-if="!isDeleteMode"
					class="add-new-memory-button"
					style="margin-right: 5px;"
					@click="toggleDeleteMode"
				) Delete
				button(
					v-if="isDeleteMode"
					class="add-new-memory-button"
					style="margin-right: 5px;"
					@click="stopDeleteMode"
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
				:class="{ shake : isDeleteMode || isEditMode }"
			)
				ImageCard(
					:image="image"
				)
				div(
					v-if="isDeleteMode"
					class="delete-overlay"
					@click="deleteImage(image)"
				)
					ion-icon(
						name="close-circle-outline"
						style="z-index: 3; font-size: 60px; padding-top: 55%;"
					)
				div(
					v-if="isEditMode"
					class="edit-overlay"
					@click="enableEditModal(image)"
				)
					ion-icon(
						name="pencil-outline"
						style="z-index: 3; font-size: 60px; padding-top: 55%;"
					)
		AddImageModal(
			:boardID = "this.$route.params.boardid"
			v-show="showAddImageModal"
			@close="closeAddModal"
			@add:image="getImages"
		)
		EditImageModal(
			:image = "imageToEdit"
			v-show="showEditImageModal"
			@close="closeEditModal"
			@edit:memory="getImages"
		)
</template>

<script>
import axios from "axios";
import ImageCard from "./ImageCard.vue";
import AddImageModal from "./AddImageModal.vue";
import EditImageModal from "./EditImageModal.vue";

export default {
	components: {
		AddImageModal,
		EditImageModal,
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
			imageToEdit: null,
			isDeleteMode: false,
			isEditMode: false,
			showAddImageModal: false,
			showEditImageModal: false
		};
	},
	// Methods
	methods: {
		closeAddModal() {
			this.showAddImageModal = false;
		},
		closeEditModal() {
			this.showEditImageModal = false;
		},
		deleteImage($event) {
			let data = {
				id: $event.imageID
			};
			axios.post(`${this.$apiURL}deleteImage`, data).then(() => {
				this.getImages();
			});
		},
		enableAddImageModal() {
			this.isEditMode = false;
			this.isDeleteMode = false;
			this.showAddImageModal = true;
		},
		enableEditModal($event) {
			this.isEditMode = false;
			this.isDeleteMode = false;
			this.imageToEdit = $event;
			this.showEditImageModal = true;
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
		stopDeleteMode() {
			this.isDeleteMode = false;
		},
		toggleDeleteMode() {
			this.isEditMode = false;
			this.isDeleteMode = true;
		},
		stopEditMode() {
			this.isEditMode = false;
		},
		toggleEditMode() {
			this.isDeleteMode = false;
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
		background-color: transparent;
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
			padding-left: 3px;
			padding-right: 3px;
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

			.delete-overlay {
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

			.edit-overlay {
				background: #d8d8d8;
				height: 100%;
				width: 100%;
				opacity: 0;
				z-index: 2;
				position: absolute;
				padding: 0;
				transition: opacity 0.5s;

				&:hover {
					opacity: 0.4;
					transition: opacity 0.5s;
				}
			}
		}
	}
}
</style>