---
UID: NF.dbgeng.IDebugSymbols4.GetLineByInlineContextWide
title: IDebugSymbols4::GetLineByInlineContextWide
author: windows-driver-content
description: Gets a line by inline context.
old-location: debugger\idebugsymbols4_getlinebyinlinecontextwide.htm
old-project: debugger
ms.assetid: 5DCD8407-1C30-475F-9741-62DB9C86297B
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols4, GetLineByInlineContextWide, IDebugSymbols4::GetLineByInlineContextWide
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
req.alt-api: IDebugSymbols4.GetLineByInlineContextWide
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

# IDebugSymbols4::GetLineByInlineContextWide method



## -description
<p>Gets a line by inline context.</p>


## -syntax

````
HRESULT GetLineByInlineContextWide(
  [in]            ULONG64                            Offset,
  [in]            ULONG                              InlineContext,
  [out, optional] PULONG                             Line,
  [out]           _writes_opt_(FileBufferSize) PWSTR FileBuffer,
  [in]            ULONG                              FileBufferSize,
  [out, optional] PULONG                             FileSize,
  [out, optional] PULONG64                           Displacement
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>An offset for the line.</p>
</dd>

### -param <i>InlineContext</i> [in]

<dd>
<p>The inline context. </p>
</dd>

### -param <i>Line</i> [out, optional]

<dd>
<p>A pointer to the returned line.</p>
</dd>

### -param <i>FileBuffer</i> [out]

<dd>
<p>A pointer to a buffer for a Unicode character string.</p>
</dd>

### -param <i>FileBufferSize</i> [in]

<dd>
<p>The size of the file buffer.</p>
</dd>

### -param <i>FileSize</i> [out, optional]

<dd>
<p>A pointer to the length of the file.</p>
</dd>

### -param <i>Displacement</i> [out, optional]

<dd>
<p>A pointer to the displacement value of the file.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols4::GetLineByInlineContextWide method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
