from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    section1 = "Chia Coin is a digital money worked since 2017 by the Chia organization, established by Bram Cohen, " \
               "the maker of the BitTorrent distributed record sharing framework. The organization, thus the basic " \
               "crypto, has an attention on decreasing the ecological harm brought about by mining digital curencies, " \
               "and proposes to supplant Bitcoin's 'proof of work' framework. However, how precisely does this work? " \
               "So, every digital currency receives various strategies to check exchanges. Typically, this cycle is " \
               "finished by aggregately utilizing the PC force of the miners, who are compensated for their " \
               "contribute. Mining on the Chia organization, on the other hand, depends on the empty memory space of " \
               "the miners' hard drives, in an interaction known as farming. In fact, instead of dedicated hardware, " \
               "it simply uses software that uses free space on hard drives and SSDs to generate the cryptocurrency. " \
               "Rather than Bitcoin's 'Verification of Work' model, Chia utilizes a mix of 'Evidence of Room' and " \
               "'Confirmation of Time'. Clients are called farmers (not miners) since they 'seed' the free space on " \
               "hard drives and SSDs by installing software that stores an assortment of cryptographic numbers. These " \
               "'plots of land' are remunerated with blocks of the blockchain. A VDF (Evident Defer Capacity) worker, " \
               "called 'Timelord', confirms the blocks to permit the blockchain to advance and rewards the client " \
               "with Chia. "
    return render_template('index.html', section1=section1)


'''
@app.errorhandler(404)
def page_not_found():
    return render_template('404.html')


@app.errorhandler(500)
def internal_server_error():
    return render_template('500.html')
'''


if __name__ == '__main__':
    app.run()
