---
UID: NF.dbgeng.IDebugDataSpaces.WriteVirtual
title: IDebugDataSpaces::WriteVirtual
author: windows-driver-content
description: The WriteVirtual method writes data to the target's virtual address space.
old-location: debugger\writevirtual.htm
old-project: debugger
ms.assetid: 52813320-90a4-4dca-9b9c-44aa22fc49de
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugDataSpaces, WriteVirtual, IDebugDataSpaces::WriteVirtual
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
req.alt-api: IDebugDataSpaces.WriteVirtual,IDebugDataSpaces2.WriteVirtual,IDebugDataSpaces3.WriteVirtual,IDebugDataSpaces4.WriteVirtual
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
req.iface: IDebugDataSpaces
---

# IDebugDataSpaces::WriteVirtual method



## -description
<p>The <b>WriteVirtual</b> method writes data to the target's virtual address space.</p>


## -syntax

````
HRESULT WriteVirtual(
  [in]            ULONG64 Offset,
  [in]            PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesWritten
);
````


## -parameters
<dl>

### -param <i>Offset</i> [in]

<dd>
<p>Specifies the location in the target's virtual address space to be written.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>Specifies the buffer to write the memory from.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in bytes of the buffer.  This is also the number of bytes requested to be written.</p>
</dd>

### -param <i>BytesWritten</i> [out, optional]

<dd>
<p>Receives the number of bytes that were written.  If it is set to <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method can also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was at least partially successful.  <i>BytesWritten</i> indicates the number of bytes successfully written, which may be less than <i>BufferSize</i>.</p>

<p> </p>

## -remarks
<p>This method writes the buffer to the memory in the target's virtual address space.</p>

<p>This method may only write to a cache of memory data when storing data.  To avoid caching, use <a href="debugger.writevirtualuncached">WriteVirtualUncached</a> instead.</p>

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
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces.md">IDebugDataSpaces</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces2.md">IDebugDataSpaces2</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces3.md">IDebugDataSpaces3</a>
</dt>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugdataspaces4.md">IDebugDataSpaces4</a>
</dt>
<dt>
<a href="debugger.readvirtual">ReadVirtual</a>
</dt>
<dt>
<a href="debugger.writevirtualuncached">WriteVirtualUncached</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces::WriteVirtual method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
