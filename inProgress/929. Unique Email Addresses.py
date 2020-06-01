def numUniqueEmails(emails):
    output = []
    for email in emails:
        split = email.split("@")
        corrected_email = ""
        for alpha in split[0]:
            if alpha.lower().isalnum():
                corrected_email = corrected_email + alpha
            elif alpha == ".":
                corrected_email = corrected_email
            elif alpha == "+":
                break
        corrected_email = corrected_email + "@" + split[1]
        output.append(corrected_email)
    return len(set(output))

# best solution on leetcode
def numUniqueElmailsFast(emails):
    output = []
    for email in emails:
        split = email.split("@")
        useful_part = split[0].split("+")
        corrected_useful_part = useful_part[0].replace(".","")
        corrected_email = corrected_useful_part + "@" + split[1]
        output.append(corrected_email)
    return len(set(output))

if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    emails = ["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]
    print(numUniqueElmailsFast(emails))