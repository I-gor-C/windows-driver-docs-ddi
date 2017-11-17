---
UID: NS.ksmedia.PKSPROPERTY_EXTDEVICE_S
title: PKSPROPERTY_EXTDEVICE_S
author: windows-driver-content
description: The KSPROPERTY_EXTDEVICE_S structure describes an external device and its capabilities.
old-location: stream\ksproperty_extdevice_s.htm
ms.assetid: da866f7e-f2c6-4926-bbde-db0629571c57
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_EXTDEVICE_S
req.alt-loc: ksmedia.h
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
ms.keywords: PKSPROPERTY_EXTDEVICE_S, KSPROPERTY_EXTDEVICE_S, *PKSPROPERTY_EXTDEVICE_S
req.iface: 
---

# PKSPROPERTY_EXTDEVICE_S structure



## -description
<p>The KSPROPERTY_EXTDEVICE_S structure describes an external device and its capabilities.</p>


## -syntax

````
typedef struct {
  KSPROPERTY Property;
  union {
    DEVCAPS Capabilities;
    ULONG   DevPort;
    ULONG   PowerState;
    WCHAR   pawchString[MAX_PATH];
    DWORD   NodeUniqueID[2];
  } u;
} KSPROPERTY_EXTDEVICE_S, *PKSPROPERTY_EXTDEVICE_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>u</b>

<dd>
<dl>

### -field <b>Capabilities</b>

<dd>
<p>Describes the external device's capabilities.</p>
</dd>

### -field <b>DevPort</b>

<dd>
<p>Specifies the external device's port. For example:</p>
<p>DEV_PORT_1394</p>
<p>DEV_PORT_USB</p>
</dd>

### -field <b>PowerState</b>

<dd>
<p>Specifies the external device's power state:</p>
<p>ED_POWER_ON</p>
<p>ED_POWER_STANDBY</p>
<p>ED_POWER_OFF</p>
</dd>

### -field <b>pawchString</b>

<dd>
<p>Specifies the external device's ID and version.</p>
</dd>

### -field <b>NodeUniqueID</b>

<dd>
<p>Specifies the external device's unique node Id.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>Any ED_Xxx or DEV_PORT_Xxx tokens are defined in <i>xprtdefs.h</i> in the Microsoft DirectX SDK.</p>

## -requirements
<table>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558699">DEVCAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_EXTDEVICE_S structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
