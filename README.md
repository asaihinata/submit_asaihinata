<h1>フレームワーク</h1>
GUIのフレームワーク

フォルダ構成

submit_asaihinata/
├── .gitattributes
├── .gitignore
├── .gitmessage
├── .vscode/ **vscodeの設定ファイル**
│   └── settings.json
├── README.md **プロジェクトの説明ファイル**
├── docs/ ドキュメント
│   ├── data/ **testsフォルダやフレームワークで使わなかったデータファイルの保存先**
│   │   ├── browser_jp.csv
│   │   └── color.csv
│   └── requirements.txt **使用した外部ライブラリ**
├── pyproject.toml
├── src/ **ソースフォルダ**
│   ├── __init__.py
│   ├── __init__.pyi
│   ├── types/ **型ヒントのフォルダ**
│   │   ├── __init__.py
│   │   ├── __init__.pyi
│   │   ├── basic.py
│   │   └── widget.py
│   └── widget/
│       ├── __init__.py
│       ├── _color.py **色に関するモジュール**
│       ├── _dialog/ **ダイアログに関するパッケージ**
│       │   ├── __init__.py
│       │   ├── __init__.pyi
│       │   ├── dialogs.py
│       │   └── popup.py **ポップアップのモジュール**
│       ├── _font.py**ウィジェットのフォントを作成するモジュール**
│       ├── _function.py **プロジェクト内で何度も使用する関数をまとめたモジュール**
│       ├── _log/ **ログに関するモジュール**
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
│       ├── _time.py **時間に関するモジュール**
│       ├── _time.pyi
│       ├── base.py **ウィジェットの基盤を作成するモジュール**
│       ├── basic/ **ウィジェットのソースコードを保存しているパッケージ**
│       │   ├── Image/ **Image,QR,Barcodeのウィジェットを保存しているパッケージ**
│       │   │   ├── __init__.py
│       │   │   └── _photo.py
│       │   ├── Link/ **Linkウィジェットを保存しているパッケージ**
│       │   │   └── __init__.py
│       │   ├── __init__.py
│       │   ├── __init__.pyi
│       │   ├── btnpop/ **ColorbtnウィジェットやFileLoadウィジェットを保存しているパッケージ**
│       │   │   └── __init__.py
│       │   ├── calendar/ **カレンダーのウィジェットを保存しているパッケージ**
│       │   │   ├── __init__.py
│       │   │   ├── _calendar.py
│       │   │   └── tooltip.py
│       │   ├── element.py
│       │   ├── expansion/ **拡大鏡のウィジェットを保存しているパッケージ**
│       │   │   └── __init__.py
│       │   └── ttkelement.py
│       ├── data/ **プロジェクトで使用するデータを保存している**
│       │   ├── __init__.py
│       │   └── color.json **色データ**
│       ├── developer.py
│       ├── developer.pyi
│       ├── graph/ **グラフウィジェットに関するモジュール**
│       │   ├── Graph.py **グラフのウィジェットの基盤のモジュール**
│       │   ├── Graph.pyi
│       │   ├── _2D/ **主に2次元平面のグラフを保存しているパッケージ**
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
│       │   ├── _3D/ **主に3次元のグラフを保存しているパッケージ**
│       │   │   └── dscatter.py
│       │   ├── __init__.py
│       │   ├── __init__.pyi
│       │   ├── _graphhelp.py
│       │   └── support/
│       │       ├── Graphhelp.py
│       │       ├── Graphhelp.pyi
│       │       ├── List.py
│       │       └── List.pyi
│       ├── window.py **WindowControllerのみのモジュール**
│       └── window.pyi
└── tests/ **テストファイル**
    ├── _import.py
    ├── data/
    │   ├── csv/ **テストで使用するcsvファイルが保存しているフォルダ**
    │   │   ├── __init__.py **csvファイルのデータを取得する**
    │   │   ├── japan_population.csv **日本の人口のデモデータ**
    │   │   └── school_test_demo_data.csv **テストの結果のデモデータ**
    │   └── img/ **テスト用の画像が入っているフォルダ**
    │       └── Lenna.png
    ├── test-all.py **全体的なウィジェットのテストファイル**
    ├── test-graph/
    │   ├── _import.py
    │   ├── test-graph-schooldata.py **テスト結果のグラフのテストファイル**
    │   ├── test-graph.py **グラフ全体のテストファイル**
    │   └── test-japanese.py **日本人人口のグラフのテストファイル**
    ├── test-log/
    │   ├── _import.py
    │   ├── test-log.log **テスト用のログを記録するログファイル**
    │   └── test-log.py **ログのテストファイル**
    └── test-widget/
        ├── _import.py
        ├── test-all.py **全体的なウィジェットのテストファイル**
        └── test-expansion.py **拡大鏡ウィジェットのテストファイル**