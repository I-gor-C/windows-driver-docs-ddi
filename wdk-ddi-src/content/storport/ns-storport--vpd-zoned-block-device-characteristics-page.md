---
UID: NS.storport._VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE
title: VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE
author: windows-driver-content
description: Note  This structure is for internal use only and should not be called from your code. .
old-location: storage\vpd_zoned_block_device_characteristics_page.htm
old-project: storage
ms.assetid: 9b1f83fd-e367-4b0d-8f93-24f35d9a5fd8
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE, VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE, *PVPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: storport.h
req.include-header: Minitape.h, Storport.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE
req.alt-loc: scsi.h
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
req.product: Windows 10 or later.
---

# VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure



## -description
<p>
<div class="alert"><b>Note</b>  This  structure is for internal use only and should not be called from your code.</div>
<div> </div>
</p>


## -syntax

````
typedef struct _VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE {
  UCHAR  DeviceType  :5;
  UCHAR  DeviceTypeQualifier  :3;
  UCHAR  PageCode;
  UCHAR  PageLength[2];
  UCHAR  URSWRZ  :1;
  UCHAR  Reserved1  :7;
  UCHAR  Reserved2[3];
  UCHAR  OptimalNumberOfOpenSequentialWritePreferredZone[4];
  UCHAR  OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZone[4];
  UCHAR  MaxNumberOfOpenSequentialWriteRequiredZone[4];
  UCHAR  Reserved3[44];
} VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE, *PVPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE;
````


## -struct-fields
<dl>

### -field DeviceType

<dd>
<p>N/A</p>
</dd>

### -field DeviceTypeQualifier

<dd>
<p>N/A</p>
</dd>

### -field PageCode

<dd>
<p>N/A</p>
</dd>

### -field PageLength

<dd>
<p>N/A</p>
</dd>

### -field URSWRZ

<dd>
<p>N/A</p>
</dd>

### -field Reserved1

<dd>
<p>N/A</p>
</dd>

### -field Reserved2

<dd>
<p>N/A</p>
</dd>

### -field OptimalNumberOfOpenSequentialWritePreferredZone

<dd>
<p>N/A</p>
</dd>

### -field OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZone

<dd>
<p>N/A</p>
</dd>

### -field MaxNumberOfOpenSequentialWriteRequiredZone

<dd>
<p>N/A</p>
</dd>

### -field Reserved3

<dd>
<p>N/A</p>
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
<dt>Scsi.h (include Minitape.h or Storport.h)</dt>
</dl>
</td>
</tr>
</table>