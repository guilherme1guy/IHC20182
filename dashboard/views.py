from django.views.generic.base import TemplateView
from django.templatetags.static import static
from random import choice


class FeedView(TemplateView):
    template_name = "dashboard/feed.html"

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
        static('core/img/BC.png'),
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

    def get_random_content(self):
        content_list = []

        for i in range(0, 10):
            content_piece = {
                'author': FeedView.get_name(),
                'author_img' : FeedView.get_img(),
                'menssage': FeedView.get_mensage(),
            }

            content_list.append(content_piece)

        return content_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["content"] = self.get_random_content()
        
        return context
    