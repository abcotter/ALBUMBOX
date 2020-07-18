<template lang="pug">

div(
	class="main"
)
	div(
		class="header-login"
	) ALBUMBOX
	div(
		class="left-side"
	)
		div(
			class="login"
		)
			input(
				class="login-input"
				placeholder="Email or Username"
			)
			input(
				class="login-input"
				placeholder= "Password"
			) 
		div(
			class="login-label"
			@click="Login"
		) LOGIN
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
export default {
	// Data
	// Methods
	methods: {
		Login() {}
	}
};
</script>

<style lang="scss">
.main {
	width: 100%;
	height: 100%;
	display: flex;

	.header-login {
		position: absolute;
		top: 30px;
		left: 30px;
		padding: 15px;
		width: 900px;
		background: rgba(237, 179, 174, 0.856);
		font-size: 135px;
		text-shadow: 3px 3px rgba(172, 121, 121, 0.938);
		font-family: "Permanent Marker";
		color: #efefef;
		z-index: 2;
	}

	.left-side {
		width: 40%;
		background-color: rgba(211, 174, 174, 0.89);

		.login {
			width: 400px;
			height: 280px;
			margin: auto;
			border-radius: 5px;
			margin-top: 48%;
			padding-left: 65px;

			.login-input {
				color: #efefef;
				width: 300px;
				margin-top: 60px;
				font-size: 15px;
				font-weight: 400;
				padding: 10px;
				float: left;
				border-radius: 5px;
				background: transparent;
				border-color: rgba(203, 140, 137, 0.616);
			}
		}

		.login-label {
			color: #efefef;
			font-size: 35px;
			font-weight: 600;
			text-shadow: 2px 2px rgba(172, 121, 121, 0.938);
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
			margin-top: 25%;

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