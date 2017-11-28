---
UID: NS.hpmi._HPMI_BATTERY_UTILIZATION_HINT
title: HPMI_BATTERY_UTILIZATION_HINT
author: windows-driver-content
description: This hint indicates if the OEM Battery Manager should attempt to save as much charge as possible in the non-hot swappable batteries (i.e.
old-location: powermeter\hpmi_battery_utilization_hint.htm
old-project: powermeter
ms.assetid: A974998F-C9AF-496E-88B1-510413C17C4A
ms.author: windowsdriverdev
ms.date: 11/6/2017
ms.keywords: HPMI_BATTERY_UTILIZATION_HINT, HPMI_BATTERY_UTILIZATION_HINT, *PHPMI_BATTERY_UTILIZATION_HINT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hpmi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10, version 1709 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HPMI_BATTERY_UTILIZATION_HINT
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

# HPMI_BATTERY_UTILIZATION_HINT structure



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>This hint indicates if the OEM Battery Manager should attempt to save as
	much charge as possible in the non-hot swappable batteries (i.e. the
	batteries are generally referred to as "internal batteries", these
	batteries cannot be removed while system is operational).
</p>


## -syntax

````
typedef struct _HPMI_BATTERY_UTILIZATION_HINT {
  ULONG          Version;
  HPMI_HINT_BOOL PreserveNonHotSwappableBatteries;
} HPMI_BATTERY_UTILIZATION_HINT, *PHPMI_BATTERY_UTILIZATION_HINT;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Set to HPMI_BATTERY_UTILIZATION_HINT_VERSION_1.</p>
</dd>

### -field <b>PreserveNonHotSwappableBatteries</b>

<dd>
<p> Interpretation of values:</p>
<p>
    - HpmiBoolUnavailable:
    Battery utilization hint is unavailable at the moment.
</p>
<p>  - HpmiBoolFalse:
    It is not necessary to preserve charge in the internal batteries
	at the moment.
</p>
<p>- HpmiBoolTrue:
    Every attempt should be made to save as much charge as possible in
    the internal batteries.</p>
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
<dt>Hpmi.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hpmi\ne-hpmi--hpmi-hint-bool.md">HPMI_HINT_BOOL</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [powermeter\powermeter]:%20HPMI_BATTERY_UTILIZATION_HINT structure%20 RELEASE:%20(11/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
