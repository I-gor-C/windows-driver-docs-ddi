---
UID: NF.dbgeng.IDebugSymbols3.GetSourceEntryString
title: IDebugSymbols3::GetSourceEntryString
author: windows-driver-content
description: Queries symbol information and returns locations in the target's memory.
old-location: debugger\idebugsymbols3_getsourceentrystring.htm
old-project: debugger
ms.assetid: 4742F6DD-F7D6-4EF4-877B-C02630018C8E
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols3, GetSourceEntryString, IDebugSymbols3::GetSourceEntryString
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
req.alt-api: IDebugSymbols3.GetSourceEntryString
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
req.iface: IDebugSymbols3
---

# IDebugSymbols3::GetSourceEntryString method



## -description
<p>Queries symbol information and returns locations in the target's memory.</p>


## -syntax

````
HRESULT GetSourceEntryString(
  [in]            PDEBUG_SYMBOL_SOURCE_ENTRY    Entry,
  [in]            ULONG                         Which,
  [out]           _writes_opt_(BufferSize) PSTR Buffer,
  [in]            ULONG                         BufferSize,
  [out, optional] PULONG                        StringSize
);
````


## -parameters
<dl>

### -param <i>Entry</i> [in]

<dd>
<p>An entry as a <a href="..\dbgeng\ns-dbgeng--debug-symbol-source-entry.md">DEBUG_SYMBOL_SOURCE_ENTRY</a> structure. </p>
</dd>

### -param <i>Which</i> [in]

<dd>
<p>A value that determines which types to return.</p>
</dd>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to a string buffer for the results.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>The size of the buffer.</p>
</dd>

### -param <i>StringSize</i> [out, optional]

<dd>
<p>Pointer to the size of the string. </p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

<p>    This method can return multiple results for a source lookup. This allows for all possible results to be returned.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetSourceEntryString method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
