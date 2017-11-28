---
UID: NF.midatlax.RxMapMidToContext
title: RxMapMidToContext
author: windows-driver-content
description: RxMapMidToContext maps a Multiplex ID (MID) to its associated context in a MID_ATLAS structure.
old-location: ifsk\rxmapmidtocontext.htm
old-project: ifsk
ms.assetid: e0625c27-6de9-401f-a6bd-52697c4a57c0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxMapMidToContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: midatlax.h
req.include-header: Midatlax.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxMapMidToContext
req.alt-loc: midatlax.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# RxMapMidToContext function



## -description
<p><b>RxMapMidToContext</b> maps a Multiplex ID (MID) to its associated context in a MID_ATLAS structure. </p>


## -syntax

````
PVOID RxMapMidToContext(
   PRX_MID_ATLAS pMidAtlas,
   USHORT        Mid
);
````


## -parameters
<dl>

### -param <i>pMidAtlas</i> 

<dd>
<p>A pointer to the MID_ATLAS structure.</p>
</dd>

### -param <i>Mid</i> 

<dd>
<p>The multiplex ID to be mapped.</p>
</dd>
</dl>

## -returns
<p><b>RxMapMidToContext</b> returns a pointer to the associated context, or <b>NULL</b> if none exists.</p>

## -remarks
<p>RDBSS defines a Multiplex ID (MID), a 16-bit value, that can be used by both the network client (mini-redirector) and the server to distinguish between the concurrently active requests on any connection. A MID is a component of a MID_ATLAS data structure allocated by calling <b>RxCreateMidAtlas</b>. A MID_MAP data structure is allocated and used for mapping MIDs to RX_CONTEXT data structures. </p>

<p>RDBSS defines a Multiplex ID (MID), a 16-bit value, that can be used by both the network client (mini-redirector) and the server to distinguish between the concurrently active requests on any connection. A MID is a component of a MID_ATLAS data structure allocated by calling <b>RxCreateMidAtlas</b>. A MID_MAP data structure is allocated and used for mapping MIDs to RX_CONTEXT data structures. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Midatlax.h (include Midatlax.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553388">RxAssociateContextWithMid</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554352">RxCreateMidAtlas</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554395">RxDestroyMidAtlas</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554541">RxMapAndDissociateMidFromContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554686">RxReassociateMid</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxMapMidToContext function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
