---
UID: NS.ksmedia.tagDEVCAPS
title: tagDEVCAPS
author: windows-driver-content
description: The DEVCAPS structure describes the capabilities of an external device.
old-location: stream\devcaps.htm
old-project: stream
ms.assetid: 4032ec5c-c98a-44f9-9c74-dc5ada308d33
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: tagDEVCAPS, DEVCAPS, *PDEVCAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Ksmedia.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVCAPS
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

# tagDEVCAPS structure



## -description
<p>The DEVCAPS structure describes the capabilities of an external device.</p>


## -syntax

````
typedef struct tagDEVCAPS {
  LONG CanRecord;
  LONG CanRecordStrobe;
  LONG HasAudio;
  LONG HasVideo;
  LONG UsesFiles;
  LONG CanSave;
  LONG DeviceType;
  LONG TCRead;
  LONG TCWrite;
  LONG CTLRead;
  LONG IndexRead;
  LONG Preroll;
  LONG Postroll;
  LONG SyncAcc;
  LONG NormRate;
  LONG CanPreview;
  LONG CanMonitorSrc;
  LONG CanTest;
  LONG VideoIn;
  LONG AudioIn;
  LONG Calibrate;
  LONG SeekType;
  LONG SimulatedHardware;
} DEVCAPS, *PDEVCAPS;
````


## -struct-fields
<dl>

### -field <b>CanRecord</b>

<dd>
<p>Specifies if the external device can record.</p>
</dd>

### -field <b>CanRecordStrobe</b>

<dd>
<p>For multitrack devices. Specifies if the external device can record. Switches currently recording tracks off and selected nonrecording track into record.</p>
</dd>

### -field <b>HasAudio</b>

<dd>
<p>Specifies if the external device has audio capabilities.</p>
</dd>

### -field <b>HasVideo</b>

<dd>
<p>Specifies if the external device has video capabilities.</p>
</dd>

### -field <b>UsesFiles</b>

<dd>
<p>Specifies if the external device uses files.</p>
</dd>

### -field <b>CanSave</b>

<dd>
<p>Specifies if the external device can save.</p>
</dd>

### -field <b>DeviceType</b>

<dd>
<p>Specifies the type of the external device. See Remarks.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ED_DEVTYPE_VCR</p>
</td>
<td>
<p>Video cassette recorder</p>
</td>
</tr>
<tr>
<td>
<p>ED_DEVTYPE_LASERDISC</p>
</td>
<td>
<p>Laserdisc player</p>
</td>
</tr>
<tr>
<td>
<p>ED_DEVTYPE_KEYBOARD</p>
</td>
<td>
<p>Keyboard</p>
</td>
</tr>
<tr>
<td>
<p>ED_DEVTYPE_CAMERA</p>
</td>
<td>
<p>Video camera</p>
</td>
</tr>
<tr>
<td>
<p>ED_DEVTYPE_VTR</p>
</td>
<td>
<p>Video tape recorder</p>
</td>
</tr>
<tr>
<td>
<p>ED_DEVTYPE_UNKNOWN</p>
</td>
<td>
<p>Unknown type</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>TCRead</b>

<dd>
<p>Specifies if the external device can read timecodes.</p>
</dd>

### -field <b>TCWrite</b>

<dd>
<p>Specifies if the external device can write timecodes.</p>
</dd>

### -field <b>CTLRead</b>

<dd>
<p>Specifies if the external device can read to a control track (nontimecode) target value.</p>
</dd>

### -field <b>IndexRead</b>

<dd>
<p>Specifies if the external device can read to an index (nontimecode) target value.</p>
</dd>

### -field <b>Preroll</b>

<dd>
<p>Specifies the external device's preroll time in the current time format.</p>
</dd>

### -field <b>Postroll</b>

<dd>
<p>Specifies the external device's postroll time in the current time format.</p>
</dd>

### -field <b>SyncAcc</b>

<dd>
<p>Indicates the external device's synchronization accuracy.</p>
</dd>

### -field <b>NormRate</b>

<dd>
<p>Specifies the external device's normal frame rate.</p>
</dd>

### -field <b>CanPreview</b>

<dd>
<p>Specifies if the external device can preview.</p>
</dd>

### -field <b>CanMonitorSrc</b>

<dd>
<p>Specifies if the external device can monitor source.</p>
</dd>

### -field <b>CanTest</b>

<dd>
<p>Indicates the implementation of the external device allows testing of methods/parameters by setting the high bit of a parameter that makes sense. This is not implemented an always returns FALSE.</p>
</dd>

### -field <b>VideoIn</b>

<dd>
<p>Indicates the external device accepts video as an input.</p>
</dd>

### -field <b>AudioIn</b>

<dd>
<p>Indicates the external device accepts audio as an input.</p>
</dd>

### -field <b>Calibrate</b>

<dd>
<p>Indicates if the external device requires calibrating.</p>
</dd>

### -field <b>SeekType</b>

<dd>
<p>Specifies the type of seeking the external device is capable of. For example:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>ED_SEEK_PERFECT</p>
</td>
<td>
<p>Indicates device can seek to within 1 video frame without a signal break (like a DDR).</p>
</td>
</tr>
<tr>
<td>
<p>ED_SEEK_FAST</p>
</td>
<td>
<p>Indicates device can seek quick with a short break in signal.</p>
</td>
</tr>
<tr>
<td>
<p>ED_SEEK_SLOW</p>
</td>
<td>
<p>Indicates slow seeking (like a tape transport).</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>SimulatedHardware</b>

<dd>
<p>Must be set to zero.</p>
</dd>
</dl>

## -remarks
<p>Any ED_Xxx tokens are defined in <i>xprtdefs.h</i> in the Microsoft DirectX SDK.</p>

<p>All members of the DEVCAPS structure are <b>TRUE</b>/<b>FALSE</b> unless otherwise specified.</p>

<p>The <b>DeviceType</b> member can be used by an application to detect the device type or its current operating mode. For example, it can return either ED_DEVTYPE_CAMERA or ED_DEVTYPE_VTR depending on a DV camcorder's mode of operation. Also, some DV devices may not be known and a device type of ED_DEVTYPE_UNKNOWN can be returned by the driver. This happens with some DV media converters.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568520">TIMECODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565156">KSPROPERTY_EXTDEVICE_S</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20DEVCAPS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
