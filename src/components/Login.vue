<template lang="pug">
	div(
		class="main"
	)
		div(
			class="left-side"
		)
			div(
				class="login"
			)
		div(
			class="right-side"
		)
			div(
				class="polaroid"
			)
				div(
					class="polaroid-text"
				) [Insert Memory Here]
</template>

<script>
export default {};
</script>

<style lang="scss">
.main {
	width: 100%;
	height: 100%;
	display: flex;

	.left-side {
		width: 40%;
		background-color: rgba(211, 174, 174, 0.89);

		.login {
			width: 400px;
			height: 400px;
			border-radius: 5px;
			background-color: rgba(211, 174, 174, 0.4);
		}
	}

	.right-side {
		width: 60%;
		background-image: url("../../public/login.png");
		background-position: center;
		background-repeat: no-repeat;
		background-size: cover;
		opacity: 0.7;
		justify-content: space-around;

		.polaroid {
			width: 350px;
			height: 380px;
			background-color: rgba(211, 174, 174, 0.4);
			border: 20px solid #efefef;
			border-bottom: 100px solid #efefef;
			margin: auto;
			margin-top: 30%;

			.polaroid-text {
				color: #532127;
				font-size: 25px;
				font-weight: 600;
				padding-top: 50%;
				opacity: 1;
			}
		}
	}
}
</style>