---
UID: NE.sensorsclassextension.MagnetometerAccuracy
title: MagnetometerAccuracy
author: windows-driver-content
description: Specifies the accuracy of the magnetometer.
old-location: sensors\magnetometeraccuracy.htm
old-project: sensors
ms.assetid: DC495EFB-3522-4220-87F8-3DB501831D6E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: SDP_TREE_ROOT_NODE, SDP_TREE_ROOT_NODE, *PSDP_TREE_ROOT_NODE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: sensorsclassextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1,Available in Windows 8.1.
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MagnetometerAccuracy
req.alt-loc: SensorsClassExtension.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# MagnetometerAccuracy enumeration



## -description
<p>Specifies the accuracy of the magnetometer.</p>


## -syntax

````
typedef enum _MagnetometerAccuracy { 
  Unknown      = 0,
  Unreliable   = 1,
  Approximate  = 2,
  High         = 3
} MagnetometerAccuracy;
````


## -enum-fields
<dl>

### -field <a id="Unknown"></a><a id="unknown"></a><a id="UNKNOWN"></a><b>Unknown</b>

<dd>
<p>The accuracy is currently not available, typically because the driver can't report it.</p>
</dd>

### -field <a id="Unreliable"></a><a id="unreliable"></a><a id="UNRELIABLE"></a><b>Unreliable</b>

<dd>
<p>The reported values have a high degree of inaccuracy. Apps should always ask the user to calibrate the device whenever this value is returned.</p>
</dd>

### -field <a id="Approximate"></a><a id="approximate"></a><a id="APPROXIMATE"></a><b>Approximate</b>

<dd>
<p>          The actual and reported values differ but may be accurate enough for some applications. Apps that only need a relative value, like a virtual reality app, can continue without additional calibration.</p>
</dd>

### -field <a id="High"></a><a id="high"></a><a id="HIGH"></a><b>High</b>

<dd>
<p>          The actual and reported values are accurate. No additional calibration is needed.</p>
</dd>
</dl>

## -remarks
<p>Device drivers that support magnetometer accuracy should only report the <b>Unreliable</b>, <b>Approximate</b>, and <b>High</b> values.</p>

<p>Apps that need calibration may periodically ask the user to calibrate the device. We suggest doing this once every 10 minutes.</p>

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
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 8.1.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>SensorsClassExtension.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn946698">Sensor Properties</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20MagnetometerAccuracy enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
