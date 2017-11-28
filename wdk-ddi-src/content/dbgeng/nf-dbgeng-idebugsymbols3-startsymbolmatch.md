---
UID: NF.dbgeng.IDebugSymbols3.StartSymbolMatch
title: IDebugSymbols3::StartSymbolMatch
author: windows-driver-content
description: The StartSymbolMatch method initializes a search for symbols whose names match a given pattern.
old-location: debugger\startsymbolmatch.htm
old-project: debugger
ms.assetid: 465b13a7-59e0-47f8-9e33-82043a23f146
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols3, StartSymbolMatch, IDebugSymbols3::StartSymbolMatch
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
req.alt-api: IDebugSymbols.StartSymbolMatch,IDebugSymbols2.StartSymbolMatch,IDebugSymbols3.StartSymbolMatch
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

# IDebugSymbols3::StartSymbolMatch method



## -description
<p>The <b>StartSymbolMatch</b> method initializes a search for symbols whose names match a given pattern.</p>


## -syntax

````
HRESULT StartSymbolMatch(
  [in]  PCSTR    Pattern,
  [out] PULONG64 Handle
);
````


## -parameters
<dl>

### -param <i>Pattern</i> [in]

<dd>
<p>Specifies the pattern for which to search.  The search will return all symbols whose names match this pattern.  For details of the syntax of the pattern, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558843">Symbol Syntax and Symbol Matching</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff558819">String Wildcard Syntax</a>.</p>
</dd>

### -param <i>Handle</i> [out]

<dd>
<p>Receives the handle identifying the search.  This handle can be passed to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547856">GetNextSymbolMatch</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff543008">EndSymbolMatch</a>.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>The specified module was not found.</p>

<p> </p>

## -remarks
<p>This method initializes a symbol search.  The results of the search can be obtained by repeated calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547856">GetNextSymbolMatch</a>.  When all the desired results have been found, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff543008">EndSymbolMatch</a> to release resources the engine holds for the search.</p>

<p>For more information about symbols, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

<p>This method initializes a symbol search.  The results of the search can be obtained by repeated calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff547856">GetNextSymbolMatch</a>.  When all the desired results have been found, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff543008">EndSymbolMatch</a> to release resources the engine holds for the search.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550856">IDebugSymbols</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550864">IDebugSymbols2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543008">EndSymbolMatch</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547856">GetNextSymbolMatch</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols::StartSymbolMatch method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
