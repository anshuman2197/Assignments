def longlen(*strings):
   max = 0
   for s in strings:
     print(s)
     if len(s) > max:
        max = len(s)

   return max

print(longlen('apple','banana','cantaloupe','cherry'))