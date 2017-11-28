---
UID: NF.dbgeng.IDebugSymbols2.GetNameByOffset
title: IDebugSymbols2::GetNameByOffset
author: windows-driver-content
description: The GetNameByOffset method returns the name of the symbol at the specified location in the target's virtual address space.
old-location: debugger\getnamebyoffset.htm
old-project: debugger
ms.assetid: 47f87684-339a-49e0-a349-491054ab26ff
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugSymbols2, GetNameByOffset, IDebugSymbols2::GetNameByOffset
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
req.alt-api: IDebugSymbols.GetNameByOffset,IDebugSymbols2.GetNameByOffset,IDebugSymbols3.GetNameByOffset
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

# IDebugSymbols2::GetNameByOffset method



## -description
<p>The <b>GetNameByOffset</b>  method returns the name of the symbol at the specified location in the target's virtual address space.</p>


## -syntax

````
HRESULT GetNameByOffset(
  [in]            ULONG64  Offset,
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
<p>Specifies the location in the target's virtual address space of the symbol whose name is requested.  <i>Offset</i> does not need to specify the base location of the symbol; it only needs to specify a location within the symbol's memory allocation.</p>
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
<p>Receives the difference between the value of <i>Offset</i> and the base location of the symbol.  If <i>Displacement</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful.  However, the buffer was not large enough to hold the symbol's name, so it was truncated.</p><dl>
<dt><b>E_FAIL</b></dt>
</dl><p>No symbol could be found at the specified location.</p>

<p> </p>

## -remarks
<p>For more information about symbols and symbol names, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558824">Symbols</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550856">IDebugSymbols</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550864">IDebugSymbols2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550870">IDebugSymbols3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547204">GetNearNameByOffset</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548035">GetOffsetByName</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols::GetNameByOffset method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
