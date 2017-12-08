---
UID: NF.ks.KsGateAddOffInputToOr
title: KsGateAddOffInputToOr function
author: windows-driver-content
description: The KsGateAddOffInputToOr function adds a new input in the OFF state to a given OR gate.
old-location: stream\ksgateaddoffinputtoor.htm
old-project: stream
ms.assetid: 93d5076c-d8db-4b4b-b390-5f9072d2ae63
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KsGateAddOffInputToOr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGateAddOffInputToOr
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
req.irql: Any level
---

# KsGateAddOffInputToOr function



## -description
The<b> KsGateAddOffInputToOr</b> function adds a new input in the OFF state to a given OR gate. 


## -syntax

````
void __inline KsGateAddOffInputToOr(
  _In_ PKSGATE OrGate
);
````


## -parameters

### -param OrGate [in]

A pointer to a <a href="stream.ksgate">KSGATE</a> structure representing the OR gate to which to add a new OFF input.

## -returns
None

## -remarks
This function should only be used on gates that were specifically created as OR gates; AVStream does not verify that the given gate is an OR gate.

This call is an empty function. It should be used for code readability and clarity. 

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
Any level
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="stream.ksgateremoveoffinputfromor">KsGateRemoveOffInputFromOr</a>
</dt>
<dt>
<a href="stream.ksgateaddoninputtoor">KsGateAddOnInputToOr</a>
</dt>
<dt>
<a href="stream.ksgateremoveoninputfromor">KsGateRemoveOnInputFromOr</a>
</dt>
<dt>
<a href="stream.ksgateturninputon">KsGateTurnInputOn</a>
</dt>
<dt>
<a href="stream.ksgateturninputoff">KsGateTurnInputOff</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGateAddOffInputToOr function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
