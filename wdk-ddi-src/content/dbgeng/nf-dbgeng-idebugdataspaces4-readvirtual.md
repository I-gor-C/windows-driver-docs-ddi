---
UID: NF.dbgeng.IDebugDataSpaces4.ReadVirtual
title: IDebugDataSpaces4::ReadVirtual
author: windows-driver-content
description: The ReadVirtual method reads memory from the target's virtual address space.
old-location: debugger\readvirtual.htm
old-project: debugger
ms.assetid: 083b0ab5-e2b9-4dcb-b17d-ab2ebde48665
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugDataSpaces4, ReadVirtual, IDebugDataSpaces4::ReadVirtual
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
req.alt-api: IDebugDataSpaces.ReadVirtual,IDebugDataSpaces2.ReadVirtual,IDebugDataSpaces3.ReadVirtual,IDebugDataSpaces4.ReadVirtual
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
req.iface: IDebugDataSpaces4
---

# IDebugDataSpaces4::ReadVirtual method



## -description
<p>The <b>ReadVirtual</b> method reads memory from the target's virtual address space.</p>


## -syntax

````
HRESULT ReadVirtual(
  [in]            ULONG64 Offset,
  [out]           PVOID   Buffer,
  [in]            ULONG   BufferSize,
  [out, optional] PULONG  BytesRead
);
````


## -parameters
<dl>

### -param Offset [in]

<dd>
<p>Specifies the location in the target's virtual address space to be read.</p>
</dd>

### -param Buffer [out]

<dd>
<p>Specifies the buffer to read the memory into.</p>
</dd>

### -param BufferSize [in]

<dd>
<p>Specifies the size in bytes of the buffer.  This is also the number of bytes being requested.</p>
</dd>

### -param BytesRead [out, optional]

<dd>
<p>Receives the number of bytes that were read.  If it is set to <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.  It is possible that <i>BytesRead</i> is less than <i>BufferSize</i>, but at least one byte of data was returned.</p>

<p> </p>

<p>This method can also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p>

## -remarks
<p>This method fills the buffer with the contents of the memory in the target's virtual address space.</p>

<p>This method may reference a cache of memory data when retrieving data.  If the data is volatile, such as memory-mapped hardware state, use <a href="debugger.readvirtualuncached">ReadVirtualUncached</a> instead.</p>

<p>When reading memory that contains pointers, these pointers are for the target's virtual address space and not the engine's.  For example, if a data structure contained a string, a second call to this method may be needed to read the contents of the string.</p>

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
<a href="debugger.writevirtual">WriteVirtual</a>
</dt>
<dt>
<a href="debugger.readvirtualuncached">ReadVirtualUncached</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugDataSpaces::ReadVirtual method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
