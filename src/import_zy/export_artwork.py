# coding=utf-8
import traceback

import MySQLdb
import sys
import os
import math
from docx import Document
from docx.shared import Pt
from oss import oss_kit
from import_zy import get_region

reload(sys)
sys.setdefaultencoding('utf-8')

connection = MySQLdb.connect(host='mt-58art-database-open.mysql.rds.aliyuncs.com',
                             port=3306,
                             user='mt_art58',
                             passwd='Admin_58art',
                             db='art58',
                             charset='utf8')
cursor = connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)

# artwork_dir = '/Volumes/Crayon2f/artworks/'
artwork_dir = u'g:\\artworks\\'
change_sign = '-'


def create_dir():
    sql = "SELECT user_id FROM activity_registration WHERE activity_id = 10000005 AND user_id <> ''"
    cursor.execute(sql)
    user_list = cursor.fetchall()
    for user in user_list:
        os.mkdir(artwork_dir + user['user_id'])


def get_artwork():
    sql = "SELECT  `NAME` AS name, ID id, AUTHOR author, `client` FROM voting_artwork WHERE ACTIVITY_ID = 10000005 AND  AUTHOR IN ('7f28e28b-8431-4ff9-aea4-d3fb60445673','afa8661d-d5c4-4ee5-806d-a242d53ead74','27dca2ef1eec44a78704741009f5a0a9','e171e64e-bd05-4779-af00-8d599655baca','c41a0cd6-6755-46eb-9993-6085a342feac','ef355bb7db994881980868347718d360','006f52e9102a8d3be2fe5614f42ba989','3b95969bb89a4a7a9742a6b8470d410b','d27cb226-fcdd-45a3-9875-2cc4f03bdf98','110780c3-00b8-4748-a299-9b9a63583cd8','fe822738e1a14d5fa46a4f1981a39754','6bb6d668-4222-44b7-a4a3-6e92ace71b76','dbc6efd7-10de-48b0-b793-f79be4a0ec18','2a5e8e5e-8954-41fe-a094-84939f083cae','2784815f-433c-471a-a96b-a6814a0ed0be','90172cc3-6e16-4eec-9e42-25f0d69b9322','e83560ae66284fde86c88ad0574739c6','cd823afd837f4768ac6b307d80a09848','64b7e746-0bb7-4c6e-9cbd-06e8bf9f4f42','6b34cbe76aee4ad68253780c26837aee','d645920e395fedad7bbbed0eca3fe2e0','28ee73f4-1d37-4087-ae51-b9cd856f86e5','c3ae8768-a33d-4c9e-8cc4-bc00f5cfacb0','e7b1db0c2b9b4086a07a20f949e91e05','10c21c55-af49-4334-8ccd-59b7c538e723','435fe5fd-8838-4f9a-9c6e-581b0b2d66e3','83aca35f-a4d5-4096-a403-ebe6763f1fd8','f11424e2226240dcb403956dd840c8d2','776fc52e2dfe428da437477872bfc8b0','603272fe692c40f7bc0fc46bdd5c57bc','f86c454e-fcb3-4ca6-a02d-851f27acd588','6a402d0e-f3e1-4d2d-aca9-0eb5e5f77815','907b4b46d01a4d8698a545b5f2f3d2a6','589589f365614669aebcfd970ecb3295','76ed66ccf9bf4294be224fdddf23328b','caedec98f8764dd8947b444d25bbdf7d','5102a1d0295449249b11bbd7856cc0e5','4d26d413d30b422a8a238034b0eb70ea','fe91cc67-6d3c-4c1b-b9f3-67140e4572ee','c6d4cc54f2f946819c2c8f14d8aaa653','023bcacf3eea4e63835a6085a20ce05e','3a004dd3-d10b-44bd-9b5e-9afc6a83f72e','188b1f8e741b4564ba37b08c7fede761','e1e3d4e8-f9bf-4ed6-85a6-aee677dc43cb','0c549537-fd18-4c06-a929-d60af2fcf8aa','fecc99e47b594a088e4edc784a5b77d9','52d825d1d55248d482f85a7e6cad0ed4','4d8d11be164a4644a4b5e877a257ad92','7b864b1d-0648-4221-968e-1d49a161f8fe','ff752201-694a-4fd3-b8ba-ae0c4fb27154','750b87a2-39ae-404d-8a6d-5c2a3cb0a5d2','d6391ca2-dbc8-45c6-bb9f-542688c983f2','fcc29a8f-e9cc-426f-965a-c18c0fd1eb2c','a46115541e4c427a8acc06f642f0f817','bf9d96aa-6a05-474d-bf77-6a0e7f847697','6ac912b4-9726-4f60-9b9f-4269e06f34be','6dd9307da170402dae08ec2cacb7ddc2','48909119-fb2e-426f-bce2-2120a7cd25e6','b4963aeb1d4c4b21b09a61f39305ac33','54b67f03-d1a7-4558-bc97-c0047d1e422e','6e3cefec-500d-453a-b0bc-9768340bec80','783e5480-057f-4118-a529-f5222e53f0de','02ebdc34-0a46-4cf5-81c4-c398025990d9','89068d2cd9f14f6e8209576c04e0a738','e18492564016427086569bd2ab14c037','08ac210c-51ed-48e1-b831-306163060e43','8133505a-c06e-4989-aa58-3d04fe3b5722','851314d6-f25b-41a4-b92a-998371d54676','21ade668ecb34d2c97f98f033556afc3','36a250db-e66b-4b93-ae92-0e3b4ab8edaf','d248ad4c-faee-4efc-b7eb-36bfa54660c0','9500727c5cb74adab760505212629948','a17fc1c6c3404586b329e287cc11e6b8','aea1147a-f84a-4244-affc-3bb26cb30e0a','a037b8d214ee492ab6ba6ef08ecc2c32','fe1eb63a-c9bf-46d5-b157-c6a9ee751b18','3cb72764-3f3d-4966-b1f2-109824d481c6','c2d71f41b4e54c7fba4a9fe3503b3a1d','300611eb1ff249e9a2b60771ed5d6653','028ac710-d7ad-4607-bc15-0178e3126432','d6e930599c9b47f8a65d4c6a24759d6a','0dbc2cf65c064d17bc1f879af5be155f','d35cf58319db4c81b31743f58989d51f','c7a0c36e1a3f4f6a98753fb137a1ae03','e7d8c14cff554237b8591aace2fae134','237b6a66e1c74224b14d2744cac2c8f3','7a5b4764-5571-4fb6-a8c2-4904bf05a691','04050274-374d-419e-89e7-d27cf4ab5f96','3e370c46-9937-42e5-b570-1f1921f9f2ac','99ac70603724493babf84b7b7992a17a','048c0c5a-1492-4313-a15a-a7b07f8f9a10','ac130bfd-bc2b-41d8-b22d-9fc9c7cc06ec','59f4bd9b84a64e1d8158493517e7c571','200b05ef-7003-46cf-9cb0-cc2acda85248','fef44af3-d2b4-4f67-857c-7f69f5e4ccaf','05cfab5a-5661-4e18-a82e-9313bedba7e0','cef25dc4-c423-4582-89c7-28599048fc16','d5ef7d81-8b49-4131-bf40-431d633b8b09','df483a9a-8571-4487-a80c-5a037c87a0d3','d8398fdf-2db6-4864-84cb-6e2835b8f980','05e4745c-0878-4601-a064-6633a89c23f1','303e40911bae4010b6fd5722537f3a21','34e6bc2b72c34a808e377e2524c939d7','b5a74779-8215-4d65-80c4-d5264eb1cd08','a0648c8f-8319-4769-8019-171477eb7916','d93813e0-03ee-4e8f-8677-e04e5c3f1af5','dffaba725708493f93b1cd37a6f89a67','b663a665-82da-4906-bd90-f33db6eab3ff','d1f9712e6d50450591d6b4d2e13eeb35','9b55fb6fd29d4336874795efa40d4790','579b718d9c2844edbcb1eaaee779d263','6c29f141c72e4ba4ad266e64a936ac25','07ae7d4f64e84e5298c989e47c0414fd','d905f84a33574a4caaaa8baf2f381523','06d7eaba0f8b4f04aeb178600322750b','6970d103-d299-46e0-9eda-48571a5f2738','a6966ef5122f4795b22a98a21516bfbc','28bf66ce-b92d-4557-8a89-f7adbb665686','87f36d86af33410da78708609d890b41','e92966dd-f00f-4b1f-a555-860077819b75','f72dcbce7c9a41dba06bce09c144000d','eec84fdda5aa4bddaf05f040d54d120f','b8f36d0068834377b63dc733c48e0029','c249198fba1e4f87bbe476d7dcb9e0d7','06c3e2caf26441c799d19f9ebda344c5','db0e8c0d1e854bd9904545d10303d665','232bcdda-0325-47b6-86f7-54da567be81a','43e5eaff9f6b4eba947ed4ac1fc33903','4fe8c17f-b9d3-4491-9674-50668333957b','65cb11c3-2bf2-4242-b035-9486aa762c75','bfef92383f8c4c8f95cda9fe406f2e1e','9bc13995-def5-4f2f-adbe-f19fd0f217e5','d2d05d45-0369-44f4-b7b4-e12ca6ffb1b4','deaa34da-4891-4a08-a795-07016a071214','af3c0924-9ff3-4f67-a61d-2be2bb7d82ba','11b8b49c5e8d4ff7b26bd09f44a8895a','838ef566-7ff3-4625-8da8-962ef4b6c5a1','a1ff106e-8638-4316-8e15-aca66dd21d0a','8ef162eb-044c-4a96-9295-15f0e153f3c1','05602d38-bca8-4b96-b8d8-25f865136075','1e637453-28c5-4308-8847-77edf6f85c36','ea260b18-a8b6-4618-85d9-c635c8661b53','39ce6dbb-87bd-4467-bf05-49467c7779bc','6b28165e53494e03a76f0e1d812264b2','6832b3eb13874b208484effea2d09387','d0cda62f-4d32-4e77-a527-afaa5217ace5','b5e801c4-ab6e-49a5-b033-3438d490364b','eca131ecfb854b9c8f0d96446b4a0d84','c1e075119a2246fdb632896d7e0c98d7','bbb41e70-83bf-491f-9ebc-21dc88219bf2','87d7eb90b1044ceeac9fc9adcf14a658','b099c110556546b09c73a585d2009dc1','75bbae1eb4264db28a64a404f792a3b3','82d89803-286c-45ae-9957-f07f11d75130','114124f5-9c37-44fe-8813-b185ec43634b','2c40217a-4cf7-4555-8552-13c707975ffd','32cda747403049c6a108228c012ff974','e2db537a3ff54ef8b26348de65f005da','1bf9375f-89e8-4526-87be-aa634718fed0','91e87dc6b50649e9ae48a21f7c6014e8','0e2c5b75a52146738197577040a28982','61fa04ea-3ea9-4e9d-a212-083f143d91e9','6ac9c3b8bd2f4168b04906e97df05aac','d99caeb9-b528-481d-9f86-942dbe688dcc','c64d3e0f5f384b5b8272593554fbe569','1c4b154758ea487c99f8f7e58aa625df','3a9e1b2fb0fa4defab4e6d9086536f48','20803252-1c78-46e6-a296-16c56b8b8f61','59b35bfabfd84368a732d8e0477b33c6','c6d6fcad-3a70-4509-8717-0de7cf9c40a7','8a20a4731fb14499b79a0dc30e9dff34','39f8fc0f05314462bd9c03939c027db4','8c430913bcf04b81881d7a8abab72ae4','162277093b014801b8e4b80872298e9d','9d1fadae-dc0a-4f2b-b5eb-eb2ef1dfbff9','1a62a51f-6636-48be-a92c-5c6acf95519c','17fd0adb-5b63-49ce-9997-fe506c9796d0','47af251a52644b188dbd4a9045b4bc30','5deb17dc-1fc2-475b-88cb-1b5d53ff91ce','d4578e05-025f-4c12-bfa1-c7e59f276e75','a1df6e47a5fb418e9189a0bedfb54ef1','4aa53ec93db945e684cf51daaaa4fb56','4c73cc1e-0511-4000-9ec0-cd2409a7c6c4','212ac73d4f4b4143aad82841ffc987fd','e81297691ef448a48c489ba6af706449','b59698f2f13c4d7a845ca748655d1dd9','ed160941-97cf-40ea-bf65-4bab4e94c60a','0738a5ce-0156-4695-9909-7abb06800031','B47DC428331F475DA5AE65068D5F025B','62F4A451C4DA4FB98A70410C5EC78637','A70FE6ED8AB94AF898B5F9AC761CF9BE','F4D2E0CCEED54329B27401456E42938D','6964D28095A14363961B6A713E24C503','7E75A918B97848D489AE4CDD3BB1015F','E17249CC96B8437DB1708852481AE99E','6BDCD5496FEC47F9891AA11F46212259','A5495FB872F245ED9227ECC68B5A934A','2F873EE952F64B46A8255B3B65A665DA','D80E6782944447B6BD9ECCF5D4FE4E5B','BCFA3ECEDA1448F58C71F063D5EA2381','EE03292E559340B5AFFEAFE6C5397A02','B579AD4E24234FB1B5295BA801C47BF3','36049C12F04A4FF9891CBEAA9EA42630','7B9AF0271F82407A8799F3E0B2FC90B8','B0C54E32E5324A63AEC97362CDC932C6','90473EEAAE774BE4B14383AF053831F4','3D3C951A84C346659E9415163EC6AE31','4C80FD6109D34F7788F19E7EA4E87CB1','FED748BE76AA472DB50C536E35755DF0','8E478113EDFC4AEC9CF77BE272BAD5FA','4A8FB7514594437BB7C1921E6BAB75C0','286D0058991941519186C98D07901297','0B0662D5B9684F1D8037BC8CF40CD873','D81FD067F74147E387A6CB89DA0A9765','21B9F697DB1A4B96ACB0919D7F899163','C7A430A0A23F41D1938EBEE6244FE910','DD049E838D7F406FABD5155170D15A73','7D07E090F898485E81C2A4A6AEBFD8D0','1A7C686FCC884A1E83AC3458684EDD92','D440C9F90E1B43BB9F9733E5C3B6DB74','9040B3ECC3664F3B91881F71D542CE49','31EA616F934B47B2A1335834960203FE','54034496774F4FB1ACFAEFACF41101B3','EA410E55C3B4474091FC327C5CFBAFCA','0A6CBD33E0004552A8794C0652FE61F4','E1F725570DB146EEA81430ECC43FA8A4','4CE0E03AD2C74BF2B19ACF6F9A8F6CA9','0F25E0283A8E4CEF995FC96A648460C7','E49700524B614127B3E0C63A2D6155B2','7F6894EB0D4D4A90B27C6D3CFC2C41CF','1E203F1C3C6B471787587DF448518DF2') ORDER BY   `client`"
    cursor.execute(sql)
    return cursor.fetchall()


def download_artwork_form_oss():
    artwork_list = get_artwork()
    index_out = 0
    _oss_kit = oss_kit.OssKit()
    for artwork in artwork_list:
        index_out += 1
        print index_out
        dir_name = artwork_dir + artwork['author']
        artwork_name = translate_sign(artwork['name'].strip())
        artwork_path = '%s/%s.jpg' % (dir_name, artwork_name)
        if os.path.exists(artwork_path):
            artwork_path = recursion(artwork_path, 0)
        bucket_name = 'mt-official'
        if not artwork['client'] == '58':
            bucket_name = 'mt-zy-official'
            if _oss_kit.get_bucket_name() == 'mt-official':
                _oss_kit = oss_kit.OssKit(bucket_name)
        elif artwork['client'] == '58':
            if _oss_kit.get_bucket_name() == 'mt-zy-official':
                _oss_kit = oss_kit.OssKit()

        key_list = get_oss_key(artwork['id'], bucket_name)
        try:
            if len(key_list) > 0:
                key = key_list[0]
                if not os.path.exists(artwork_path):
                    _oss_kit.download(str(key['key']), artwork_path)
                if len(key_list) > 1:
                    for index, append_key in enumerate(key_list[1:]):
                        append_dir = '%s/detail/' % dir_name
                        if not os.path.exists(append_dir):
                            os.mkdir(append_dir)
                        append_path = '%s/%s[%d].jpg' % (append_dir, artwork_name, index + 1)
                        if not os.path.exists(append_path):
                            _oss_kit.download(str(append_key['key']), append_path)
            else:
                print artwork['id'] + ' has not oss_key'
        except BaseException, exception:
            print(exception.message)
            print('===== %s =====' % artwork['id'])
            traceback.print_exc()


def get_oss_key(artwork_id, bucket_name):
    sql = "select key_value as `key` from art_images where source_id = '%s' and " \
          "bucket_name = '%s' and RULE_CODE = 'artwork_open' order by category desc " % (artwork_id, bucket_name)
    cursor.execute(sql)
    return cursor.fetchall()


def translate_sign(origin):
    if origin is '':
        return origin
    return origin.replace('<', change_sign).replace('>', change_sign).replace(':', change_sign) \
        .replace('"', change_sign).replace('/', change_sign).replace('\\', change_sign) \
        .replace('|', change_sign).replace('?', change_sign).replace('*', change_sign)


def export_resume():
    region_dict = get_region.get_name()
    sql = "SELECT ar.user_id, ar.real_name, ar.birthday, ar.live_place AS live_place, su.GRADUATEPLACE AS school," \
          " ar.terminal FROM activity_registration ar LEFT JOIN sys_user su ON ar.user_id = su.ID " \
          "WHERE ar.activity_id = 10000005 AND ar.user_id = '579cd0ef-6151-4c74-a69b-11138bf793c4'"
    cursor.execute(sql)
    user_list = cursor.fetchall()
    index = 0
    for user in user_list:
        index += 1
        print index
        personal_exhibition = []
        joint_exhibition = []
        try:
            if user['terminal'] != 'zai_yi':
                show_sql = "select NAME as name, SPACENAME as space_name, CITY as city, `YEAR` as  `year`, " \
                           "TYPE as type from art_show_extern where CRT_TELLER_ID = '%s' ORDER BY YEAR desc" % \
                           user['user_id']
                cursor.execute(show_sql)
                show_list = cursor.fetchall()
                if len(show_list) > 0:
                    for show in show_list:
                        if int(show['type']) == 0:
                            personal_exhibition.append(show)
                        else:
                            joint_exhibition.append(show)
            region_id = user['live_place'] if user['live_place'] and user['live_place'] != '' else None
            region_name = u'未知' if (None is region_id) or (type(region_id) is float and math.isnan(region_id)) else \
                region_dict[region_id]
            real_name = str(user['real_name']).strip()
            out_path = u"%s%s\\个人简历.docx" % (artwork_dir, user['user_id'])
            if not os.path.exists(artwork_dir + user['user_id']):
                out_path = u"g:\\other\\%s.docx" % translate_sign(real_name)
            write_word(joint_exhibition, personal_exhibition, out_path, real_name, user['birthday'], region_name,
                       user['school'])
            print user['real_name'] + ' resume export successful '
        except BaseException, exception:
            print exception.message
            traceback.print_exc()
            print "export word error user_id ==> %s" % user['user_id']


def write_word(joint_exhibition, personal_exhibition, out_path, real_name='', birthday='', live_place='', school=''):
    document = Document()

    document.add_heading(u'个人简历', 0)
    document.add_paragraph()

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'姓名：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if real_name is None:
        real_name = ''
    paragraph.add_run(u'%s' % real_name)

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'出生日期：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if birthday is None:
        birthday = ''
    paragraph.add_run(birthday)

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'现居住地：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if live_place is None:
        live_place = ''
    paragraph.add_run(u'%s' % live_place)

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'毕业院校：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if school is None:
        school = ''
    paragraph.add_run(u'%s' % school)

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'个展：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if len(personal_exhibition) > 0:
        for exhibition in personal_exhibition:
            paragraph.add_run(u'\r %s %s %s %s' % (exhibition['year'], exhibition['name'], exhibition['space_name'],
                                                   exhibition['city']))

    paragraph = document.add_paragraph()
    name = paragraph.add_run(u'联展：')
    name.font.size = Pt(12)
    name.font.name = u'微软雅黑'
    name.bold = True
    if len(joint_exhibition) > 0:
        for exhibition in joint_exhibition:
            text = u'\r %s %s %s %s' % (exhibition['year'], exhibition['name'], exhibition['space_name'],
                                        exhibition['city'])
            print text
            paragraph.add_run(text)
    document.save(out_path)


def recursion(path, index):
    if os.path.exists(path):
        index += 1
        path = '%s(%d)' % (path, index)
        return recursion(path, index)
    else:
        return path


def translate():
    sql = "SELECT user_id, real_name FROM activity_registration WHERE activity_id = 10000005 and user_id <> '';"
    cursor.execute(sql)
    user_list = cursor.fetchall()
    for user in user_list:
        author_dir = os.path.join(artwork_dir, user['user_id'])
        if os.path.exists(author_dir):
            new_author_dir = os.path.join(artwork_dir, translate_sign(user['real_name'].strip()))
            if os.path.exists(new_author_dir):
                new_author_dir = recursion(new_author_dir, 0)
            print(new_author_dir)
            try:
                os.rename(author_dir, new_author_dir)
                print user['real_name'] + ' success '
            except BaseException, e:
                print e.message
                traceback.print_exc()
                print user['user_id'] + ' fail'


if __name__ == '__main__':
    # download_artwork_form_oss()
    # create_dir()
    # export_resume()
    translate()
