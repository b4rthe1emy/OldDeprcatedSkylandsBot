import discord
from poll_votes import vote


async def count_poll(interaction: discord.Interaction, poll_id: int, number: int):
    vote(poll_id, number)

    await interaction.response.send_message(
        f"Vous avez voté pour l'option : {number}", ephemeral=True
    )


def get_view(options):
    if options == 1:
        return PollButtons1
    if options == 2:
        return PollButtons2
    if options == 3:
        return PollButtons3
    if options == 4:
        return PollButtons4
    if options == 5:
        return PollButtons5
    if options == 6:
        return PollButtons6
    if options == 7:
        return PollButtons7
    if options == 8:
        return PollButtons8
    if options == 9:
        return PollButtons9
    if options == 10:
        return PollButtons10


class PollButtons1(discord.ui.View):

    def __init__(self, poll_id: int):
        super().__init__()
        self.poll_id = poll_id

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button0(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 0)


class PollButtons2(discord.ui.View):

    def __init__(self, poll_id: int):
        super().__init__()
        self.poll_id = poll_id

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button0(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 0)

    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 1)


class PollButtons3(discord.ui.View):

    def __init__(self, poll_id: int):
        super().__init__()
        self.poll_id = poll_id

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button0(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 0)

    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 1)

    @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
    async def button2(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 2)


class PollButtons4(discord.ui.View):

    def __init__(self, poll_id: int):
        super().__init__()
        self.poll_id = poll_id

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button0(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 0)

    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 1)

    @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
    async def button2(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 2)

    @discord.ui.button(label="3", style=discord.ButtonStyle.gray)
    async def button3(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 3)


class PollButtons5(discord.ui.View):

    def __init__(self, poll_id: int):
        super().__init__()
        self.poll_id = poll_id

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button0(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 0)

    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 1)

    @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
    async def button2(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 2)

    @discord.ui.button(label="3", style=discord.ButtonStyle.gray)
    async def button3(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 3)

    @discord.ui.button(label="4", style=discord.ButtonStyle.gray)
    async def button4(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 4)


class PollButtons6(discord.ui.View):

    def __init__(self, poll_id: int):
        super().__init__()
        self.poll_id = poll_id

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button0(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 0)

    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 1)

    @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
    async def button02(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 2)

    @discord.ui.button(label="3", style=discord.ButtonStyle.gray)
    async def button3(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 3)

    @discord.ui.button(label="4", style=discord.ButtonStyle.gray)
    async def button4(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 4)

    @discord.ui.button(label="5", style=discord.ButtonStyle.gray)
    async def button5(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 5)


class PollButtons7(discord.ui.View):

    def __init__(self, poll_id: int):
        super().__init__()
        self.poll_id = poll_id

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button0(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 0)

    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 1)

    @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
    async def button2(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 2)

    @discord.ui.button(label="3", style=discord.ButtonStyle.gray)
    async def button3(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 3)

    @discord.ui.button(label="4", style=discord.ButtonStyle.gray)
    async def button4(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 4)

    @discord.ui.button(label="5", style=discord.ButtonStyle.gray)
    async def button5(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 5)

    @discord.ui.button(label="6", style=discord.ButtonStyle.gray)
    async def button6(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 6)


class PollButtons8(discord.ui.View):

    def __init__(self, poll_id: int):
        super().__init__()
        self.poll_id = poll_id

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button0(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 0)

    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 1)

    @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
    async def button2(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 2)

    @discord.ui.button(label="3", style=discord.ButtonStyle.gray)
    async def button3(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 3)

    @discord.ui.button(label="4", style=discord.ButtonStyle.gray)
    async def button4(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 4)

    @discord.ui.button(label="5", style=discord.ButtonStyle.gray)
    async def button5(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 5)

    @discord.ui.button(label="6", style=discord.ButtonStyle.gray)
    async def button6(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 6)

    @discord.ui.button(label="7", style=discord.ButtonStyle.gray)
    async def button7(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 7)


class PollButtons9(discord.ui.View):

    def __init__(self, poll_id: int):
        super().__init__()
        self.poll_id = poll_id

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button0(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 0)

    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 1)

    @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
    async def button2(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 2)

    @discord.ui.button(label="3", style=discord.ButtonStyle.gray)
    async def button3(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 3)

    @discord.ui.button(label="4", style=discord.ButtonStyle.gray)
    async def button4(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 4)

    @discord.ui.button(label="5", style=discord.ButtonStyle.gray)
    async def button5(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 5)

    @discord.ui.button(label="6", style=discord.ButtonStyle.gray)
    async def button6(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 6)

    @discord.ui.button(label="7", style=discord.ButtonStyle.gray)
    async def button7(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 7)

    @discord.ui.button(label="8", style=discord.ButtonStyle.gray)
    async def button8(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 8)


class PollButtons10(discord.ui.View):

    def __init__(self, poll_id: int):
        super().__init__()
        self.poll_id = poll_id

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def button0(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 0)

    @discord.ui.button(label="1", style=discord.ButtonStyle.gray)
    async def button1(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 1)

    @discord.ui.button(label="2", style=discord.ButtonStyle.gray)
    async def button2(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 2)

    @discord.ui.button(label="3", style=discord.ButtonStyle.gray)
    async def button3(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 3)

    @discord.ui.button(label="4", style=discord.ButtonStyle.gray)
    async def button4(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 4)

    @discord.ui.button(label="5", style=discord.ButtonStyle.gray)
    async def button5(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 5)

    @discord.ui.button(label="6", style=discord.ButtonStyle.gray)
    async def button6(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 6)

    @discord.ui.button(label="7", style=discord.ButtonStyle.gray)
    async def button7(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 7)

    @discord.ui.button(label="8", style=discord.ButtonStyle.gray)
    async def button8(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 8)

    @discord.ui.button(label="9", style=discord.ButtonStyle.gray)
    async def button9(self, interaction: discord.Interaction, button):
        await count_poll(interaction, self.poll_id, 9)
