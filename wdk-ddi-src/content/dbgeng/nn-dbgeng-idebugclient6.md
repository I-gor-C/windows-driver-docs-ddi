---
UID: NN.dbgeng.IDebugClient6
title: IDebugClient6
author: windows-driver-content
description: This interface supports event context callbacks.
old-location: debugger\idebugclient6.htm
old-project: debugger
ms.assetid: 9F8DFF33-DE07-4061-9A9E-3C8172F75EB5
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: DebugCreateEx
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
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
---

# IDebugClient6 interface



## -description
This interface supports event context callbacks.


## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugClient6</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugClient6</b> also has these types of members:

The <b>IDebugClient6</b> interface has these methods.

Registers an event callbacks object with this client. 

 

## -members
The <b>IDebugClient6</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugclient6_seteventcontextcallbacks">SetEventContextCallbacks</a>
</td>
<td align="left" width="63%">
Registers an event callbacks object with this client. 
</td>
</tr>
</table>Registers an event callbacks object with this client. 

 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>