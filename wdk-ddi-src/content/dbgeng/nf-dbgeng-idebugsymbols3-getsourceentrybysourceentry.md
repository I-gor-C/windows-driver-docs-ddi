---
UID: NF.dbgeng.IDebugSymbols3.GetSourceEntryBySourceEntry
title: IDebugSymbols3::GetSourceEntryBySourceEntry
author: windows-driver-content
description: Allows navigation within the source entries.
old-location: debugger\idebugsymbols3_getsourceentrybysourceentry.htm
old-project: debugger
ms.assetid: 4ED5D2DC-8D31-458A-80F2-F681DC375769
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols3, GetSourceEntryBySourceEntry, IDebugSymbols3::GetSourceEntryBySourceEntry
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
req.alt-api: IDebugSymbols3.GetSourceEntryBySourceEntry
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

# IDebugSymbols3::GetSourceEntryBySourceEntry method



## -description
<p>Allows navigation within the
    source entries.</p>


## -syntax

````
HRESULT GetSourceEntryBySourceEntry(
  [in]  PDEBUG_SYMBOL_SOURCE_ENTRY FromEntry,
  [in]  ULONG                      Flags,
  [out] PDEBUG_SYMBOL_SOURCE_ENTRY ToEntry
);
````


## -parameters
<dl>

### -param <i>FromEntry</i> [in]

<dd>
<p>A pointer to a <a href="..\dbgeng\ns-dbgeng--debug-symbol-source-entry.md">DEBUG_SYMBOL_SOURCE_ENTRY</a> as the input entry.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A bit-set that contains options that affect the behavior of this method. </p>
</dd>

### -param <i>ToEntry</i> [out]

<dd>
<p>A pointer to a <a href="..\dbgeng\ns-dbgeng--debug-symbol-source-entry.md">DEBUG_SYMBOL_SOURCE_ENTRY</a> as the output entry.</p>
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
<a href="..\dbgeng\ns-dbgeng--debug-symbol-source-entry.md">DEBUG_SYMBOL_SOURCE_ENTRY</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetSourceEntryBySourceEntry method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
