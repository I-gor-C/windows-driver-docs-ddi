---
UID: NS.61883._FCP_SEND_RESPONSE
title: FCP_SEND_RESPONSE
author: windows-driver-content
description: This structure is used for a send response.
old-location: ieee\fcp_send_response.htm
ms.assetid: 65C76CA1-F7F2-4DFD-B928-0595A137BF28
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 61883.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FCP_SEND_RESPONSE
req.alt-loc: 61883.h
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
ms.keywords: FCP_SEND_RESPONSE, FCP_SEND_RESPONSE, *PFCP_SEND_RESPONSE
---

# FCP_SEND_RESPONSE structure



## -description
<p>This structure is used for a send response.</p>


## -syntax

````
typedef struct _FCP_SEND_RESPONSE {
  NODE_ADDRESS NodeAddress;
  ULONG        Length;
  PFCP_FRAME   Frame;
} FCP_SEND_RESPONSE, *PFCP_SEND_RESPONSE;
````


## -struct-fields
<dl>

### -field <b><b>NodeAddress</b></b>

<dd>
<p>If the protocol driver is being used to control a virtual device, <b>NodeAddress</b> must contain the node address of the device that sent the FCP request obtained with <a href="https://msdn.microsoft.com/library/windows/hardware/ff536974">Av61883_GetFcpRequest</a> so the 1394 bus driver can route the response to the correct device. </p>
<p>If the protocol driver is being used to control a physical device, <b>NodeAddress</b> is not used.</p>
</dd>

### -field <b><b>Length</b></b>

<dd>
<p>The length of the frame payload in bytes, including the FCP header.</p>
</dd>

### -field <b><b>Frame</b></b>

<dd>
<p>Pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff537113">FCP_FRAME</a> structure that contains the FCP response to send to the device.</p>
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
<dt>61883.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537008">AV_61883_REQUEST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20FCP_SEND_RESPONSE structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
