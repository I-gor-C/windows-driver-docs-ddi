---
UID: NS.scsi._VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE
title: VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE
author: windows-driver-content
description: Note  This structure is for internal use only and should not be called from your code. .
old-location: storage\vpd_zoned_block_device_characteristics_page.htm
ms.assetid: 9b1f83fd-e367-4b0d-8f93-24f35d9a5fd8
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: scsi.h
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
req.irql: <= APC_LEVEL
ms.keywords: VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE, VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE, *PVPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE
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

### -field <b>DeviceType</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>DeviceTypeQualifier</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>PageCode</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>PageLength</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>URSWRZ</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>OptimalNumberOfOpenSequentialWritePreferredZone</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>OptimalNumberOfNonSequentiallyWrittenSequentialWritePreferredZone</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>MaxNumberOfOpenSequentialWriteRequiredZone</b>

<dd>
<p>N/A</p>
</dd>

### -field <b>Reserved3</b>

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