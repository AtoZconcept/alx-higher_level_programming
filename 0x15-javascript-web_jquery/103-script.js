$(document).ready(function () {
    $('#btn_translate').click(function () {
        const languageCode = $('#language_code').val();

        $.ajax({
            url: 'https://hellosalut.stefanbohacek.dev/?lang=',
            type: 'GET',
            data: { lang: languageCode },
            success: function (response) {
                $('#hello').text(response.hello);
            },
            error: function (error) {
                console.log('Error:', error);
            }
        });
    });
	$('#language_code').keypress(function (e) {
		const languageCode = $('#language_code').val();

		if (e.which === 13)
		{
			$.ajax({
				url: 'https://hellosalut.stefanbohacek.dev/?lang=',
				type: 'GET',
				data: { lang: languageCode },
				success: function (response) {
					$('#hello').text(response.hello);
				},
				error: function (error) {
					console.log('Error:', error);
				}
			});
		}
	});
});
