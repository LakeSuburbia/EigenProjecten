# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['writetracker.pyw'],
             pathex=['/Users/sandermangelschots/Documents/GitHub/EigenProjecten/Daan_writetracker'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='writetracker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='ndowed')
app = BUNDLE(exe,
             name='writetracker.app',
             icon='ndowed',
             bundle_identifier=None)
