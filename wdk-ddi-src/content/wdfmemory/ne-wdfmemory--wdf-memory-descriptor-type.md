---
UID: NE.wdfmemory._WDF_MEMORY_DESCRIPTOR_TYPE
title: WDF_MEMORY_DESCRIPTOR_TYPE
author: windows-driver-content
description: The WDF_MEMORY_DESCRIPTOR_TYPE enumeration identifies the types of memory descriptions that a WDF_MEMORY_DESCRIPTOR structure can specify.
old-location: wdf\wdf_memory_descriptor_type.htm
old-project: wdf
ms.assetid: ab364ad8-1b04-4ad0-a036-9b1c41e16604
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_IO_TARGET_OPEN_PARAMS, WDF_IO_TARGET_OPEN_PARAMS, *PWDF_IO_TARGET_OPEN_PARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfmemory.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_MEMORY_DESCRIPTOR_TYPE
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_MEMORY_DESCRIPTOR_TYPE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_MEMORY_DESCRIPTOR_TYPE</b> enumeration identifies the types of memory descriptions that a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure can specify.</p>


## -syntax

````
typedef enum _WDF_MEMORY_DESCRIPTOR_TYPE { 
  WdfMemoryDescriptorTypeInvalid  = 0,
  WdfMemoryDescriptorTypeBuffer   = 1,
  WdfMemoryDescriptorTypeMdl      = 2,
  WdfMemoryDescriptorTypeHandle   = 3
} WDF_MEMORY_DESCRIPTOR_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfMemoryDescriptorTypeInvalid"></a><a id="wdfmemorydescriptortypeinvalid"></a><a id="WDFMEMORYDESCRIPTORTYPEINVALID"></a><b>WdfMemoryDescriptorTypeInvalid</b>

<dd>
<p>Reserved for internal use only.</p>
</dd>

### -field <a id="WdfMemoryDescriptorTypeBuffer"></a><a id="wdfmemorydescriptortypebuffer"></a><a id="WDFMEMORYDESCRIPTORTYPEBUFFER"></a><b>WdfMemoryDescriptorTypeBuffer</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure contains a buffer description.</p>
</dd>

### -field <a id="WdfMemoryDescriptorTypeMdl"></a><a id="wdfmemorydescriptortypemdl"></a><a id="WDFMEMORYDESCRIPTORTYPEMDL"></a><b>WdfMemoryDescriptorTypeMdl</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure contains a memory descriptor list (MDL).</p>
</dd>

### -field <a id="WdfMemoryDescriptorTypeHandle"></a><a id="wdfmemorydescriptortypehandle"></a><a id="WDFMEMORYDESCRIPTORTYPEHANDLE"></a><b>WdfMemoryDescriptorTypeHandle</b>

<dd>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a> structure contains a handle to a memory object.</p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552392">WDF_MEMORY_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_MEMORY_DESCRIPTOR_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
