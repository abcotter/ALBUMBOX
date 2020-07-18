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
					@click="$router.push('/home')"
				) ALBUMBOX / &nbsp;
				div(
					class="board-title"
					style="padding-left: 10px;"
				) {{$route.params.boardName}}
			div(
				style="display: flex;"
			)
				button(
					v-if="isEditMode || isDeleteMode"
					class="add-new-memory-button"
					@click="onDone"
				) Done
				Slide(
					right
					:isOpen="showDropdown"
					@openMenu="showDropdown = true"
					:burgerIcon="showBurger"
				)
					span(
						v-if="images"
						@click="toggleEditMode"
					) Edit Memories
					span(
						v-if="images"
						@click="toggleDeleteMode"
					) Delete Memories
					span(
						@click="enableAddImageModal"
					) Add New Memory
					span(
						@click="deleteBoard"
					) Delete Board
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
import { Slide } from "vue-burger-menu";

import ImageCard from "./ImageCard.vue";
import AddImageModal from "./AddImageModal.vue";
import EditImageModal from "./EditImageModal.vue";

export default {
	components: {
		AddImageModal,
		EditImageModal,
		ImageCard,
		Slide
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
			options: ["Edit", "Delete", "Add New Memory"],
			showAddImageModal: false,
			showBurger: true,
			showDropdown: false,
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
		deleteBoard() {
			let data = {
				id: this.$route.params.boardid
			};
			axios.post(`${this.$apiURL}deleteBoard`, data).then(() => {
				this.getBoards();
			});
			this.$router.push({ path: "/" });
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
			this.showDropdown = false;
			this.isEditMode = false;
			this.isDeleteMode = false;
			this.showAddImageModal = true;
		},
		enableEditModal($event) {
			this.isEditMode = false;
			this.isDeleteMode = false;
			this.showBurger = true;
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
					if (response.data.length > 0) {
						this.images = response.data;
					}
				});
		},
		onDone() {
			if (this.isEditMode) {
				this.stopEditMode();
			} else {
				this.stopDeleteMode();
			}
		},
		stopDeleteMode() {
			this.showBurger = true;
			this.isDeleteMode = false;
		},
		toggleDeleteMode() {
			this.showBurger = false;
			this.showDropdown = false;
			this.isEditMode = false;
			this.isDeleteMode = true;
		},
		stopEditMode() {
			this.showBurger = true;
			this.isEditMode = false;
		},
		toggleEditMode() {
			this.showBurger = false;
			this.showDropdown = false;
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
	background-image: url("../../public/board.png");
	background-position: center;
	background-repeat: no-repeat;
	background-size: cover;
	padding-bottom: 30px;
	overflow: scroll;

	.board-header {
		height: 85px;
		background-color: rgba(237, 179, 174, 0.6);
		display: flex;
		padding: 10px 25px 10px 25px;
		justify-content: space-between;
		border-bottom: 3px solid #efefef;

		.board-title {
			vertical-align: middle;
			font-size: 60px;
			font-weight: 600;
			font-family: "Permanent Marker";
			text-shadow: 3px 3px rgba(172, 121, 121, 0.938);
			font-family: "Permanent Marker";
			color: #efefef;
		}

		.dropdown {
			position: relative;
			width: 200px;
			height: 130px;
			perspective: 1000px;
			display: block;
			z-index: 100;
			padding-inline-start: 0px;
			list-style-type: none;
			background-color: #efef;
		}

		.add-new-memory-button {
			padding-left: 3px;
			padding-right: 3px;
			margin-top: 30px;
			height: 60px;
			width: 60px;
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

// Burger menu classes
.bm-burger-button {
	position: fixed;
	width: 36px;
	height: 30px;
	left: 36px;
	top: 36px;
	cursor: pointer;
}
.bm-burger-bars {
	background-color: #efefef;
}
.line-style {
	position: absolute;
	height: 5px;
	border-radius: 3px;
	left: 0;
	right: 0;
}
.cross-style {
	position: absolute;
	top: 24px;
	cursor: pointer;
}
.bm-cross {
	background: #efefef;
}
.bm-cross-button {
	height: 34px;
	width: 34px;
}
.bm-menu {
	height: 100%; /* 100% Full-height */
	width: 0; /* 0 width - change this with JavaScript */
	position: fixed; /* Stay in place */
	z-index: 1000; /* Stay on top */
	top: 0;
	left: 0;
	background-color: rgba(153, 115, 115, 0.89); /* Black*/
	overflow-x: hidden; /* Disable horizontal scroll */
	padding-top: 60px; /* Place content 60px from the top */
	transition: 0.5s; /*0.5 second transition effect to slide in the sidenav*/
}

.bm-overlay {
	background: rgba(0, 0, 0, 0.3);
}
.bm-item-list {
	color: #b8b7ad;
	margin-left: 10%;
	font-size: 20px;
}
.bm-item-list > * {
	display: flex;
	text-decoration: none;
	padding: 0.7em;
	color: #efefef;
	font-weight: 600;
	cursor: pointer;
}
.bm-item-list > * > span {
	margin-left: 10px;
	font-weight: 700;
	color: #efefef;
}
</style>