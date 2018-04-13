import tarfile

with tarfile.open('tarfile_add.tar', mode='w') as out:
    out.add('passwd_copy')
