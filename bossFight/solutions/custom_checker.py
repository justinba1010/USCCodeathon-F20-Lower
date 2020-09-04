
# Start of BODY
'''
TestStruct::
testcase_id                   [int] ID of the test-case
testcase_input_path           [str] File path to test-case input
testcase_output_path          [str] File path to test-case output generated by the problem solver
testcase_expected_output_path [str] File path to test-case expected output to be matched with
testcase_error_path           [str] File path to test-case STDERR
metadata_file_paths           [list<str>] File paths to Question metadata (Extra files usually used for defining traning sets)
submission_code_path          [str] File path to submission source code
submission_language           [str] Language token of submission
testcase_result               [bool] Set to True if test-case output matches test-case expected output. Matching is done line by line
testcase_signal               [int] Exit code of the test-case process
testcase_time                 [float] Time taken by the test-case process in seconds
testcase_memory               [int] Peak memory of the test-case process determined in bytes
data                          [str] <Future use>
ResultStruct::
result      [bool]  Assign test-case result. True determines success. False determines failure
score       [float] Assign test-case score. Normalized between 0 to 1
message     [str] Assign test-case message. This message is visible to the problem solver
'''

def invalid(mes):
    r_obj.result = False
    r_obj.score = 0.0
    r_obj.message = mes


def run_custom_checker(t_obj, r_obj):
    # Don't print anything to STDOUT in this function
    # Enter your custom checker scoring logic here
    outputfile = open(t_obj.testcase_output_path, "r")
    infile = open(t_obj.testcase_input_path, "r")
    startHealth = int(infile.read())
    moves = outputfile.read().rstrip().split("\n")
    moves = list(map(int, moves))
    r_obj.result = False
    r_obj.score = 0.0
    r_obj.message = "Failure"
    pos = 0
    playerHealth = 100
    bossHealth = startHealth
    timestep = 0
    restCooldown = 0
    poisonCooldown = 0
    while bossHealth > 0 and playerHealth > 0:
        if timestep > startHealth * 8:
            invalid("Too many moves to complete")
            break
        restCooldown = max(restCooldown - 1, 0)
        if restCooldown and moves[pos] != 0:
            invalid("Invalid Move1")
            break
        if restCooldown == 0:
            if moves[pos] == 1:
                if timestep % 2 == 0:
                    bossHealth -= 9
                else:
                    invalid("Invalid Move2", timestep)
                    break
            elif moves[pos] == 2:
                if timestep % 3 == 0:
                    restCooldown = 3
                    playerHealth = min(100, playerHealth + 15)
                else:
                    invalid("Invalid Move3")
                    break
            elif moves[pos] != 0:
                invalid("Invalid Move4")
                break
        if bossHealth <= 0:
            r_obj.result = True;
            r_obj.score = 1.0;
            r_obj.message = "The monster was defeated!";
            break
        if timestep != 0:
            if timestep % 20 == 0:
                playerHealth -= playerHealth//2
            if timestep % 5 == 0:
                playerHealth -= 11
            if timestep % 14 == 0: # was 17, but that was too easy
                poisonCooldown = 3
        timestep += 1

    if playerHealth <= 0:
        invalid("You ran out of health!")
    # if output in a:
    #     r_obj.result = True
    #     r_obj.score = 1.0
    #     r_obj.message = "Success"
    
        
#     r_obj.result = False
#     r_obj.score = 0.0
#     r_obj.message = "Failure"
    
#     if (output > expected*0.9 and output < expected*1.1):
#         r_obj.result = True
#         r_obj.score = 1.0
#         r_obj.message = "Success"

    # r_obj.result = True;
    # r_obj.score = 1.0;
    # r_obj.message = "Success";

# End of BODY
        