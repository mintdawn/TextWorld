# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

import os
import glob
from subprocess import check_call
from os.path import join as pjoin

import textworld
import textworld.agents
from textworld.utils import make_temp_directory


def test_making_a_custom_game():
    with make_temp_directory(prefix="test_tw-make") as tmpdir:
        output_folder = pjoin(tmpdir, "gen_games")
        game_file = pjoin(output_folder, "game_1234.ulx")
        command = ["tw-make", "custom", "--seed", "1234", "--output", game_file]
        assert check_call(command) == 0

        assert os.path.isdir(output_folder)
        assert os.path.isfile(game_file)

        # Solve the game using WalkthroughAgent.
        agent = textworld.agents.WalkthroughAgent()
        textworld.play(game_file, agent=agent, silent=True)

    with make_temp_directory(prefix="test_tw-make") as tmpdir:
        output_folder = pjoin(tmpdir, "gen_games")
        game_file = pjoin(output_folder, "game_1234")  # Default extension is .ulx
        command = ["tw-make", "custom", "--seed", "1234", "--output", game_file]
        assert check_call(command) == 0

        assert os.path.isdir(output_folder)
        assert os.path.isfile(game_file + ".ulx")

        # Solve the game using WalkthroughAgent.
        agent = textworld.agents.WalkthroughAgent()
        textworld.play(game_file + ".ulx", agent=agent, silent=True)

    with make_temp_directory(prefix="test_tw-make") as tmpdir:
        output_folder = pjoin(tmpdir, "gen_games", "")
        command = ["tw-make", "custom", "--seed", "1234", "--output", output_folder]
        assert check_call(command) == 0

        assert os.path.isdir(output_folder)
        game_file = glob.glob(pjoin(output_folder, "*.ulx"))[0]

        # Solve the game using WalkthroughAgent.
        agent = textworld.agents.WalkthroughAgent()
        textworld.play(game_file, agent=agent, silent=True)

    with make_temp_directory(prefix="test_tw-make") as tmpdir:
        output_folder = pjoin(tmpdir, "gen_games")
        command = ["tw-make", "custom", "--seed", "1234", "--output", output_folder]
        assert check_call(command) == 0

        assert os.path.isfile(output_folder + ".ulx")

        # Solve the game using WalkthroughAgent.
        agent = textworld.agents.WalkthroughAgent()
        textworld.play(output_folder + ".ulx", agent=agent, silent=True)
