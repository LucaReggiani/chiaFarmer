from flask import Flask, render_template, url_for

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

    section2 = "To farm Chia, you should initially make at least one 'Plot'. Plots are files that take up space on " \
               "your hard drive. Making plots requires significant investment and the number of plots you can create " \
               "in parallel depends on the power of your CPU (number of cores). You can move plots from one machine " \
               "to another without any restrictions, so it is also possible to generate plots on a more powerful " \
               "machine, and transfer them once finished to a less powerful one. "

    section3 = "The Plotting process requires more space than the final output, known as temporary space. The amount " \
               "of space required depends on the size k you are plotting. For instance, a k32 Plot has a size of " \
               "around 100 GB yet needs around 239 GB of transitory space to be made. The area of the impermanent " \
               "space is a significant choice while plotting. The best arrangement is to devote the quickest hard " \
               "plate to deal with the impermanent space.  Plotting on a slower disk such as the classic HDD is " \
               "possible, but will take longer. The slow speed of the disk can be compensated by plotting on several " \
               "disks in parallel. However, if you are plotting on HDD, it is not a good idea to plot on the same " \
               "disk more than one Plot at a time, otherwise the read/write head will bounce around trying to write " \
               "Plot files to different sectors of the disk at the same time, which will make it slow. Toward the " \
               "finish of the Plotting cycle, the substance of the impermanent records are compressed and moved to " \
               "the destination Plot file. "

    section4 = "It is by using the created plots that farming can be done. Farming, or harvesting, can be considered " \
               "as a round of bingo. The plots are the bingo folders and the way of collecting consists of waiting " \
               "that the number will be called and checking the envelope to check whether you have won. This is a " \
               "trivial activity and utilizations an extremely limited quantity of power. Farming is a real green " \
               "alternative to the status quo imposed by Bitcoin, in spite of the fact that it actually requires a " \
               "force supply. \n\n You can download and install the farming software visiting the following link: " \
               "https://github.com/Chia-Organization/chia-blockchain "

    section5 = "After this brief introduction, it should be clearer to understand the service we offer: we sell " \
               "pre-created plots. Do you want to enter the world of farming, but don't have machines powerful enough " \
               "to generate plots? Do you want to avoid wasting time and money by getting started in the world of " \
               "cryptocurrencies right away? Don't worry, the plots we produce are at your disposal. Everyone can " \
               "buy, but only a few are able to generate cryptocurrencies and sell them. Be your own source, " \
               "not the buyer. "

    return render_template('index.html',
                           section1=section1,
                           section2=section2,
                           section3=section3,
                           section4=section4,
                           section5=section5
                           )


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
