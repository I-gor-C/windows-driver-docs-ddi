---
UID: NS.wdfmemory._WDF_MEMORY_DESCRIPTOR
title: WDF_MEMORY_DESCRIPTOR
author: windows-driver-content
description: The WDF_MEMORY_DESCRIPTOR structure describes a memory buffer.
old-location: wdf\wdf_memory_descriptor.htm
old-project: wdf
ms.assetid: 0683cb81-4ae7-4296-b46a-ad2e8b25a781
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_MEMORY_DESCRIPTOR, WDF_MEMORY_DESCRIPTOR, *PWDF_MEMORY_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfmemory.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_MEMORY_DESCRIPTOR
req.alt-loc: wdfmemory.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# WDF_MEMORY_DESCRIPTOR structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_MEMORY_DESCRIPTOR</b> structure describes a memory buffer.</p>


## -syntax

````
typedef struct _WDF_MEMORY_DESCRIPTOR {
  WDF_MEMORY_DESCRIPTOR_TYPE Type;
  union {
    struct {
      PVOID Buffer;
      ULONG Length;
    } BufferType;
    struct {
      PMDL  Mdl;
      ULONG BufferLength;
    } MdlType;
    struct {
      WDFMEMORY         Memory;
      PWDFMEMORY_OFFSET Offsets;
    } HandleType;
  } u;
} WDF_MEMORY_DESCRIPTOR, *PWDF_MEMORY_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field Type

<dd>
<p>A <a href="..\wdfmemory\ne-wdfmemory--wdf-memory-descriptor-type.md">WDF_MEMORY_DESCRIPTOR_TYPE</a>-typed value that identifies the type of buffer description that this <b>WDF_MEMORY_DESCRIPTOR</b> structure contains.</p>
</dd>

### -field u

<dd>
<p>A union of three structures, one of which describes a buffer.</p>
<dl>

### -field BufferType

<dd>
<p>If the <b>Type</b> member is <b>WdfMemoryDescriptorTypeBuffer</b>, the members of the <b>BufferType</b> structure describe a buffer. This structure contains the following two members:</p>
<dl>

### -field Buffer

<dd>
<p>A pointer to a buffer. </p>
</dd>

### -field Length

<dd>
<p>The length, in bytes, of the buffer. </p>
</dd>
</dl>
</dd>

### -field MdlType

<dd>
<p>If the <b>Type</b> member is <b>WdfMemoryDescriptorTypeMdl</b>, the members of the <b>MdlType</b> structure describe a buffer. This structure contains the following two members:</p>
<dl>

### -field Mdl

<dd>
<p>A pointer to a memory descriptor list (MDL). </p>
</dd>

### -field BufferLength

<dd>
<p>The length, in bytes, of the buffer.</p>
</dd>
</dl>
</dd>

### -field HandleType

<dd>
<p>If the <b>Type</b> member is <b>WdfMemoryDescriptorTypeHandle</b>, the members of the <b>HandleType</b> structure describe a buffer. This structure contains the following two members:</p>
<dl>

### -field Memory

<dd>
<p>A handle to a framework memory object. </p>
</dd>

### -field Offsets

<dd>
<p>A pointer to a <a href="..\wudfddi_types\ns-wudfddi-types--wdfmemory-offset.md">WDFMEMORY_OFFSET</a> structure that describes a subsection of the buffer that is represented by the memory object. </p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>WDF_MEMORY_DESCRIPTOR</b> structure is used as input to several of the framework's <a href="wdf.wdf_i_o_target_object_reference">I/O target object methods</a> and <a href="wdf.wdf_usb_reference">USB device object methods</a>.</p>

<p>To initialize a <b>WDF_MEMORY_DESCRIPTOR</b> structure, your driver should call <a href="..\wdfmemory\nf-wdfmemory-wdf-memory-descriptor-init-buffer.md">WDF_MEMORY_DESCRIPTOR_INIT_BUFFER</a>, or <a href="..\wdfmemory\nf-wdfmemory-wdf-memory-descriptor-init-mdl.md">WDF_MEMORY_DESCRIPTOR_INIT_MDL</a>, or <a href="..\wdfmemory\nf-wdfmemory-wdf-memory-descriptor-init-handle.md">WDF_MEMORY_DESCRIPTOR_INIT_HANDLE</a>.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfmemory\ne-wdfmemory--wdf-memory-descriptor-type.md">WDF_MEMORY_DESCRIPTOR_TYPE</a>
</dt>
<dt>
<a href="..\wudfddi_types\ns-wudfddi-types--wdfmemory-offset.md">WDFMEMORY_OFFSET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_MEMORY_DESCRIPTOR structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
