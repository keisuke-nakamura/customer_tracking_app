
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
			title: '入力フォーム',
			html: '新規に登録する見込客の情報を入力します *が付いている項目は必須項目です。',
			buttons: { 前に戻る: -1, 次に進む: 1 },
			focus: 1,
			position: { container: '#profile', x:-320, y:0, width: 300, arrow: 'rt' },
			submit: tourSubmitFunc
		},

				{
			title: '各種ボタン',
			html: '必須項目が入力されている場合、Nextボタンで次のフォームに進みます。Previousボタンで一つ前のステップに戻ります。' +
				'Finishボタンでフォームに入力されている見込み客を登録します。',
			buttons: { 前に戻る: -1, 終了する: 2 },
			focus: 1,
			position: { container: '#next-button', x:-320, y:0, width: 300, arrow: 'rt' },
			submit: tourSubmitFunc
		},



	];
$.prompt(tourStates);