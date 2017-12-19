---
UID: NF.video.VideoPortGetDmaAdapter
title: VideoPortGetDmaAdapter function
author: windows-driver-content
description: The VideoPortGetDmaAdapter function returns a pointer to a VP_DMA_ADAPTER structure, which is used in subsequent calls to other DMA-related functions.
old-location: display\videoportgetdmaadapter.htm
old-project: display
ms.assetid: e28649d3-cb4f-4589-b421-a7cdd9139e4c
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: VideoPortGetDmaAdapter
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
req.alt-api: VideoPortGetDmaAdapter
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
req.product: Windows 10 or later.
---

# VideoPortGetDmaAdapter function



## -description
The <b>VideoPortGetDmaAdapter</b> function returns a pointer to a <b>VP_DMA_ADAPTER</b> structure, which is used in subsequent calls to other DMA-related functions.



## -syntax

````
PVP_DMA_ADAPTER VideoPortGetDmaAdapter(
  _In_ PVOID                  HwDeviceExtension,
  _In_ PVP_DEVICE_DESCRIPTION VpDeviceDescription
);
````


## -parameters

### -param HwDeviceExtension [in]

Pointer to the miniport driver's device extension.


### -param VpDeviceDescription [in]

Pointer to a <a href="display.vp_device_description">VP_DEVICE_DESCRIPTION</a> structure, which describes the attributes of the physical device.


## -returns
<b>VideoPortGetDmaAdapter</b> returns a pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570570">VP_DMA_ADAPTER</a> structure on success; if it is unsuccessful in obtaining information about the DMA adapter, it returns <b>NULL</b>.


## -remarks
The <b>VP_DMA_ADAPTER</b> structure contains attribute information about a particular DMA adapter. This structure is an opaque data type that is used internally by the video port driver.

A video miniport driver should call the video port driver's <b>VideoPortGetDmaAdapter</b> to obtain information about a DMA adapter.


<div class="code"><span codelanguage="ManagedCPlusPlus"><table>
<tr>
<th>C++</th>
</tr>
<tr>
<td>
<pre>typedef struct __VP_DMA_ADAPTER* PVP_DMA_ADAPTER;
</pre>
</td>
</tr>
</table></span></div>


This structure has no public members.

This structure is available in Windows XP and later.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows XP and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.videoportstartdma">VideoPortStartDma</a>
</dt>
<dt>
<a href="display.videoportputdmaadapter">VideoPortPutDmaAdapter</a>
</dt>
<dt>
<a href="display.videoportcompletedma">VideoPortCompleteDma</a>
</dt>
<dt>
<a href="display.vp_device_description">VP_DEVICE_DESCRIPTION</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortGetDmaAdapter function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

