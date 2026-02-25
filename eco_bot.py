import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "/", intents = intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    canal = bot.get_channel(1468742078786703383)
    if canal:
        await canal.send(
            "Comandos disponibles\n"
            "/how_to_recicle\n"
            "/eco_fact\n"
            "/eco_tip\n"
            "/recycling_bin\n"
            'Usa "/how_to_recicle lista" y "/recycling_bin lista" para ver sus listas'
        )

@bot.command()
async def how_to_recicle(ctx, *, material):
    if material == "lista":
        await ctx.send("La lista de objetos que tiene este bot es: plástico, cartón, papel, baterías, aceite usado, vidrio, metales, residuos organicos, electronicos")
    elif material == "plástico":
        await ctx.send("El plástico debe estar limpio y seco antes de reciclar, se recomienda aplastarlos para ahorrar espacio, algunos plásticos muy delgados o con comida no son reciclables")
    elif material == "cartón":
        await ctx.send("El cárton debe estar limpio y seco, se puede aplastar para facilitar su transporte, cartón humedo o manchado no se puede reciclar")
    elif material == "papel":
        await ctx.send("El papel debe estar limpio y seco, el papel sucio o mojado no se puede reciclar")
    elif material == "baterías":
        await ctx.send("Las baterias no se deben reciclar de manera normal, debido a que tienen sustancias que pueden ser contaminantes, deben llevarse a puntos de recoleccion especiales")
    elif material == "vidrio":
        await ctx.send("El vidrio debe limpiarse antes de reciclar, si esta roto, debe envolverse en papel o carton para evitar daños")
    elif material == "metales":
        await ctx.send("Los metales deben enjuagarse antes de reciclar, reciclarlos ahorra energia y recursos naturales")
    elif material == "residuos organicos":
        await ctx.send("Los restos de comida se pueden combertir en abono o compost para darles otro uso")
    elif material == "aceite usado":
        await ctx.send("El aceite usado debe dejarse enfriar, guardar en una botella, y llevarse a un punto de recoleccion especializado")
    elif material == "electronicos":
        await ctx.send("Los materiales electonicos no deben reciclarse de manera normal, tienen ambos materiales recicables y sustancias peligrosas, deben llevarse a centros especializados de reciclaje electronico")
    else:
        await ctx.send("Ese material no esta en los datos del bot")
        
@bot.command()
async def eco_fact(ctx):
    listoffacts = [
        "Una botella de plastico puede tardar hasta 450 años en degradarse",
        "Reciclar aluminio ahorra hasta el 95% de la energia necesaria para producirlo",
        "Cada persona genera más de 1kg de basura al día en promedio",
        "El vidrio puede reciclarse infinitamente sin perder calidad",
        "Apagar las luces innecesarias reduce el consumo de energía y la contaminación",
        "Una bolsa plástica puede tardar siglos en descomponerse",
        "El compostaje reduce significativamente la basura dómestica",
        "Los océanos reciben millones de toneladas de plástico cada año",
        "Usar botellas reutilizables reduce la contaminación plástica en hasta un 70%"
    ]
    fact = random.choice(listoffacts)
    await ctx.send(fact)

@bot.command()
async def eco_tip(ctx):
    tips = [
    "Lleva una botella reutilizable para reducir el uso de plástico.",
    "Apaga las luces cuando salgas de una habitación.",
    "Desconecta los cargadores cuando no los estés usando.",
    "Usa bolsas reutilizables en lugar de bolsas plásticas.",
    "Cierra el grifo mientras te cepillas los dientes para ahorrar agua.",
    "Reutiliza hojas de papel antes de desecharlas.",
    "Prefiere caminar o usar bicicleta en trayectos cortos.",
    "Compra solo lo necesario para evitar desperdicios.",
    "Separa los residuos en casa para facilitar el reciclaje.",
     "Evita productos con exceso de empaques."
    ]
        
    tip = random.choice(tips)
    await ctx.send(tip)
        
@bot.command()
async def recycling_bin(ctx, *, color):
    bins = {
        "azul": "El tacho azul es para papel y carton",
        "verde": "El tacho verde es para botellas y envases de vidrio",
        "amarillo": "El tacho amarillo es para plasticos, latas y envases",
        "marron": "El tacho marron es para residuos organicos",
        "negro": "El tacho negro es para basura no reciclable",
        "gris": "El tacho gris es para residuos no reciclables",
        "rojo": "El tacho rojo es para residuos peligrosos"
    }
    
    if color in bins:
        await ctx.send(bins[color])
    elif color == "lista":
        await ctx.send("Los colores de los cual tengo informacion son: azul, verde, amarillo, marron, negro, gris, rojo")
    else:
        await ctx.send("No tengo información sobre ese color")

bot.run('token')
