# -*- mode: python -*-

block_cipher = None


a = Analysis(['F:\\document\\项目\\测试代码\\Real_Time_Port_Scaner_V1.0\\Real_Time_Port_Scaner.py'],
             pathex=['F:\\document\\项目\\测试代码\\Real_Time_Port_Scaner_V1.0'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Real_Time_Port_Scaner',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Real_Time_Port_Scaner')
