---
UID: NS.ksmedia._KSCAMERA_PROFILE_MEDIAINFO
title: KSCAMERA_PROFILE_MEDIAINFO
author: windows-driver-content
description: This structure contains the relevant media type information presented for each camera profile.
old-location: stream\kscamera_profile_mediainfo.htm
old-project: stream
ms.assetid: 55B9F032-A3F5-434E-9EB6-CB832DC0EB45
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KSCAMERA_PROFILE_MEDIAINFO, KSCAMERA_PROFILE_MEDIAINFO, *PKSCAMERA_PROFILE_MEDIAINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSCAMERA_PROFILE_MEDIAINFO
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

# KSCAMERA_PROFILE_MEDIAINFO structure



## -description
<p>This structure contains the relevant media type information presented for each camera profile.</p>


## -syntax

````
typedef struct _KSCAMERA_PROFILE_MEDIAINFO {
  struct {
    UINT32 X;
    UINT32 Y;
  } Resolution;
  struct {
    UINT32 Numerator;
    UINT32 Denominator;
  } MaxFrameRate;
  ULONGLONG Flags;
  UINT32    Data0;
  UINT32    Data1;
  UINT32    Data2;
  UINT32    Data3;
} KSCAMERA_PROFILE_MEDIAINFO, *PKSCAMERA_PROFILE_MEDIAINFO;
````


## -struct-fields
<dl>

### -field Resolution

<dd>
<p>The X (horizontal) and Y (vertical) frame size in pixels.</p>
</dd>

### -field MaxFrameRate

<dd>
<p>The numerator/denominator ratio of frame rate (for example, 30 / 1 = 30fps).  This frame rate represents the maximum frame rate of the specified resolution under ideal lighting conditions.  Actual frame rate may be lower than this value.</p>
<p>For photo media information, if photo sequence cannot be enabled because of hardware constraints for the given photo resolution, the frame rate must be set to 0 (numerator=0, denominator=0).  This will inform the application layer that photo sequence control will be rejected by the driver when that particular photo media type is selected.</p>
</dd>

### -field Flags

<dd>
<p>The  bitwise OR of one or more of the following flags:</p>
<ul>
<li>KSCAMERAPROFILE_FLAGS_VIDEOHDR<p>When the video HDR flag is set for the media info, for that media setting, video HDR may be enabled for the record stream.</p>
<p>This flag may not be set for media info on the photo pin.</p>
</li>
<li>KSCAMERAPROFILE_FLAGS_VARIABLEPHOTOSEQUENCE<p>When the Variable Photo Sequence flag is set for the media info, VPS support is available even if the photo media info does not provide a frame rate.</p>
<p>If this flag is set and the frame rate is non-zero, for that photo media info, VPS and Photo Sequence is available.</p>
<p>If this flag is set and the frame rate is zero, for that photo media info, VPS is available but not Photo Sequence.</p>
<p>If this flag is not set and the  frame rate is non-zero, for that photo media info, VPS is not available but Photo Sequence is available.</p>
<p>If  this flag is not set and the frame rate is zero, neither VPS nor Photo Sequence is available for that media info.</p>
<p>This flag may only be set for media info on the photo pin.  Presence of this flag on non-photo pin media info will result in the profile set being rejected.</p>
</li>
</ul>
</dd>

### -field Data0

<dd>
<p>Reserved. Must be set to 0.</p>
</dd>

### -field Data1

<dd>
<p>Reserved. Must be set to 0.</p>
</dd>

### -field Data2

<dd>
<p>Reserved. Must be set to 0.</p>
</dd>

### -field Data3

<dd>
<p>Reserved. Must be set to 0.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>