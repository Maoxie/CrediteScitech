# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/9/23 13:33'

import os
try:
    import cPickle as pickle
except ImportError:
    import pickle

basedir = os.path.abspath(os.path.dirname(__file__))
profession_media_path = os.path.join(basedir, 'app/static/media/profession')

profession_contents = [
    {
        'id': 0,
        'name': u'医学医药',
        'english_name': 'MEDICAL AND MEDICINE',
        'introduction': [ u'我们的翻译团队不仅有英语专业译者，而且有具备医学、药学、生物学学术背景的专业人才，' +
                          u'他们有牢固的学术基础及良好的语言驾驭能力，具备SCI论文写作、投稿及发表经验，' +
                          u'旨在提供专业的医学翻译、药学翻译、医疗器械注册、药品注册等领域的专业翻译服务。' +
                          u'资深翻译人员既能翻译医学类专业文献，又精通SCI论文、学生毕业及职称晋升所需论文的写作及投稿工作。' +
                          u'到目前为止，启信科技医学翻译团队累积翻译字数达百万字，帮助发表论文影响因子累积400多分'
                        ],
        'items': [
            {
                'icon': '\e9f4',
                'title': u'制药',
                'content': u'启信科技的译员都具有制药行业的相关背景，了解制药项目的程序,熟悉相关知识,从而在各个环节都能更好地工作',
                'url': ''
            },
            {
                'icon': '\e607',
                'title': u'医学论文翻译',
                'content': u'启信科技专注医学论文翻译，清华医药学博士担当初译，外籍语言专家深度润色，是您论文发表的不二之选',
                'url': ''
            },
            {
                'icon': '\e949',
                'title': u'病例翻译',
                'content': u'启信科技在病例翻译方面经验丰富，能够确保病例翻译专业、准确、规范',
                'url': ''
            },
            {
                'icon': '\e9dd',
                'title': u'医药文献翻译',
                'content': u'启信科技拥有大量医药学硕博研究生担任特约翻译，在医药学文献翻译的专业性方面全国领先，日翻译量超过10万字，远胜一般同行',
                'url': ''
            },
            {
                'icon': '\e668',
                'title': u'检查报告翻译',
                'content': u'启信科技的译员中有很多医药学专业的硕博研究生，医学知识扎实，语言功底深厚，完全可以确保检查报告翻译的准确性',
                'url': ''
            },
            {
                'icon': '\e989',
                'title': u'医疗器械翻译',
                'content': u'医疗器械翻译需要译者掌握相关专业知识，熟悉行业背景，启信科技精选医疗器械领域的专业译者，为客户呈现最专业的学术翻译',
                'url': ''
            }
        ],
        'advantage': os.path.join(profession_media_path, 'advantage-1.png'),
        'service': os.path.join(profession_media_path, 'service.png'),
        'example': {
            'img': os.path.join(profession_media_path, 'example-1.png'),
            'title': u'题为《细胞质RNA与基因检测》的英语论文翻译'
        }
    },
    {
        'id': 1,
        'name': u'机械电子',
        'english_name': 'MECHANICAL & ELECTRONICS',
        'introduction': [ u'启信科技机械电子翻译组特聘清华、北大等著名院校的高材生担当英译中科技文献的初译以及英语论文' +
                          u'的专业术语审校，用顶尖专业人才扫除机械电子翻译的一切盲点。' ,
                          u'我们愿为每一位客户提供质量最高、速度最快的机械电子翻译以及本地化服务，' +
                          u'依靠严格的质量控制体系、规范化的运作流程和独特的审核标准，我们已经为众多公司企业、政府机构、' +
                          u'科研单位提供了高水准的机械电子翻译，并签订了长期合作协议。'
                         ],
        'items': [
            {
                'icon': '\ea74',
                'title': u'机械制造翻译',
                'content': u'启信科技的译员都具有机械制造业的相关背景，了解 机械制造程序,熟悉相关知识,从而在各个环节都能更好地工作',
                'url': ''
            },
            {
                'icon': '\e607',
                'title': u'机械电子论文翻译',
                'content': u'启信科技专注机械电子论文翻译，由相关专业博士担当初译，外籍语言专家深度润色，是您论文发表的不二之选',
                'url': ''
            },
            {
                'icon': '\e949',
                'title': u'技术说明书翻译',
                'content': u'启信科技在技术说明书翻译方面经验丰富，能够确保技术说明书翻译专业、准确、规范',
                'url': ''
            },
            {
                'icon': '\e9dd',
                'title': u'机械电子文献翻译',
                'content': u'启信科技拥有大量机械电子专业硕博研究生担任特约翻译，在文献翻译的专业性方面全国领先，日翻译量超过10万字，远胜一般同行',
                'url': ''
            },
            {
                'icon': '\e668',
                'title': u'机械电子类专利翻译',
                'content': u'启信科技与全国多家知识产权公司合作，由熟悉专利文件写作的译者提供专利文件翻译，保证翻译语言符合专利文件规范',
                'url': ''
            },
            {
                'icon': '\e989',
                'title': u'仪器仪表翻译',
                'content': u'仪器仪表翻译需要译者掌握相关专业知识，熟悉行业背景，启信科技精选仪器仪表领域的专业译者，为客户呈现最专业的学术翻译',
                'url': ''
            }
        ],
        'advantage': os.path.join(profession_media_path, 'advantage-1.png'),
        'service': os.path.join(profession_media_path, 'service.png'),
        'example': {
            'img': os.path.join(profession_media_path, 'example-1.png'),
            'title': u'题为《细胞质RNA与基因检测》的英语论文翻译'
        }
    }

]

profession_pkl_file = os.path.join(basedir, 'app/static/profession_data.pkl')
output_file = open(profession_pkl_file, 'wb')
P = pickle.dump(profession_contents, output_file)
output_file.close()



import pprint, pickle

pkl_file = open(profession_pkl_file, 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

pkl_file.close()

