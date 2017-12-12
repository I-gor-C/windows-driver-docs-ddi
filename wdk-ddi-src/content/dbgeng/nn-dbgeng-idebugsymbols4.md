---
UID: NN.dbgeng.IDebugSymbols4
title: IDebugSymbols4
author: windows-driver-content
description: This interface supports determination of the symbol of an inline frame.
old-location: debugger\idebugsymbols4.htm
old-project: debugger
ms.assetid: BE2734B5-1E67-4E38-B4DF-0C353BFB1F0B
ms.author: windowsdriverdev
ms.date: 12/8/2017
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
---

# IDebugSymbols4 interface



## -description
This interface supports determination of the symbol of an inline frame.



## -inheritance
The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IDebugSymbols4</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IDebugSymbols4</b> also has these types of members:

The <b>IDebugSymbols4</b> interface has these methods.

Gets a line by inline context.

Gets a line by inline context.

Gets a name by inline context.

Gets a name by inline context.

Gets the scope as an extended frame structure. 

Specifies an output symbol by using an inline context.

Sets the scope as an extended frame structure. 

 


## -members
The <b>IDebugSymbols4</b> interface has these methods.
<table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_getlinebyinlinecontext">GetLineByInlineContext</a>
</td>
<td align="left" width="63%">
Gets a line by inline context.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_getlinebyinlinecontextwide">GetLineByInlineContextWide</a>
</td>
<td align="left" width="63%">
Gets a line by inline context.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_getnamebyinlinecontext">GetNameByInlineContext</a>
</td>
<td align="left" width="63%">
Gets a name by inline context.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_getnamebyinlinecontextwide">GetNameByInlineContextWide</a>
</td>
<td align="left" width="63%">
Gets a name by inline context.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_getscopeex">GetScopeEx</a>
</td>
<td align="left" width="63%">
Gets the scope as an extended frame structure. 

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_outputsymbolbyinlinecontext">OutputSymbolByInlineContext</a>
</td>
<td align="left" width="63%">
Specifies an output symbol by using an inline context.

</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="debugger.idebugsymbols4_setscopeex">SetScopeEx</a>
</td>
<td align="left" width="63%">
Sets the scope as an extended frame structure. 

</td>
</tr>
</table>Gets a line by inline context.

Gets a line by inline context.

Gets a name by inline context.

Gets a name by inline context.

Gets the scope as an extended frame structure. 

Specifies an output symbol by using an inline context.

Sets the scope as an extended frame structure. 

 


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