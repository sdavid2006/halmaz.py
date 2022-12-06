
reggeli = {'sajt','tea', 'vaj', 'piritós'}
    

ebed = set()


ebed = { 'halászlé', 'kenyér', True}
  
reggeli.add('lekvár')
reggeli.remove('sajt')
reggeli.discard('sajt')
    
  
reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}
print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)
    
  