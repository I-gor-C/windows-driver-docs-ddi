---
UID: NF.storport.StorPortFreeHostMemoryBuffer
title: StorPortFreeHostMemoryBuffer
author: windows-driver-content
description: The StorPortFreeHostMemoryBuffer routine frees the physically contiguous memory that was allocated to be used for a Host Memory Buffer (HMB).
old-location: storage\storportfreehostmemorybuffer.htm
ms.assetid: 686D141E-E6EA-4BB6-8556-0ECAC592E8F0
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortFreeHostMemoryBuffer
req.alt-loc: storport.h
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
ms.keywords: StorPortFreeHostMemoryBuffer
req.iface: 
req.product: Windows 10 or later.
---

# StorPortFreeHostMemoryBuffer function



## -description
<p>The <b>StorPortFreeHostMemoryBuffer</b> routine frees the physically contiguous memory
    that was allocated to be used for a Host Memory Buffer (HMB) </p>


## -syntax

````
ULONG StorPortFreeHostMemoryBuffer(
  _In_ PVOID                                               HwDeviceExtension,
       _In_reads_(PhysicalAddressRangeCount) PACCESS_RANGE PhysicalAddressRanges,
  _In_ ULONG                                               PhysicalAddressRangeCount
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>PhysicalAddressRanges</i> 

<dd>
<p>The array of physical address ranges that make up
        the Host Memory Buffer previously allocated by  <b>StorPortAllocateHostMemoryBuffer</b>.</p>
</dd>

### -param <i>PhysicalAddressRangeCount</i> [in]

<dd>
<p> The number of entries in <b>PhysicalAddressRanges</b>. </p>
</dd>
</dl>

## -returns
<p><b>StorPortFreeHostMemoryBuffer</b> returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The host memory buffer was successfully freed.</p><dl>
<dt><b>STOR_STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The host memory buffer was not valid (likely already freed).</p>

<p> </p>

## -remarks


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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p></p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.StorPortAllocateHostMemoryBuffer">StorPortAllocateHostMemoryBuffer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortFreeHostMemoryBuffer routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
