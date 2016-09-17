
import os

###############################################################################
def sys_api_test(param):
	print("os.getcwd", os.getcwd());
	print("os.listdir", os.listdir());

###############################################################################
def copy_file_test(param):
	print("copy file.py to file.cp...")
	fp1 = open("file.py", 'rb');
	fp2 = open("file.cp", 'wb');
	str = fp1.read(); # if read x bytes: fp1.read(x);
	fp2.write(str);
	fp1.close();
	fp2.close();
	print("done\n")

###############################################################################
def main():
	sys_api_test(0)
	copy_file_test(0);

if __name__ == "__main__":
	main()
###############################################################################

