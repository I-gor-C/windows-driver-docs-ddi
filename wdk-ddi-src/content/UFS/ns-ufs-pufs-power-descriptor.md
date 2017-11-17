---
UID: NS.ufs.PUFS_POWER_DESCRIPTOR
title: PUFS_POWER_DESCRIPTOR
author: windows-driver-content
description: UFS_POWER_DESCRIPTOR contains information about the power capabilities and power states of the device.
old-location: storage\ufs_power_descriptor.htm
ms.assetid: FCF9DCD1-2C04-47E3-97C5-7ACC28B28C6C
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ufs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFS_POWER_DESCRIPTOR
req.alt-loc: Ufs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: PUFS_POWER_DESCRIPTOR, UFS_POWER_DESCRIPTOR, *PUFS_POWER_DESCRIPTOR
req.iface: 
req.product: Windows 10 or later.
---

# PUFS_POWER_DESCRIPTOR structure



## -description
<p><b>UFS_POWER_DESCRIPTOR </b>contains information about the power capabilities and power states of the device.</p>


## -syntax

````
typedef struct _UFS_POWER_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR wActiveICCLevelsVCC[32];
  UCHAR wActiveICCLevelsVCCQ[32];
  UCHAR wActiveICCLevelsVCCQ2[32];
} UFS_POWER_DESCRIPTOR, *PUFS_POWER_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>bLength</b>

<dd>
<p>Specifies the length, in bytes, of this descriptor.</p>
</dd>

### -field <b>bDescriptorIDN</b>

<dd>
<p>Specifies the type of the descriptor. This descriptor will have a value of <b>UFS_DESC_POWER_IDN</b>.</p>
</dd>

### -field <b>wActiveICCLevelsVCC</b>

<dd>
<p>Specifies the maximum VCC current value for
each UFS_bActiveICCLevel, based on the index value.</p>
</dd>

### -field <b>wActiveICCLevelsVCCQ</b>

<dd>
<p>Specifies the maximum VCCQ current value for
each UFS_bActiveICCLevel, based on the index value.</p>
</dd>

### -field <b>wActiveICCLevelsVCCQ2</b>

<dd>
<p>Specifies the maximum VCCQ current value for
each UFS_bActiveICCLevel, based on the index value.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufs.h</dt>
</dl>
</td>
</tr>
</table>