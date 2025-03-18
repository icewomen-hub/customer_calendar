import pandas as pd


class CustomerCalendar:
    data = None
    data_file = "../data/CalendarLog.json"

    def __init__(self):
        self.data = pd.read_json(self.data_file)

    def save(self):
        self.data.to_json(self.data_file)

    def book(
        self,
        c_start,
        c_end,
        appt_id,
        member_id,
        status="beantragt",
        comment="",
        add_info="",
    ):
        data_len = len(self.data)
        self.data.loc[data_len] = {
            "id": data_len + 1,
            "start": c_start,
            "end": c_end,
            "app_type_id": appt_id,
            "member_id": member_id,
            "status": status,
            "comment": comment,
            "add_info": add_info,
        }

    def edit(self, line):
        work_line = self.data[self.data["id"] == line["id"]]
        # print(work_line)
        # print(line)
        # exit()
        for i in work_line:
            work_line[i] = line[i]
            
        self.data[self.data["id"] == line["id"]] = work_line


cc = CustomerCalendar()


##cc.book(c_start='2025-05-21 09:30:12', c_end='2025-05-21 10:00:11', appt_id=53, member_id=68)
# cc.save()
# w = cc.data[cc.data['id']== 4]
# w['app_type_id'] = 44
# äprint(w)


to_be_editd = {
    "id": 4,
    "start": "2025-12-23 12:11:09",
    "end": "2025-03-12 20:00:06",
    "app_type_id": 53,
    "member_id": 68,
    "status": "beantragt",
    "comment": 'Foo bar info',
    "add_info": 'No milk today',
}
# cc.save()}
cc.edit(to_be_editd)
print(cc.data)
cc.save() 
