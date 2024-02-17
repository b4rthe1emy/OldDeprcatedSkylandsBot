import discord
from dataclasses import dataclass as dt
from dataclasses import field


@dt
class Poll:
    poll_id: int
    poll_message: discord.Message
    votes: list[int] = field(default=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def vote(self, number):
        self.votes[number] += 1


def find_poll(poll_id):
    polls_id = [poll.poll_id for poll in polls]
    poll_index = polls_id.index(poll_id)
    return polls[poll_index]


polls: list[Poll] = []


def create_poll(poll_message: discord.Message, poll_id: int):
    poll = Poll(poll_id, poll_message)
    polls.append(poll)


def vote(poll_id, number):
    poll = find_poll(poll_id)
    poll.vote(number)
