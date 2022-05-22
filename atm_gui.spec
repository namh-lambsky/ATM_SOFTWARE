# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['atm_gui.py'],
             pathex=['C:\\DesktopFolders\\ProgramsData\\dataU\\Proyecto5toSemestre\\ATM_SOFTWARE'],
             binaries=[('libiconv.dll', '.'), ('libzbar-64.dll', '.')],
             datas=[('IMAGES/*.png','IMAGES'),('IMAGES/*.ico','IMAGES')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='atm_gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='C:\\DesktopFolders\\ProgramsData\\dataU\\Proyecto5toSemestre\\ATM_SOFTWARE\\IMAGES\\LogoBancolombia.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='atm_gui')
