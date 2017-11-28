---
UID: NE.hpmi._HPMI_HINT_BOOL
title: HPMI_HINT_BOOL
author: windows-driver-content
description: Boolean type value used to track availability of HPMI hint data.
old-location: powermeter\hpmi_hint_bool.htm
old-project: powermeter
ms.assetid: E056400C-A0FE-4740-945D-C529C8804DF3
ms.author: windowsdriverdev
ms.date: 11/6/2017
ms.keywords: HIDD_ATTRIBUTES, HIDD_ATTRIBUTES, *PHIDD_ATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: hpmi.h
req.include-header: Hpmi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10, version 1709 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HPMI_HINT_BOOL
req.alt-loc: hpmi.h
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

# HPMI_HINT_BOOL enumeration



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Boolean type value used to track availability of HPMI hint data. </p>


## -syntax

````
typedef enum _HPMI_HINT_BOOL { 
  HpmiBoolUnavailable  = 0,
  HpmiBoolFalse        = ,
  HpmiBoolTrue         = ,
  HpmiBoolMax          = 
} HPMI_HINT_BOOL;
````


## -enum-fields
<dl>

### -field <a id="HpmiBoolUnavailable"></a><a id="hpmiboolunavailable"></a><a id="HPMIBOOLUNAVAILABLE"></a><b>HpmiBoolUnavailable</b>

<dd>
<p>No data is available.</p>
</dd>

### -field <a id="HpmiBoolFalse"></a><a id="hpmiboolfalse"></a><a id="HPMIBOOLFALSE"></a><b>HpmiBoolFalse</b>

<dd>
<p>Condition is asserted to be false.
</p>
</dd>

### -field <a id="HpmiBoolTrue"></a><a id="hpmibooltrue"></a><a id="HPMIBOOLTRUE"></a><b>HpmiBoolTrue</b>

<dd>
<p>Condition is asserted to be true.
</p>
</dd>

### -field <a id="HpmiBoolMax"></a><a id="hpmiboolmax"></a><a id="HPMIBOOLMAX"></a><b>HpmiBoolMax</b>

<dd>
<p>Value is not used. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 10, version 1709 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hpmi.h (include Hpmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hpmi\ns-hpmi--hpmi-battery-utilization-hint.md">HPMI_BATTERY_UTILIZATION_HINT</a>
</dt>
<dt>
<a href="..\hpmi\ni-hpmi-ioctl-hpmi-battery-utilization-hint.md">IOCTL_HPMI_BATTERY_UTILIZATION_HINT</a>
</dt>
<dt>
<a href="powermeter.hpmi_h">hpmi.h</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [powermeter\powermeter]:%20HPMI_HINT_BOOL enumeration%20 RELEASE:%20(11/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
