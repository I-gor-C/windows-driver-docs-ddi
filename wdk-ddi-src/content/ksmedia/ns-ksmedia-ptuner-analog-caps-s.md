---
UID: NS.ksmedia.PTUNER_ANALOG_CAPS_S
title: PTUNER_ANALOG_CAPS_S
author: windows-driver-content
description: The TUNER_ANALOG_CAPS_S structure describes the hardware scanning capabilities of a tuning device that supports an analog broadcast network.
old-location: stream\tuner_analog_caps_s.htm
ms.assetid: 350ec4b2-a96a-420a-bb52-d09cc8c5029e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: stream
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TUNER_ANALOG_CAPS_S
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
ms.keywords: PTUNER_ANALOG_CAPS_S, TUNER_ANALOG_CAPS_S, *PTUNER_ANALOG_CAPS_S
req.iface: 
---

# PTUNER_ANALOG_CAPS_S structure



## -description
<p>The TUNER_ANALOG_CAPS_S structure describes the hardware scanning capabilities of a tuning device that supports an analog broadcast network.</p>


## -syntax

````
typedef struct {
  ULONG Mode;
  ULONG StandardsSupported;
  ULONG MinFrequency;
  ULONG MaxFrequency;
  ULONG TuningGranularity;
  ULONG SettlingTime;
  ULONG ScanSensingRange;
  ULONG FineTuneSensingRange;
} TUNER_ANALOG_CAPS_S, *PTUNER_ANALOG_CAPS_S;
````


## -struct-fields
<dl>

### -field <b>Mode</b>

<dd>
<p>The current tuner mode, which can be represented by one of the following tuner mode flags from the KSPROPERTY_TUNER_MODES enumeration that is defined in <i>Ksmedia.h.</i></p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>KSPROPERTY_TUNER_MODE_TV</p>
</td>
<td>
<p>The tuner is currently tuning broadcast or cable television channels.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_TUNER_MODE_FM_RADIO</p>
</td>
<td>
<p>The tuner is currently tuning FM radio channels.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_TUNER_MODE_AM_RADIO</p>
</td>
<td>
<p>The tuner is currently tuning AM radio channels.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_TUNER_MODE_DSS</p>
</td>
<td>
<p>The tuner is currently tuning DSS channels.</p>
</td>
</tr>
<tr>
<td>
<p>KSPROPERTY_TUNER_MODE_ATSC</p>
</td>
<td>
<p>The tuner is capable of tuning Advanced Television Systems Committee broadcasts (Digital TV for the United States). This setting can also be used by DVB-T and DVB-C systems.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>StandardsSupported</b>

<dd>
<p>If the <b>Mode</b> member is set to KSPROPERTY_TUNER_MODE_TV or KSPROPERTY_TUNER_MODE_DSS, a bitwise OR of values from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567297">KS_AnalogVideoStandard</a> enumeration that indicates the analog video standards that the tuner supports. Otherwise, this member is ignored.</p>
</dd>

### -field <b>MinFrequency</b>

<dd>
<p>The lowest frequency, in Hz, that the tuner supports. </p>
</dd>

### -field <b>MaxFrequency</b>

<dd>
<p>The highest frequency, in Hz, that the tuner supports. </p>
</dd>

### -field <b>TuningGranularity</b>

<dd>
<p>The smallest possible step size, in Hz, between two settings of the tuning frequency. </p>
</dd>

### -field <b>SettlingTime</b>

<dd>
<p>The time, in milliseconds, for a new frequency setting to become stable.</p>
<p><i>KsTvTune.ax</i> uses the value in <b>SettlingTime</b> to evaluate the total time its scanning algorithm might take so that it can determine wait time. The value in <b>SettlingTime</b> along with the number of stepping increments in the entire frequency range that is based on the sensing range should provide an estimate of the total time that is required for the scanning algorithm. </p>
</dd>

### -field <b>ScanSensingRange</b>

<dd>
<p>The range that the tuning device provides and that the tuner filter uses to determine the presence of a signal. This range represents the larger step sizes that a signal search algorithm can use to advance through the range of frequencies to search. The driver can report the actual lock frequency of a signal and the lock status on the signal through a call to the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff565893">KSPROPERTY_TUNER_SCAN_STATUS</a> property. If the driver reports the lock status as Tuner_LockType_Within_Scan_Sensing_Range in the <b>LockStatus</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565898">KSPROPERTY_TUNER_SCAN_STATUS_S</a> structure, the increment step size changes to the smaller value in <b>FineTuneSensingRange</b> until the actual lock frequency is determined. </p>
</dd>

### -field <b>FineTuneSensingRange</b>

<dd>
<p>The range that the tuning device provides and that the tuner filter uses to determine the actual frequency of a signal. The tuner filter uses this fine-tune-sensing range only when the underlying tuner hardware cannot support hardware-assisted scanning. The driver indicates such support by setting the <b>fSupportsHardwareAssistedScanning</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565892">KSPROPERTY_TUNER_SCAN_CAPS_S</a> structure to <b>TRUE</b> in a call to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff565887">KSPROPERTY_TUNER_SCAN_CAPS</a> property. When the tuner filter starts a scan, it initially probes the driver in increments within the range that the <b>ScanSensingRange</b> member specifies until the driver returns Tuner_LockType_Within_Scan_Sensing_Range. The tuner filter then switches into steps of <b>FineTuneSensingRange</b> until the driver reports a complete lock. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567297">KS_AnalogVideoStandard</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565887">KSPROPERTY_TUNER_SCAN_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565892">KSPROPERTY_TUNER_SCAN_CAPS_S</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565893">KSPROPERTY_TUNER_SCAN_STATUS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565898">KSPROPERTY_TUNER_SCAN_STATUS_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20TUNER_ANALOG_CAPS_S structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
