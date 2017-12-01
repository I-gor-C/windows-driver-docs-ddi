---
UID: NN.dbgeng.IDebugSymbols5
title: IDebugSymbols5
author: windows-driver-content
description: This interface supports using index values for the current frame.
old-location: debugger\idebugsymbols5.htm
old-project: debugger
ms.assetid: 0D239C0E-96C8-49F9-BDFD-182F3F7C3976
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
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
req.alt-api: IDebugSymbols5
req.alt-loc: Dbgeng.h
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
req.iface: IDebugSystemObjects4
---

# IDebugSymbols5 interface



## -description
<p>This interface supports using index values for the current frame. </p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSymbols5</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugSymbols5</b> also has these types of members:</p>

<p>The <b>IDebugSymbols5</b> interface has these methods.</p>

<p>Gets the index of the current frame.</p>

<p>Sets the current frame by using an index.</p>

<p> </p>

## -members
<p>The <b>IDebugSymbols5</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols5_getcurrentscopeframeindexex">GetCurrentScopeFrameIndexEx</a>
</td>
<td align="left" width="63%">
<p>Gets the index of the current frame.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols5_setscopeframebyindexex">SetScopeFrameByIndexEx</a>
</td>
<td align="left" width="63%">
<p>Sets the current frame by using an index.</p>
</td>
</tr>
</table><p>Gets the index of the current frame.</p>

<p>Sets the current frame by using an index.</p>

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