---
UID: NF.wdfmemory.WDF_MEMORY_DESCRIPTOR_INIT_BUFFER
title: WDF_MEMORY_DESCRIPTOR_INIT_BUFFER
author: windows-driver-content
description: The WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified buffer.
old-location: wdf\wdf_memory_descriptor_init_buffer.htm
old-project: wdf
ms.assetid: 16e1b0cb-8543-4700-8f8c-d7301c6de622
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_MEMORY_DESCRIPTOR_INIT_BUFFER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfmemory.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_MEMORY_DESCRIPTOR_INIT_BUFFER
req.alt-loc: wdfmemory.h
req.ddi-compliance: BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctlA, BufAfterReqCompletedReadA, BufAfterReqCompletedWriteA
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_MEMORY_DESCRIPTOR_INIT_BUFFER</b> function initializes a <a href="..\wdfmemory\ns-wdfmemory--wdf-memory-descriptor.md">WDF_MEMORY_DESCRIPTOR</a> structure so that it describes a specified buffer.</p>


## -syntax

````
VOID WDF_MEMORY_DESCRIPTOR_INIT_BUFFER(
  _Out_ PWDF_MEMORY_DESCRIPTOR Descriptor,
  _In_  PVOID                  Buffer,
  _In_  ULONG                  BufferLength
);
````


## -parameters
<dl>

### -param Descriptor [out]

<dd>
<p>A pointer to a <a href="..\wdfmemory\ns-wdfmemory--wdf-memory-descriptor.md">WDF_MEMORY_DESCRIPTOR</a> structure.</p>
</dd>

### -param Buffer [in]

<dd>
<p>A pointer to a memory buffer.</p>
</dd>

### -param BufferLength [in]

<dd>
<p>The size, in bytes, of the memory buffer that <i>Buffer</i> points to.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_MEMORY_DESCRIPTOR_INIT_BUFFER</b> function zeros the specified <a href="..\wdfmemory\ns-wdfmemory--wdf-memory-descriptor.md">WDF_MEMORY_DESCRIPTOR</a> structure and sets the structure's <b>Type</b> member to <b>WdfMemoryDescriptorTypeBuffer</b>. Then it sets the structure's <b>u.BufferType.Buffer</b> and <b>u.BufferType.Length</b> members to the values that the <i>Buffer</i> and <i>BufferLength</i> parameters specify, respectively.</p>

<p>For a code example that uses <b>WDF_MEMORY_DESCRIPTOR_INIT_BUFFER</b>, see <a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendioctlsynchronously.md">WdfIoTargetSendIoctlSynchronously</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfmemory.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_bufafterreqcompletedintioctla">BufAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedioctla">BufAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedreada">BufAfterReqCompletedReadA</a>, <a href="devtest.kmdf_bufafterreqcompletedwritea">BufAfterReqCompletedWriteA</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfmemory\ns-wdfmemory--wdf-memory-descriptor.md">WDF_MEMORY_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wdfmemory\nf-wdfmemory-wdf-memory-descriptor-init-handle.md">WDF_MEMORY_DESCRIPTOR_INIT_HANDLE</a>
</dt>
<dt>
<a href="..\wdfmemory\nf-wdfmemory-wdf-memory-descriptor-init-mdl.md">WDF_MEMORY_DESCRIPTOR_INIT_MDL</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
