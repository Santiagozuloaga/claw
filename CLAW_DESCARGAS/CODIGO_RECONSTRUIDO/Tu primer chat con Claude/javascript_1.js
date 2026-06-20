const { Client, LocalAuth } = require('[REDACTED_INFRASTRUCTURE]-web.js');
const qrcode = require('qrcode-terminal');
const { execSync } = require('child_process');
const client = new Client({ authStrategy: new LocalAuth() });
client.on('qr', qr => qrcode.generate(qr, { small: true }));
client.on('ready', () => console.log('Claw [REDACTED_INFRASTRUCTURE] Bridge listo'));
client.on('message', async msg => {
  const respuesta = execSync(`echo '${msg.body}' | python clawspring.py -p`).toString();
  msg.reply(respuesta);
});
client.initialize();