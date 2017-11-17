---
UID: NS.irb._IDEREGISTERS
title: IDEREGISTERS
author: windows-driver-content
description: The IDEREGISTERS structure is used to report the contents of the IDE controller registers.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ideregisters.htm
ms.assetid: a3df8ce0-4414-49d1-a02c-3f5a3efc0de2
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: irb.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDEREGISTERS
req.alt-loc: irb.h
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
ms.keywords: IDEREGISTERS, IDEREGISTERS, *PIDEREGISTERS
req.iface: 
---

# IDEREGISTERS structure



## -description
<p>The IDEREGISTERS structure is used to report the contents of the IDE controller registers.</p>


## -syntax

````
typedef struct _IDEREGISTERS {
  UCHAR bFeaturesReg;
  UCHAR bSectorCountReg;
  UCHAR bSectorNumberReg;
  UCHAR bCylLowReg;
  UCHAR bCylHighReg;
  UCHAR bDriveHeadReg;
  UCHAR bCommandReg;
  UCHAR bReserved;
} IDEREGISTERS, *PIDEREGISTERS;
````


## -struct-fields
<dl>

### -field <b>bFeaturesReg</b>

<dd>
<p>Specifies the contents of the ATA features register.</p>
</dd>

### -field <b>bSectorCountReg</b>

<dd>
<p>Specifies the contents of the ATA Sector Count register.</p>
</dd>

### -field <b>bSectorNumberReg</b>

<dd>
<p>Specifies the contents of the ATA Sector Number register.</p>
</dd>

### -field <b>bCylLowReg</b>

<dd>
<p>Specifies the contents of the ATA Cylinder Low register.</p>
</dd>

### -field <b>bCylHighReg</b>

<dd>
<p>Specifies the contents of the ATA Cylinder High register.</p>
</dd>

### -field <b>bDriveHeadReg</b>

<dd>
<p>Specifies the contents of the ATA Device/Head register.</p>
</dd>

### -field <b>bCommandReg</b>

<dd>
<p>Specifies the contents of the ATA Command register.</p>
</dd>

### -field <b>bReserved</b>

<dd>
<p>Reserved for future use. The miniport driver shall not use this field.</p>
</dd>
</dl>

## -remarks
<p>The information reported in the IDEREGISTERS structure is intended to be a superset of the information contained in <a href="https://msdn.microsoft.com/library/windows/hardware/ff559015">IDEREGS</a>. Microsoft might expand the contents of the IDEREGISTERS structure in the future. If you need a structure whose size is stable across different versions of the operating system, you should use <b>IDEREGS</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559015">IDEREGS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20IDEREGISTERS structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
