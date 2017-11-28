---
UID: NF.dbgeng.IDebugSymbols3.GetSymbolEntriesByOffset
title: IDebugSymbols3::GetSymbolEntriesByOffset
author: windows-driver-content
description: The GetSymbolEntriesByOffset method returns the symbols which are located at a specified address.
old-location: debugger\getsymbolentriesbyoffset.htm
old-project: debugger
ms.assetid: 93df59dc-adae-49b7-acf4-1cfdd142fd96
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols3, GetSymbolEntriesByOffset, IDebugSymbols3::GetSymbolEntriesByOffset
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols3.GetSymbolEntriesByOffset
req.alt-loc: dbgeng.h
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

# IDebugSymbols3::GetSymbolEntriesByOffset method



## -description
<p>The <b>GetSymbolEntriesByOffset</b> method returns the <a href="debugger.symbols#symbols#symbols">symbols</a> which are located at a specified address.</p>


## -syntax

````
HRESULT GetSymbolEntriesByOffset(
  [in]            ULONG64              Offset,
  [in]            ULONG                Flags,
  [out, optional] PDEBUG_MODULE_AND_ID Ids,
  [out, optional] PULONG64             Displacements,
  [in]            ULONG                IdsCount,
  [out, optional] PULONG               Entries
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies a location in the process's memory address space within the desired symbol's range.  Not all symbols have a known range, so, for best results, use the base address of the symbol.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Set to zero.</p>
</dd>

### -param <i>Ids</i> [out, optional]

<dd>
<p>Receives the symbols.  This is an array of <i>IdsCount</i> entries of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541511">DEBUG_MODULE_AND_ID</a>.  If <i>Ids</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>Displacements</i> [out, optional]

<dd>
<p>Receives the differences between the base addresses of the found symbols and the given address according to the symbol's range.  </p>
</dd>

### -param <i>IdsCount</i> [in]

<dd>
<p>Specifies the number of entries that the arrays <i>Ids</i> and <i>Displacements</i> can hold.</p>
</dd>

### -param <i>Entries</i> [out, optional]

<dd>
<p>Receives the number of symbols located at <i>Offset</i>.  If <i>Entries</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

<p>For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548458">GetSymbolEntriesByName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetSymbolEntriesByOffset method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
