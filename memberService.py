from repository import Repository


class MemberService():
    def get_memberList(self):
        return Repository.member

    def listar(self):
        print("\n     Listando")
        for key in self.Repository.membersList:
            print("-> %s" % (self.repository.member[key]))

    def add_member(self, member):
        print("\n     Agregando")
        lastKey = -1
        for i in Repository.membersList:
            lastKey = i
        memberkey = lastKey + 1
        Repository.membersList[memberkey] = member.__dict__
        return memberkey

    def update_member(self, key, member):
        Repository.member[key]['_name'] = member.name
        Repository.member[key]['_surname'] = member.surname
        Repository.member[key]['_age'] = member.age

    def delete_member(self, key):
        del Repository.member[key]
