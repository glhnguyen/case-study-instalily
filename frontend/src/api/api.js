import axios from "axios";

const apiURL = process.env.REACT_APP_API_BASE_URL;

async function getAIMessage(input) {
  const url = `${apiURL}/ask`;
  const req = { question: input };
  return axios.post(url, req, { withCredentials: true });
}

export default getAIMessage;
