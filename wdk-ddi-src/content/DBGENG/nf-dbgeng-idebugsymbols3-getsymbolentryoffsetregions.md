---
UID: NF.dbgeng.IDebugSymbols3.GetSymbolEntryOffsetRegions
title: IDebugSymbols3::GetSymbolEntryOffsetRegions
author: windows-driver-content
description: Returns all the memory regions known to be associated with a symbol.
old-location: debugger\idebugsymbols3_getsymbolentryoffsetregions.htm
ms.assetid: 986774F6-5256-4703-990A-EAB4AB09AF55
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols3.GetSymbolEntryOffsetRegions
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
ms.keywords: IDebugSymbols3, GetSymbolEntryOffsetRegions, IDebugSymbols3::GetSymbolEntryOffsetRegions
req.iface: IDebugSymbols3
---

# IDebugSymbols3::GetSymbolEntryOffsetRegions method



## -description
<p>Returns all the memory regions known to be associated
    with a symbol.  </p>


## -syntax

````
HRESULT GetSymbolEntryOffsetRegions(
  [in]            PDEBUG_MODULE_AND_ID                            Id,
  [in]            ULONG                                           Flags,
  [out]           _writes_opt_(RegionsCount) PDEBUG_OFFSET_REGION Regions,
  [in]            ULONG                                           RegionsCount,
  [out, optional] PULONG                                          RegionsAvail
);
````


## -parameters
<dl>

### -param <i>Id</i> [in]

<dd>
<p>The ID of a module as a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541511">DEBUG_MODULE_AND_ID</a> structure. </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A bit-set that contains options that affect the behavior of this method. </p>
</dd>

### -param <i>Regions</i> [out]

<dd>
<p>The memory regions associated with the symbol. </p>
</dd>

### -param <i>RegionsCount</i> [in]

<dd>
<p>The number of regions associated with the symbol.</p>
</dd>

### -param <i>RegionsAvail</i> [out, optional]

<dd>
<p>A pointer to the number of regions available to the symbol. </p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

<p>This function returns all known memory regions that associated
    with a specified symbol.  Simple symbols have a single region that starts from their base. More complicated regions, such as functions that have multiple code areas, can have an arbitrarily
    large number of regions.</p>

<p>The quality of information returned is highly
    dependent on the symbolic information available.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541511">DEBUG_MODULE_AND_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/A39FF088-1AA3-4E2F-8EF6-AD7F79FBBC92">IDebugSymbols3::GetSourceEntryOffsetRegions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetSymbolEntryOffsetRegions method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
