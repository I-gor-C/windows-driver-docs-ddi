---
UID: NF.dbgeng.IDebugSymbols2.GetNearNameByOffset
title: IDebugSymbols2::GetNearNameByOffset
author: windows-driver-content
description: The GetNearNameByOffset method returns the name of a symbol that is located near the specified location.
old-location: debugger\getnearnamebyoffset.htm
old-project: debugger
ms.assetid: bcda26ae-484e-41b9-b86a-552b5cecb9a7
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols2, GetNearNameByOffset, IDebugSymbols2::GetNearNameByOffset
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
req.alt-api: IDebugSymbols.GetNearNameByOffset,IDebugSymbols2.GetNearNameByOffset,IDebugSymbols3.GetNearNameByOffset
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
req.iface: IDebugSymbols2
---

# IDebugSymbols2::GetNearNameByOffset method



## -description
<p>The <b>GetNearNameByOffset</b>  method returns the name of a symbol that is located near the specified location.</p>


## -syntax

````
HRESULT GetNearNameByOffset(
  [in]            ULONG64  Offset,
  [in]            LONG     Delta,
  [out, optional] PSTR     NameBuffer,
  [in]            ULONG    NameBufferSize,
  [out, optional] PULONG   NameSize,
  [out, optional] PULONG64 Displacement
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's virtual address space of the symbol from which the desired symbol is determined.</p>
</dd>

### -param <i>Delta</i> [in]

<dd>
<p>Specifies the relationship between the desired symbol and the symbol located at <i>Offset</i>.  If positive, the engine will return the symbol that is <i>Delta</i> symbols after the symbol located at <i>Offset</i>.  If negative, the engine will return the symbol that is <i>Delta</i> symbols before the symbol located at <i>Offset</i>.</p>
</dd>

### -param <i>NameBuffer</i> [out, optional]

<dd>
<p>Receives the symbol's name.  The name is qualified by the module to which the symbol belongs (for example, <b>mymodule!main</b>).  If <i>NameBuffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>NameBufferSize</i> [in]

<dd>
<p>Specifies the size in characters of the buffer <i>NameBuffer</i>.</p>
</dd>

### -param <i>NameSize</i> [out, optional]

<dd>
<p>Receives the size in characters of the symbol's name.  If <i>NameSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>Displacement</i> [out, optional]

<dd>
<p>Receives the difference between the value of <i>Offset</i> and the location in the target's memory address space of the symbol.  If <i>Displacement</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  However, the buffer was not large enough to hold the symbol's name so it was truncated.</p><dl>
<dt><b>E_NOINTERFACE</b></dt>
</dl><p>No symbol matching the specifications of <i>Offset</i> and <i>Delta</i> was found.</p>

<p> </p>

## -remarks
<p>By increasing or decreasing the value of <i>Delta</i>, these methods can be used to iterate over the target's symbols starting at a particular location.</p>

<p>If <i>Delta</i> is zero, these methods behave the same way as <a href="debugger.getnamebyoffset">GetNameByOffset</a>.</p>

<p>For more information about symbols and symbol names, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols.md">IDebugSymbols</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols2.md">IDebugSymbols2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.getnamebyoffset">GetNameByOffset</a>
</dt>
<dt>
<a href="debugger.getoffsetbyname">GetOffsetByName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols::GetNearNameByOffset method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
