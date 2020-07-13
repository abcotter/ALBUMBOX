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
						style="display: flex;"
					)
						div(

						) Image:
						input(
							type="file"
						)
					div(
						style="display: flex;"
					)
						div(

						) Date:
						DatePicker(
							
						)
					div(
						style="display: flex;"
					)
						div(

						)
							div(
								
							) Message:
							div(

							) (max. 300)
						textarea(
							type="text"
							maxlength="300"
						)
</template>
<script>
import DatePicker from "v-calendar/lib/components/date-picker.umd";

export default {
	components: {
		DatePicker
	},
	methods: {
		close() {
			this.$emit("close");
		}
	}
};
</script>
<style>
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
	padding: 20px 10px;
}

.btn-close {
	border: none;
	font-size: 20px;
	cursor: pointer;
	font-weight: bold;
	background: transparent;
}
</style>