---
UID: NS.ks.PKSE_NODE
title: PKSE_NODE
author: windows-driver-content
description: The KSE_NODE structure specifies an event request on a specific node.
old-location: stream\kse_node.htm
ms.assetid: 89446165-cdc3-414d-bcce-f2c978d94547
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSE_NODE
req.alt-loc: ks.h
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
ms.keywords: PKSE_NODE, KSE_NODE, *PKSE_NODE
req.iface: 
---

# PKSE_NODE structure



## -description
<p>The KSE_NODE structure specifies an event request on a specific node.</p>


## -syntax

````
typedef struct {
  KSEVENT Event;
  ULONG   NodeId;
  ULONG   Reserved;
} KSE_NODE, *PKSE_NODE;
````


## -struct-fields
<dl>

### -field <b>Event</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff561744">KSEVENT</a> that identifies the requested event.</p>
</dd>

### -field <b>NodeId</b>

<dd>
<p>Specifies the node ID.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use. Should be set to zero.</p>
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
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566720">KSP_NODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSE_NODE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
