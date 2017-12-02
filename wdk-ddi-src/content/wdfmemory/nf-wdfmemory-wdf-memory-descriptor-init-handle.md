---
UID: NF.wdfmemory.WDF_MEMORY_DESCRIPTOR_INIT_HANDLE
title: WDF_MEMORY_DESCRIPTOR_INIT_HANDLE
author: windows-driver-content
description: The WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified framework memory object.
old-location: wdf\wdf_memory_descriptor_init_handle.htm
old-project: wdf
ms.assetid: e5449684-dd37-4d49-ae9f-372f295cecf8
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_MEMORY_DESCRIPTOR_INIT_HANDLE
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
req.alt-api: WDF_MEMORY_DESCRIPTOR_INIT_HANDLE
req.alt-loc: wdfmemory.h
req.ddi-compliance: MemAfterReqCompletedIntIoctlA, MemAfterReqCompletedIoctlA, MemAfterReqCompletedReadA, MemAfterReqCompletedWriteA
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

# WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_MEMORY_DESCRIPTOR_INIT_HANDLE</b> function initializes a <a href="..\wdfmemory\ns-wdfmemory--wdf-memory-descriptor.md">WDF_MEMORY_DESCRIPTOR</a> structure so that it describes a specified framework memory object.</p>


## -syntax

````
VOID WDF_MEMORY_DESCRIPTOR_INIT_HANDLE(
  _Out_    PWDF_MEMORY_DESCRIPTOR Descriptor,
  _In_     WDFMEMORY              Memory,
  _In_opt_ PWDFMEMORY_OFFSET      Offsets
);
````


## -parameters
<dl>

### -param Descriptor [out]

<dd>
<p>A pointer to a <a href="..\wdfmemory\ns-wdfmemory--wdf-memory-descriptor.md">WDF_MEMORY_DESCRIPTOR</a> structure.</p>
</dd>

### -param Memory [in]

<dd>
<p>A handle to a framework memory object.</p>
</dd>

### -param Offsets [in, optional]

<dd>
<p>A pointer to a <a href="..\wudfddi_types\ns-wudfddi-types--wdfmemory-offset.md">WDFMEMORY_OFFSET</a> structure. This parameter is optional and can be <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_MEMORY_DESCRIPTOR_INIT_HANDLE</b> function zeros the specified <a href="..\wdfmemory\ns-wdfmemory--wdf-memory-descriptor.md">WDF_MEMORY_DESCRIPTOR</a> structure and sets the structure's <b>Type</b> member to <b>WdfMemoryDescriptorTypeHandle</b>. Then it sets the structure's <b>u.HandleType.Memory</b> and <b>u.HandleType.Offsets</b> members to the values that the <i>Memory</i> and <i>Offsets</i> parameters specify, respectively.</p>

<p>The following code example obtains a handle to a framework memory object that represents an I/O request's input buffer. The example uses the memory object handle to initialize a <a href="..\wdfmemory\ns-wdfmemory--wdf-memory-descriptor.md">WDF_MEMORY_DESCRIPTOR</a> structure. Then, the example initializes a <a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a> structure and sends a USB control transfer request to an I/O target.</p>

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
<a href="devtest.kmdf_memafterreqcompletedintioctla">MemAfterReqCompletedIntIoctlA</a>, <a href="devtest.kmdf_memafterreqcompletedioctla">MemAfterReqCompletedIoctlA</a>, <a href="devtest.kmdf_memafterreqcompletedreada">MemAfterReqCompletedReadA</a>, <a href="devtest.kmdf_memafterreqcompletedwritea">MemAfterReqCompletedWriteA</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfmemory\ns-wdfmemory--wdf-memory-descriptor.md">WDF_MEMORY_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wdfmemory\nf-wdfmemory-wdf-memory-descriptor-init-buffer.md">WDF_MEMORY_DESCRIPTOR_INIT_BUFFER</a>
</dt>
<dt>
<a href="..\wdfmemory\nf-wdfmemory-wdf-memory-descriptor-init-mdl.md">WDF_MEMORY_DESCRIPTOR_INIT_MDL</a>
</dt>
<dt>
<a href="..\wudfddi_types\ns-wudfddi-types--wdfmemory-offset.md">WDFMEMORY_OFFSET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
