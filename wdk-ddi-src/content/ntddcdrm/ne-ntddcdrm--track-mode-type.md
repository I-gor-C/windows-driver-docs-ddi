---
UID: NE.ntddcdrm._TRACK_MODE_TYPE
title: TRACK_MODE_TYPE
author: windows-driver-content
description: The TRACK_MODE_TYPE enumeration type is used in conjunction with the IOCTL_CDROM_RAW_READ request and the RAW_READ_INFO structure to read data from a CD-ROM in raw mode.
old-location: storage\track_mode_type.htm
ms.assetid: ea7d7b5a-625f-41f7-b3fd-96a6bf338db9
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TRACK_MODE_TYPE
req.alt-loc: ntddcdrm.h
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
ms.keywords: OUTPUT_PACKET, OUTPUT_PACKET, *POUTPUT_PACKET
req.iface: 
---

# TRACK_MODE_TYPE enumeration



## -description
<p>The TRACK_MODE_TYPE enumeration type is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559361">IOCTL_CDROM_RAW_READ</a> request and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563958">RAW_READ_INFO</a> structure to read data from a CD-ROM in raw mode.  </p>


## -syntax

````
typedef enum _TRACK_MODE_TYPE { 
  YellowMode2          = 0,
  XAForm2              = 1,
  CDDA                 = 2,
  RawWithC2AndSubCode  = 3,
  RawWithC2            = 4,
  RawWithSubCode       = 5
} TRACK_MODE_TYPE, *PTRACK_MODE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="YellowMode2"></a><a id="yellowmode2"></a><a id="YELLOWMODE2"></a><b>YellowMode2</b>

<dd>
<p>Indicates that CD-ROM mode should be used. This mode is used with read-only 120 mm Optical Data Discs (CD-ROM). For more information, see the ISO/IEC 10149 specification.</p>
</dd>

### -field <a id="XAForm2"></a><a id="xaform2"></a><a id="XAFORM2"></a><b>XAForm2</b>

<dd>
<p>Indicates that compact disc read-only memory extended architecture mode should be used. For more information see the specification for CD-ROM XA published by NV Philips and Sony Corporation.</p>
</dd>

### -field <a id="CDDA"></a><a id="cdda"></a><b>CDDA</b>

<dd>
<p>Indicates that digital audio information mode should be used. For more information, see the IEC 908:1987 specification.</p>
</dd>

### -field <a id="RawWithC2AndSubCode"></a><a id="rawwithc2andsubcode"></a><a id="RAWWITHC2ANDSUBCODE"></a><b>RawWithC2AndSubCode</b>

<dd>
<p>CD_RAW_SECTOR_WITH_C2_AND_SUBCODE_SIZE per sector</p>
</dd>

### -field <a id="RawWithC2"></a><a id="rawwithc2"></a><a id="RAWWITHC2"></a><b>RawWithC2</b>

<dd>
<p>CD_RAW_SECTOR_WITH_C2_SIZE per sector</p>
</dd>

### -field <a id="RawWithSubCode"></a><a id="rawwithsubcode"></a><a id="RAWWITHSUBCODE"></a><b>RawWithSubCode</b>

<dd>
<p>CD_RAW_SECTOR_WITH_SUBCODE_SIZE per sector</p>
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
<dt>Ntddcdrm.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559361">IOCTL_CDROM_RAW_READ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563958">RAW_READ_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20TRACK_MODE_TYPE enumeration%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
