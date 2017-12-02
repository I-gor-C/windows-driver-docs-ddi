---
UID: NF.wdfmemory.WdfMemoryCreatePreallocated
title: WdfMemoryCreatePreallocated
author: windows-driver-content
description: The WdfMemoryCreatePreallocated method creates a framework memory object for a driver-supplied memory buffer.
old-location: wdf\wdfmemorycreatepreallocated.htm
old-project: wdf
ms.assetid: 8c4f9abc-f03d-4084-b0ce-34aea5dd7d96
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfMemoryCreatePreallocated
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
req.alt-api: WdfMemoryCreatePreallocated
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: BufAfterReqCompletedIntIoctlA, BufAfterReqCompletedIoctlA, BufAfterReqCompletedReadA, BufAfterReqCompletedWriteA, DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfMemoryCreatePreallocated function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfMemoryCreatePreallocated</b> method creates a framework memory object for a driver-supplied memory buffer. </p>


## -syntax

````
NTSTATUS WdfMemoryCreatePreallocated(
  _In_opt_ PWDF_OBJECT_ATTRIBUTES Attributes,
  _In_     PVOID                  Buffer,
  _In_     size_t                 BufferSize,
  _Out_    WDFMEMORY              *Memory
);
````


## -parameters
<dl>

### -param Attributes [in, optional]

<dd>
<p>A pointer to a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that contains object attributes for the new memory object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param Buffer [in]

<dd>
<p>A pointer to a driver-supplied buffer.</p>
</dd>

### -param BufferSize [in]

<dd>
<p>The nonzero size, in bytes, of the buffer that <i>Buffer</i> points to.</p>
</dd>

### -param Memory [out]

<dd>
<p>A pointer to a location that receives a handle to the new memory object.</p>
</dd>
</dl>

## -returns
<p><b>WdfMemoryCreatePreallocated</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There was insufficient memory.</p>

<p> </p>

<p>For a list of other return values that the <b>WdfMemoryCreatePreallocated</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

</p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>The <b>WdfMemoryCreatePreallocated</b> method creates a framework memory object for a buffer that the driver has previously allocated or obtained. </p>

<p>Your driver can call <b>WdfMemoryCreatePreallocated</b> if you need to create memory objects that represent pre-existing memory buffers. For example, the driver might receive a driver-defined structure within a buffer for an I/O request that contains an internal I/O control code. The driver can call <b>WdfMemoryCreatePreallocated</b> to create a memory object so that the driver can pass the structure to an I/O target. </p>

<p>After a driver has called <b>WdfMemoryCreatePreallocated</b>, the driver can call <a href="..\wdfmemory\nf-wdfmemory-wdfmemoryassignbuffer.md">WdfMemoryAssignBuffer</a> to assign a different buffer to the memory object that <b>WdfMemoryCreatePreallocated</b> created.</p>

<p>The default parent object for each memory object is the framework driver object that represents the driver that called <b>WdfMemoryCreatePreallocated</b>. If your driver creates a memory object that it uses with a specific device object, request object, or other framework object, it should set the memory object's parent appropriately. The memory object will be deleted when the parent object is deleted. If you do not change the default parent object, the memory object will remain in memory until the I/O manager unloads your driver.</p>

<p>A driver can also delete a memory object by calling <a href="..\wdfobject\nf-wdfobject-wdfobjectdelete.md">WdfObjectDelete</a>.</p>

<p>When the framework memory object that <b>WdfMemoryCreatePreallocated</b> created is deleted, the framework does not deallocate the pre-existing buffer. Likewise, a call to <a href="..\wdfmemory\nf-wdfmemory-wdfmemoryassignbuffer.md">WdfMemoryAssignBuffer</a> does not deallocate the previously assigned buffer.</p>

<p>For more information about framework memory objects, see <a href="wdf.using_memory_buffers">Using Memory Buffers</a>.</p>

<p>The following code example allocates a buffer and then creates a framework memory object for the buffer.</p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.kmdf_bufafterreqcompletedintioctla">BufAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedioctla">BufAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_bufafterreqcompletedreada">BufAfterReqCompletedReadA</a>, <a href="devtest.kmdf_bufafterreqcompletedwritea">BufAfterReqCompletedWriteA</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-exallocatepoolwithtag.md">ExAllocatePoolWithTag</a>
</dt>
<dt>
<a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\wdfobject\nf-wdfobject-wdf-object-attributes-init.md">WDF_OBJECT_ATTRIBUTES_INIT</a>
</dt>
<dt>
<a href="..\wdfmemory\nf-wdfmemory-wdfmemoryassignbuffer.md">WdfMemoryAssignBuffer</a>
</dt>
<dt>
<a href="..\wdfmemory\nf-wdfmemory-wdfmemorycreate.md">WdfMemoryCreate</a>
</dt>
<dt>
<a href="..\wdfmemory\nf-wdfmemory-wdfmemorycreatefromlookaside.md">WdfMemoryCreateFromLookaside</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfMemoryCreatePreallocated method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
