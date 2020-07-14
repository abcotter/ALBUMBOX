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

					) New Memory
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

						div(
							class="input-label"
						) Image:
						input(
							v-if="!fileUploaded"
							type="file"
							id="image"
							hidden=true
							@change="onChangeInputFile"
						)
						label(
							v-if="!fileUploaded"
							class="upload-icon"
							for="image"
						)
							ion-icon(
								name="cloud-upload-outline"
								size="large"
							)
						div(
							v-else
							style="display: flex;"
						)
							div(
								style="width: 90px; padding-top: 6px; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;"
							) {{file.name}}
							ion-icon(
								name="checkmark-circle-outline"
								size="large"
							)
					div(
						class="input-row"
						style="padding-right: 40px;"
					)
						div(
							class="input-label"
						) Date:
						DatePicker(
							style="width: 182px;"
							v-model="date"
						)
					div(
						class="input-row"
					)
						div(
							class="input-label"
						) Message: (max. 300)
						textarea(
							type="text"
							maxlength="300"
							style="width: 200px; height: 200px;"
							v-model="description"
						)
					button(
						class="add-new-memory-button"
						@click="addMemory"
					) Add
</template>
<script>
import axios from "axios";
import DatePicker from "v-calendar/lib/components/date-picker.umd";

export default {
	components: {
		DatePicker
	},
	props: ["boardID"],
	// Data
	data() {
		return {
			date: new Date(),
			description: null,
			file: null,
			fileType: null,
			fileUploaded: false
		};
	},
	// Methods
	methods: {
		addMemory() {
			if (!this.fileUploaded) {
				this.$toast.error("Whoops! Look like you forgot to upload the memory.");
				return;
			}
			let memDate = `${this.date.getDate()}/${this.date.getMonth()}/${this.date.getFullYear()}`;

			let memDescription = this.description;

			let formData = new FormData();

			formData.append("file", this.file);
			formData.append("fileType", this.fileType);
			formData.append("memDate", memDate);
			formData.append("memDescription", memDescription);
			formData.append("altText", this.file.name);
			formData.append("boardId", this.boardID);

			axios.post(`${this.$apiURL}addImage`, formData).then(() => {
				this.file = null;
				this.fileType = null;
				this.fileUploaded = false;
				this.description = null;
				this.$emit("add:image");
				this.close();
			});
		},
		close() {
			this.$emit("close");
		},
		onChangeInputFile($event) {
			let file = $event.target.files[0];
			this.file = file;
			this.fileType = file.type.split("/")[1];
			this.fileUploaded = true;
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
	width: 500px;
	height: 500px;
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
		justify-content: space-between;
		padding: 15px;

		.input-label {
			padding-top: 6px;
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