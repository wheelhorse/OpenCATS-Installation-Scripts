#!/usr/bin/python3
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import pdb


class CandidateInfo(object):
    def __init__(self, 
            first_name='',           
            middle_name='',                      
            last_name='',            
            email1='',               
            email2='',               
            phone_home='',           
            phone_cell='',           
            phone_work='',           
            address='',              
            city='',                 
            state='',                
            zzip='',                 
            source='',               
            key_skills='',           
            date_available='',       
            current_employer='',     
            can_relocate='',         
            current_pay='',          
            desired_pay='',          
            notes='',                
            web_site='',             
            best_time_to_call='',    
            entered_by='',           
            owner='',                
            site_id='',              
            eeo_ethnic_type_id='',   
            eeo_veteran_type_id='',  
            eeo_disability_status='',
            eeo_gender='',
            ):
        self.first_name           = first_name           
        self.middle_name          = middle_name          
        self.last_name            = last_name            
        self.email1               = email1               
        self.email2               = email2               
        self.phone_home           = phone_home           
        self.phone_cell           = phone_cell           
        self.phone_work           = phone_work           
        self.address              = address              
        self.city                 = city                 
        self.state                = state                
        self.zzip                 = zzip                 
        self.source               = source               
        self.key_skills           = key_skills           
        self.date_available       = date_available       
        self.current_employer     = current_employer     
        self.can_relocate         = can_relocate         
        self.current_pay          = current_pay          
        self.desired_pay          = desired_pay          
        self.notes                = notes                
        self.web_site             = web_site             
        self.best_time_to_call    = best_time_to_call    
        self.entered_by           = entered_by           
        self.owner                = owner                
        self.site_id              = site_id              
        self.eeo_ethnic_type_id   = eeo_ethnic_type_id   
        self.eeo_veteran_type_id  = eeo_veteran_type_id  
        self.eeo_disability_status= eeo_disability_status
        self.eeo_gender           = eeo_gender           


def sql_insert_candidate(candidate_info):
    try:
        command = """INSERT INTO candidate (
                first_name,
                middle_name,
                last_name,
                email1,
                email2,
                phone_home,
                phone_cell,
                phone_work,
                address,
                city,
                state,
                zip,
                source,
                key_skills,
                date_available,
                current_employer,
                can_relocate,
                current_pay,
                desired_pay,
                notes,
                web_site,
                best_time_to_call,
                entered_by,
                is_hot,
                owner,
                site_id,
                date_created,
                date_modified,
                eeo_ethnic_type_id,
                eeo_veteran_type_id,
                eeo_disability_status,
                eeo_gender
            )
            VALUES (
                "{first_name}",
                "{middle_name}",
                "{last_name}",
                "{email1}",
                "{email2}",
                "{phone_home}",
                "{phone_cell}",
                "{phone_work}",
                "{address}",
                "{city}",
                "{state}",
                "{zzip}",
                "{source}",
                "{key_skills}",
                "{date_available}",
                "{current_employer}",
                "{can_relocate}",
                "{current_pay}",
                "{desired_pay}",
                "{notes}",
                "{web_site}",
                "{best_time_to_call}",
                "{entered_by}",
                0,
                "{owner}",
                "{site_id}",
                NOW(),
                NOW(),
                "{eeo_ethnic_type_id}",
                "{eeo_veteran_type_id}",
                "{eeo_disability_status}",
                "{eeo_gender}"
            )""".format(
                    first_name            = candidate_info.first_name,
                    middle_name           = candidate_info.middle_name,
                    last_name             = candidate_info.last_name,
                    email1                = candidate_info.email1,
                    email2                = candidate_info.email2,
                    phone_home            = candidate_info.phone_home,
                    phone_cell            = candidate_info.phone_cell,
                    phone_work            = candidate_info.phone_work,
                    address               = candidate_info.address,
                    city                  = candidate_info.city,
                    #state                 = candidate_info.state,
                    state                 = 'autoL',
                    zzip                  = candidate_info.zzip,
                    source                = candidate_info.source,
                    key_skills            = candidate_info.key_skills,
                    date_available        = candidate_info.date_available,
                    current_employer      = candidate_info.current_employer,
                    can_relocate          = candidate_info.can_relocate,
                    current_pay           = candidate_info.current_pay,
                    desired_pay           = candidate_info.desired_pay,
                    notes                 = candidate_info.notes,
                    web_site              = candidate_info.web_site,
                    best_time_to_call     = candidate_info.best_time_to_call,
                    entered_by            = candidate_info.entered_by,
                    owner                 = candidate_info.owner,
                    site_id               = candidate_info.site_id,
                    eeo_ethnic_type_id    = candidate_info.eeo_ethnic_type_id,
                    eeo_veteran_type_id   = candidate_info.eeo_veteran_type_id,
                    eeo_disability_status = candidate_info.eeo_disability_status,
                    eeo_gender            = candidate_info.eeo_gender
                    )
    except Exception as e:
        pdb.set_trace()
        raise(e)

    return command 

class resume(object):
    def __init__(self, csv=''):
        self.csv = csv
        self.df = None

    def load_csv(self):
        self.df = pd.read_csv(self.csv) 
        self.df = self.df.dropna(how='all')
        self.df = self.df.loc[:,self.df.columns[:18]]

    def export_as_db(self):
        for cand in self.gen_db_entry():
            print(cand.first_name)

    @staticmethod
    def convert_str(series_data):
        # (['姓名','联系电话','邮箱','居住地','备注','期间','公司','职位','薪资状况']

        note = ''
        for item in series_data:
            if item is not None and str(item) != 'nan':
                note += "{}\n".format(item)

        return note.replace('"', '')


    def gen_candidate_entry(self) -> CandidateInfo:
        size = self.df.shape[0]
        for i in range(size):
            if type(self.df.iloc[i]['姓名']) is float:
                self.df.iloc[i]['姓名'] = '某某某'

            try:
                cand = CandidateInfo(first_name=self.df.iloc[i]['姓名'][1:],
                        last_name=self.df.iloc[i]['姓名'][0],
                        email1=self.df.iloc[i]['邮箱'],
                        phone_cell=str(self.df.iloc[i]['联系电话']).replace(' ', ''),
                        city=self.df.iloc[i]['居住地'],
                        key_skills=self.df.iloc[i]['职位'],
                        current_employer=self.df.iloc[i]['公司'],
                        current_pay='',
                        notes=self.convert_str(self.df.iloc[i][4:]),
                        site_id=1,
                        owner=1251)
                yield cand
            except TypeError as e:
                print(self.df.iloc[i])
                print('index : {}'.format(i))
                raise(e)

    

class AttachmentInfo(object):
    def __init__(self, 
                data_item_type=100,
                data_item_id=0,
                title='',
                original_filename='',
                stored_filename='',
                content_type='',
                resume='',
                text='',
                profile_image='',
                site_id=1,
                directory_name='',
                md5_sum=0,
                md5_sum_text='',
                file_size_kb=0
                ):
        self.data_item_type=data_item_type
        self.data_item_id=data_item_id
        self.title=title
        self.original_filename=original_filename
        self.stored_filename=stored_filename
        self.content_type=content_type
        self.resume=resume
        self.text=text
        self.profile_image=profile_image
        self.site_id=site_id
        self.directory_name=directory_name
        self.md5_sum=md5_sum
        self.md5_sum_text=md5_sum_text
        self.file_size_kb=file_size_kb


def sql_insert_attachment(attachment):
    sql_command = """INSERT INTO attachment (
                data_item_type,
                data_item_id,
                title,
                original_filename,
                stored_filename,
                content_type,
                resume,
                text,
                profile_image,
                site_id,
                date_created,
                date_modified,
                directory_name,
                md5_sum,
                md5_sum_text,
                file_size_kb
            )
            VALUES (
                "{data_item_type:d}",
                "{data_item_id:d}",
                "{title:s}",
                "{original_filename:s}",
                "{stored_filename:s}",
                "{content_type:s}",
                "{resume:s}",
                "{text:s}",
                "{profile_image:s}",
                "{site_id:d}",
                NOW(),
                NOW()",
                "{directory_name:s}",
                "{md5_sum:s}",
                "{md5_sum_text:s}",
                "{file_size_kb:d}"
            )""".format(
                    data_item_type=attachment.data_item_type,
                    data_item_id=attachment.data_item_id,
                    title=attachment.title,
                    original_filename=attachment.original_filename,
                    stored_filename=attachment.stored_filename,
                    content_type=attachment.content_type,
                    resume=attachment.resume,
                    text=attachment.text,
                    profile_image=attachment.profile_image,
                    site_id=attachment.site_id,
                    directory_name=attachment.directory_name,
                    md5_sum=attachment.md5_sum,
                    md5_sum_text=attachment.md5_sum_text,
                    file_size_kb=attachment.file_size_kb
                    )
    return sql_command



#+-------------------+--------------+------+-----+---------------------+----------------+
#| Field             | Type         | Null | Key | Default             | Extra          |
#+-------------------+--------------+------+-----+---------------------+----------------+
#| attachment_id     | int(11)      | NO   | PRI | NULL                | auto_increment |
#| data_item_id      | int(11)      | NO   | MUL | 0                   |                |
#| data_item_type    | int(11)      | NO   | MUL | 0                   |                |
#| site_id           | int(11)      | NO   | MUL | 0                   |                |
#| title             | varchar(128) | YES  |     | NULL                |                |
#| original_filename | varchar(255) | NO   |     |                     |                |
#| stored_filename   | varchar(255) | NO   |     |                     |                |
#| content_type      | varchar(255) | YES  |     | NULL                |                |
#| resume            | int(1)       | NO   |     | 0                   |                |
#| text              | text         | YES  |     | NULL                |                |
#| date_created      | datetime     | NO   |     | 1000-01-01 00:00:00 |                |
#| date_modified     | datetime     | NO   |     | 1000-01-01 00:00:00 |                |
#| profile_image     | int(1)       | YES  |     | 0                   |                |
#| directory_name    | varchar(64)  | YES  |     | NULL                |                |
#| md5_sum           | varchar(40)  | NO   | MUL |                     |                |
#| file_size_kb      | int(11)      | YES  |     | 0                   |                |
#| md5_sum_text      | varchar(40)  | NO   |     |                     |                |
#+-------------------+--------------+------+-----+---------------------+----------------+


def check_duplicate(phone_cell):
    global existing_cands
    for ele in existing_cands:
        if phone_cell == ele.phone_cell:
            return True

    return False


if __name__ == '__main__':

    # 初始化数据库连接:
    engine = create_engine('mysql+pymysql://cats:password@localhost:3306/cats_dev')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    
    
    
    #cand = CandidateInfo('吴', '吴', '吴', 'test@test.com', '', '188-8888-8888', '188-8888-8888', '', '', 'shanghai', '', '', '','test','', 'test', '', '', '')
    #
    #result = session.execute(
    #        generate_sql_command(cand) 
    #        )
    
    existing_cands = session.execute(
            "SELECT * FROM candidate"
            ).fetchall()
    session.close()
    #[print(i) for i in result[0]]
    #result = session.execute(
    #        "SELECT * FROM candidate where candidate_id=93"
    #        ).fetchall()
    #[print(i) for i in result[0]]
    
    #user = session.query(User).filter(User.id=='5').one()
    ## 打印类型和对象的name属性:
    #print('type:', type(user))
    #print('name:', user.name)
    ## 关闭Session:
    #session.close()
    #resumedb = resume('qe.csv')
#    resumedb = resume('sales.csv')
    #resumedb.load_csv()

    session = DBSession()
    #for cand in resumedb.gen_candidate_entry():
    #    if check_duplicate(cand.phone_cell):
    #        print("alreay existing")
    #        continue

    #    result = session.execute(
    #            sql_insert_candidate(cand) 
    #            )
    #    print("Inserted {}".format(cand.last_name+cand.first_name))
    print("hahahaha!")
    session.close()

