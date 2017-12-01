---
UID: NF.dbgeng.IDebugSymbols3.GetOffsetByLineWide
title: IDebugSymbols3::GetOffsetByLineWide
author: windows-driver-content
description: The GetOffsetByLineWide method returns the location of the instruction that corresponds to a specified line in the source code.
old-location: debugger\getoffsetbylinewide.htm
old-project: debugger
ms.assetid: ba09333e-84a5-4166-a859-e09c0cf74347
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols3, GetOffsetByLineWide, IDebugSymbols3::GetOffsetByLineWide
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
req.alt-api: IDebugSymbols3.GetOffsetByLineWide
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

# IDebugSymbols3::GetOffsetByLineWide method



## -description
<p>The <b>GetOffsetByLineWide</b>  method returns the location of the instruction that corresponds to a specified line in the source code.</p>


## -syntax

````
HRESULT GetOffsetByLineWide(
  [in]  ULONG    Line,
  [in]  PCWSTR   File,
  [out] PULONG64 Offset
);
````


## -parameters
<dl>

### -param <i>Line</i> [in]

<dd>
<p>Specifies the line number in the source file.</p>
</dd>

### -param <i>File</i> [in]

<dd>
<p>Specifies the file name of the source file.</p>
</dd>

### -param <i>Offset</i> [out]

<dd>
<p>Receives the location in the target's virtual address space of an instruction for the specified line.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>A line in a source file might correspond to multiple instructions and this method can return any one of these instructions.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.getlinebyoffset">GetLineByOffset</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols3::GetOffsetByLineWide method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
