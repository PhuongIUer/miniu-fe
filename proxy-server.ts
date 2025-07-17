// proxy-server.ts
import express from 'express';
import cors from 'cors';
import axios from 'axios';

const app = express();
app.use(cors());

app.get('/proxy-image', async (req, res) => {
  const imageUrl = req.query.url as string;
  if (!imageUrl) return res.status(400).send("Missing image URL");

  try {
    const response = await axios.get(imageUrl, {
      responseType: 'arraybuffer',
    });

    const contentType = response.headers['content-type'] || 'image/jpeg';
    res.setHeader('Content-Type', contentType);
    res.send(response.data);
  } catch (error) {
    console.error('❌ Proxy fetch error:', error);
    res.status(500).send('Failed to fetch image');
  }
});

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`🚀 Proxy server is running at http://localhost:${PORT}`);
});
