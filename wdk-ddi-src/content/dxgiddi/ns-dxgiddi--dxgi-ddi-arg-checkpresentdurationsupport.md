---
UID: NS.dxgiddi._DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT
title: DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT
author: windows-driver-content
description: Used in a call to the pfnCheckPresentDurationSupport(DXGI) function to check details on hardware device support for seamlessly switching to a new monitor refresh rate.
old-location: display\dxgi_ddi_arg_checkpresentdurationsupport.htm
old-project: display
ms.assetid: FE12CFAB-3936-4453-88B5-A4CF0CA51E1A
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT, DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT
req.alt-loc: Dxgiddi.h
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
req.iface: 
---

# DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT structure



## -description
<p>Used in a call to the <a href="..\dxgiddi\ns-dxgiddi--dxgi-ddi-arg-checkpresentdurationsupport.md">pfnCheckPresentDurationSupport(DXGI)</a> function to check details on hardware device support for seamlessly switching to a new monitor refresh rate.</p>


## -syntax

````
typedef struct _DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT {
  DXGI_DDI_HDEVICE               hDevice;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           DesiredPresentDuration;
  UINT                           ClosestSmallerDuration;
  UINT                           ClosestLargerDuration;
} DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the display device (graphics context) on which the driver performs the presentation. The Direct3D runtime passes this handle to the driver in the <b>hDrvDevice</b> member of the <a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createdevice.md">D3D10DDIARG_CREATEDEVICE</a> structure when the runtime calls the driver's <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a> function to create the display device. </p>
</dd>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based video present network (VidPN) source identification number of the input for which the hardware support is queried.</p>
</dd>

### -field <b>DesiredPresentDuration</b>

<dd>
<p>[in] The desired duration of a single present operation, in units of 100 nanoseconds.</p>
</dd>

### -field <b>ClosestSmallerDuration</b>

<dd>
<p>[out] The smallest supported desired duration of a single present operation on the given VidPN source, in units of 100 nanoseconds. The value must be ≤ <b>DesiredPresentDuration</b>.</p>
<p>See Remarks for more limitations on this value.</p>
</dd>

### -field <b>ClosestLargerDuration</b>

<dd>
<p>[out] The largest supported desired duration of a single present operation on the given VidPN source, in units of 100 nanoseconds. The value must be ≥ <b>DesiredPresentDuration</b>.</p>
<p>See Remarks for more limitations on this value.</p>
</dd>
</dl>

## -remarks
<p>Either  <b>ClosestSmallerDuration</b> or <b>ClosestLargerDuration</b> can be zero. However, if both  are zero, the device cannot seamlessly switch to a new refresh rate.</p>

<p>If both <b>ClosestSmallerDuration</b> and <b>ClosestLargerDuration</b> have the same value as <b>DesiredPresentDuration</b>, the device can precisely match <b>DesiredPresentDuration</b>.</p>

<p>The difference between <b>DesiredPresentDuration</b> and <b>ClosestSmallerDuration</b> (or <b>ClosestLargerDuration</b>) represents the driver’s knowledge of the device capabilities, but there will be additional error during execution. The final accuracy of the device when using per-present durations should typically be the same as the accuracy using  existing presentation modes.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>WDDM 1.3 and later</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3d10ddi-createdevice.md">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="..\d3d10umddi\ns-d3d10umddi-d3d10ddiarg-createdevice.md">D3D10DDIARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="..\dxgiddi\ns-dxgiddi--dxgi-ddi-arg-checkpresentdurationsupport.md">pfnCheckPresentDurationSupport(DXGI)</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
