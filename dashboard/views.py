from django.views.generic.base import TemplateView
from django.templatetags.static import static
from random import choice, sample, shuffle, randint


class FeedView(TemplateView):
    template_name = "dashboard/feed.html"

    CONTENT_MUSIC = 'cm'
    CONTENT_VIDEO = 'cv'
    # there is no content type for text, because all
    # posts can have text
    CONTENT_PHOTO = 'cph'
    CONTENT_PLAYLIST = 'cpl'

    content_types = [
        CONTENT_MUSIC,
        CONTENT_PLAYLIST,
        CONTENT_VIDEO,
        CONTENT_PHOTO,
    ]

    musics = [
        {
            'music_name': 'Diamond Heart',
            'music_author': 'Lady Gaga',
            'music_album' : 'Joane',
            'music_image_link':  static('core/img/album1.png'),
        },
        {
            'music_name': 'American Teen',
            'music_author': 'Khalid',
            'music_album' : 'American Teen',
            'music_image_link':  static('core/img/album2.jpg'),
        },
        {
            'music_name': 'In My Blood',
            'music_author': 'Shawn Mendes',
            'music_album' : 'Shawn Mendes',
            'music_image_link':  static('core/img/album3.jpg'),
        },
        {
            'music_name': 'One Last Time',
            'music_author': 'Ariana Grande',
            'music_album' : 'My Everything',
            'music_image_link':  static('core/img/album4.png'),
        },
        {
            'music_name': 'Hold Me Down',
            'music_author': 'Halsey',
            'music_album' : 'Badlands',
            'music_image_link':  static('core/img/album5.png'),
        },
        {
            'music_name': 'Shake It Off',
            'music_author': 'Taylor Swift',
            'music_album' : '1989',
            'music_image_link':  static('core/img/album6.jpg'),
        },
        {
            'music_name': 'Die for You',
            'music_author': 'The Weeknd',
            'music_album' : 'Starboy',
            'music_image_link':  static('core/img/album7.jpg'),
        },
        {
            'music_name': 'Hold Up',
            'music_author': 'Beyonce',
            'music_album' : 'Lemonade',
            'music_image_link':  static('core/img/album8.png'),
        },
        {
            'music_name': 'Sugar',
            'music_author': 'Maroon 5',
            'music_album' : 'V',
            'music_image_link':  static('core/img/album9.png'),
        },
        {
            'music_name': 'Cake by the Ocean',
            'music_author': 'DNCE',
            'music_album' : 'Swaay',
            'music_image_link':  static('core/img/album10.png'),
        },


    ]

    names = [
        'João Silva',
        'Anthony Manuel Santos',
        'Bernardo Barros',
        'Isis Alves',
        'Luiza Brito',
        'Caroline Oliveira',
        'Joaquim dos Santos',
        'Felipe Bezerra',
        'Haimundo Kosta',
        'Ana Carla',
        'Márcia Fogaça',
        'Laura Lima'
    ]

    imgs = [
        static('core/img/user.png'),
        static('core/img/user1.png'),
        static('core/img/user2.png'),
        static('core/img/user3.png'),
        static('core/img/user4.png'),
        static('core/img/user5.png'),
        static('core/img/user6.png'),
        static('core/img/user7.png'),
        static('core/img/user8.png'),
        static('core/img/user9.png'),
        static('core/img/user10.png'),
        static('core/img/user11.png'),
        static('core/img/user12.png'),
    ]

    mensages = [
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse pretium tortor purus, sed accumsan dui mattis quis. Aliquam ultrices tempor urna.',
        'Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas placerat nisi quis lacinia tincidunt.',
        'Nullam non nulla eros.',
        'Donec sed ante venenatis, convallis eros finibus, sollicitudin ex. Maecenas elementum lectus nibh, sed ultricies ex pulvinar quis. In hac habitasse platea dictumst.',
        'In varius, tortor eget convallis pretium, ligula est finibus neque, non lacinia purus sapien sodales magna. Nam ultricies condimentum lacus nec tristique. Fusce at nisl eros. Nulla facilisi. ',
        'Ameno, dorime, ameno!',
        'Deus vult!',
        ' Vestibulum ultricies, leo at convallis luctus, urna tellus tempor dolor, eget malesuada metus orci a augue. Fusce gravida, libero ut tristique consectetur, neque dolor molestie elit, in accumsan sem quam quis purus. Nullam dignissim tortor ex, non posuere urna suscipit eu. Sed elementum venenatis diam, at tristique lacus feugiat at. In sit amet tellus vel magna aliquam blandit ultrices vitae felis.',
    ]

    @staticmethod
    def get_name():
        return choice(FeedView.names)

    @staticmethod
    def get_img():
        return choice(FeedView.imgs)

    @staticmethod
    def get_mensage():
        return choice(FeedView.mensages)

    @staticmethod
    def get_music():
        return choice(FeedView.musics)

    @staticmethod
    def get_playlist(size):
        return shuffle(sample(FeedView.musics, size))

    def get_random_content(self):
        content_list = []

        for i in range(0, 10):

            random_type = choice(FeedView.content_types)

            content_piece = {
                'author': FeedView.get_name(),
                'author_img': FeedView.get_img(),
                'menssage': FeedView.get_mensage(),
                'date_time': "26 de Abril de 2018 às 16:00h",
                'content_type': random_type,
                'number_likes' : randint(0,101)
            }

            if random_type is FeedView.CONTENT_MUSIC:
                content_piece.update({'music': FeedView.get_music()})

            if random_type is FeedView.CONTENT_PLAYLIST:
                content_piece.update(
                    {
                        'playlist': FeedView.get_playlist(choice(range(3,len(self.musics))))
                    }
                )







            content_list.append(content_piece)

        return content_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = self.get_random_content()

        return context
