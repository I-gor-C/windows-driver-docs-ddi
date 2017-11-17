---
UID: NF.video.VideoPortGetVgaStatus
title: VideoPortGetVgaStatus
author: windows-driver-content
description: The VideoPortGetVgaStatus function detects whether the calling device is decoding a VGA I/O address.
old-location: display\videoportgetvgastatus.htm
ms.assetid: 5a2bb69c-b10a-41bb-a92a-de7add3ca2c5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortGetVgaStatus
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
ms.keywords: VideoPortGetVgaStatus
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortGetVgaStatus function



## -description
<p>The <b>VideoPortGetVgaStatus</b> function detects whether the calling device is decoding a VGA I/O address.</p>


## -syntax

````
VP_STATUS VideoPortGetVgaStatus(
        PVOID  HwDeviceExtension,
  _Out_ PULONG VgaStatus
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> 

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>VgaStatus</i> [out]

<dd>
<p>Pointer to the resulting VGA status. A value of zero (0) indicates that VGA is not enabled; a value of one (1) indicates that VGA is enabled.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortGetVgaStatus</b> returns one of the following values:</p><dl>
<dt><b>NO_ERROR</b></dt>
</dl><p>The function completed successfully.</p><dl>
<dt><b>ERROR_INVALID_FUNCTION</b></dt>
</dl><p>The device was not a PCI device.</p>

<p> </p>

## -remarks
<p>The <b>VideoPortGetVgaStatus</b> function is mainly used to determine whether a device is the sole VGA-enabled device in a <a href="https://msdn.microsoft.com/ba15af67-94c0-4c37-8b3d-b1472e731d88">multiple monitor</a> system. </p>

<p>The <b>VideoPortGetVgaStatus</b> function is mainly used to determine whether a device is the sole VGA-enabled device in a <a href="https://msdn.microsoft.com/ba15af67-94c0-4c37-8b3d-b1472e731d88">multiple monitor</a> system. </p>

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
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
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