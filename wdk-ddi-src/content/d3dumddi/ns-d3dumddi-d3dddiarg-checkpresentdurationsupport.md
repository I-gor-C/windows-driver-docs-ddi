---
UID: NS.d3dumddi.D3DDDIARG_CHECKPRESENTDURATIONSUPPORT
title: D3DDDIARG_CHECKPRESENTDURATIONSUPPORT
author: windows-driver-content
description: Used in a call to the CheckPresentDurationSupport function to check details on hardware device support for seamlessly switching to a new monitor refresh rate.
old-location: display\d3dddiarg_checkpresentdurationsupport.htm
old-project: display
ms.assetid: D72D6C06-DD6A-4051-9AD0-FD1E240C164A
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_CHECKPRESENTDURATIONSUPPORT, D3DDDIARG_CHECKPRESENTDURATIONSUPPORT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_CHECKPRESENTDURATIONSUPPORT
req.alt-loc: D3dumddi.h
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

# D3DDDIARG_CHECKPRESENTDURATIONSUPPORT structure



## -description
<p>Used in a call to the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-checkpresentdurationsupport.md">CheckPresentDurationSupport</a> function to check details on hardware device support for seamlessly switching to a new monitor refresh rate.</p>


## -syntax

````
typedef struct {
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  UINT                           DesiredPresentDuration;
  UINT                           ClosestSmallerDuration;
  UINT                           ClosestLargerDuration;
} D3DDDIARG_CHECKPRESENTDURATIONSUPPORT;
````


## -struct-fields
<dl>

### -field VidPnSourceId

<dd>
<p>[in] The zero-based video present network (VidPN) source identification number of the input for which the hardware support is queried.</p>
</dd>

### -field DesiredPresentDuration

<dd>
<p>[in] The desired duration of a single present operation, in units of 100 nanoseconds.</p>
</dd>

### -field ClosestSmallerDuration

<dd>
<p>[out] The smallest supported desired duration of a single present operation on the given VidPN source, in units of 100 nanoseconds. The value must be ≤ <b>DesiredPresentDuration</b>.</p>
<p>See Remarks for more limitations on this value.</p>
</dd>

### -field ClosestLargerDuration

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
<dt>D3dumddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-checkpresentdurationsupport.md">CheckPresentDurationSupport</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_CHECKPRESENTDURATIONSUPPORT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
