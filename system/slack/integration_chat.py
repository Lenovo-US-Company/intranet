import axios from 'axios';

const options = {
  text: "Message from slack bot!!",
};

axios.post('<SLACK_WEBHOOK_URL>', JSON.stringify(options))
.then((response) => {
  console.log('SUCCEEDED: Sent slack webhook: \n', response.data);
  resolve(response.data);
})
.catch((error) => {
  console.log('FAILED: Send slack webhook', error);
  reject(new Error('FAILED: Send slack webhook'));
});
