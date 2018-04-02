---
UID: NS:ksmedia.tagDEVCAPS
title: tagDEVCAPS
author: windows-driver-content
description: The DEVCAPS structure describes the capabilities of an external device.
old-location: stream\devcaps.htm
old-project: stream
ms.assetid: 4032ec5c-c98a-44f9-9c74-dc5ada308d33
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PDEVCAPS, DEVCAPS, DEVCAPS structure [Streaming Media Devices], PDEVCAPS, PDEVCAPS structure pointer [Streaming Media Devices], ksmedia/DEVCAPS, ksmedia/PDEVCAPS, stream.devcaps, tagDEVCAPS, vidcapstruct_61cce92e-4f74-48ff-ae84-72579136a64f.xml"
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ksmedia.h
api_name:
-	DEVCAPS
product:
- Windows
targetos: Windows
req.typenames: DEVCAPS, *PDEVCAPS
---

# tagDEVCAPS structure
The DEVCAPS structure describes the capabilities of an external device.

## Syntax
```
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
```

## Members


`CanRecord`

Specifies if the external device can record.

`CanRecordStrobe`

For multitrack devices. Specifies if the external device can record. Switches currently recording tracks off and selected nonrecording track into record.

`HasAudio`

Specifies if the external device has audio capabilities.

`HasVideo`

Specifies if the external device has video capabilities.

`UsesFiles`

Specifies if the external device uses files.

`CanSave`

Specifies if the external device can save.

`DeviceType`

Specifies the type of the external device. See Remarks.

<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
ED_DEVTYPE_VCR

</td>
<td>
Video cassette recorder

</td>
</tr>
<tr>
<td>
ED_DEVTYPE_LASERDISC

</td>
<td>
Laserdisc player

</td>
</tr>
<tr>
<td>
ED_DEVTYPE_KEYBOARD

</td>
<td>
Keyboard

</td>
</tr>
<tr>
<td>
ED_DEVTYPE_CAMERA

</td>
<td>
Video camera

</td>
</tr>
<tr>
<td>
ED_DEVTYPE_VTR

</td>
<td>
Video tape recorder

</td>
</tr>
<tr>
<td>
ED_DEVTYPE_UNKNOWN

</td>
<td>
Unknown type

</td>
</tr>
</table>

`TCRead`

Specifies if the external device can read timecodes.

`TCWrite`

Specifies if the external device can write timecodes.

`CTLRead`

Specifies if the external device can read to a control track (nontimecode) target value.

`IndexRead`

Specifies if the external device can read to an index (nontimecode) target value.

`Preroll`

Specifies the external device's preroll time in the current time format.

`Postroll`

Specifies the external device's postroll time in the current time format.

`SyncAcc`

Indicates the external device's synchronization accuracy.

`NormRate`

Specifies the external device's normal frame rate.

`CanPreview`

Specifies if the external device can preview.

`CanMonitorSrc`

Specifies if the external device can monitor source.

`CanTest`

Indicates the implementation of the external device allows testing of methods/parameters by setting the high bit of a parameter that makes sense. This is not implemented an always returns FALSE.

`VideoIn`

Indicates the external device accepts video as an input.

`AudioIn`

Indicates the external device accepts audio as an input.

`Calibrate`

Indicates if the external device requires calibrating.

`SeekType`

Specifies the type of seeking the external device is capable of. For example:

<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
ED_SEEK_PERFECT

</td>
<td>
Indicates device can seek to within 1 video frame without a signal break (like a DDR).

</td>
</tr>
<tr>
<td>
ED_SEEK_FAST

</td>
<td>
Indicates device can seek quick with a short break in signal.

</td>
</tr>
<tr>
<td>
ED_SEEK_SLOW

</td>
<td>
Indicates slow seeking (like a tape transport).

</td>
</tr>
</table>

`SimulatedHardware`

Must be set to zero.

## Remarks
Any ED_Xxx tokens are defined in <i>xprtdefs.h</i> in the Microsoft DirectX SDK.

All members of the DEVCAPS structure are <b>TRUE</b>/<b>FALSE</b> unless otherwise specified.

The <b>DeviceType</b> member can be used by an application to detect the device type or its current operating mode. For example, it can return either ED_DEVTYPE_CAMERA or ED_DEVTYPE_VTR depending on a DV camcorder's mode of operation. Also, some DV devices may not be known and a device type of ED_DEVTYPE_UNKNOWN can be returned by the driver. This happens with some DV media converters.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ksmedia.h (include Ksmedia.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff565156">KSPROPERTY_EXTDEVICE_S</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff568520">TIMECODE</a>