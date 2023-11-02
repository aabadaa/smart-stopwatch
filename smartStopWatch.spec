# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
a = Analysis(
    ['smartStopWatch.py'],
    pathex=['D:\a projects\pyton\smart stop watch'],
    binaries=[],
             datas=[('stopwatch.py', '.'), ('stopwatch_ui.py', '.'), ('fileUtils.py', '.'), ('saved_state_util.py', '.')],
                 hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['altgraph', 'packaging', 'pefile', 'pip', 'pyinstaller', 'pyinstaller-hooks-contrib', 'pyperclip', 'pywin32-ctypes', 'setuptools'],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='smartStopWatch',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
