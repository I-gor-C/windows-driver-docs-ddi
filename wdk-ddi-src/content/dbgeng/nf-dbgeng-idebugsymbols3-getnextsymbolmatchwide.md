---
UID: NF.dbgeng.IDebugSymbols3.GetNextSymbolMatchWide
title: IDebugSymbols3::GetNextSymbolMatchWide
author: windows-driver-content
description: The GetNextSymbolMatchWide method returns the next symbol found in a symbol search.
old-location: debugger\getnextsymbolmatchwide.htm
old-project: debugger
ms.assetid: 0400ff8c-a6d5-4fbf-b2fb-eb9fd7aabd7e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols3, GetNextSymbolMatchWide, IDebugSymbols3::GetNextSymbolMatchWide
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
req.alt-api: IDebugSymbols3.GetNextSymbolMatchWide
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

# IDebugSymbols3::GetNextSymbolMatchWide method



## -description
<p>The <b>GetNextSymbolMatchWide</b>  method returns the next symbol found in a symbol search.</p>


## -syntax

````
HRESULT GetNextSymbolMatchWide(
  [in]            ULONG64  Handle,
  [out, optional] PWSTR    Buffer,
  [in]            ULONG    BufferSize,
  [out, optional] PULONG   MatchSize,
  [out, optional] PULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Specifies the handle returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff558815">StartSymbolMatch</a> when the search was initialized.</p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Receives the name of the symbol.  If <i>Buffer</i> is <b>NULL</b>, the same symbol will be returned again next time one of these methods are called (with the same handle); this can be used to determine the size of the name of the symbol.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in characters of the buffer.</p>
</dd>

### -param <i>MatchSize</i> [out, optional]

<dd>
<p>Receives the size in characters of the name of the symbol.  If <i>MatchSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>Offset</i> [out, optional]

<dd>
<p>Receives the location in the target's virtual address space of the symbol.  If <i>Offset</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The size of the buffer was too small for the name of the symbol, or <i>Buffer</i> was <b>NULL</b>.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>No more symbols were found matching the pattern.</p>

<p> </p>

## -remarks
<p>The search must first be initialized by <a href="https://msdn.microsoft.com/library/windows/hardware/ff558815">StartSymbolMatch</a>.  Once all the desired symbols have been found, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543008">EndSymbolMatch</a> can be used to release the resources the engine holds for the search.</p>

<p>For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

<p>The search must first be initialized by <a href="https://msdn.microsoft.com/library/windows/hardware/ff558815">StartSymbolMatch</a>.  Once all the desired symbols have been found, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543008">EndSymbolMatch</a> can be used to release the resources the engine holds for the search.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543008">EndSymbolMatch</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558815">StartSymbolMatch</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetNextSymbolMatchWide method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
