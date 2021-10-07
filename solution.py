"""Welcome_assignment answers
Author: Armando Flores Munos
Date: 10/7/2021
Really cool assignment posted for the start of the semester programming work
Input -All eight questions given in the assignment
 Output - The right answer for the specific question """

def welcome_assignment_answers(question):
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?":
        answer = "mTLS"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        answer = "42b76fe51778764973077a5a94056724"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        answer = "4"
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        answer = "3"
    return answer

#Complete all the questions

if __name__ == "__main__":

    debug_question = "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"
    print(welcome_assignment_answers(debug_question))