---
UID: NS.ufs.PUFS_INTERCONNECT_DESCRIPTOR
title: PUFS_INTERCONNECT_DESCRIPTOR
author: windows-driver-content
description: UFS_INTERCONNECT_DESCRIPTOR contains the MIPI M-PHY® specification version number and the MIPI 6338 UniPro℠ specification version number.
old-location: storage\ufs_interconnect_descriptor.htm
old-project: storage
ms.assetid: 6C6EAA96-40E9-467F-903B-AE44CE5B77CF
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PUFS_INTERCONNECT_DESCRIPTOR, UFS_INTERCONNECT_DESCRIPTOR, *PUFS_INTERCONNECT_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ufs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFS_INTERCONNECT_DESCRIPTOR
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
req.iface: 
req.product: Windows 10 or later.
---

# PUFS_INTERCONNECT_DESCRIPTOR structure



## -description
<p><b>UFS_INTERCONNECT_DESCRIPTOR</b> contains the MIPI M-PHY® specification version number and the MIPI
6338 UniPro℠ specification version number.</p>


## -syntax

````
typedef struct _UFS_INTERCONNECT_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR bcdUniproVersion[2];
  UCHAR bcdMphyVersion[2];
} UFS_INTERCONNECT_DESCRIPTOR, *PUFS_INTERCONNECT_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field bLength

<dd>
<p>Specifies the length, in bytes, of this descriptor.</p>
</dd>

### -field bDescriptorIDN

<dd>
<p>Specifies the type of the descriptor. This descriptor will have a value of <b>UFS_DESC_INTERCONNECT_IDN</b>.</p>
</dd>

### -field bcdUniproVersion

<dd>
<p>Specifies the MIPI UniPro℠ version number in Binary Coded Decimal (BCD) format.</p>
</dd>

### -field bcdMphyVersion

<dd>
<p>Specifies the MIPI M-PHY® version number in BCD format.</p>
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