from functools import partial

import pandas as pd
import numpy as np
from execution_environment.command_executor import Argument
from otlang.sdk.syntax import Keyword
from pp_exec_env.base_command import BaseCommand, Syntax


def match(df: pd.DataFrame, arg: Argument) -> pd.DataFrame:
    return df[arg.key].str.match(arg.value)


class Match(BaseCommand):
    syntax = Syntax([Keyword(name="vals", inf=True)], use_timewindow=False)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        m = partial(match, df)
        return df[np.logical_or.reduce(list(map(m, self.get_iter("vals"))))].copy()
