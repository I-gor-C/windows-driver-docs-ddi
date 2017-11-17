---
UID: NN.dbgeng.IDebugClient6
title: IDebugClient6
author: windows-driver-content
description: This interface supports event context callbacks.
old-location: debugger\idebugclient6.htm
ms.assetid: 9F8DFF33-DE07-4061-9A9E-3C8172F75EB5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: interface
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient6
req.alt-loc: dbgeng.h
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
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
req.iface: IDebugSystemObjects4
---

# IDebugClient6 interface



## -description
<p>This interface supports event context callbacks.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugClient6</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugClient6</b> also has these types of members:</p>

<p>The <b>IDebugClient6</b> interface has these methods.</p>

<p>Registers an event callbacks object with this client. </p>

<p> </p>

## -members
<p>The <b>IDebugClient6</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/246573DB-5FEB-4068-8DB8-950F5EDFD1A9">SetEventContextCallbacks</a>
</td>
<td align="left" width="63%">
<p>Registers an event callbacks object with this client. </p>
</td>
</tr>
</table><p>Registers an event callbacks object with this client. </p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>