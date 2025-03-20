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
        for i in work_line:
            work_line[i] = line[i]
            
        self.data[self.data["id"] == line["id"]] = work_line
        
    def get_data(self, topic):
        return self.data


