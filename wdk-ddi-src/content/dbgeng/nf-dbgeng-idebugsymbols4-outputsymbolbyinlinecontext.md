---
UID: NF.dbgeng.IDebugSymbols4.OutputSymbolByInlineContext
title: IDebugSymbols4::OutputSymbolByInlineContext
author: windows-driver-content
description: Specifies an output symbol by using an inline context.
old-location: debugger\idebugsymbols4_outputsymbolbyinlinecontext.htm
old-project: debugger
ms.assetid: 55BA214C-7161-4B2C-8107-11EE22D63CD6
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols4, OutputSymbolByInlineContext, IDebugSymbols4::OutputSymbolByInlineContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols4.OutputSymbolByInlineContext
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
req.iface: IDebugSymbols4
---

# IDebugSymbols4::OutputSymbolByInlineContext method



## -description
<p>Specifies an output symbol by using an inline context.</p>


## -syntax

````
HRESULT OutputSymbolByInlineContext(
  [in] ULONG   OutputControl,
  [in] ULONG   Flags,
  [in] ULONG64 Offset,
  [in] ULONG   InlineContext
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>An output control.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A bit-set that contains options that affect the behavior of this method. </p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>An offset.</p>
</dd>

### -param <i>InlineContext</i> [in]

<dd>
<p>An inline context.</p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

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

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols4.md">IDebugSymbols4</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols4::OutputSymbolByInlineContext method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
