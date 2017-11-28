---
UID: NS.ksmedia.PKSAUDIO_MICROPHONE_COORDINATES
title: PKSAUDIO_MICROPHONE_COORDINATES
author: windows-driver-content
description: The KSAUDIO_MICROPHONE_COORDINATES structure specifies the type and the coordinates of a single microphone in the microphone array.
old-location: audio\ksaudio_microphone_coordinates.htm
old-project: audio
ms.assetid: 443fb3c0-0e75-4abc-b44f-047752b3cab7
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PKSAUDIO_MICROPHONE_COORDINATES, KSAUDIO_MICROPHONE_COORDINATES, *PKSAUDIO_MICROPHONE_COORDINATES
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
req.alt-api: KSAUDIO_MICROPHONE_COORDINATES
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

# PKSAUDIO_MICROPHONE_COORDINATES structure



## -description
<p>The KSAUDIO_MICROPHONE_COORDINATES structure specifies the type and the coordinates of a single microphone in the microphone array.</p>


## -syntax

````
typedef struct {
  USHORT usType;
  SHORT  wXCoord;
  SHORT  wYCoord;
  SHORT  wZCoord;
  SHORT  wVerticalAngle;
  SHORT  wHorizontalAngle;
} KSAUDIO_MICROPHONE_COORDINATES, *PKSAUDIO_MICROPHONE_COORDINATES;
````


## -struct-fields
<dl>

### -field <b>usType</b>

<dd>
<p>Specifies the type of microphone in use at this coordinate location. The value of this member is one of the <b>KSMICARRAY_MICTYPE</b> enumeration values shown in the following table.</p>
<table>
<tr>
<td>
<p><b>Value</b></p>
</td>
<td>
<p><b>Microphone type</b></p>
</td>
</tr>
<tr>
<td>
<p>KSMICARRAY_MICTYPE_OMNIDIRECTIONAL</p>
</td>
<td>
<p>Omni directional</p>
</td>
</tr>
<tr>
<td>
<p>KSMICARRAY_MICTYPE_SUBCARDIOID</p>
</td>
<td>
<p>Sub cardioid</p>
</td>
</tr>
<tr>
<td>
<p>KSMICARRAY_MICTYPE_CARDIOID</p>
</td>
<td>
<p>Cardioid</p>
</td>
</tr>
<tr>
<td>
<p>KSMICARRAY_MICTYPE_SUPERCARDIOID</p>
</td>
<td>
<p>Super cardioid</p>
</td>
</tr>
<tr>
<td>
<p>KSMICARRAY_MICTYPE_HYPERCARDIOID</p>
</td>
<td>
<p>Hyper cardioid</p>
</td>
</tr>
<tr>
<td>
<p>KSMICARRAY_MICTYPE_8SHAPED</p>
</td>
<td>
<p>8-shaped</p>
</td>
</tr>
<tr>
<td>
<p>KSMICARRAY_MICTYPE_VENDORDEFINED</p>
</td>
<td>
<p>0x0F</p>
</td>
</tr>
</table>
<p> </p>
<p>If the microphone is of type KSMICARRAY_MICTYPE_VENDORDEFINED, the value must be set to 0x0F. Additionally, the most significant bits will further define the type of microphone.</p>
</dd>

### -field <b>wXCoord</b>

<dd>
<p>Specifies the signed X-coordinate of the microphone, in millimeters. Acceptable values range from -32768 to 32767, inclusive.</p>
</dd>

### -field <b>wYCoord</b>

<dd>
<p>Specifies the signed Y-coordinate of the microphone, in millimeters. Acceptable values range from -32768 to 32767, inclusive.</p>
</dd>

### -field <b>wZCoord</b>

<dd>
<p>Specifies the signed Z-coordinate of the microphone, in millimeters. Acceptable values range from -32768 to 32767, inclusive.</p>
</dd>

### -field <b>wVerticalAngle</b>

<dd>
<p>Specifies a value between -15708 and +15708.  When divided by 10,000, it gives a radian angle measurement.</p>
</dd>

### -field <b>wHorizontalAngle</b>

<dd>
<p>Specifies a value between -31416 and +31416.  When divided by 10,000, it gives a radian angle measurement.</p>
</dd>
</dl>

## -remarks
<p>To better understand the descriptions for <i>wHorizontalAngle</i>  and <i>wVericalAngle</i>, consider the following diagram:</p>

<p>Let <b>x</b> be the axis which points from the center of the microphone array toward the most probable location of the user - that is, perpendicular to the screen.  Positive is toward the user, negative is behind the screen. Let <b>y</b> by the horizontal axis perpendicular to the x-axis - that is, from the left of the screen to the right.  Positive is to the user's right; negative is to the user's left. Let <b>z</b> be the vertical axis.</p>

<p>Now assume that there are three microphones in the array, as shown in the preceding diagram. And assume also, that one of the microphones (<b>Mic 1</b>) is pointed in a horizontal direction that is not parallel to the x-axis, as indicated by the blue center line through <b>Mic 1</b>. Now when you imagine a line that runs through the origin (0,0,0) of the (x,y,z) coordinate system and is parallel to the center line of <b>Mic 1</b>, you will find that there is a horizontal angle between the positive x-axis and the projection of the mic’s center line onto the x-y plane. This angle is represented by <i>wHorizontalAngle</i>.</p>

<p>If one of the microphones, for example <b>Mic 1</b>, happens to be dipped downward, or raised up, then this microphone would also have a vertical angle between its center line and the projection of its center line onto the x-y plane. This angle is represented by <i>wVericalAngle</i>.</p>

<p>For more information about how to process a microphone array in Windows, see <a href="http://go.microsoft.com/fwlink/p/?linkid=8751">Audio Technologies for Windows </a> and refer to the following white papers:</p><dl>
<dd>
<p><a href="http://go.microsoft.com/fwlink/p/?linkid=120592">Microphone Array Support in Windows Vista</a></p>
</dd>
<dd>
<p><a href="http://go.microsoft.com/fwlink/p/?linkid=120593">How to Build and Use Microphone Arrays for Windows Vista</a></p>
</dd>
</dl><p><a href="http://go.microsoft.com/fwlink/p/?linkid=120592">Microphone Array Support in Windows Vista</a></p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=120593">How to Build and Use Microphone Arrays for Windows Vista</a></p>

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