# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/william/Documents/Kuliah/!SKRIPSI/CODE'],
             binaries=[],
             datas=[('./img/illustration.jpg', './img'),('./img/i.png', './img'),('./img/warning.png', './img'), ('./img/icon.ico', './img')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='air pollution simulation',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='./img/icon.ico' )
app = BUNDLE(exe,
             name='air pollution simulation.app',
             icon='./img/icon.icns',
             bundle_identifier=None)
