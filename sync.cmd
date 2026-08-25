@echo off
REM Sync this folder with GitHub. Run before a Cowork session and again after.
REM Optional argument becomes the commit message:
REM     sync.cmd added three candidate audiences
setlocal
cd /d "%~dp0"

echo.
echo == Pulling latest from GitHub ==
git pull --no-rebase
if errorlevel 1 goto err

git add -A
git diff --cached --quiet
if errorlevel 1 goto commit
echo.
echo == Nothing new to save. You are up to date. ==
goto done

:commit
set "MSG=%*"
if "%MSG%"=="" set "MSG=Update from Cowork session"
echo.
echo == Saving: %MSG% ==
git commit -m "%MSG%"
if errorlevel 1 goto err
echo.
echo == Pushing to GitHub ==
git push
if errorlevel 1 goto err

:done
echo.
echo == Done. Claude Code can see your changes. ==
endlocal
exit /b 0

:err
echo.
echo == Something went wrong above. ==
echo If it mentions CONFLICT, stop and ask Claude Code. Do not force anything.
endlocal
exit /b 1
