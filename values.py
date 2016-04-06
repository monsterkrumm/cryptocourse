
orig = "9F0B13944841A832B2421B9EAF6D9836813EC9D944A5C8347A7CA69AA34D8DC0DF70E343C4000A2AE35874CE75E64C31"
origlist = [int(orig[i:i+2],16) for i in range(0,len(orig),2)]

defpadder = 11 # the default padding value
defbl = 16 # the default blocklength
