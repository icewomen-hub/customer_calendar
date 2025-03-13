entry = { 
            'id': 1,
            'start': '2025-03-13 14:00:12',
            'end': '2025-03-13 14:45:12',
            'app_type_id': 4711,
            'member_id': 23,
            'status': 'beantragt',
            'comment': 'Blaa',
            'add_info': None

         
        }
cols = ['id', 'start', 'end', 'app_type_id', 'member_id', 'status', 'comment', 'add_info']

db = pd.DataFrame(columns=cols)

#print(len(db))

db.loc[len(db)] = entry

print(db)

db.to_json('../../data/calendar_log.json')
