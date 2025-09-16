# Warm Call Transfer Backend

This backend service uses **LiveKit Agent Worker** to enable warm call transfer functionality.

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/vanamkarthiknetha/warm-call-transfer-backend.git
```

Go to project directory
```bash
cd warm-call-transfer-backend
```

### 2. Create and Activate Virtual Environment
Windows (PowerShell)
```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```

macOS/Linux
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env File
```bash
LIVEKIT_API_KEY=
LIVEKIT_API_SECRET=
LIVEKIT_URL=
LIVEKIT_SIP_OUTBOUND_TRUNK=ST_XXXXX # Optional, only for Twilio call
LIVEKIT_SUPERVISOR_PHONE_NUMBER=+91.....   # Optional, only for Twilio call

DEEPGRAM_API_KEY=
GOOGLE_API_KEY=
HF_TOKEN=

```

### 5.After setting up .env variables, Download Related Files
```bash
python warm_transfer.py download-files
```
### 6. Run the Agent in Development Mode
```bash
python warm_transfer.py dev
```

# Environment Variables Explanation
- LIVEKIT_API_KEY / LIVEKIT_API_SECRET → LiveKit credentials for authentication.
- LIVEKIT_URL → Your LiveKit server URL.
- DEEPGRAM_API_KEY → API key for Deepgram speech recognition.
- GOOGLE_API_KEY → API key for Google LLM.
- HF_TOKEN → Hugging Face token for model access.(https://huggingface.co/settings/tokens/new?tokenType=read
)
- LIVEKIT_SIP_OUTBOUND_TRUNK → (Optional) Outbound trunk ID for SIP calls. Example: ST_abcxyz
- LIVEKIT_SUPERVISOR_PHONE_NUMBER → (Optional) Supervisor’s phone number for warm transfer (Twilio) with coutnry code(+91..).

## 📞 Setting up Twilio SIP Trunk

1. **Create a Twilio account**

   * Free trial accounts can only call **verified numbers**.
   * Buy a phone number from Twilio.

2. **Create a SIP Trunk**

   * Go to [Twilio SIP Trunking Console](https://console.twilio.com/us1/develop/sip-trunking/manage/trunks?frameUrl=/console/sip-trunking/trunks).
   * Create a new trunk.

3. **Create a Termination URI**

   * Configure a termination URI for the trunk.
   * Add credentials (username & password).
   * Note down the termination URI.

4. **Attach a Phone Number**

   * Add the phone number you bought to the trunk.

5. **Configure in LiveKit Cloud**

   * Go to **LiveKit Cloud → Telephony → Configuration → Outbound Trunks**.
   * Add a new trunk using the JSON editor:

   ```json
   {
     "sipTrunkId": "ST_ncFoRHJRLv9K", 
     "name": "My Twilio Trunk",
     "address": "<copied termination uri>",
     "numbers": [
       "+12136986234"
     ],
     "authUsername": "XXXXX",
     "authPassword": "XXXXX"
   }
   ```

   * Copy the **`sipTrunkId`** (`ST_xxxxxxx`) and set it in `.env` as `LIVEKIT_SIP_OUTBOUND_TRUNK`.

6. **Add Supervisor Phone Number (Optional)**

   * If you want to test warm transfer with Twilio, add your **verified phone number** to:

     ```env
     LIVEKIT_SUPERVISOR_PHONE_NUMBER=+91XXXXXXXXXX
     ```