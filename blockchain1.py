# initializing out blockchain list
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Theo'


def get_last_blockchain_value():
    """Return the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


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
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    # list comprehention i.ex. [el * 2 for el in simple_list if el in calc_items]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)
    # for key in last_block:
    #     value = last_block[key]
    #     hashed_block = hashed_block + str(value)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


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
    block_index = 0
    is_valid = True
    for block in blockchain:
        print('\nChecking block')
        print('block 0: {0} is equal to {1}. Is that true?\n'.format(
            str(block[0]), str(blockchain[block_index - 1])))
        if block_index == 0:
            block_index += 1
            continue
        if block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchains')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(
            'You have sent {1} to {0} in a blockchain! Thank you!'.format(recipient, amount))
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'q':
        print('Option menu terminated...')
        break
    elif user_choice == 'h':
        # Make sure that I don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == '2':
        print_blockchain_elements()
        print('\nThat was full blockchain!')
    else:
        print('input was invalid, please pick a value from the list!')
    # if not verify_chain():
    #     print('Invalid blockchain')
    #     break
print(blockchain)
print('Done!')
