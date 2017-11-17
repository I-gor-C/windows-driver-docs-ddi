---
UID: NF.dbgeng.IDebugSymbolGroup2.OutputSymbols
title: IDebugSymbolGroup2::OutputSymbols
author: windows-driver-content
description: The OutputSymbols method prints the specified symbols to the debugger console.
old-location: debugger\outputsymbols.htm
ms.assetid: 1fe99cc4-35d9-432a-aed9-074d40438976
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
req.alt-api: IDebugSymbolGroup.OutputSymbols,IDebugSymbolGroup2.OutputSymbols
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
ms.keywords: IDebugSymbolGroup2, OutputSymbols, IDebugSymbolGroup2::OutputSymbols
req.iface: IDebugSymbolGroup2
---

# IDebugSymbolGroup2::OutputSymbols method



## -description
<p>The <b>OutputSymbols</b> method prints the specified <a href="debugger.symbols#symbols#symbols">symbols</a> to the debugger console.</p>


## -syntax

````
HRESULT OutputSymbols(
  [in] ULONG OutputControl,
  [in] ULONG Flags,
  [in] ULONG Start,
  [in] ULONG Count
);
````


## -parameters
<dl>

### -param <i>OutputControl</i> [in]

<dd>
<p>The output control to use when printing the symbols' information.  For more information about possible values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff541517">DEBUG_OUTCTL_XXX</a>.  For more information about output, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff550971">Input and Output</a>.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>The flags that determine what information is printed for each symbol.  By default, the output includes the symbol's name, offset, value, and type.  The format for the output is as follows:</p>
<p><code>Name**NAME**Offset**OFF**Value**VALUE**Type**TYPE**</code></p>
<p>You can use the following bit flags to suppress the output of one of these pieces of information together with the corresponding marker.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DEBUG_OUTPUT_SYMBOLS_NO_NAMES</p>
</td>
<td>
<p>Suppress output of the symbol's name.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_OUTPUT_SYMBOLS_NO_OFFSETS</p>
</td>
<td>
<p>Suppress output of the symbol's offset.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_OUTPUT_SYMBOLS_NO_VALUES</p>
</td>
<td>
<p>Suppress output of the symbol's value.</p>
</td>
</tr>
<tr>
<td>
<p>DEBUG_OUTPUT_SYMBOLS_NO_TYPES</p>
</td>
<td>
<p>Suppress output of the symbol's type.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Start</i> [in]

<dd>
<p>The index of the first symbol in the symbol group to print.  The index of a symbol is an identification number. This number ranges from zero through the number of symbols in the symbol group minus one.</p>
</dd>

### -param <i>Count</i> [in]

<dd>
<p>The number of symbols to print.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a>.</p>

## -remarks
<p>For more information about symbol groups, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554702">Scopes and Symbol Groups</a>.</p>

<p>For more information about symbol groups, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554702">Scopes and Symbol Groups</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550838">IDebugSymbolGroup</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550846">IDebugSymbolGroup2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547975">GetNumberSymbols</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup::OutputSymbols method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
