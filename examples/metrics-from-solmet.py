import glob, re, subprocess 

class MetricsFromSolMet(object):
    '''
    You need to run the script after smartcontracs-from-etherchain.py
    This class reads solidity code and produce the output using solmet tool.
    Input: ./output/a6/a6e0b24c65758154cac6f33b0c455727ab6193cb_BasicTokenSC.sol
    Output: ./output/a6/a6e0b24c65758154cac6f33b0c455727ab6193cb_BasicTokenSC.out
    '''
    def __init__(self):
        pass

    def write_solidity_metrics(self):
        jar = '../target/SolMet-1.0-SNAPSHOT.jar'
        for input in glob.glob("./output/*/*.sol"):
            output = re.sub('.sol$','.out' , input)
            subprocess.call(['java', '-jar', jar, '-inputFile', input, '-outFile', output])


if __name__ == "__main__":
    m = MetricsFromSolMet()
    m.write_solidity_metrics()