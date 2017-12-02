---
UID: NF.storport.StorPortSetDeviceQueueDepth
title: StorPortSetDeviceQueueDepth
author: windows-driver-content
description: The StorPortSetDeviceQueueDepth routine sets the maximum depth of the device queue for the indicated device.
old-location: storage\storportsetdevicequeuedepth.htm
old-project: storage
ms.assetid: e79b4294-5ba4-4fcc-97e2-69613b65f574
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortSetDeviceQueueDepth
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortSetDeviceQueueDepth
req.alt-loc: Storport.lib,Storport.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Storport.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# StorPortSetDeviceQueueDepth function



## -description
<p>The <b>StorPortSetDeviceQueueDepth</b> routine sets the maximum depth of the device queue for the indicated device. </p>


## -syntax

````
STORPORT_API BOOLEAN StorPortSetDeviceQueueDepth(
  _In_ PVOID HwDeviceExtension,
  _In_ UCHAR PathId,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun,
  _In_ ULONG Depth
);
````


## -parameters
<dl>

### -param HwDeviceExtension [in]

<dd>
<p>A pointer to the miniport driver's per-HBA storage area. </p>
</dd>

### -param PathId [in]

<dd>
<p>Contains the path ID of the target device. </p>
</dd>

### -param TargetId [in]

<dd>
<p>Contains the device number of the target device. </p>
</dd>

### -param Lun [in]

<dd>
<p>Contains the logical unit number of the target device. </p>
</dd>

### -param Depth [in]

<dd>
<p>Supplies the depth to which the queue is to be set. This value is always &gt; 0.</p>
</dd>
</dl>

## -returns
<p><b>StorPortSetDeviceQueueDepth</b> returns <b>TRUE</b> if the queue depth was successfully set, or <b>FALSE</b> if the operation failed. </p>

## -remarks
<p>Before the first call to <b>StorPortSetDeviceQueueDepth</b>, the device queue depth is set to the default value. The following conditional description determines the default queue depth.</p>

<p>The <b>StorPortSetDeviceQueueDepth</b> routine should be called when the miniport driver receives the first SCSI Inquiry command for the specified LUN, or at any time thereafter (but not before), as long as the LUN is valid.</p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Storport.lib</dt>
</dl>
</td>
</tr>
</table>