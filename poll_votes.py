import discord
from dataclasses import dataclass as dt
from prints import debug


class Poll:
    def __init__(
        self, poll_id: int, poll_message: discord.Message, options: int = 10
    ) -> None:
        self.poll_id: int = poll_id
        self.poll_message: discord.Message = poll_message
        self.options: int = options
        self.votes: tuple[int] = tuple([0 for _ in range(self.options)])

    def __repr__(self) -> str:
        return f'Poll(poll_id={self.poll_id}, poll_title="{self.poll_message.embeds[0].title}", votes={self.votes})'

    def vote(self, number):
        votes = list(self.votes)
        votes[number] += 1
        self.votes = tuple(votes)


def find_poll(poll_id):
    polls_id = [poll.poll_id for poll in polls]
    poll_index = polls_id.index(poll_id)
    return polls[poll_index]


polls: list[Poll] = []


def create_poll(poll_message: discord.Message, poll_id: int, options: int):
    poll = Poll(poll_id, poll_message, options)
    polls.append(poll)


def vote(poll_id, number):
    poll = find_poll(poll_id)
    poll.vote(number)
    debug(poll.votes)
