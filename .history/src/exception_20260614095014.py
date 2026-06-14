import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    fle_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occures in python script name[{0} line nume[{}] ]" 