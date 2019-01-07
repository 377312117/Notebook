import re 





html =  '''
    <div class='animal'>
        <p class='name'>
            <a title='Rabbit'></a>
        <p>

        <p class='content'>
            Small white rabbit white and white
        </p>
    </div>
'''

# 要求1: [('Tiger','Two tigers ...'),('Rabbit','.')]
# 要求2: 动物名称: Tiger
        # 动物描述: Two  tigers two tigers ...
        # *******************
        # 动物名称: Rabbit
        # 动物描述: Small ........

p = 'div class="animal">.*?title="(.*?)".*?class="content">(.*?)</p>'
