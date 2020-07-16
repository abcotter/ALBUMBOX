<template lang="pug">
	transition(
		name="modal-fade"
	)
		div(
			class="modal-backdrop"
		)
			div(
				class="modal"
			)
				header(
					class="modal-header"
				)
					div(

					) Edit Memory
					button(
						type="button"
						class="btn-close"
						@click="close"
					) x
				section(
					class="modal-body"
				)
					div(
						class="input-row"
					)
						img(
							class="image"
							:src="image.imageURL"
						)
						div(
							style="width: 500px;"
						)
							div(
								class="input-row"
							)
								div(
									class="input-label"
								) Message:
								textarea(
									type="text"
									maxlength="300"
									style="width: 200px; height: 200px;"
									:placeholder="image.description"
									v-model="description"
								)
					button(
						class="add-new-memory-button"
						@click="editMemory"
					) Apply
</template>
<script>
import axios from "axios";
import DatePicker from "v-calendar/lib/components/date-picker.umd";

export default {
	components: {
		DatePicker
	},
	props: ["image"],
	// Data
	data() {
		return {
			description: null,
			file: null,
			fileType: null,
			fileUploaded: false,
			acceptedTypes: ["jpeg", "png", "jpg"]
		};
	},
	computed: {},
	// Methods
	methods: {
		editMemory() {
			if (this.description) {
				let memDescription = this.image.description;

				if (this.description) {
					memDescription = this.description;
				}

				let formData = new FormData();

				formData.append("memDescription", memDescription);
				formData.append("imageID", this.image.imageID);

				axios.post(`${this.$apiURL}editImage`, formData).then(() => {
					this.date = null;
					this.description = null;
					this.$emit("edit:memory");
					this.close();
				});
			}
		},
		close() {
			this.$emit("close");
		}
	}
};
</script>
<style lang="scss">
.modal-backdrop {
	position: fixed;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	background-color: rgba(0, 0, 0, 0.3);
	display: flex;
	justify-content: center;
	align-items: center;
}

.modal {
	background: rgb(230, 199, 181);
	display: flex;
	flex-direction: column;
	width: 900px;
	height: 600px;
}

.modal-header {
	padding: 10px;
	display: flex;
}

.modal-header {
	border-bottom: 1px solid #eeeeee;
	justify-content: space-between;
	font-size: 15px;
	font-weight: 900;
}

.modal-body {
	position: relative;
	padding: 20px 35px;

	.input-row {
		display: flex;
		justify-content: space-around;
		padding: 15px;

		.image {
			width: 300px;
			height: 400px;
			object-fit: cover;
			border: 2px solid #efefef;
		}
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
}

.btn-close {
	border: none;
	font-size: 20px;
	cursor: pointer;
	font-weight: bold;
	background: transparent;
}
</style>