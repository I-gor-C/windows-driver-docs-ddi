---
UID: NF.dbgeng.IDebugSymbols3.GetSourceEntryOffsetRegions
title: IDebugSymbols3::GetSourceEntryOffsetRegions
author: windows-driver-content
description: Returns all memory regions known to be associated with a source entry.
old-location: debugger\idebugsymbols3_getsourceentryoffsetregions.htm
old-project: debugger
ms.assetid: A39FF088-1AA3-4E2F-8EF6-AD7F79FBBC92
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols3, GetSourceEntryOffsetRegions, IDebugSymbols3::GetSourceEntryOffsetRegions
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
req.alt-api: IDebugSymbols3.GetSourceEntryOffsetRegions
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

# IDebugSymbols3::GetSourceEntryOffsetRegions method



## -description
<p> Returns all memory regions known to be associated
    with a source entry.  </p>


## -syntax

````
HRESULT GetSourceEntryOffsetRegions(
  [in]            PDEBUG_SYMBOL_SOURCE_ENTRY                      Entry,
  [in]            ULONG                                           Flags,
  [out]           _writes_opt_(RegionsCount) PDEBUG_OFFSET_REGION Regions,
  [in]            ULONG                                           RegionsCount,
  [out, optional] PULONG                                          RegionsAvail
);
````


## -parameters
<dl>

### -param <i>Entry</i> [in]

<dd>
<p>An entry as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541680">DEBUG_SYMBOL_SOURCE_ENTRY</a> structure. </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A bit-set that contains options that affect the behavior of this method. </p>
</dd>

### -param <i>Regions</i> [out]

<dd>
<p>The memory regions associated with the source entry. </p>
</dd>

### -param <i>RegionsCount</i> [in]

<dd>
<p>The number of regions associated with the entry.</p>
</dd>

### -param <i>RegionsAvail</i> [out, optional]

<dd>
<p>A pointer to the number of regions available to the entry.</p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

<p>This function returns all known memory regions that associated
    with a specified source entry.  Simple symbols have a single region that starts from their base. More complicated regions, such as functions that have multiple code areas, can have an arbitrarily
    large number of regions.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541680">DEBUG_SYMBOL_SOURCE_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.idebugsymbols3_getsymbolentryoffsetregions">IDebugSymbols3::GetSymbolEntryOffsetRegions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetSourceEntryOffsetRegions method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
