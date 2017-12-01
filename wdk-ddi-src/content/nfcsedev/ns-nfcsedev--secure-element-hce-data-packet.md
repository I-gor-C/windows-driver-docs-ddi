---
UID: NS.nfcsedev._SECURE_ELEMENT_HCE_DATA_PACKET
title: SECURE_ELEMENT_HCE_DATA_PACKET
author: windows-driver-content
description: SECURE_ELEMENT_HCE_DATA_PACKET is an input buffer to IOCTL_NFCSE_HCE_REMOTE_SEND and output buffer for IOCTL_NFCSE_HCE_REMOTE_RECV.
old-location: nfpdrivers\_secure_element_hce_data_packet.htm
old-project: nfpdrivers
ms.assetid: A287CBC7-BB22-487E-8E06-47702DF29DCE
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: SECURE_ELEMENT_HCE_DATA_PACKET, SECURE_ELEMENT_HCE_DATA_PACKET, *PSECURE_ELEMENT_HCE_DATA_PACKET
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
req.alt-api: SECURE_ELEMENT_HCE_DATA_PACKET
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

# SECURE_ELEMENT_HCE_DATA_PACKET structure



## -description
<p><b>SECURE_ELEMENT_HCE_DATA_PACKET</b> is an input buffer to <a href="..\nfcsedev\ni-nfcsedev-ioctl-nfcse-hce-remote-send.md">IOCTL_NFCSE_HCE_REMOTE_SEND</a> and output buffer for <a href="..\nfcsedev\ni-nfcsedev-ioctl-nfcse-hce-remote-recv.md">IOCTL_NFCSE_HCE_REMOTE_RECV</a>.</p>


## -syntax

````
typedef struct _SECURE_ELEMENT_HCE_DATA_PACKET {
  USHORT                             bConnectionId;
  USHORT                             cbPayload;
  _Field_size_bytes_(cbPayload) BYTE pbPayload[ANYSIZE_ARRAY];
} SECURE_ELEMENT_HCE_DATA_PACKET, *PSECURE_ELEMENT_HCE_DATA_PACKET;
````


## -struct-fields
<dl>

### -field <b>bConnectionId</b>

<dd>
<p>The ID of the connection established between the device and the smart card reader, on which to send and receive the HCE packet. This ID is also received from <a href="..\nfcsedev\ni-nfcsedev-ioctl-nfcse-get-next-event.md">IOCTL_NFCSE_GET_NEXT_EVENT</a> when the event type (<a href="..\nfcsedev\ne-nfcsedev--secure-element-event-type.md">SECURE_ELEMENT_EVENT_TYPE</a>) is <b>HceActivated</b> or <b>HceDeactivated</b>. Then the <b>pbEventData</b> field of the returned <a href="..\nfcsedev\ns-nfcsedev--secure-element-event-info.md">SECURE_ELEMENT_EVENT_INFO</a> structure is a <a href="..\nfcsedev\ns-nfcsedev--secure-element-hce-activation-payload.md">SECURE_ELEMENT_HCE_ACTIVATION_PAYLOAD</a> structure, which contains a <b>bConnectionId</b> member.</p>
</dd>

### -field <b>cbPayload</b>

<dd>
<p>Length of ISO 7816-4 APDU buffer.</p>
</dd>

### -field <b>pbPayload[ANYSIZE_ARRAY]</b>

<dd>
<p>Buffer holding ISO 7816-4 APDU.</p>
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