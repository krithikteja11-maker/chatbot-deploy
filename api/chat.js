export default async function handler(req, res) {
    const response = await fetch("https://chatbot-deploy-g0i7.onrender.com/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(req.body)
    });

    const data = await response.json();
    res.status(200).json(data);
}