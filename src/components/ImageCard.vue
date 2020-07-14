<template lang='pug'>
	
	div(
		class="postcard-wrapper"
	)
		div(
			class="postcard-inner"
			:class="{flip : flipped}"
			@click="flipMe"
		)
			div(
				class="image-front"
			)
				img(
					class="image"
					:src="image.imageURL"
				)
				div(
					class="image-date"
				) {{image.date}}
			div(
				class="image-back"
			)
				div(
					class="memory"
				) {{image.description}}
</template>

<script>
export default {
	// Data
	props: ["image"],
	data() {
		return {
			flipped: false
		};
	},
	// Methods
	methods: {
		flipMe() {
			this.flipped = !this.flipped;
		}
	}
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Cedarville+Cursive");
.postcard-wrapper {
	width: 100%;
	height: 100%;
	perspective: 1000px;

	.postcard-inner {
		position: relative;
		width: 100%;
		height: 100%;
		perspective: 1000px;
		text-align: center;
		transition: transform 0.6s;
		transform-style: preserve-3d;
		box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
	}

	.flip {
		transform: rotateY(180deg);
	}

	.image-front,
	.image-back {
		position: absolute;
		width: 100%;
		height: 100%;
		-webkit-backface-visibility: hidden;
		backface-visibility: hidden;
	}

	.image-front {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		background-color: #ffffff;

		.image {
			width: 90%;
			height: 80%;
			margin: auto;
			object-fit: cover;
			border: 1px solid #efefef;
		}
		.image-date {
			height: 30px;
			font-size: 20px;
			font-family: "Permanent Marker";
			padding-bottom: 30px;
		}
	}

	.image-back {
		transform: rotateY(180deg);
		font-family: "Cedarville Cursive";
		font-size: 20px;
		background-color: #fff;

		.memory {
			padding: 15px;
			width: 90%;
			vertical-align: middle;
		}
	}
}
</style>