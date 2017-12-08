---
UID: NS.ksmedia.PKSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S
title: PKSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S
author: windows-driver-content
description: Describes region of interest (ROI) control properties in the PROPSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST camera control property set.
old-location: stream\ksproperty_cameracontrol_region_of_interest_s.htm
old-project: stream
ms.assetid: 0a488d9f-1e34-4482-a2a8-7c160b00766c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S, KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S, *PKSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S
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
req.alt-api: KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S
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

# PKSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S structure



## -description
<p>Describes region of interest (ROI) control properties in the <b>PROPSETID_VIDCAP_CAMERACONTROL_REGION_OF_INTEREST</b> camera control property set. The region of interest is a rectangle in the image that is used to focus the camera. This structure specifies property values that are used in requests to the camera driver.</p>


## -syntax

````
typedef struct {
  RECT  FocusRect;
  BOOL  AutoFocusLock;
  BOOL  AutoExposureLock;
  BOOL  AutoWhitebalanceLock;
  union {
    ULONG Capabilities;
    ULONG Configuration;
  };
} KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S, *PKSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S;
````


## -struct-fields
<dl>

### -field FocusRect

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that specifies the rectangular region in which the device should set the focus. This structure is available only to Windows apps.</p>
<p>If <b>FocusRect</b> is not a valid value, or if all members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure are zero, the device should focus the center of the image and the remaining members of this structure can be ignored.</p>
<p>The rectangle's coordinates are with respect to the preview video resolution.</p>
</dd>

### -field AutoFocusLock

<dd>
<p>If <b>TRUE</b>, the device should lock the focus to the current value.</p>
<p>This member should be ignored if <b>FocusRect</b> is not a valid value.</p>
</dd>

### -field AutoExposureLock

<dd>
<p>If <b>TRUE</b>, the device should lock the exposure to the current value.</p>
<p>This member should be ignored if <b>FocusRect</b> is not a valid value.</p>
</dd>

### -field AutoWhitebalanceLock

<dd>
<p>If <b>TRUE</b>, the device should lock the white balance setting to the current value.</p>
<p>This member should be ignored if <b>FocusRect</b> is not a valid value.</p>
</dd>

### -field Capabilities

<dd>
<p>Indicates whether the device and driver support setting the region of interest automatically or manually. This member a bitwise <b>OR</b> of these possible values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_AUTO"></a><a id="ksproperty_cameracontrol_region_of_interest_flags_auto"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_AUTO

</dl>
</td>
<td width="60%">
<p>The device and driver can automatically set the region of interest.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_MANUAL"></a><a id="ksproperty_cameracontrol_region_of_interest_flags_manual"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_MANUAL

</dl>
</td>
<td width="60%">
<p>The user can manually set the region of interest.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_ASYNC"></a><a id="ksproperty_cameracontrol_region_of_interest_flags_async"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_FLAGS_ASYNC

</dl>
</td>
<td width="60%">
<p>ROI control features execute asynchronously.</p>
<p>This capability is available starting with Windows 8.1.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Configuration

<dd>
<p>Configuration flags for control operations for the region. This is a bitwise OR combination of the following values.</p>
<p>This member is available starting with Windows 8.1.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="_KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_FOCUS"></a><a id="_ksproperty_cameracontrol_region_of_interest_config_focus"></a><dl>

### -field  KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_FOCUS

</dl>
</td>
<td width="60%">
<p>Set auto focus for the region.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_EXPOSURE"></a><a id="ksproperty_cameracontrol_region_of_interest_config_exposure"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_EXPOSURE

</dl>
</td>
<td width="60%">
<p>Set auto exposure for the region.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_WB"></a><a id="ksproperty_cameracontrol_region_of_interest_config_wb"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONFIG_WB

</dl>
</td>
<td width="60%">
<p>Set auto white balance for the region.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONVERGEMODE"></a><a id="ksproperty_cameracontrol_region_of_interest_convergemode"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_CONVERGEMODE

</dl>
</td>
<td width="60%">
<p>Enable convergence of objects in the region</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/jj156041">KSPROPERTY_CAMERACONTROL_FLASH_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
