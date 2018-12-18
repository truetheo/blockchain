import functools
import hashlib

# initializing out blockchain list
MINING_REWARD = 10

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Theo'
# set of UNIQUE values for participants of the system use set or {'Theo'}
paricipants = set(['Theo'])


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(paricipant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == paricipant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == paricipant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == paricipant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def get_last_blockchain_value():
    """Return the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    # true if sender has suficient means
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    """Append a new value as well as the last blockchain value to the block

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of the coins sent with the transaction (default = 1.0).
    """
    transaction = {'sender': sender,
                   'recipient': recipient,
                   'amount': amount}
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        # set will ignore the item if it is duplicated
        paricipants.add(sender)
        paricipants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    # list comprehention i.ex. [el * 2 for el in simple_list if el in calc_items]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    # copy a list in case transaction will be broadcasted. Range selector allows copy making [:]
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    # tx_sender = input('Enter the sender of the transaction: ') I am the sender!!!
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)  # i can omit the parenthasis


def get_user_choice():
    return input('Please enter your selection: ')


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting a block...')
        print(block)


def verify_chain():
    # Veridy the blockchain
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchains')
    print('4: Output paritipants.')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print(
                'You have sent {1} to {0} in a blockchain! Thank you!'.format(recipient, amount))
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print('Current users of the blockchain: {0}.'.format(str(paricipants)))
    elif user_choice == 'q':
        print('Option menu terminated...')
        break
    elif user_choice == 'h':
        # Make sure that I don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Magda',
                                  'recipient': 'Theo',
                                  'amount': 100.0}]
            }
    elif user_choice == '2':
        print_blockchain_elements()
        print('\nThat was full blockchain!')
    else:
        print('input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain')
        # leave loop
        break
    print('Balance: ', get_balance(owner))
else:
    print('User left')


print('Done!')
