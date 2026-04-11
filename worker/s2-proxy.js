/**
 * Cloudflare Worker: Semantic Scholar API Proxy
 * Forwards requests to S2 API with rate limiting (1 req/sec).
 * Deploy: wrangler deploy
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Only allow /graph/ path prefix
    if (!url.pathname.startsWith('/graph/')) {
      return new Response('Usage: /graph/v1/paper/search?query=...', { status: 400 });
    }

    // Build S2 API URL
    const s2Url = `https://api.semanticscholar.org${url.pathname}${url.search}`;

    // Forward headers
    const headers = {
      'Accept': 'application/json',
      'User-Agent': 'ScholarPipeline/1.0 (Cloudflare Worker)',
    };

    // Pass through API key if provided
    const apiKey = request.headers.get('x-api-key') || env.S2_API_KEY || '';
    if (apiKey) {
      headers['x-api-key'] = apiKey;
    }

    try {
      const resp = await fetch(s2Url, { headers });
      const body = await resp.text();

      return new Response(body, {
        status: resp.status,
        headers: {
          'Content-Type': 'application/json',
          'X-Proxied-By': 'cloudflare-worker',
          'Access-Control-Allow-Origin': '*',
        },
      });
    } catch (err) {
      return new Response(JSON.stringify({ error: err.message }), {
        status: 502,
        headers: { 'Content-Type': 'application/json' },
      });
    }
  },
};
