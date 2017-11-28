---
UID: NS.ksmedia.PKSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S
title: PKSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S
author: windows-driver-content
description: Describes video stabilization control properties in the PROPSETID_VIDCAP_CAMERACONTROL_VIDEO_STABILIZATION camera control property set. This structure specifies property values that are used in requests to the camera driver.
old-location: stream\ksproperty_cameracontrol_videostabilization_mode_s.htm
old-project: stream
ms.assetid: 7cbf015c-4756-4d5c-a5fb-9cd8a5e0e3fd
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S, KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S, *PKSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S
req.alt-loc: Ksmedia.h
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

# PKSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S structure



## -description
<p>Describes video stabilization control properties in the <b>PROPSETID_VIDCAP_CAMERACONTROL_VIDEO_STABILIZATION</b> camera control property set. This structure specifies property values that are used in requests to the camera driver.</p>


## -syntax

````
typedef struct {
  ULONG VideoStabilizationMode;
  ULONG Capabilities;
} KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S, *PKSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S;
````


## -struct-fields
<dl>

### -field <b>VideoStabilizationMode</b>

<dd>
<p>Indicates the selected video stabilization modes. This member has one of these possible values:</p>
<dl class="indent">

### -field <a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_OFF"></a><a id="ksproperty_cameracontrol_videostabilization_mode_off"></a><p><a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_OFF"></a><a id="ksproperty_cameracontrol_videostabilization_mode_off"></a><b>KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_OFF</b></p>


<dd>
<p>The video stabilization mode should not activate.</p>
</dd>

### -field <a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_AUTO"></a><a id="ksproperty_cameracontrol_videostabilization_mode_auto"></a><p><a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_AUTO"></a><a id="ksproperty_cameracontrol_videostabilization_mode_auto"></a><b>KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_AUTO</b></p>


<dd>
<p>The device automatically controls video stabilization.  This value is valid only if <b>KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_AUTO</b> is set in the <b>Capabilities</b> member.</p>
</dd>

### -field <a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_LOW"></a><a id="ksproperty_cameracontrol_videostabilization_mode_low"></a><p><a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_LOW"></a><a id="ksproperty_cameracontrol_videostabilization_mode_low"></a><b>KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_LOW</b></p>


<dd>
<p>Video stabilization is set at a low level.</p>
</dd>

### -field <a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_MEDIUM"></a><a id="ksproperty_cameracontrol_videostabilization_mode_medium"></a><p><a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_MEDIUM"></a><a id="ksproperty_cameracontrol_videostabilization_mode_medium"></a><b>KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_MEDIUM</b></p>


<dd>
<p>Video stabilization is set at a medium level.</p>
</dd>

### -field <a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_HIGH"></a><a id="ksproperty_cameracontrol_videostabilization_mode_high"></a><p><a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_HIGH"></a><a id="ksproperty_cameracontrol_videostabilization_mode_high"></a><b>KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_HIGH</b></p>


<dd>
<p>Video stabilization is set at a high level.</p>
</dd>
</dl>
</dd>

### -field <b>Capabilities</b>

<dd>
<p>Indicates whether the device and driver support setting video stabilization control automatically or manually. This member a bitwise <b>OR</b> of these possible values:</p>
<dl class="indent">

### -field <a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_AUTO"></a><a id="ksproperty_cameracontrol_videostabilization_mode_flags_auto"></a><p><a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_AUTO"></a><a id="ksproperty_cameracontrol_videostabilization_mode_flags_auto"></a><b>KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_AUTO</b></p>


<dd>
<p>The device and driver can automatically control video stabilization.</p>
</dd>

### -field <a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_MANUAL"></a><a id="ksproperty_cameracontrol_videostabilization_mode_flags_manual"></a><p><a id="KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_MANUAL"></a><a id="ksproperty_cameracontrol_videostabilization_mode_flags_manual"></a><b>KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_FLAGS_MANUAL</b></p>


<dd>
<p>The user can manually set video stabilization modes.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The video stabilization settings specified with this structure affect only the device and have no effect on applications' software video stabilization.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj151595">KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj156043">KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE_PROPERTY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
