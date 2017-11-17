---
UID: NN.dbgeng.IDebugSymbols4
title: IDebugSymbols4
author: windows-driver-content
description: This interface supports determination of the symbol of an inline frame.
old-location: debugger\idebugsymbols4.htm
ms.assetid: BE2734B5-1E67-4E38-B4DF-0C353BFB1F0B
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
ms.keywords: IDebugSystemObjects4, SetImplicitThreadDataOffset, IDebugSystemObjects4::SetImplicitThreadDataOffset
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
<a href="https://msdn.microsoft.com/AFDB4DB4-3C63-44A0-88D7-C8047ECB2261">GetLineByInlineContext</a>
</td>
<td align="left" width="63%">
<p>Gets a line by inline context.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/5DCD8407-1C30-475F-9741-62DB9C86297B">GetLineByInlineContextWide</a>
</td>
<td align="left" width="63%">
<p>Gets a line by inline context.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/C87E70ED-FCB0-47B6-B6A3-A8EBC8E84058">GetNameByInlineContext</a>
</td>
<td align="left" width="63%">
<p>Gets a name by inline context.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/D77F5755-75B0-48E6-BC5C-565022F884E1">GetNameByInlineContextWide</a>
</td>
<td align="left" width="63%">
<p>Gets a name by inline context.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/B91EF786-51F7-406E-BCC2-C917E6881886">GetScopeEx</a>
</td>
<td align="left" width="63%">
<p>Gets the scope as an extended frame structure. </p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/55BA214C-7161-4B2C-8107-11EE22D63CD6">OutputSymbolByInlineContext</a>
</td>
<td align="left" width="63%">
<p>Specifies an output symbol by using an inline context.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/22844EBB-9BE7-47C0-BE1F-075473430F11">SetScopeEx</a>
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