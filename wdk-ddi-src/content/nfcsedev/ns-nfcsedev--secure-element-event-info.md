---
UID: NS.nfcsedev._SECURE_ELEMENT_EVENT_INFO
title: SECURE_ELEMENT_EVENT_INFO
author: windows-driver-content
description: This structure provides information about a secure element event.
old-location: nfpdrivers\secure_element_event_info.htm
old-project: nfpdrivers
ms.assetid: 72B31C26-89D3-49B2-A404-E6F096D0A334
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: SECURE_ELEMENT_EVENT_INFO, SECURE_ELEMENT_EVENT_INFO, *PSECURE_ELEMENT_EVENT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: nfcsedev.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SECURE_ELEMENT_EVENT_INFO
req.alt-loc: nfcsedev.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# SECURE_ELEMENT_EVENT_INFO structure



## -description
<p>This structure provides information about a secure element event.</p>


## -syntax

````
typedef struct _SECURE_ELEMENT_EVENT_INFO {
  GUID                                     guidSecureElementId;
  SECURE_ELEMENT_EVENT_TYPE                eEventType;
  DWORD                                    cbEventData;
  _Field_size_bytes_(cbEventData)
    BYTE pbEventData[ANYSIZE_ARRAY];
} SECURE_ELEMENT_EVENT_INFO, *PSECURE_ELEMENT_EVENT_INFO;
````


## -struct-fields
<dl>

### -field <b>guidSecureElementId</b>

<dd>
<p>This is a unique identifier for the secure element.</p>
</dd>

### -field <b>eEventType</b>

<dd>
<p>This is an event type. For more information about the types, see the <a href="..\nfcsedev\ne-nfcsedev--secure-element-event-type.md">SECURE_ELEMENT_EVENT_TYPE</a> enumeration topic.</p>
</dd>

### -field <b>cbEventData</b>

<dd>
<p>This is the amount of bytes for the pbEventData array.</p>
</dd>

### -field <b>pbEventData[ANYSIZE_ARRAY]</b>

<dd>
<p>This is the event data buffer. When <b>eEventType</b> is <b>HceActivated</b> or <b>HceDeactivated</b>, this member contains a pointer to a <a href="..\nfcsedev\ns-nfcsedev--secure-element-hce-activation-payload.md">SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD</a> structure. The <b>bConnectionId</b> member in that structure is the same ID value that’s used in <a href="..\nfcsedev\ns-nfcsedev--secure-element-hce-data-packet.md">SECURE_ELEMENT_HCE_DATA_PACKET</a> to send and receive an HCE packet with <a href="..\nfcsedev\ni-nfcsedev-ioctl-nfcse-hce-remote-send.md">IOCTL_NFCSE_HCE_REMOTE_SEND</a> and <a href="..\nfcsedev\ni-nfcsedev-ioctl-nfcse-hce-remote-recv.md">IOCTL_NFCSE_HCE_REMOTE_RECV</a>.</p>
<p>When <b>eEventType</b> is <b>ExternalReaderArrival</b> or <b>ExternalReaderDeparture</b>, <b>pbEventData</b> is empty and <b>cbEventData</b> is 0.</p>
<p>When <b>eEventType</b> is <b>Transaction</b>, <b>pbEventData</b> contains a list of parameters that is encoded in BER-TLV fields. This event is mapped to EVT_TRANSACTION.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Nfcsedev.h</dt>
</dl>
</td>
</tr>
</table>