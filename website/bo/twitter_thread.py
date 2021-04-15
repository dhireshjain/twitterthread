from website.node import Node
from website.sao import twitter


def get_tweet(tweet_id):
    return twitter.get_tweet(tweet_id)


def get_replies(tweet):
    return twitter.get_replies(tweet)


def build_tree(root):
    queue = [Node(root)]
    tree = queue[0]
    while len(queue) != 0:
        node = queue.pop(0)
        current_replies = get_replies(node.tweet)
        node_replies = convert_to_nodes(current_replies)
        for node_reply in node_replies:
            queue.append(node_reply)
        node.set_replies(node_replies)
    return Node.convert_to_dict2(tree)


def convert_to_nodes(tweets):
    return list(map(lambda t: Node(t), tweets))
