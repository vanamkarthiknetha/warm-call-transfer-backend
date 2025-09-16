# 📞 Warm Call Transfer Flow

This document explains the **warm call transfer flow** used in this backend service.  
Reference: [LiveKit Warm Transfer Documentation](https://docs.livekit.io/sip/transfer-warm/)

---

## 🔄 Call Flow

1. **User joins a call with the Agent**  
   - The user connects via SIP/WebRTC.  
   - The Agent handles the conversation initially.  

2. **User requests transfer to a Human Agent**  
   - The Agent recognizes the request (via intent or explicit command).  

3. **Agent puts User on Hold**  
   - The Agent places the User on hold.  
   - Hold music or a message is played for the User.  

4. **Agent sets up a Consultation with Human Agent (HA)**  
   - A **consultation room** is created, and a secondary **TransferAgent** session is started.  
   - The Agent either:  
     - Summarizes the ongoing call with the User in the consultation room, **or**  
     - Directly dials the HA’s phone number via SIP trunk.  

5. **Supervisor Joins Consultation Room**  
   - The Human Agent (supervisor) is dialed through the **SIP outbound trunk**.  
   - The TransferAgent provides context (conversation history / summary).  

6. **Merge Calls**  
   - Once the supervisor is ready, they are moved from the consultation room into the User’s call.  
   - The SupportAgent may introduce the supervisor to the User.  
   - Both the SupportAgent and TransferAgent exit, leaving the User and Human Agent connected.  

---

## 📝 Example Use Case

- A customer calls into a support line.  
- AI Agent handles basic queries.  
- Customer asks to “speak with a real person.”  
- Agent:  
  - Places the customer on hold with music.  
  - Summarizes the issue to a live support agent in a consultation room.  
  - Connects the support agent to the customer by merging calls.  
- The live agent takes over, and the AI Agent leaves.  

---
