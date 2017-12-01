---
UID: NS.ksmedia.PKSPROPERTY_TUNER_SCAN_STATUS_S
title: PKSPROPERTY_TUNER_SCAN_STATUS_S
author: windows-driver-content
description: The KSPROPERTY_TUNER_SCAN_STATUS_S structure describes status for a scanning operation.
old-location: stream\ksproperty_tuner_scan_status_s.htm
old-project: stream
ms.assetid: b09373ef-7b65-46f7-b5b7-a6dcecf0166c
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PKSPROPERTY_TUNER_SCAN_STATUS_S, KSPROPERTY_TUNER_SCAN_STATUS_S, *PKSPROPERTY_TUNER_SCAN_STATUS_S
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_TUNER_SCAN_STATUS_S
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
req.iface: 
---

# PKSPROPERTY_TUNER_SCAN_STATUS_S structure



## -description
<p>The KSPROPERTY_TUNER_SCAN_STATUS_S structure describes status for a scanning operation.</p>


## -syntax

````
typedef struct {
  KSPROPERTY    Property;
  TunerLockType LockStatus;
  ULONG         CurrentFrequency;
} KSPROPERTY_TUNER_SCAN_STATUS_S, *PKSPROPERTY_TUNER_SCAN_STATUS_S;
````


## -struct-fields
<dl>

### -field <b>Property</b>

<dd>
<p>Specifies an initialized <a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a> structure that describes the property set, property ID, and request type.</p>
</dd>

### -field <b>LockStatus</b>

<dd>
<p>One of the following values from the <b>TunerLockType</b> enumeration that indicates the lock status of the scanning operation.</p>
<table>
<tr>
<th>Status</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p><b>Tuner_LockType_None</b> (0x00)</p>
</td>
<td>
<p>The tuner is not locked on a signal. The driver can return this value at the end of a scan.</p>
</td>
</tr>
<tr>
<td>
<p><b>Tuner_LockType_Within_Scan_Sensing_Range</b> (0x01)</p>
</td>
<td>
<p>The signal is nearby; however, the driver cannot report the exact frequency.</p>
</td>
</tr>
<tr>
<td>
<p><b>Tuner_LockType_Locked</b> (0x02)</p>
</td>
<td>
<p>A fine-tune signal lock was established. The driver can return this value at the end of a scan.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CurrentFrequency</b>

<dd>
<p>The current locked-in frequency, in Hz, on the tuning device. </p>
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
<p>Available in Windows Vista and later versions of the operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561898">KSEVENT_TUNER_INITIATE_SCAN</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ikscontrol-ksproperty.md">KSPROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567800">PROPSETID_TUNER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565893">KSPROPERTY_TUNER_SCAN_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_TUNER_SCAN_STATUS_S structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
