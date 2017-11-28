---
UID: NF.wpprecorder.WppRecorderLinkCounters
title: WppRecorderLinkCounters
author: windows-driver-content
description: The WppRecorderLinkCounters.
old-location: devtest\wpprecorderlinkcounters.htm
old-project: devtest
ms.assetid: D8FF1E87-EB3E-491E-9649-076376C272B3
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: WppRecorderLinkCounters
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wpprecorder.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WppRecorderLinkCounters
req.alt-loc: wpprecorder.h
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
req.product: Windows 10 or later.
---

# WppRecorderLinkCounters function



## -description
<p>The <b>WppRecorderLinkCounters</b> method  uses a sequence number to merge logs captured in different buffers by a driver.</p>


## -syntax

````
NTSTATUS WppRecorderLinkCounters(
  _In_ WPP_RECORDER_COUNTER CounterOwner
);
````


## -parameters
<dl>

### -param <i>CounterOwner</i> [in]

<dd>
<p>ID of the counter whose current value is to be read.</p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS if the operation succeeds. Otherwise, one of appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> values</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wpprecorder.h</dt>
</dl>
</td>
</tr>
</table>