
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
			title: '見込客一覧',
			html: '登録済みの見込客一覧です クリックすると詳細情報画面に移動します。',
			buttons: { 前に戻る: -1, 終了する: 2 },
			focus: 1,
			position: { container: '.table', x:0, y:260, width: 300, arrow: 'rt' },
			submit: tourSubmitFunc
		},

	];
$.prompt(tourStates);