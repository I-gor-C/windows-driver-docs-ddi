---
UID: NF.dbgeng.IDebugSymbols3.GetSourceEntriesByLine
title: IDebugSymbols3::GetSourceEntriesByLine
author: windows-driver-content
description: The GetSourceEntriesByLine method queries symbol information and returns locations in the target's memory that correspond to lines in a source file.
old-location: debugger\getsourceentriesbyline.htm
ms.assetid: 02ab63fe-0c59-480c-a333-a9b14d83ad68
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugSymbols3.GetSourceEntriesByLine
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
ms.keywords: IDebugSymbols3, GetSourceEntriesByLine, IDebugSymbols3::GetSourceEntriesByLine
req.iface: IDebugSymbols3
---

# IDebugSymbols3::GetSourceEntriesByLine method



## -description
<p>The <b>GetSourceEntriesByLine</b>  method queries symbol information and returns locations in the target's memory that correspond to lines in a source file.</p>


## -syntax

````
HRESULT GetSourceEntriesByLine(
  [in]            ULONG                      Line,
  [in]            PCSTR                      File,
  [in]            ULONG                      Flags,
  [out, optional] PDEBUG_SYMBOL_SOURCE_ENTRY Entries,
  [in]            ULONG                      EntriesCount,
  [out, optional] PULONG                     EntriesAvailable
);
````


## -parameters
<dl>

### -param <i>Line</i> [in]

<dd>
<p>Specifies the line in the source file for which to query.  The number for the first line is <b>1</b>.</p>
</dd>

### -param <i>File</i> [in]

<dd>
<p>Specifies the source file.  The symbols for each module in the target are queried for this file.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies bit flags that control the behavior of this method.  <i>Flags</i> can be any combination of values from the following table.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_GSEL_NO_SYMBOL_LOADS</p>
</td>
<td>
<p>The <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> will only search for the file among the modules whose symbols have already been loaded.  Symbols for the other modules will not be loaded.</p>
<p>If this option is not set, the debugger engine will load the symbols for all modules until it finds the file specified in <i>File</i>.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_GSEL_ALLOW_LOWER</p>
</td>
<td>
<p>Include all the lines in <i>File</i> before <i>Line</i> in the result.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_GSEL_ALLOW_HIGHER</p>
</td>
<td>
<p>Include all the lines in <i>File</i> after <i>Line</i> in the result.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_GSEL_NEAREST_ONLY</p>
</td>
<td>
<p>Only return at most one result.  If DEBUG_GSEL_ALLOW_LOWER or DEBUG_GSEL_ALLOW_HIGHER are set, the returned result will be for a line close to <i>Line</i> but cannot be <i>Line</i> if there is no symbol information for that line.</p>
</td>
</tr>
</table>
<p> </p>
<p>To use the default set of flags, set <i>Flags</i> to DEBUG_GSEL_DEFAULT.  This has all the flags in the previous table turned off.</p>
</dd>

### -param <i>Entries</i> [out, optional]

<dd>
<p>Receives the locations in the target's memory that correspond to the source lines queried for.  Each entry in this array is of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff541680">DEBUG_SYMBOL_SOURCE_ENTRY</a> and contains the source line number along with a location in the target's memory.</p>
</dd>

### -param <i>EntriesCount</i> [in]

<dd>
<p>Specifies the number of entries in the <i>Entries</i> array.</p>
</dd>

### -param <i>EntriesAvailable</i> [out, optional]

<dd>
<p>Receives the number of locations that match the query found in the target's memory.</p>
</dd>
</dl>

## -returns
<p>These methods can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  However, the <i>Entries</i> array was not large enough to hold all the results that matched the query and the extra results were discarded.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>The query yielded no results.  This includes the case where the symbol information was not available for the specified file.</p>

<p> </p>

## -remarks
<p>These methods can be used by debugger applications to fetch locations in the target's memory for setting breakpoints or matching source code with disassembled instructions.  For example, setting the flags DEBUG_GSEL_ALLOW_HIGHER and DEBUG_GSEL_NEAREST_ONLY will return the target's memory location for the first piece of code starting at the specified line.</p>

<p>For more information about source files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560141">Using Source Files</a>.</p>

<p>These methods can be used by debugger applications to fetch locations in the target's memory for setting breakpoints or matching source code with disassembled instructions.  For example, setting the flags DEBUG_GSEL_ALLOW_HIGHER and DEBUG_GSEL_NEAREST_ONLY will return the target's memory location for the first piece of code starting at the specified line.</p>

<p>For more information about source files, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560141">Using Source Files</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541680">DEBUG_SYMBOL_SOURCE_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548339">GetSourceFileLineOffsets</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetSourceEntriesByLine method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
