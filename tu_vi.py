import requests


class TuVi():
    def __init__(self):
        pass

    def con_giap(self, Cgiap=''):
        url = 'https://api.kma-chatbot.com/tuvi.php?tuoi={}'.format(Cgiap.strip())
        loi_phan = ''  # Lời phán

        try:
            r = requests.get(url)
            data_json = r.json()

            set_attributes = data_json.get('set_attributes')

            if set_attributes:
                loi_phan = '-----{}-----\n- {}\n- {}\n- {}\n- {}\n'.format(
                    set_attributes.get('tvcongiap'),
                    set_attributes.get('congviec'),
                    set_attributes.get('tinhcam'),
                    set_attributes.get('taivan'),
                    set_attributes.get('cantrong')
                )
        except:
            loi_phan = 'Có thể con giáp bạn nhập bị sai :('

        return loi_phan

    def cung_hoang_dao(self, cung_hd=''):
        # Cái này mình cho API rồi các bạn tự viết nha =)) Lười!
        pass
