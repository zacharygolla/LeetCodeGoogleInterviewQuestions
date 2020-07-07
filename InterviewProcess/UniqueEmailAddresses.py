def main():
    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(numUniqueEmails(emails))


def numUniqueEmails(emails):
    seen = set()
    for email in emails:
        local, domain = email.split('@')
        if '+' in local:
            local = local[:local.index('+')]
        seen.add(local.replace('.', '') + '@' + domain)
    return len(seen)


if __name__ == "__main__":
    main()
