const { app, BrowserWindow } = require('electron');
const path = require('path');

// try {
//     require('electron-reloader')(module)
// } catch(_) {}

const createWindow = () => {
    const win = new BrowserWindow({
        width: 1366,
        height: 720,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    win.loadFile('index.html');
}

app.whenReady().then(() => {
    createWindow();
});

app.on('window-all-closed', () => {
    if (process.platform != 'darwin') app.quit();
});