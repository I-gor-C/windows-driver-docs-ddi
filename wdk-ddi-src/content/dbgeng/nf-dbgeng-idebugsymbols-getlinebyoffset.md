---
UID: NF.dbgeng.IDebugSymbols.GetLineByOffset
title: IDebugSymbols::GetLineByOffset
author: windows-driver-content
description: The GetLineByOffset method returns the source filename and the line number within the source file of an instruction in the target.
old-location: debugger\getlinebyoffset.htm
old-project: debugger
ms.assetid: 1b470ae8-49d3-467d-aa08-08bd9c9e9466
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugSymbols, GetLineByOffset, IDebugSymbols::GetLineByOffset
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
req.alt-api: IDebugSymbols.GetLineByOffset,IDebugSymbols2.GetLineByOffset,IDebugSymbols3.GetLineByOffset
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
req.iface: IDebugSymbols
---

# IDebugSymbols::GetLineByOffset method



## -description
<p>The <b>GetLineByOffset</b>  method returns the source filename and the line number within the source file of an instruction in the target.</p>


## -syntax

````
HRESULT GetLineByOffset(
  [in]            ULONG64  Offset,
  [out, optional] PULONG   Line,
  [out, optional] PSTR     FileBuffer,
  [in]            ULONG    FileBufferSize,
  [out, optional] PULONG   FileSize,
  [out, optional] PULONG64 Displacement
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's virtual address space of the instruction for which to return the source file and line number.</p>
</dd>

### -param <i>Line</i> [out, optional]

<dd>
<p>Receives the line number within the source file of the instruction specified by <i>Offset</i>.  If <i>Line</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>FileBuffer</i> [out, optional]

<dd>
<p>Receives the file name of the file that contains the instruction specified by <i>Offset</i>.  If <i>FileBuffer</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>FileBufferSize</i> [in]

<dd>
<p>Specifies the size, in characters, of the <i>FileBuffer</i> buffer.</p>
</dd>

### -param <i>FileSize</i> [out, optional]

<dd>
<p>Specifies the size, in characters, of the source filename.  If <i>FileSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>

### -param <i>Displacement</i> [out, optional]

<dd>
<p>Receives the difference between the location specified in <i>Offset</i> and the location of the first instruction of the returned line.  If <i>Displacement</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The method was successful. However, the buffer was not large enough to hold the name of the source file and the name was truncated.</p>

<p> </p>

## -remarks
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
<a href="..\dbgeng\nn-dbgeng-idebugsymbols.md">IDebugSymbols</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols2.md">IDebugSymbols2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugsymbols3.md">IDebugSymbols3</a>
</dt>
<dt>
<a href="debugger.getoffsetbyline">GetOffsetByLine</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugSymbols::GetLineByOffset method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
