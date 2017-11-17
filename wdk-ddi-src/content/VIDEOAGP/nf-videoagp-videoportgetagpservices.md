---
UID: NF.videoagp.VideoPortGetAgpServices
title: VideoPortGetAgpServices
author: windows-driver-content
description: The VideoPortGetAgpServices function is obsolete and is supported only for backward compatibility with existing drivers.
old-location: display\videoportgetagpservices.htm
ms.assetid: 3b01831d-d429-4dc5-9b12-a0e1fc58634d
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: videoagp.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortGetAgpServices
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
ms.keywords: VideoPortGetAgpServices
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortGetAgpServices function



## -description
<p>The <b>VideoPortGetAgpServices</b> function is <b>obsolete</b> and is supported only for backward compatibility with existing drivers. In its place, driver writers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff570337">VideoPortQueryServices</a>.</p>
<p><b>VideoPortGetAgpServices</b> returns a list of video port driver-implemented AGP service functions.</p>


## -syntax

````
BOOLEAN VideoPortGetAgpServices(
  _In_ PVOID                    HwDeviceExtension,
  _In_ PVIDEO_PORT_AGP_SERVICES AgpServices
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>AgpServices</i> [in]

<dd>
<p>Pointer to an uninitialized, miniport driver-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff570529">VIDEO_PORT_AGP_SERVICES</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortGetAgpServices</b> returns <b>TRUE</b> after it successfully initializes the VIDEO_PORT_AGP_SERVICES structure to which <i>AgpServices</i> points; otherwise it returns <b>FALSE</b>.</p>

## -remarks
<p>PnP video miniport drivers that can use AGP should call <b>VideoPortGetAgpServices</b>.</p>

<p>The video port driver initializes the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570529">VIDEO_PORT_AGP_SERVICES</a> structure as follows:</p>

<p>All function pointers are initialized to point to the corresponding video port driver-implemented AGP service functions.</p>

<p>The <b>AllocationLimit</b> field is initialized to the maximum amount of AGP memory that a miniport driver is allowed to commit, in bytes.</p>

<p>PnP video miniport drivers that can use AGP should call <b>VideoPortGetAgpServices</b>.</p>

<p>The video port driver initializes the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570529">VIDEO_PORT_AGP_SERVICES</a> structure as follows:</p>

<p>All function pointers are initialized to point to the corresponding video port driver-implemented AGP service functions.</p>

<p>The <b>AllocationLimit</b> field is initialized to the maximum amount of AGP memory that a miniport driver is allowed to commit, in bytes.</p>

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
<dt>Videoagp.h (include Video.h)</dt>
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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570337">VideoPortQueryServices</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3c3a6936-7435-4a42-99e6-2c048613af23">AgpCommitPhysical</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8a3e7fcd-d838-47ad-a42b-7eb070f81418">AgpCommitVirtual</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/bb0e3330-5601-47dd-afc6-94a70b42daaf">AgpFreePhysical</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/a6f689ab-8cf1-4207-af2b-30957500c190">AgpFreeVirtual</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4da0f5cb-a017-4df5-958b-c76b7a08495a">AgpReleasePhysical</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/4e880b39-e0ee-4801-86b7-ffc06ed415ab">AgpReleaseVirtual</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b3e21c94-acd5-4767-8ba5-70b2dcfb2aaa">AgpReservePhysical</a>
</dt>
<dt><b>AgpReleasePhysical</b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570529">VIDEO_PORT_AGP_SERVICES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortGetAgpServices function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
