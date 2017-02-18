#!/usr/bin/env python3

'''
qiime-plugin.py

abstracts command line functions of qiime to be loaded into biocloud

Prerequisites
    * Qiime Docker Image is installed on the host


'''
import subprocess



debug = True

qiime_binary = []



def main():
    global qiime_binary
    qiime_binary = ['docker' ,'run','-it', '-v', getWD()+'/:/data', 'qiime2/core:2017.2', 'qiime']


    print("Welcome to QIIME plug-in tests.")
    
    
    print(qiime_binary)
    
    runProgram()
# Command to Run Qiime
# docker run -t -i -v $(pwd):/data qiime2/core:2017.2 qiime




def runProgram ():
    
    # process = subprocess.run(
    #     args=['qiime', 'demux', 'emp',
    #     '--i-seqs', inputFile.path+inputFile.fileName,
    #     '--m-barcodes-file', metadataFile.path+metadataFile.fileName,
    #     '--m-barcodes-category', barcodeCategory,
    #     '--o-per-sample-sequences', outputFile],
    #     shell=False,
    #     stdout=subprocess.PIPE,
    #     stderr=subprocess.PIPE)

    process = subprocess.run(
        args=qiime_binary+['demux']
        ,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


    debugPrint(process.stderr.decode('utf-8'))
    debugPrint(process.stdout.decode('utf-8'))


def getWD():

    process = subprocess.run(
        args=['pwd'],
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    #process.stderr.decode('utf-8')
    #process.stdout.decode('utf-8')

    if process.returncode != 0:
        raise ValueError('Cannot run pwd command')

    #This line of code makes me smile.
    return process.stdout.decode('utf-8')[:-1]+'/'




def debugPrint(str):
    if debug:
        print(str)





if __name__ == '__main__':
    main()
