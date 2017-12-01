---
UID: NF.dbgeng.IDebugSymbolGroup2.GetSymbolValueTextWide
title: IDebugSymbolGroup2::GetSymbolValueTextWide
author: windows-driver-content
description: The GetSymbolValueTextWide method returns a string that represents the value of a symbol.
old-location: debugger\getsymbolvaluetextwide.htm
old-project: debugger
ms.assetid: 56e147ea-497b-4691-8a62-8165828b1f36
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbolGroup2, GetSymbolValueTextWide, IDebugSymbolGroup2::GetSymbolValueTextWide
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
req.alt-api: IDebugSymbolGroup2.GetSymbolValueTextWide
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
req.iface: IDebugSymbolGroup2
---

# IDebugSymbolGroup2::GetSymbolValueTextWide method



## -description
<p>The <b>GetSymbolValueTextWide</b> method returns a string that represents the value of a symbol.</p>


## -syntax

````
HRESULT GetSymbolValueTextWide(
  [in]            ULONG  Index,
  [out, optional] PWSTR  Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG NameSize
);
````


## -parameters
<dl>

### -param <i>Index</i> [in]

<dd>
<p>The index of the symbol whose value you want.  The index of a symbol is an identification number. The index ranges from zero through the number of symbols in the symbol group minus one.</p>
</dd>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>The value of the symbol as a string.  If <i>Buffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>The size, in characters, of the <i>Buffer </i>buffer.</p>
</dd>

### -param <i>NameSize</i> [out, optional]

<dd>
<p>The size, in characters, of the value of the symbol.  If <i>NameSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  However, the value of the symbol would not fit in the buffer referred to by the <i>Buffer</i> parameter, so a truncated value was returned.</p>

<p> </p>

<p>This method can also return error values.  For more information, see <a href="debugger.hresult_values">Return Values</a>.</p>

## -remarks
<p>If you added the symbol to the symbol group by using the <a href="debugger.addsymbol">AddSymbol</a> method, the string that is returned to <i>Buffer</i> is the name of the symbol that is passed to <b>AddSymbol</b>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbolgroup2.md">IDebugSymbolGroup2</a>
</dt>
<dt>
<a href="debugger.getnumbersymbols">GetNumberSymbols</a>
</dt>
<dt>
<a href="debugger.writesymbol">WriteSymbol</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbolGroup2::GetSymbolValueTextWide method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
