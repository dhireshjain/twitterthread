from twitter.models import Status
import json


class Node:
    tweet: Status
    replies = []

    def __init__(self, tweet):
        self.tweet = tweet

    def get_replies(self):
        return self.replies

    def set_replies(self, replies):
        self.replies = replies

    @staticmethod
    def convert_to_dict2(root):
        tree = Node.dfs(root, 0)
        return json.loads(json.dumps(tree))

    @staticmethod
    def dfs(root, level):
        if len(root.get_replies()) == 0:
            return Node.convert_node_to_dict(root, level)

        curr_dict = Node.convert_node_to_dict(root, level)
        for node in root.get_replies():
            temp_dict = Node.dfs(node, level + 1)
            curr_dict['children'].append(temp_dict)
        return curr_dict

    @staticmethod
    def convert_node_to_dict(node, level):
        return {'username': node.tweet.user.screen_name, 'text': node.tweet.full_text, 'level': level, 'children': []}
