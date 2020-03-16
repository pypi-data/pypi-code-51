import argparse
import json
import logging.handlers
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

import annofabapi
import pandas as pd
from annofabapi.models import ProjectMemberRole, TaskPhase

import annofabcli
from annofabcli import AnnofabApiFacade
from annofabcli.common.cli import AbstractCommandLineInterface, ArgumentParser, build_annofabapi_resource_and_login
from annofabcli.statistics.csv import Csv
from annofabcli.statistics.database import Database
from annofabcli.statistics.histogram import Histogram
from annofabcli.statistics.linegraph import LineGraph
from annofabcli.statistics.table import AggregationBy, Table

logger = logging.getLogger(__name__)


def write_project_name_file(annofab_service: annofabapi.Resource, project_id: str, output_project_dir: Path):
    """
    ファイル名がプロジェクト名のjsonファイルを生成する。
    """
    project_info = annofab_service.api.get_project(project_id)[0]
    project_title = project_info["title"]
    logger.info(f"project_titile = {project_title}")
    filename = annofabcli.utils.to_filename(project_title)
    output_project_dir.mkdir(exist_ok=True, parents=True)
    with open(str(output_project_dir / f"{filename}.json"), "w") as f:
        json.dump(project_info, f, ensure_ascii=False, indent=2)


def catch_exception(function: Callable[..., Any]) -> Callable[..., Any]:
    """
    Exceptionをキャッチしてログにstacktraceを出力する。
    """

    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:  # pylint: disable=broad-except
            logger.warning(e)
            logger.exception(e)

    return wrapped


class WriteCsvGraph:
    task_df: Optional[pd.DataFrame] = None
    annotation_df: Optional[pd.DataFrame] = None
    account_statistics_df: Optional[pd.DataFrame] = None
    df_by_date_user: Optional[pd.DataFrame] = None
    task_history_df: Optional[pd.DataFrame] = None

    def __init__(self, table_obj: Table, output_dir: Path, project_id: str):
        self.table_obj = table_obj
        self.csv_obj = Csv(str(output_dir), project_id)
        self.histogram_obj = Histogram(str(output_dir), project_id)
        self.graph_obj = LineGraph(str(output_dir), project_id)

    def _get_task_df(self):
        if self.task_df is None:
            self.task_df = self.table_obj.create_task_df()
        return self.task_df

    def _get_task_history_df(self):
        if self.task_history_df is None:
            self.task_history_df = self.table_obj.create_task_history_df()
        return self.task_history_df

    def _get_annotation_df(self):
        if self.annotation_df is None:
            self.annotation_df = self.table_obj.create_task_for_annotation_df()
        return self.annotation_df

    def _get_account_statistics_df(self):
        if self.account_statistics_df is None:
            self.account_statistics_df = self.table_obj.create_account_statistics_df()
        return self.account_statistics_df

    def _get_df_by_date_user(self):
        if self.df_by_date_user is None:
            task_df = self._get_task_df()
            self.df_by_date_user = self.table_obj.create_dataframe_by_date_user(task_df)
        return self.df_by_date_user

    def write_histogram_for_task(self) -> None:
        """
        タスクに関するヒストグラムを出力する。

        """
        task_df = self._get_task_df()
        catch_exception(self.histogram_obj.write_histogram_for_worktime)(task_df)
        catch_exception(self.histogram_obj.write_histogram_for_annotation_worktime_by_user)(task_df)
        catch_exception(self.histogram_obj.write_histogram_for_inspection_worktime_by_user)(task_df)
        catch_exception(self.histogram_obj.write_histogram_for_acceptance_worktime_by_user)(task_df)
        catch_exception(self.histogram_obj.write_histogram_for_other)(task_df)

    def write_histogram_for_annotation(self) -> None:
        """
        アノテーションに関するヒストグラムを出力する。
        """
        annotation_df = self._get_annotation_df()
        catch_exception(self.histogram_obj.write_histogram_for_annotation_count_by_label)(annotation_df)

    def write_linegraph_for_task_overall(self) -> None:
        """
        タスク関係の折れ線グラフを出力する。

        Args:
            user_id_list: 折れ線グラフに表示するユーザ

        Returns:

        """
        task_df = self._get_task_df()

        task_cumulative_df_overall = self.table_obj.create_cumulative_df_overall(task_df)
        catch_exception(self.graph_obj.write_cumulative_line_graph_overall)(task_cumulative_df_overall)

    def write_linegraph_for_by_user(self, user_id_list: Optional[List[str]] = None) -> None:
        """
        折れ線グラフをユーザごとにプロットする。

        Args:
            user_id_list: 折れ線グラフに表示するユーザ

        Returns:

        """
        task_df = self._get_task_df()

        task_cumulative_df_by_annotator = self.table_obj.create_cumulative_df_by_first_annotator(task_df)
        catch_exception(self.graph_obj.write_cumulative_line_graph_for_annotator)(
            df=task_cumulative_df_by_annotator, first_annotation_user_id_list=user_id_list,
        )

        task_cumulative_df_by_inspector = self.table_obj.create_cumulative_df_by_first_inspector(task_df)
        catch_exception(self.graph_obj.write_cumulative_line_graph_for_inspector)(
            df=task_cumulative_df_by_inspector, first_inspection_user_id_list=user_id_list,
        )

        task_cumulative_df_by_acceptor = self.table_obj.create_cumulative_df_by_first_acceptor(task_df)
        catch_exception(self.graph_obj.write_cumulative_line_graph_for_acceptor)(
            df=task_cumulative_df_by_acceptor, first_acceptance_user_id_list=user_id_list,
        )

        df_by_date_user = self._get_df_by_date_user()
        catch_exception(self.graph_obj.write_productivity_line_graph_for_annotator)(
            df=df_by_date_user, first_annotation_user_id_list=user_id_list
        )

        account_statistics_df = self._get_account_statistics_df()
        cumulative_account_statistics_df = self.table_obj.create_cumulative_df_by_user(account_statistics_df)
        catch_exception(self.graph_obj.write_cumulative_line_graph_by_date)(
            df=cumulative_account_statistics_df, user_id_list=user_id_list
        )

    def write_csv_for_task(self) -> None:
        """
        タスク関係のCSVを出力する。
        """
        task_df = self._get_task_df()
        catch_exception(self.csv_obj.write_task_list)(task_df, dropped_columns=["input_data_id_list"])
        catch_exception(self.csv_obj.write_task_count_summary)(task_df)
        catch_exception(self.csv_obj.write_worktime_summary)(task_df)
        catch_exception(self.csv_obj.write_count_summary)(task_df)

        member_df = self.table_obj.create_member_df(task_df)
        catch_exception(self.csv_obj.write_member_list)(member_df)

    def _write_メンバー別作業時間平均_画像1枚あたり_by_phase(self, phase: TaskPhase):
        df_by_inputs = self.table_obj.create_worktime_per_image_df(AggregationBy.BY_INPUTS, phase)
        self.csv_obj.write_メンバー別作業時間平均_画像1枚あたり(df_by_inputs, phase)

        df_by_tasks = self.table_obj.create_worktime_per_image_df(AggregationBy.BY_TASKS, phase)
        self.csv_obj.write_メンバー別作業時間平均_タスク1個あたり(df_by_tasks, phase)

    def write_メンバー別作業時間平均_画像1枚あたり_by_phase(self):
        for phase in TaskPhase:
            catch_exception(self._write_メンバー別作業時間平均_画像1枚あたり_by_phase)(phase)

    def write_csv_for_inspection(self) -> None:
        """
        検査コメント関係の情報をCSVに出力する。
        """
        inspection_df = self.table_obj.create_inspection_df()
        inspection_df_all = self.table_obj.create_inspection_df(only_error_corrected=False)

        catch_exception(self.csv_obj.write_inspection_list)(
            df=inspection_df, dropped_columns=["data"], only_error_corrected=True
        )
        catch_exception(self.csv_obj.write_inspection_list)(
            df=inspection_df_all, dropped_columns=["data"], only_error_corrected=False,
        )

    def write_csv_for_task_history(self) -> None:
        """
        タスク履歴関係の情報をCSVに出力する。
        """
        task_history_df = self._get_task_history_df()
        catch_exception(self.csv_obj.write_task_history_list)(task_history_df)

    def write_csv_for_annotation(self) -> None:
        """
        アノテーション関係の情報をCSVに出力する。
        """
        annotation_df = self._get_annotation_df()
        catch_exception(self.csv_obj.write_ラベルごとのアノテーション数)(annotation_df)

    def write_csv_for_date_user(self) -> None:
        """
        ユーザごと、日ごとの情報をCSVに出力する。
        """
        df_by_date_user = self._get_df_by_date_user()
        catch_exception(self.csv_obj.write_教師付作業者別日毎の情報)(df_by_date_user)

    def write_csv_for_account_statistics(self) -> None:
        account_statistics_df = self._get_account_statistics_df()
        catch_exception(self.csv_obj.write_ユーザ別日毎の作業時間)(account_statistics_df)

    def write_worktime_ratio(self) -> None:
        task_df = self._get_task_df()
        task_history_df = self._get_task_history_df()

        annotation_count_ratio_df = self.table_obj.create_annotation_count_ratio_df(task_history_df, task_df)
        catch_exception(self.csv_obj._write_csv)("タスク、フェーズ、他当者ごとの作業時間の比率.csv", annotation_count_ratio_df)


class VisualizeStatistics(AbstractCommandLineInterface):
    """
    統計情報を可視化する。
    """

    def visualize_statistics(
        self,
        project_id: str,
        work_dir: Path,
        output_dir: Path,
        task_query: Dict[str, Any],
        ignored_task_id_list: List[str],
        user_id_list: List[str],
        update: bool = False,
        should_update_annotation_zip: bool = False,
        should_update_task_json: bool = False,
    ):
        """
        タスク一覧を出力する

        Args:
            project_id: 対象のproject_id
            task_query: タスク検索クエリ

        """

        super().validate_project(project_id, project_member_roles=[ProjectMemberRole.OWNER])

        checkpoint_dir = work_dir / project_id
        checkpoint_dir.mkdir(exist_ok=True, parents=True)

        database = Database(self.service, project_id, str(checkpoint_dir))
        if update:
            database.update_db(
                task_query,
                ignored_task_id_list,
                should_update_annotation_zip=should_update_annotation_zip,
                should_update_task_json=should_update_task_json,
            )

        table_obj = Table(database, task_query, ignored_task_id_list)
        write_project_name_file(self.service, project_id, output_dir)

        write_obj = WriteCsvGraph(table_obj, output_dir, project_id)

        # テスト用のファイルを出力
        write_obj.write_worktime_ratio()

        # ヒストグラム
        write_obj.write_histogram_for_task()
        write_obj.write_histogram_for_annotation()

        # 折れ線グラフ
        write_obj.write_linegraph_for_by_user(user_id_list)
        write_obj.write_linegraph_for_task_overall()

        write_obj.write_csv_for_task()
        write_obj.write_csv_for_task_history()
        write_obj.write_csv_for_annotation()
        write_obj.write_csv_for_account_statistics()
        write_obj.write_csv_for_date_user()
        write_obj.write_csv_for_inspection()
        write_obj.write_メンバー別作業時間平均_画像1枚あたり_by_phase()

    def main(self):
        args = self.args
        task_query = annofabcli.common.cli.get_json_from_args(args.task_query)
        ignored_task_id_list = annofabcli.common.cli.get_list_from_args(args.ignored_task_id)
        user_id_list = annofabcli.common.cli.get_list_from_args(args.user_id)

        if args.work_dir is not None:
            work_dir = args.work_dir
        else:
            work_dir = annofabcli.utils.get_cache_dir()

        self.visualize_statistics(
            args.project_id,
            output_dir=Path(args.output_dir),
            work_dir=Path(work_dir),
            task_query=task_query,
            ignored_task_id_list=ignored_task_id_list,
            user_id_list=user_id_list,
            update=not args.not_update,
            should_update_annotation_zip=args.update_annotation,
            should_update_task_json=args.update_task_json,
        )


def main(args):
    service = build_annofabapi_resource_and_login(args)
    facade = AnnofabApiFacade(service)
    VisualizeStatistics(service, facade, args).main()


def parse_args(parser: argparse.ArgumentParser):
    argument_parser = ArgumentParser(parser)

    argument_parser.add_project_id()
    parser.add_argument("-o", "--output_dir", type=str, required=True, help="出力ディレクトリのパス")

    parser.add_argument(
        "-u",
        "--user_id",
        nargs="+",
        help=(
            "メンバごとの統計グラフに表示するユーザのuser_idを指定してください。"
            "指定しない場合は、辞書順に並べた上位20人が表示されます。"
            "file://`を先頭に付けると、一覧が記載されたファイルを指定できます。"
        ),
    )

    parser.add_argument(
        "-tq",
        "--task_query",
        type=str,
        help="タスクの検索クエリをJSON形式で指定します。指定しない場合はすべてのタスクを取得します。"
        "`file://`を先頭に付けると、JSON形式のファイルを指定できます。"
        "クエリのキーは、phase, statusのみです。[getTasks API](https://annofab.com/docs/api/#operation/getTasks) 参照",
    )

    parser.add_argument(
        "--ignored_task_id",
        nargs="+",
        help=("可視化対象外のタスクのtask_id。" "指定しない場合は、すべてのタスクが可視化対象です。" "file://`を先頭に付けると、一覧が記載されたファイルを指定できます。"),
    )

    parser.add_argument(
        "--not_update", action="store_true", help="作業ディレクトリ内のファイルを参照して、統計情報を出力します。" "AnnoFab Web APIへのアクセスを最小限にします。",
    )

    parser.add_argument(
        "--update_annotation",
        action="store_true",
        help="アノテーションzipを更新してから、アノテーションzipをダウンロードします。" "ただし、アノテーションzipの最終更新日時がタスクの最終更新日時より新しい場合は、アノテーションzipを更新しません。",
    )

    parser.add_argument(
        "--update_task_json", action="store_true", help="タスク全件ファイルJSONを更新してから、タスク全件ファイルJSONをダウンロードします。",
    )

    parser.add_argument(
        "--work_dir", type=str, help="作業ディレクトリのパス。指定しない場合はannofabcliのキャッシュディレクトリ（'$HOME/.cache/annofabcli'）に保存します。",
    )

    parser.set_defaults(subcommand_func=main)


def add_parser(subparsers: argparse._SubParsersAction):
    subcommand_name = "visualize"
    subcommand_help = "統計情報を可視化したファイルを出力します。"
    description = "統計情報を可視化したファイルを出力します。毎日 03:00JST頃に更新されます。"
    epilog = "チェッカーまたはオーナロールを持つユーザで実行してください。"

    parser = annofabcli.common.cli.add_parser(subparsers, subcommand_name, subcommand_help, description, epilog=epilog)
    parse_args(parser)
