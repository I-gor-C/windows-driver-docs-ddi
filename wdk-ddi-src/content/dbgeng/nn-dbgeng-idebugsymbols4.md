---
UID: NN.dbgeng.IDebugSymbols4
title: IDebugSymbols4
author: windows-driver-content
description: This interface supports determination of the symbol of an inline frame.
old-location: debugger\idebugsymbols4.htm
old-project: debugger
ms.assetid: BE2734B5-1E67-4E38-B4DF-0C353BFB1F0B
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
req.alt-api: IDebugSymbols4
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

# IDebugSymbols4 interface



## -description
<p>This interface supports determination of the symbol of an inline frame.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSymbols4</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugSymbols4</b> also has these types of members:</p>

<p>The <b>IDebugSymbols4</b> interface has these methods.</p>

<p>Gets a line by inline context.</p>

<p>Gets a line by inline context.</p>

<p>Gets a name by inline context.</p>

<p>Gets a name by inline context.</p>

<p>Gets the scope as an extended frame structure. </p>

<p>Specifies an output symbol by using an inline context.</p>

<p>Sets the scope as an extended frame structure. </p>

<p> </p>

## -members
<p>The <b>IDebugSymbols4</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_getlinebyinlinecontext">GetLineByInlineContext</a>
</td>
<td align="left" width="63%">
<p>Gets a line by inline context.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_getlinebyinlinecontextwide">GetLineByInlineContextWide</a>
</td>
<td align="left" width="63%">
<p>Gets a line by inline context.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_getnamebyinlinecontext">GetNameByInlineContext</a>
</td>
<td align="left" width="63%">
<p>Gets a name by inline context.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_getnamebyinlinecontextwide">GetNameByInlineContextWide</a>
</td>
<td align="left" width="63%">
<p>Gets a name by inline context.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_getscopeex">GetScopeEx</a>
</td>
<td align="left" width="63%">
<p>Gets the scope as an extended frame structure. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_outputsymbolbyinlinecontext">OutputSymbolByInlineContext</a>
</td>
<td align="left" width="63%">
<p>Specifies an output symbol by using an inline context.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_setscopeex">SetScopeEx</a>
</td>
<td align="left" width="63%">
<p>Sets the scope as an extended frame structure. </p>
</td>
</tr>
</table><p>Gets a line by inline context.</p>

<p>Gets a line by inline context.</p>

<p>Gets a name by inline context.</p>

<p>Gets a name by inline context.</p>

<p>Gets the scope as an extended frame structure. </p>

<p>Specifies an output symbol by using an inline context.</p>

<p>Sets the scope as an extended frame structure. </p>

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