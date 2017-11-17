---
UID: NS.ksmedia._KSPROPERTY_SPHLI
title: KSPROPERTY_SPHLI
author: windows-driver-content
description: The KSPROPERTY_SPHLI structure is used to describe a rectangle of subpicture or screen whose color or contrast is to be changed.
old-location: stream\ksproperty_sphli.htm
ms.assetid: e1ee8d13-7f83-4020-9f34-4b2c3626685b
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
req.alt-api: KSPROPERTY_SPHLI
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
ms.keywords: KSPROPERTY_SPHLI, KSPROPERTY_SPHLI, *PKSPROPERTY_SPHLI
req.iface: 
---

# KSPROPERTY_SPHLI structure



## -description
<p>The KSPROPERTY_SPHLI structure is used to describe a rectangle of subpicture or screen whose color or contrast is to be changed.</p>


## -syntax

````
typedef struct _KSPROPERTY_SPHLI {
  USHORT    HLISS;
  USHORT    Reserved;
  ULONG     StartPTM;
  ULONG     EndPTM;
  USHORT    StartX;
  USHORT    StartY;
  USHORT    StopX;
  USHORT    StopY;
  KS_COLCON ColCon;
} KSPROPERTY_SPHLI, *PKSPROPERTY_SPHLI;
````


## -struct-fields
<dl>

### -field <b>HLISS</b>

<dd>
<p>Indicates the highlight status of the current selection. A value of zero indicates that all highlights are invalid and the decoder should disable all highlights.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field <b>StartPTM</b>

<dd>
<p>Indicates the start of presentation time.</p>
</dd>

### -field <b>EndPTM</b>

<dd>
<p>Indicates the end of presentation time.</p>
</dd>

### -field <b>StartX</b>

<dd>
<p>Indicates the start x-coordinate pixel of the current highlight button.</p>
</dd>

### -field <b>StartY</b>

<dd>
<p>Indicates the start y-coordinate pixel of the current highlight button.</p>
</dd>

### -field <b>StopX</b>

<dd>
<p>Indicates the ending x-coordinate pixel of the current highlight button.</p>
</dd>

### -field <b>StopY</b>

<dd>
<p>Indicates the ending y-coordinate pixel of the current highlight button.</p>
</dd>

### -field <b>ColCon</b>

<dd>
<p>Specifies the color/contrast of the highlight rectangle.</p>
</dd>
</dl>

## -remarks
<p>The KSPROPERTY_SPHLI structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565150">KSPROPERTY_DVDSUBPIC_HLI</a> property.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565150">KSPROPERTY_DVDSUBPIC_HLI</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPROPERTY_SPHLI structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
