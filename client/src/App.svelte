<script>
	let product_data;
	let loading = false;

	async function get_price() {
		loading = true;
		console.log(loading)
		let p_id = document.getElementById("pnumber").value;
		await fetch(`http://localhost:5000/price/${p_id}`)
			.then(response => response.json())
			.then(data => product_data = data);
		loading = false;
	}

</script>

<main>
	<h1>Prisjakt Price checker</h1>
	<table>
		<tr>
			<td>
				<form class="card">
					<label for="pnumber">Skriv inn produktnavn:</label>
					<input type="text" id="pnumber" name="pnumber">
					<div class="submit" on:click={get_price}>Søk</div>
				</form>
			</td>
		</tr>
		{#if loading}
			<tr>
				<td>Laster inn...</td>
			</tr>
		{/if}
		<tr>
			<td>
				{#if product_data !== undefined}
					<div class="card">
						<p>{product_data.title}</p>
						<img src={product_data.img_src} alt="product">
						<p>{product_data.price}</p>
						<div class="submit">Varsle meg om prisendring</div>
					</div>
				{/if}
			</td>
		</tr>
	</table>
	
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	h1 {
		color: #2ECC40;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	img {
		max-height: 180px;
	}

	.card {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2);
		border-radius: 6px;
		border: 1px solid rgba(0, 0, 0, 0.2);
		width: 350px;
		min-height: 125px;
		padding: 5px;
		margin: 5px;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	#pnumber {
		border-radius: 6px;
	}

	.submit {
		border-radius: 6px;
		border: 1px solid rgba(0, 0, 0, 0.2);
		min-width: 160px;
		max-width: 200px;
		padding: 5px;
	}

	.submit:hover {
		cursor: pointer;
	}
</style>