
var tourSubmitFunc = function(e,v,m,f){
		if(v === -1){
			$.prompt.prevState();
			return false;
		}
		else if(v === 1){
			$.prompt.nextState();
			return false;
		}
	},
	tourStates = [

		{
			title: 'サイドメニューボタン',
			html: 'クリックするとサイドメニューを開閉します。',
			buttons: { 前に戻る: -1, 次に進む: 1 },
			focus: 1,
			position: { container: '.sidemenu-btn', x: 60, y: 0, width: 300, arrow: 'lt' },
			submit: tourSubmitFunc
		},

		{
			title: 'トップメニュー',
			html: 'アプリケーションの使い方やサインアウトなどが行えます。',
			buttons: { 前に戻る: -1, 次に進む: 1 },
			focus: 1,
			position: { container: '.launcher', x:-320, y: 10, width: 300, arrow: 'rt' },
			submit: tourSubmitFunc
		},

		{
			title: '顧客情報入力フォーム',
			html: '見込客のデータを入力・編集・削除します。',
			buttons: { 前に戻る: -1, 次に進む: 1 },
			focus: 1,
			position: { container: '.widget-title', x:0, y:0, width: 300, arrow: 'rt' },
			submit: tourSubmitFunc
		},

		{
			title: '保存ボタン',
			html: '現在フォームに入力されている情報を登録します。',
			buttons: { 前に戻る: -1, 次に進む: 1 },
			focus: 1,
			position: { container: '#save-button', x:-320, y:0, width: 300, arrow: 'rt' },
			submit: tourSubmitFunc
		},

				{
			title: '追客停止ボタン',
			html: 'この見込客の追客を停止します。 見込客一覧に表示されなくなり、メール送信も停止されます。',
			buttons: { 前に戻る: -1, 次に進む: 1 },
			focus: 1,
			position: { container: '#stop-button', x:-320, y:0, width: 300, arrow: 'rt' },
			submit: tourSubmitFunc
		},

				{
			title: 'キャンセルボタン',
			html: '編集を破棄して見込客一覧画面へ戻ります。',
			buttons: { 前に戻る: -1, 終了する: 2 },
			focus: 1,
			position: { container: '#cancel-button', x:-320, y:0, width: 300, arrow: 'rt' },
			submit: tourSubmitFunc
		},

	];
$.prompt(tourStates);