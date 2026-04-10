<style>
pre.class_folder_structure span{
color:red;
background:yellow;
}
</style>
<h1>フレームワーク</h1>
GUIのフレームワーク<br>


<p>フォルダ構成</p>
<pre class='class_folder_structure'><code>
submit_asaihinata/
├── .gitattributes
├── .gitignore
├── .gitmessage
├── .vscode/ <span style="color:red;">vscodeの設定ファイル</span>
│   └── settings.json
├── README.md <span style="color:red;">プロジェクトの説明ファイル</span>
├── docs/ <span style="color:red;">ドキュメント</span>
│   ├── data/ <span style="color:red;">testsフォルダやフレームワークで使わなかったデータファイルの保存先</span>
│   │   ├── browser_jp.csv
│   │   └── color.csv
│   └── requirements.txt <span style="color:red;">使用した外部ライブラリ</span>
├── pyproject.toml
├── src/ <span style="color:red;">ソースフォルダ</span>
│   ├── __init__.py
│   ├── __init__.pyi
│   ├── types/ <span style="color:red;">型ヒントのフォルダ</span>
│   │   ├── __init__.py
│   │   ├── __init__.pyi
│   │   ├── basic.py
│   │   └── widget.py
│   └── widget/
│       ├── __init__.py
│       ├── _color.py
│       ├── _dialog/ <span style="color:red;">ダイアログに関するフォルダ</span>
│       │   ├── __init__.py
│       │   ├── __init__.pyi
│       │   ├── dialogs.py
│       │   └── popup.py
│       ├── _font.py
│       ├── _function.py
│       ├── _log/
│       │   ├── __init__.py
│       │   ├── __init__.pyi
│       │   ├── _clearsave.py
│       │   ├── _data.py
│       │   ├── _logfile.py
│       │   ├── data/
│       │   │   └── log.log
│       │   ├── logs.py
│       │   └── logtext.py
│       ├── _save.py
│       ├── _time.py
│       ├── _time.pyi
│       ├── base.py
│       ├── basic/
│       │   ├── Image/
│       │   │   ├── __init__.py
│       │   │   └── _photo.py
│       │   ├── Link/
│       │   │   └── __init__.py
│       │   ├── __init__.py
│       │   ├── __init__.pyi
│       │   ├── btnpop/
│       │   │   └── __init__.py
│       │   ├── calendar/
│       │   │   ├── __init__.py
│       │   │   ├── _calendar.py
│       │   │   └── tooltip.py
│       │   ├── element.py
│       │   ├── expansion/
│       │   │   └── __init__.py
│       │   └── ttkelement.py
│       ├── data/
│       │   ├── __init__.py
│       │   └── color.json
│       ├── developer.py
│       ├── developer.pyi
│       ├── graph/
│       │   ├── Graph.py
│       │   ├── Graph.pyi
│       │   ├── _2D/
│       │   │   ├── bargraph.py
│       │   │   ├── boxplot.py
│       │   │   ├── bubble.py
│       │   │   ├── ecdf.py
│       │   │   ├── errorbar.py
│       │   │   ├── eventplot.py
│       │   │   ├── hexbin.py
│       │   │   ├── hist.py
│       │   │   ├── hist2d.py
│       │   │   ├── linefill.py
│       │   │   ├── linegraph.py
│       │   │   ├── pie.py
│       │   │   ├── scatter.py
│       │   │   ├── stack.py
│       │   │   ├── stem.py
│       │   │   ├── step.py
│       │   │   ├── violinplot.py
│       │   │   └── waterfall.py
│       │   ├── _3D/
│       │   │   └── dscatter.py
│       │   ├── __init__.py
│       │   ├── __init__.pyi
│       │   ├── _graphhelp.py
│       │   └── support/
│       │       ├── Graphhelp.py
│       │       ├── Graphhelp.pyi
│       │       ├── List.py
│       │       └── List.pyi
│       ├── window.py
│       └── window.pyi
└── tests/ <span style="color:red;">テストファイル</span>
    ├── _import.py
    ├── data/
    │   ├── csv/ <span style="color:red;">テストで使用するcsvファイルが保存しているフォルダ</span>
    │   │   ├── __init__.py <span style="color:red;">csvファイルのデータを取得する</span>
    │   │   ├── japan_population.csv <span style="color:red;">日本の人口のデモデータ</span>
    │   │   └── school_test_demo_data.csv <span style="color:red;">テストの結果のデモデータ</span>
    │   └── img/ <span style="color:red;">テスト用の画像が入っているフォルダ</span>
    │       └── Lenna.png
    ├── test-all.py <span style="color:red;">全体的なウィジェットのテストファイル</span>
    ├── test-graph/
    │   ├── _import.py
    │   ├── test-graph-schooldata.py <span style="color:red;">テスト結果のグラフのテストファイル</span>
    │   ├── test-graph.py <span style="color:red;">グラフ全体のテストファイル</span>
    │   └── test-japanese.py <span style="color:red;">日本人人口のグラフのテストファイル</span>
    ├── test-log/
    │   ├── _import.py
    │   ├── test-log.log <span style="color:red;">テスト用のログを記録するログファイル</span>
    │   └── test-log.py <span style="color:red;">ログのテストファイル</span>
    └── test-widget/
        ├── _import.py
        ├── test-all.py <span style="color:red;">全体的なウィジェットのテストファイル</span>
        └── test-expansion.py <span style="color:red;">拡大鏡ウィジェットのテストファイル</span>
</code></pre>