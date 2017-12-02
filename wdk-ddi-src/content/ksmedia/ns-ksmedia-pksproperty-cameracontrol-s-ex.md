---
UID: NS.ksmedia.PKSPROPERTY_CAMERACONTROL_S_EX
title: PKSPROPERTY_CAMERACONTROL_S_EX
author: windows-driver-content
description: Specifies a camera control operation, including setting the flash, the image pin control properties, the region of interest in the image, or video stabilization.
old-location: stream\ksproperty_cameracontrol_s_ex.htm
old-project: stream
ms.assetid: fa015adf-93b6-472f-8a78-a627a59c032e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_CAMERACONTROL_S_EX, KSPROPERTY_CAMERACONTROL_S_EX, *PKSPROPERTY_CAMERACONTROL_S_EX
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
req.alt-api: KSPROPERTY_CAMERACONTROL_S_EX
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

# PKSPROPERTY_CAMERACONTROL_S_EX structure



## -description
<p>Specifies a camera control operation, including setting the flash, the image pin control properties, the region of interest in the image, or video stabilization. This structure describes filter-based properties in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567802">PROPSETID_VIDCAP_CAMERACONTROL</a> property set.</p>
<p>Supported starting with Windows 8.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  LONG       Value;
  ULONG      Flags;
  ULONG      Capabilities;
  RECT       FocusRect;
} KSPROPERTY_CAMERACONTROL_S_EX, *PKSPROPERTY_CAMERACONTROL_S_EX;
````


## -struct-fields
<dl>

### -field Property

<dd>
<p>Specifies an initialized <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field Value

<dd>
<p>Specifies the value of the property. This member is read/write.</p>
</dd>

### -field Flags

<dd>
<p>Indicates, for Get requests, the current setting for the specified property from the values listed below. Indicates, for Set requests, the desired setting for the specified property from the values listed below. This member can be a bitwise <b>OR</b> of the following values that are defined in Ksmedia.h:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_FLAGS_AUTO"></a><a id="ksproperty_cameracontrol_flags_auto"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_FLAGS_AUTO

</dl>
</td>
<td width="60%">
<p>Indicates that the setting is controlled automatically.
If the driver receives this value, it should set the camera control synchronously to automatic mode and then return.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_FLAGS_MANUAL"></a><a id="ksproperty_cameracontrol_flags_manual"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_FLAGS_MANUAL

</dl>
</td>
<td width="60%">
<p>Indicates that the setting is controlled manually. If the driver receives this value, it should set the camera control synchronously to manual mode and then return.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_FLAGS_ASYNCHRONOUS"></a><a id="ksproperty_cameracontrol_flags_asynchronous"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_FLAGS_ASYNCHRONOUS

</dl>
</td>
<td width="60%">
<p>Indicates whether the driver should perform the camera control operation asynchronously—where the application has issued a command for the driver to set up the camera control settings in advance of taking a picture.</p>
<p>This flag must be set only if either <b>KSPROPERTY_CAMERACONTROL_FLAGS_MANUAL</b> or <b>KSPROPERTY_CAMERACONTROL_FLAGS_AUTO</b> are set.</p>
<p>If this flag value and and the <b>KSPROPERTY_CAMERACONTROL_FLAGS_AUTO</b> flag value are both set, the driver should initiate a worker thread to start one requested control operation and should reject all other requests for the same operation until it has completed the first one. After the operation has successfully completed, the driver should trigger the <a href="https://msdn.microsoft.com/library/windows/hardware/jj714740">KSEVENTSETID_CameraAsyncControl</a> event.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Capabilities

<dd>
<p>If set, indicates that when the application submits a query, the driver should return the value of the <b>Capabilities</b> member of the appropriate camera control structure from the following list.</p>
<ul>
<li>
<a href="stream.ksproperty_cameracontrol_flash_s">KSPROPERTY_CAMERACONTROL_FLASH_S</a>
</li>
<li>
<a href="stream.ksproperty_cameracontrol_image_pin_capability_s">KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S</a>
</li>
<li>
<a href="stream.ksproperty_cameracontrol_region_of_interest_s">KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S</a>
</li>
<li>
<a href="stream.ksproperty_cameracontrol_videostabilization_mode_s">KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S</a>
</li>
</ul>
</dd>

### -field FocusRect

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a> structure that specifies the rectangular region in which the device should set the focus. This structure is available only to Windows desktop applications.</p>
</dd>
</dl>

## -remarks
<p>When a requested camera focus operation is completed or is canceled, the driver should generate an event specified by the <b>KSEVENT_CAMERACONTROL_FOCUS</b> enumeration value.</p>

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
<a href="..\ksmedia\ne-ksmedia-ksevent-cameracontrol.md">KSEVENT_CAMERACONTROL</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a>
</dt>
<dt>
<a href="stream.ksproperty_cameracontrol_flash_s">KSPROPERTY_CAMERACONTROL_FLASH_S</a>
</dt>
<dt>
<a href="stream.ksproperty_cameracontrol_region_of_interest_s">KSPROPERTY_CAMERACONTROL_REGION_OF_INTEREST_S</a>
</dt>
<dt>
<a href="stream.ksproperty_cameracontrol_videostabilization_mode_s">KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569234">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_CAMERACONTROL_S_EX structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
