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

    playlist = [
        'Chorar no banho',
        'Só música boa',
        'Rock pesadão',
        'Caminho do trabalho',
        'Só SS',
        'To de férias',
    ]

    @staticmethod
    def get_name():
        return choice(FeedView.names)

    @staticmethod
    def get_comments():

        comments = []

        for i in range(0, choice([0, 0, 0, 1, 1, 2])):
            comments.append(
                {
                    'author': FeedView.get_name(),
                    'img': FeedView.get_img(),
                    'text': FeedView.get_mensage()
                }
            )

        return comments


    @staticmethod
    def get_name_playlist():
        return choice(FeedView.playlist)

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
        return sample(FeedView.musics, size)

    @staticmethod
    def get_chat_friends():

        size = randint(2,10)
        friends = []

        for i in range(0, size):
            friends.append(
                {
                    'img': FeedView.get_img(),
                    'name': FeedView.get_name()
                }
            )

        return friends

    
    @staticmethod
    def get_chat_conversation():

        size = randint(1,4)
        menssages = []

        persons = [
            {
                'img': FeedView.get_img(),
                'type': 'sender'
            },
            {
                'img': FeedView.get_img(),
                'type': 'receiver'
            }
        ]

        for i in range(0, size):
        
            menssages.append(
                {
                    'menssage': FeedView.get_mensage(),
                    'author': choice(persons)
                }
            )
          

        menssages.append(
            {
                'author': persons[0],
                'menssage': FeedView.get_mensage()
            }
        )
        
        menssages.append(
            {
                'author': persons[1],
                'menssage': FeedView.get_mensage()
            }
        )

        return menssages

    @staticmethod
    def get_only_text():
        content_list = []

        for i in range(3, 10):

            content_piece = {
                'author': FeedView.get_name(),
                'author_img': FeedView.get_img(),
                'menssage': FeedView.get_mensage(),
                'date_time': "26 de Abril de 2018 às 16:00h",
                'content_type': 'txt',
                'number_likes' : randint(0,101),
                'comments': FeedView.get_comments()
            }


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
                'number_likes' : randint(0,101),
                'comments': FeedView.get_comments()
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

class GroupView(TemplateView):
    template_name = "dashboard/group.html"

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

    playlist = [
        'Chorar no banho',
        'Só música boa',
        'Rock pesadão',
        'Caminho do trabalho',
        'Só SS',
        'To de férias',
    ]

    @staticmethod
    def get_name():
        return choice(FeedView.names)

    @staticmethod
    def get_comments():

        comments = []

        for i in range(0, choice([0, 0, 0, 1, 1, 2])):
            comments.append(
                {
                    'author': FeedView.get_name(),
                    'img': FeedView.get_img(),
                    'text': FeedView.get_mensage()
                }
            )

        return comments


    @staticmethod
    def get_name_playlist():
        return choice(FeedView.playlist)

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
        return sample(FeedView.musics, size)

    @staticmethod
    def get_chat_friends():

        size = randint(2,10)
        friends = []

        for i in range(0, size):
            friends.append(
                {
                    'img': FeedView.get_img(),
                    'name': FeedView.get_name()
                }
            )

        return friends

    
    @staticmethod
    def get_chat_conversation():

        size = randint(1,4)
        menssages = []

        persons = [
            {
                'img': FeedView.get_img(),
                'type': 'sender'
            },
            {
                'img': FeedView.get_img(),
                'type': 'receiver'
            }
        ]

        for i in range(0, size):
        
            menssages.append(
                {
                    'menssage': FeedView.get_mensage(),
                    'author': choice(persons)
                }
            )
          

        menssages.append(
            {
                'author': persons[0],
                'menssage': FeedView.get_mensage()
            }
        )
        
        menssages.append(
            {
                'author': persons[1],
                'menssage': FeedView.get_mensage()
            }
        )

        return menssages


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
                'number_likes' : randint(0,101),
                'comments': FeedView.get_comments()
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
