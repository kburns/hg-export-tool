def build_filter(args):
    return Filter(args)

class Filter:
    def __init__(self, args):
        pass

    def commit_message_filter(self, commit_data):
        commit_data['desc'] = (
            commit_data['desc'] +
            b'\n\n' +
            b'hg hash: ' +
            commit_data['hg_hash'])
