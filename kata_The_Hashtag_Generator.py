def generate_hashtag(s):
    # s = s.title().replace(' ','')   
    # return False if len(s) == 0 or len(s)>=140 else f'#{s}' 
    return '#' + s.title().replace(' ','') if 0<len(s)<=140 else False

print(generate_hashtag('Do We have A Hashtag'))