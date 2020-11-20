<script>
	let product_data;
	let loading = false;
	let not_found;
	let show_main = true;

	async function get_price() {
		not_found = false;
		loading = true;
		let p_id = document.getElementById("pnumber").value;

		await fetch(`http://localhost:5000/price/${p_id}`)
			.then(response => response.json())
			.then(data => product_data = data)
			.catch(err => not_found = true);

		loading = false;
	};

	document.addEventListener('keypress', function (e) {
        if (e.keyCode === 13 || e.which === 13) {
            e.preventDefault();
			get_price()
        }        
    });

	function handleClick() {
		if (show_main) {
			show_main = false;
		} else {
			show_main = true;
		}
		
	};

	function sendAlert() {
		let email = document.getElementById("email").value;
		let priceLimit = document.getElementById("price").value;
		
		let user_data = {
			'email': email,
			'price_limit': priceLimit,
			'product_data': product_data, 
		}

		console.log(user_data);
	}
</script>

<main>
	<h1>Price alert</h1>
	{#if show_main}
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
					{#if not_found}
						<p>Produktet ble ikke funnet...</p>
					{/if}
					{#if product_data !== undefined}
						<div class="card">
							<p><a href={product_data.url}>{product_data.title}</a></p>
							<img src={product_data.img_src} alt="product">
							<p>kr {product_data.price}</p>
							<div class="submit" id="varsel" on:click={handleClick}>Varsle meg om prisendring</div>
						</div>
					{/if}
				</td>
			</tr>
		</table>
	{:else}
		<div>	
			<form class="card">
				<div class="submit" on:click={handleClick}>Tilbake til hovedmenyen</div>
				<label for="email">Skriv inn din epost-adresse:</label>
				<input type="text" id="email" name="email">
				<label for="price">Skriv inn prisgrense for når du vil varsles:</label>
				<input type="number" id="price" name="price">
				<div class="submit" id="sendAlert" on:click={sendAlert}>Send meg varsel</div>
			</form>
		</div>
	{/if}
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
		max-height: 150px;
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
		padding: 7px;
		margin: 10px 0px 10px 0px;
	}

	.submit:hover {
		cursor: pointer;
	}

	#varsel {
		margin: 0px 0px 10px 0px;
	}
</style>