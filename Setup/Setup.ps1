<#
.SYNOPSIS
    Downloads and installs Python silently with common options

.DESCRIPTION
    This script downloads the specified Python version and installs it with:
    - Installation for all users
    - Python added to PATH
    - File associations for .py files
    - Start menu shortcuts
    - Python launcher installed
    - Documentation and test suite excluded

.NOTES
    File Name      : Install-Python.ps1
    Requires Admin : Yes
#>

# Parameters - adjust these as needed
$PythonVersion = "3.11.4"
$PythonArch = "amd64"  # or "win32" for 32-bit
$InstallDir = "C:\Python$($PythonVersion.Substring(0,3))" # e.g. C:\Python3.11

# Construct download URL
$PythonURL = "https://www.python.org/ftp/python/$PythonVersion/python-$PythonVersion-$PythonArch.exe"
$Installer = "$env:TEMP\python-$PythonVersion-$PythonArch.exe"

# Check if running as administrator
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "This script requires administrator privileges. Restarting with elevated permissions..." -ForegroundColor Yellow
    Start-Process -FilePath "powershell.exe" -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$($MyInvocation.MyCommand.Path)`"" -Verb RunAs
    exit
}

# Download Python installer
Write-Host "Downloading Python $PythonVersion..." -ForegroundColor Cyan
try {
    Invoke-WebRequest -Uri $PythonURL -OutFile $Installer -UseBasicParsing
    Write-Host "Download completed successfully." -ForegroundColor Green
}
catch {
    Write-Host "Failed to download Python installer: $_" -ForegroundColor Red
    exit 1
}

# Install Python silently
Write-Host "Installing Python $PythonVersion to $InstallDir..." -ForegroundColor Cyan
$InstallArgs = @(
    "/quiet",
    "InstallAllUsers=1",
    "PrependPath=1",
    "AssociateFiles=1",
    "Shortcuts=1",
    "Include_doc=0",
    "Include_launcher=1",
    "Include_test=0",
    "TargetDir=`"$InstallDir`""
)

try {
    $process = Start-Process -FilePath $Installer -ArgumentList $InstallArgs -Wait -PassThru
    
    if ($process.ExitCode -ne 0) {
        Write-Host "Python installation failed with exit code $($process.ExitCode)" -ForegroundColor Red
        exit $process.ExitCode
    }
    
    Write-Host "Python $PythonVersion installed successfully." -ForegroundColor Green
}
catch {
    Write-Host "Installation failed: $_" -ForegroundColor Red
    exit 1
}

# Verify installation
Write-Host "Verifying Python installation..." -ForegroundColor Cyan
try {
    $pythonPath = Join-Path $InstallDir "python.exe"
    & $pythonPath --version
    Write-Host "Python verification successful." -ForegroundColor Green
}
catch {
    Write-Host "Failed to verify Python installation: $_" -ForegroundColor Yellow
}

# Clean up installer
Remove-Item -Path $Installer -Force -ErrorAction SilentlyContinue

# Update environment variables (for current session)
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

Write-Host "Installation complete. You may need to restart your shell or computer for PATH changes to take full effect." -ForegroundColor Green