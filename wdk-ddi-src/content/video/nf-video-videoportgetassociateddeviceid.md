---
UID: NF.video.VideoPortGetAssociatedDeviceID
title: VideoPortGetAssociatedDeviceID
author: windows-driver-content
description: The VideoPortGetAssociatedDeviceID function obtains the child ID for a specified device object.
old-location: display\videoportgetassociateddeviceid.htm
old-project: display
ms.assetid: 6c40f98b-4d93-4ee8-8217-51e6f1170cf8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortGetAssociatedDeviceID
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortGetAssociatedDeviceID
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortGetAssociatedDeviceID function



## -description
<p>The <b>VideoPortGetAssociatedDeviceID</b> function obtains the child ID for a specified device object.</p>


## -syntax

````
ULONG VideoPortGetAssociatedDeviceID(
  _In_ PVOID DeviceObject
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the child device object, a <a href="wdkgloss.p#wdkgloss.pdo#wdkgloss.pdo"><i>PDO</i></a>.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortGetAssociatedDeviceID</b> returns the child ID for the given device object.</p>

## -remarks
<p><b>VideoPortGetAssociatedDeviceID</b> can be used to obtain the child ID for a child device object. For example, this is useful with <a href="wdkgloss.i#wdkgloss.inter_integrated_circuit__i2c_#wdkgloss.inter_integrated_circuit__i2c_"><i>I2C</i></a>. See <a href="https://msdn.microsoft.com/5eea2257-49ca-4d76-a6a1-91401595750f">Using I2C to Communicate with a Child Device</a> for more information. </p>

<p><b>VideoPortGetAssociatedDeviceID</b> can be used to obtain the child ID for a child device object. For example, this is useful with <a href="wdkgloss.i#wdkgloss.inter_integrated_circuit__i2c_#wdkgloss.inter_integrated_circuit__i2c_"><i>I2C</i></a>. See <a href="https://msdn.microsoft.com/5eea2257-49ca-4d76-a6a1-91401595750f">Using I2C to Communicate with a Child Device</a> for more information. </p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>