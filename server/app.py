from fastapi import FastAPI, Request
from datetime import datetime
import json
import responder

app = FastAPI(title="ZeroToken Deception Server", version="1.0.0")

@app.get("/api/v1/trap")
async def handle_canary_trip(request: Request):
    client_ip = request.client.host
    user_agent = request.headers.get("user-agent", "Unknown")
    query_params = dict(request.query_params)

    incident = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": "CANARY_TOKEN_ACCESSED",
        "severity": "CRITICAL",
        "source_ip": client_ip,
        "user_agent": user_agent,
        "payload": query_params
    }

    print("\n" + "="*55, flush=True)
    print("🚨 [CRITICAL ALERT] Canary Token Hijacked by Attacker!", flush=True)
    print(f"Timestamp   : {incident['timestamp']}", flush=True)
    print(f"Attacker IP : {client_ip}", flush=True)
    print(f"User-Agent  : {user_agent}", flush=True)
    print(f"Trap Params : {query_params}", flush=True)
    print("="*55, flush=True)

    host_target = query_params.get("host", "node_01")
    responder.execute_autonomous_containment(host_target=host_target, attacker_ip=client_ip)

    with open("incidents.log", "a", encoding="utf-8") as f:
        f.write(json.dumps(incident) + "\n")

    return {"status": "ok", "message": "Authentication error - Token expired"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)