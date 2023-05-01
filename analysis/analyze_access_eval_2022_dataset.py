#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import json
import logging
import sys
import traceback
from shutil import rmtree

import plotting_2022_third_party
from core_2022 import (
    get_crucial_stats,
    load_access_eval_2022_dataset,
)

###############################################################################

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)4s: %(module)s:%(lineno)4s %(asctime)s] %(message)s",
)
log = logging.getLogger(__name__)

###############################################################################


class Args(argparse.Namespace):
    def __init__(self) -> None:
        self.__parse()

    def __parse(self) -> None:
        p = argparse.ArgumentParser(
            prog="analyze-access-eval-2022-dataset",
            description=(
                "Generate the access evaluation dataset plots and tables for "
                "all races covered in the 2022 preliminary study."
            ),
        )
        p.add_argument(
            "--all-plots",
            dest="all_plots",
            action="store_true",
            help=(
                "Should all plots be generated (including ones not in the final paper)."
            ),
        )
        p.parse_args(namespace=self)


###############################################################################


def main() -> None:
    try:
        args = Args()

        # Load data
        data = load_access_eval_2022_dataset()

        # Clear prior plots
        if plotting_2022_third_party.PLOTTING_DIR.exists():
            rmtree(plotting_2022_third_party.PLOTTING_DIR)

        # Generate plots
        log.info("Generating plots used in paper...")
        plotting_2022_third_party.plot_computed_fields_over_vote_share(data)
        plotting_2022_third_party.plot_computed_fields_over_vote_share_distance(data)
        plotting_2022_third_party.plot_summary_stats(data)
        plotting_2022_third_party.plot_location_based_summary_stats(data)
        plotting_2022_third_party.plot_party_based_summary_stats(data)
        plotting_2022_third_party.plot_electoral_position_based_summary_stats(data)
        plotting_2022_third_party.plot_categorical_against_errors_boxplots(data)
        plotting_2022_third_party.plot_electoral_level_against_vote_share(data)
        plotting_2022_third_party.plot_electoral_branch_against_vote_share(data)

    except Exception as e:
        log.error("=============================================")
        log.error("\n\n" + traceback.format_exc())
        log.error("=============================================")
        log.error("\n\n" + str(e) + "\n")
        log.error("=============================================")
        sys.exit(1)


###############################################################################
# Allow caller to directly run this module (usually in development scenarios)

if __name__ == "__main__":
    main()
