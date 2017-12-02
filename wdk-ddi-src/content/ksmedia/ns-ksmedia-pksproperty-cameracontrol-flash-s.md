---
UID: NS.ksmedia.PKSPROPERTY_CAMERACONTROL_FLASH_S
title: PKSPROPERTY_CAMERACONTROL_FLASH_S
author: windows-driver-content
description: Describes flash control properties in the PROPSETID_VIDCAP_CAMERACONTROL_FLASH camera control property set. This structure specifies property values that are used by applications to configure the camera's flash.
old-location: stream\ksproperty_cameracontrol_flash_s.htm
old-project: stream
ms.assetid: 5d02c019-9a4a-458a-8361-7597bb1fe1a2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_CAMERACONTROL_FLASH_S, KSPROPERTY_CAMERACONTROL_FLASH_S, *PKSPROPERTY_CAMERACONTROL_FLASH_S
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
req.alt-api: KSPROPERTY_CAMERACONTROL_FLASH_S
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

# PKSPROPERTY_CAMERACONTROL_FLASH_S structure



## -description
<p>Describes flash control properties in the <b>PROPSETID_VIDCAP_CAMERACONTROL_FLASH</b> camera control property set. This structure specifies property values that are used by applications to configure the camera's flash.</p>


## -syntax

````
typedef struct {
  ULONG Flash;
  ULONG Capabilities;
} KSPROPERTY_CAMERACONTROL_FLASH_S, *PKSPROPERTY_CAMERACONTROL_FLASH_S;
````


## -struct-fields
<dl>

### -field Flash

<dd>
<p>Indicates requested flash settings. This value must be one of these possible values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_FLASH_OFF"></a><a id="ksproperty_cameracontrol_flash_off"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_FLASH_OFF

</dl>
</td>
<td width="60%">
<p>The flash should never activate.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_FLASH_ON"></a><a id="ksproperty_cameracontrol_flash_on"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_FLASH_ON

</dl>
</td>
<td width="60%">
<p>The flash should activate regardless of lighting conditions.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_FLASH_AUTO"></a><a id="ksproperty_cameracontrol_flash_auto"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_FLASH_AUTO

</dl>
</td>
<td width="60%">
<p>The flash should be controlled by the device and driver based on lighting conditions.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Capabilities

<dd>
<p>Indicates the flash modes that the device supports. This value is a bitwise <b>OR</b> of these possible values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_FLASH_FLAGS_AUTO"></a><a id="ksproperty_cameracontrol_flash_flags_auto"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_FLASH_FLAGS_AUTO

</dl>
</td>
<td width="60%">
<p>The device and driver automatically control flash settings.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="KSPROPERTY_CAMERACONTROL_FLASH_FLAGS_MANUAL"></a><a id="ksproperty_cameracontrol_flash_flags_manual"></a><dl>

### -field KSPROPERTY_CAMERACONTROL_FLASH_FLAGS_MANUAL

</dl>
</td>
<td width="60%">
<p>The user manually sets the flash settings.</p>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_CAMERACONTROL_FLASH_S structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
