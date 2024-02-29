import axios from 'axios';

const options = {
  text: "Message from slack bot!!",
};

slack = "T06L0LNHA58/B06LX4U4J4B/alSW0feBStQwRsjT1pFrKJ1j"
axios.post('https://hooks.slack.com/services/ + slack', JSON.stringify(options))
.then((response) => {
  console.log('SUCCEEDED: Sent slack webhook: \n', response.data);
  resolve(response.data);
})
.catch((error) => {
  console.log('FAILED: Send slack webhook', error);
  reject(new Error('FAILED: Send slack webhook'));
});
