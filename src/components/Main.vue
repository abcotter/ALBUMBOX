<template lang="pug">
	div(
		class="main-page"
	)
		div(
			class="header"
		)
			div(
				class="title"
			) ALBUMBOX
		div(
			class="main-body"
		)
			div(
				style="font-size: 30px; font-weight: 600; margin-bottom: 10px;"
			) My Boards
			ul(
				class="board-list"
			)
				li(
					class="board-list"
					v-for="board in boards"
					:key="board.id"
				)
					div(
						style="display: flex;"
					)
						div(
							class="board-list-item"
							@click="goToBoard(board)"
						) {{ board.name }}
						button(
							class="delete-item"
							@click="deleteBoard(board)"
						) x
			button(
				class="add-new-board-button"
				@click="addBoardModal = !addBoardModal"
			) Add New Board
			div(
				v-show="addBoardModal"
			)
				div(
					class="new-board-form"
				)
					div(
						style="margin-bottom: 10px;"
					) To get started just give us an awesome name for your new board!
					div(

					)
						span(
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

export default {
	components: {},
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

.main-page {
	width: 100%;
	height: 100%;
	background-color: rgba(230, 184, 156, 0.6);

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

	.main-body {
		padding: 30px;
		overflow: scroll;

		.board-list {
			width: 200px;
			max-height: 300px;
			padding-left: 13px;
			margin-top: 10px;
			margin: auto;
			list-style-type: circle;
			display: flex;
			flex-direction: column;
			justify-content: space-between;

			.board-list-item {
				font-size: 20px;
				font-weight: 500;
				width: 100%;
				text-align: left;
			}

			.board-list-item:hover {
				color: #efefef;
				cursor: pointer;
			}

			.delete-item {
				background-color: transparent;
				border: none;
				font-size: 13px;
				font-weight: 600;

				&:hover {
					cursor: pointer;
					font-weight: 900;
				}
			}
		}

		.add-new-board-button {
			width: 170px;
			height: 30px;
			background-color: #904e55;
			color: #efefef;
			font-size: 15px;
			font-weight: 600;
			border-radius: 5px;
			border: none;
			margin-bottom: 15px;
			margin-top: 15px;

			&:hover {
				width: 173px;
				height: 32px;
				background-color: #843f55;
				cursor: pointer;
			}
		}

		.new-board-form {
			margin: auto;
			padding: 10px;
			width: 400px;
			height: 200px;
			background-color: rgba(230, 184, 156, 0.7);
			border: 2px solid rgba(230, 184, 156, 1);
			border-radius: 7px;
			display: flex;
			flex-direction: column;
			justify-content: space-between;

			.board-name-input {
				height: 30px;
				font-size: 15px;
				padding-left: 5px;
			}
		}
	}
}
</style>