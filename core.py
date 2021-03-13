class core():
    class student_data():
        def __init__(self, properties):
            self.values = {}
            for i in properties:
                self.values[i] = None
        
        def dict(self):
            return self.values

        def changeValue(self, valuedict):
            for key in valuedict.keys():
                if key in self.properties:
                    self.values[key] = valuedict[key]

        def dump(obj):
            return obj.values

    class student_info(student_data):
        properties = ['name', 'id', 'birthym', 'school', 'department']
        def __init__(self, valuedict = None):
            super(core.student_info, self).__init__(self.properties)
            if valuedict:
                self.changeValue(valuedict)
        
        def load(obj):
            return core.student_info(obj)

    class student_score(student_data):
        properties = ['id', 'class', 'score']
        def __init__(self, valuedict = None):
            super(core.student_score, self).__init__(self.properties)
            if valuedict:
                self.changeValue(valuedict)
        
        def load(obj):
            return core.student_score(obj)
    
    def __init__(self):
        self.loadFile()
    
    def loadFile(self):
        import json
        try:
            with open("infolist.db", "r") as f:
                self.infoList = json.load(f, object_hook=core.student_info.load)
        except:
            self.infoList = []
        try:
            with open("scorelist.db", "r") as f:
                self.scoreList = json.load(f, object_hook=core.student_score.load)
        except:
            self.scoreList = []
    
    def saveFile(self):
        import json
        with open("infolist.db", "w") as f:
            json.dump(self.infoList, f, default=core.student_data.dump, indent=4, separators=(',', ':'))
        with open("scorelist.db", "w") as f:
            json.dump(self.scoreList, f, default=core.student_data.dump, indent=4, separators=(',', ':'))
    
    def query(self, request, type = 0):
        requestSatisfied = []
        if type == 0:
            cnt = 0
            for info in self.infoList:
                if not request or request == info.dict()['name'] or request == info.dict()['id']:
                    tmp = info.dict().copy()
                    tmp['index'] = cnt
                    requestSatisfied.append(tmp)
                cnt += 1
        else:
            cnt = 0
            for score in self.scoreList:
                if not request or request == score.dict()['id']:
                    tmp = score.dict().copy()
                    tmp['index'] = cnt
                    requestSatisfied.append(tmp)
                cnt += 1
        return requestSatisfied
    
    def changeValueByIndex(self, index, data, type = 0):
        if type == 0:
            self.infoList[index].changeValue(data)
        else:
            self.scoreList[index].changeValue(data)
    
    def append(self, data, type = 0):
        if type == 0:
            tmp = core.student_info()
            tmp.changeValue(data)
            self.infoList.append(tmp)
        else:
            tmp = core.student_score()
            tmp.changeValue(data)
            self.scoreList.append(tmp)
    
    def delete(self, index, type = 0):
        if type == 0:
            self.infoList.pop(index)
        else:
            self.scoreList.pop(index)
    
    def getHeaders(self, type = 0):
        if type == 0:
            return ['姓名', '学号', '出生年月', '所在院', '所在系'], core.student_info.properties
        else:
            return ['学号', '课程名称', '成绩'], core.student_score.properties

#x = core()
#tmp = x.student_score()