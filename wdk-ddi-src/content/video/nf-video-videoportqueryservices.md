---
UID: NF.video.VideoPortQueryServices
title: VideoPortQueryServices
author: windows-driver-content
description: The VideoPortQueryServices function exposes a specified interface that is implemented by the video port driver.
old-location: display\videoportqueryservices.htm
old-project: display
ms.assetid: 88d54fbc-e865-4a59-bb1c-75adfb49c355
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortQueryServices
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
req.alt-api: VideoPortQueryServices
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

# VideoPortQueryServices function



## -description
<p>The <b>VideoPortQueryServices</b> function exposes a specified interface that is implemented by the video port driver.</p>


## -syntax

````
VP_STATUS VideoPortQueryServices(
  _In_    PVOID               HwDeviceExtension,
  _In_    VIDEO_PORT_SERVICES ServicesType,
  _Inout_ PINTERFACE          Interface
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>ServicesType</i> [in]

<dd>
<p>A value from the <a href="..\video\ne-video-video-port-services.md">VIDEO_PORT_SERVICES</a> enumerated type that specifies which interface is being requested.</p>
</dd>

### -param <i>Interface</i> [in, out]

<dd>
<p>Pointer to an <a href="..\wdm\ns-wdm--interface.md">INTERFACE</a> structure, which contains basic information about the requested interface. See the following <b>Remarks</b> section for more information.</p>
</dd>
</dl>

## -returns
<p>If <b>VideoPortQueryServices</b> succeeds, it returns NO_ERROR; otherwise, it returns an error code.</p>

## -remarks
<p>If the <i>ServicesType</i> parameter is set to <b>VideoPortServicesI2C</b>, the <i>Interface</i> parameter must be a pointer to a <a href="..\video\ns-video--video-port-i2c-interface.md">VIDEO_PORT_I2C_INTERFACE</a> structure, cast as a pointer to an INTERFACE structure.</p>

<p>Similarly, if the <i>ServicesType</i> parameter is set to <b>VideoPortServicesAGP</b>, the <i>Interface</i> parameter must be a pointer to either a <a href="..\video\ns-video--video-port-agp-interface.md">VIDEO_PORT_AGP_INTERFACE</a> structure, or a <a href="..\video\ns-video--video-port-agp-interface-2.md">VIDEO_PORT_AGP_INTERFACE_2</a> structure, each cast as a pointer to an <a href="..\wdm\ns-wdm--interface.md">INTERFACE</a> structure. </p>

<p>The VIDEO_PORT_AGP_INTERFACE and VIDEO_PORT_AGP_INTERFACE_2 structures are nearly identical, except that the latter structure has a member that points to the <a href="..\videoagp\nc-videoagp-pagp-set-rate.md">AgpSetRate</a> function, which is used to reset the transfer rate for an AGP chipset. A video miniport driver querying AGP support should call <b>VideoPortQueryServices</b> first with <i>Interface</i> pointing to a VIDEO_PORT_AGP_INTERFACE_2 structure. If that call fails, the miniport driver can then make another call to <b>VideoPortQueryServices</b>, this time with <i>Interface</i> pointing to a VIDEO_PORT_AGP_INTERFACE structure.</p>

<p>If the <i>ServicesType</i> parameter is set to <b>VideoPortServicesInt10</b>, the <i>Interface</i> parameter must be a pointer to a <a href="..\video\ns-video--video-port-int10-interface.md">VIDEO_PORT_INT10_INTERFACE</a> structure, cast as a pointer to an INTERFACE structure.</p>

<p>If the <i>ServicesType</i> parameter is set to <b>VideoPortServicesDebugReport</b>, the <i>Interface</i> parameter must be a pointer to a <a href="..\video\ns-video--video-port-debug-report-interface.md">VIDEO_PORT_DEBUG_REPORT_INTERFACE</a> structure, cast as a pointer to an INTERFACE structure.</p>

<p>If the <i>ServicesType</i> parameter is set to <b>VideoPortServicesWCMemoryProtection</b>, the <i>Interface</i> parameter must be a pointer to a <a href="..\video\ns-video--video-port-wcmemoryprotection-interface.md">VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE</a> structure, cast as a pointer to an INTERFACE structure. </p>

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

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--interface.md">INTERFACE</a>
</dt>
<dt>
<a href="..\video\ns-video--video-port-agp-interface.md">VIDEO_PORT_AGP_INTERFACE</a>
</dt>
<dt>
<a href="..\video\ns-video--video-port-agp-interface-2.md">VIDEO_PORT_AGP_INTERFACE_2</a>
</dt>
<dt>
<a href="..\video\ns-video--video-port-i2c-interface.md">VIDEO_PORT_I2C_INTERFACE</a>
</dt>
<dt>
<a href="..\video\ns-video--video-port-int10-interface.md">VIDEO_PORT_INT10_INTERFACE</a>
</dt>
<dt>
<a href="..\video\ns-video--video-port-debug-report-interface.md">VIDEO_PORT_DEBUG_REPORT_INTERFACE</a>
</dt>
<dt>
<a href="..\video\ns-video--video-port-wcmemoryprotection-interface.md">VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE</a>
</dt>
<dt>
<a href="..\videoagp\nc-videoagp-pagp-set-rate.md">AgpSetRate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortQueryServices function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
