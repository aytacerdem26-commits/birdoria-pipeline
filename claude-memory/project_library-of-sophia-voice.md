---
name: library-of-sophia-voice
description: "Library of Sophia YouTube channel's established narrator voice_id for genaipro TTS"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9709bff5-8a6c-4ec0-89f8-401e7a7cec3f
  modified: 2026-09-20T11:06:36.869Z
---

Library of Sophia channel (esoteric wisdom/manifestation audiobook channel) uses genaipro TTS voice_id **jfIS2w2yJi0grJZPyEsk** for all narration, established across videos 1-4.

**Why:** User confirmed this voice_id directly after a session reset wiped the record of it (video 5 was accidentally generated with a wrong substitute voice, "Michael Wogenburg", which the user caught as inconsistent).

**How to apply:** Always use `jfIS2w2yJi0grJZPyEsk` as `voice_id` for genaipro `/v1/labs/task` TTS calls for this channel, with `model_id: eleven_turbo_v2_5`, `stability: 0.7`, `similarity: 0.8`, `style: 0.3`, `speed: 0.90` (this speed setting is what produced the empirically observed ~700-838 char/min rate used to hit the 42-45 min target duration — see [[library-of-sophia-production-pipeline]] if that memory exists). Never substitute a different voice_id without explicit user confirmation, even if the genaipro voices list endpoint doesn't show this ID by name (the endpoint returns a rotating subset, not the full catalog, so absence from a listing does not mean the voice is invalid).
