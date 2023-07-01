import check50
import check50.c
#         un      repo   branch folder
# slug is wadecss/checks/master/hello-wade
# must be submitted!!!

@check50.check()
def exists():
  check50.exists("hello-wade.py")
