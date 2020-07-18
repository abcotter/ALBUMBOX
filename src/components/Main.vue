<template lang="pug">
	div(
		class="main"
	)
		div(
			class="background"
		)
		div(
			class="main-page"
		)
			div(
				class="header"
			)
				div(
					class="title"
				) ALBUMBOX
			Slide(
				right
			)
			div(
				class="main-body"
			)
				div(
					class="board-section"
				)
					div(
						style="font-size: 50px; font-weight: 600; margin-bottom: 10px; font-family: Permanent Marker"
					) Boards
					div(
						class="board-list"
						v-for="board in boards"
						:key="board.id"
					)
						div(
							style="display: flex; margin-bottom: 20px;"
						)
							div(
								class="board-list-item"
								@click="goToBoard(board)"
							) {{ board.name }}
							button(
								v-if="false"
								class="delete-item"
								@click="deleteBoard(board)"
							)
								ion-icon(
									name="close-outline"
								)
					button(
						class="add-new-board-button"
						@click="addBoardModal = !addBoardModal"
					) Add New Board
				div(
					class="new-board-section"
				)
					div(
						v-show="addBoardModal"
					)
						div(
							class="new-board-form"
						)
							div(
								style="display: flex;"
							)
								div(
									style="margin-bottom: 40px; margin-top: 80px; font-size: 30px;"
								) To get started just give us an awesome name for your new board!
								div(
									@click="addBoardModal = false;"
									class="close-icon"
								)
									ion-icon(
										style="font-size: 30px;"
										name="close-outline"
									)
							div(
								
							)
								span(
									style="font-size: 20px;"
								) Board Name: &nbsp;
								input(
									class="board-name-input"
									type="text"
									placeholder="Insert name here!"
									v-model="boardName"
								)
							button(
								class="add-new-board-button"
								style="margin: auto;"
								@click="onClickNewBoard"
							) Create
</template>

<script>
import axios from "axios";
import { Slide } from "vue-burger-menu";

export default {
	components: {
		Slide
	},
	//Life hooks
	mounted() {
		this.getBoards();
	},
	// Data
	data() {
		return {
			addBoardModal: false,
			boards: [],
			boardName: null
		};
	},
	computed: {},
	// Methods
	methods: {
		deleteBoard(board) {
			let data = {
				id: board.id
			};
			axios.post(`${this.$apiURL}deleteBoard`, data).then(() => {
				this.getBoards();
			});
		},
		getBoards() {
			axios.get(`${this.$apiURL}getBoards`).then(response => {
				this.boards = response.data;
			});
		},
		goToBoard(board) {
			this.$router.push({
				path: `/board/${board.id}/${board.name}`
			});
		},
		onClickNewBoard() {
			if (this.boardName == null) {
				this.$toast.error("you forgot a name!");
			} else {
				let data = {
					name: this.boardName
				};
				axios.post(`${this.$apiURL}createBoard`, data).then(response => {
					let board = {
						id: response.data.boardID,
						name: response.data.boardName
					};
					this.getBoards();
					this.goToBoard(board);
				});
			}
		}
	}
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Permanent+Marker");
@import url("https://fonts.googleapis.com/css?family=Cedarville+Cursive");

.main {
	width: 100%;
	height: 100%;

	.background {
		width: 100%;
		height: 100%;
		background-image: url("../../public/main.jpg");
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
		opacity: 0.6;
	}

	.main-page {
		width: 100%;
		height: 100%;
		background: transparent;
		z-index: 2;
		position: absolute;
		top: 0;
		left: 0;
		padding: 0;
		display: flex;
		flex-direction: column;

		.header {
			height: 85px;
			background-color: rgba(211, 174, 174, 0.89);
			display: flex;
			padding: 10px 25px 10px 25px;
			justify-content: space-between;
			opacity: 1;
			border-bottom: 3px solid #1b1b1b;

			.title {
				vertical-align: middle;
				font-size: 60px;
				font-weight: 600;
				font-family: "Permanent Marker";
			}
		}

		.main-body {
			overflow: scroll;
			width: 100%;
			height: 100%;
			display: flex;

			.board-section {
				padding: 30px;
				background-color: rgba(240, 226, 226, 0.89);
				border-right: 3px solid #1b1b1b;
				width: 400px;

				.add-new-board-button {
					width: 160px;
					height: 50px;
					border-radius: 5px;
					background-color: #904e55;
					color: #efefef;
					font-size: 15px;
					font-weight: 600;
					border: none;

					&:hover {
						background-color: #843f55;
						cursor: pointer;
					}
				}

				.board-list {
					width: 300px;
					max-height: 300px;
					margin: auto;
					display: flex;
					flex-direction: column;
					justify-content: space-between;

					.board-list-item {
						font-size: 20px;
						font-weight: 500;
						text-align: center;
						line-height: 40px;
						height: 40px;
						border-radius: 5px;
						width: 100%;
						background-color: #eeebeb;
						border: 1px solid #dfdcdc;
					}

					.board-list-item:hover {
						font-weight: 900;
						background-color: #dfdbdb;
						cursor: pointer;
					}
					.delete-item {
						background-color: transparent;
						border: none;
						font-size: 20px;
						font-weight: 600;

						&:hover {
							cursor: pointer;
							font-weight: 900;
						}
					}
				}
			}

			.new-board-section {
				width: 100%;
				display: flex;
				justify-content: space-around;

				.new-board-form {
					padding: 10px;
					margin-top: 25%;
					width: 600px;
					height: 500px;
					background-color: rgba(211, 174, 174, 0.89);
					border: 2px solid rgba(172, 140, 140, 0.89);
					border-radius: 7px;
					display: flex;
					flex-direction: column;
					justify-content: space-between;

					.close-icon {
						height: 40px;
						&:hover {
							cursor: pointer;
						}
					}

					.board-name-input {
						height: 30px;
						font-size: 20px;
						padding-left: 5px;
					}

					.add-new-board-button {
						width: 160px;
						height: 40px;
						border-radius: 5px;
						background-color: #904e55;
						color: #efefef;
						font-size: 15px;
						font-weight: 600;
						border: none;

						&:hover {
							background-color: #843f55;
							cursor: pointer;
						}
					}
				}
			}
		}
	}
}
</style>