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
			v-if="!signup"
			class="login"
		)
			input(
				class="login-input"
				placeholder="Email"
				v-model="email"
			)
			input(
				type="password"
				class="login-input"
				placeholder= "Password"
				v-model="password"
			) 
		div(
			v-if="signup"
			class="login"
		)
			input(
				class="login-input"
				placeholder="Enter Email"
				v-model="email"
			)
			input(
				type="password"
				class="login-input"
				placeholder= "Enter Password"
				v-model="password"
			)
			input(
				class="login-input"
				placeholder= "Enter Nickname"
				v-model="name"
			) 
		div(
			v-if="!signup"
			class="login-label"
			@click="Login"
		) LOGIN
		div(
			v-if="signup"
			class="login-label"
			@click="createAccount"
		) CREATE ACCOUNT
		div(
			v-if="!signup"
			style="font-sixe: 15px; color: #efefef; cursor: pointer;"
			@click="signup = true"
		) SIGN-UP
		div(
			v-if="signup"
			style="font-sixe: 15px; color: #efefef; cursor: pointer;"
			@click="signup = false"
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
import axios from "axios";

export default {
	// Data
	data() {
		return {
			email: null,
			name: null,
			password: null,
			signup: false
		};
	},
	// Methods
	methods: {
		createAccount() {
			let email = this.email;
			if (!this.email || !this.name || !this.password) {
				this.$toast.error("You are missing some important information!");
				return;
			}
			if (this.ValidateEmail(email)) {
				let data = {
					email: email,
					name: this.name,
					password: this.password
				};
				axios.post(`${this.$apiURL}createAccount`, data).then(response => {
					console.log(response);
				});
			}
		},
		Login() {},
		ValidateEmail(mail) {
			let pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
			if (pattern.test(mail)) {
				return true;
			}
			this.$toast.error("You have entered an invalid email address!");
			return false;
		}
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
		width: 850px;
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
			height: 330px;
			margin: auto;
			border-radius: 5px;
			margin-top: 35vh;
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
			cursor: pointer;
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
			margin-top: 28vh;

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