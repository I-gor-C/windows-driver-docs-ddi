---
UID: NS.video._VP_DEVICE_DESCRIPTION
title: VP_DEVICE_DESCRIPTION
author: windows-driver-content
description: The VP_DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA object.
old-location: display\vp_device_description.htm
old-project: display
ms.assetid: a605e37d-56cd-4d72-a713-314e20c2f630
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VP_DEVICE_DESCRIPTION, VP_DEVICE_DESCRIPTION, *PVP_DEVICE_DESCRIPTION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: video.h
req.include-header: Video.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VP_DEVICE_DESCRIPTION
req.alt-loc: video.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# VP_DEVICE_DESCRIPTION structure



## -description
<p>The VP_DEVICE_DESCRIPTION structure describes the attributes of the physical device for which a driver is requesting a DMA object.</p>


## -syntax

````
typedef struct _VP_DEVICE_DESCRIPTION {
  BOOLEAN ScatterGather;
  BOOLEAN Dma32BitAddresses;
  BOOLEAN Dma64BitAddresses;
  ULONG   MaximumLength;
} VP_DEVICE_DESCRIPTION, *PVP_DEVICE_DESCRIPTION;
````


## -struct-fields
<dl>

### -field ScatterGather

<dd>
<p>If <b>TRUE</b>, indicates that the device supports scatter/gather DMA. If <b>FALSE</b>, the device does not support scatter/gather DMA.</p>
</dd>

### -field Dma32BitAddresses

<dd>
<p>If <b>TRUE</b>, specifies that 32-bit addresses are being used for DMA operations. </p>
</dd>

### -field Dma64BitAddresses

<dd>
<p>If <b>TRUE</b>, specifies that 64-bit addresses are being used for DMA operations.</p>
</dd>

### -field MaximumLength

<dd>
<p>Specifies the maximum number of bytes the device can handle in each DMA operation.</p>
</dd>
</dl>

## -remarks
<p>This structure is available in Windows XP and later.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
</table>