---
UID: NF.dbgeng.IDebugSymbols3.OutputSymbolByOffset
title: IDebugSymbols3::OutputSymbolByOffset
author: windows-driver-content
description: The OutputSymbolByOffset method looks up a symbol by address and prints the symbol name and other symbol information to the debugger console.
old-location: debugger\outputsymbolbyoffset.htm
old-project: debugger
ms.assetid: a9b3ac31-2001-45cc-a917-de687419b561
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols3, OutputSymbolByOffset, IDebugSymbols3::OutputSymbolByOffset
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
req.alt-api: IDebugSymbols3.OutputSymbolByOffset
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

# IDebugSymbols3::OutputSymbolByOffset method



## -description
<p>The <b>OutputSymbolByOffset</b> method looks up a symbol by address and prints the symbol name and other symbol information to the debugger console.</p>


## -syntax

````
HRESULT OutputSymbolByOffset(
  [in] ULONG   OutputControl,
  [in] ULONG   Flags,
  [in] ULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>Specifies where to send the output. For possible values, see <a href="debugger.debug_outctl_xxx">DEBUG_OUTCTL_XXX</a>.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Specifies the flags used to determine what information is printed with the symbol.</p>
<p>The following flags can be present:</p>
<table>
<tr>
<th>Bit-flag</th>
<th>Effect</th>
</tr>
<tr>
<td>
<p>DEBUG_OUTSYM_FORCE_OFFSET</p>
</td>
<td>
<p>Include the location of the symbol.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_OUTSYM_SOURCE_LINE</p>
</td>
<td>
<p>Include the file name and line number of the source file where the symbol is defined.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_OUTSYM_ALLOW_DISPLACEMENT</p>
</td>
<td>
<p>Do not require an exact match for the symbols location.</p>
<p>This allows the <i>Offset</i> parameter to specify any address within the symbol's memory allocation - not just the base address.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the process's virtual address space of the symbol to be printed.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>No symbol was found at the specified location.</p>

<p> </p>

## -remarks
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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.getnamebyoffset">GetNameByOffset</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::OutputSymbolByOffset method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
