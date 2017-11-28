---
UID: NS.ufs.PUFS_RPMB_UNIT_DESCRIPTOR
title: PUFS_RPMB_UNIT_DESCRIPTOR
author: windows-driver-content
description: The UFS_RPMB_UNIT_DESCRIPTOR structure describes the contents of a Replay Protected Memory Block (RBMB) Unit.
old-location: storage\ufs_rpmb_unit_descriptor.htm
old-project: storage
ms.assetid: 19A066BD-1099-475C-BF81-F1BE7C7778E5
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PUFS_RPMB_UNIT_DESCRIPTOR, UFS_RPMB_UNIT_DESCRIPTOR, *PUFS_RPMB_UNIT_DESCRIPTOR
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
req.alt-api: UFS_RPMB_UNIT_DESCRIPTOR
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

# PUFS_RPMB_UNIT_DESCRIPTOR structure



## -description
<p>The <b>UFS_RPMB_UNIT_DESCRIPTOR</b> structure describes the contents of a Replay Protected Memory Block (RBMB) Unit.</p>


## -syntax

````
typedef struct _UFS_RPMB_UNIT_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR bUnitIndex;
  UCHAR bLUEnable;
  UCHAR bBootLUNID;
  UCHAR bLUWriteProtect;
  UCHAR bLUQueueDepth;
  UCHAR bPSASensitive;
  UCHAR bMemoryType;
  UCHAR Reserved;
  UCHAR  bLogicalBlockSize;
  UCHAR qLogicalBlockCount[8];
  UCHAR dEraseBlockSize[4];
  UCHAR bProvisioningType;
  UCHAR qPhyMemResourceCount[8];
  UCHAR Reserved[3];
} UFS_RPMB_UNIT_DESCRIPTOR, *PUFS_RPMB_UNIT_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>bLength</b>

<dd>
<p>Specifies the length, in bytes, of this descriptor.</p>
</dd>

### -field <b>bDescriptorIDN</b>

<dd>
<p>Specifies the type of the descriptor. This descriptor will have a value of <b>UFS_DESC_UNIT_IDN</b>.</p>
</dd>

### -field <b>bUnitIndex</b>

<dd>
<p>Specifies unit index</p>
</dd>

### -field <b>bLUEnable</b>

<dd>
<p>Specifies if the logic unit number (LUN) is enabled. If <b>bLUEnable</b> is equal to 0x00, the logical unit is disabled.</p>
</dd>

### -field <b>bBootLUNID</b>

<dd>
<p>Specifies the boot LUN id.</p>
</dd>

### -field <b>bLUWriteProtect</b>

<dd>
<p>Specifies if the logical unit is write-protected. Contains one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>The logical unit is not write protected.</td>
</tr>
<tr>
<td>0x01</td>
<td>The logical unit is write protected.</td>
</tr>
<tr>
<td>0x02 </td>
<td>The logical unit is permanently write protected.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>bLUQueueDepth</b>

<dd>
<p>Specifies the logical unit queue depth. Can be any value from 0x00 to 0xff.</p>
</dd>

### -field <b>bPSASensitive</b>

<dd>
<p>Specifies if the logical unit is sensitive to soldering. Contains one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>The logical unit is not sensitive to soldering.</td>
</tr>
<tr>
<td>0x01</td>
<td>The logical unit is sensitive to soldering.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>bMemoryType</b>

<dd>
<p>Specifies the desired memory type. Equal to 0x0F.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b> bLogicalBlockSize</b>

<dd>
<p>Specifies the logical block size of the descriptor.</p>
</dd>

### -field <b>qLogicalBlockCount</b>

<dd>
<p>Specifies the total number of addressable logical blocks in the logical unit.</p>
</dd>

### -field <b>dEraseBlockSize</b>

<dd>
<p>Specifies the erase block size.</p>
</dd>

### -field <b>bProvisioningType</b>

<dd>
<p>Specifies the provisioning type.</p>
</dd>

### -field <b>qPhyMemResourceCount</b>

<dd>
<p>Specifies the total physical memory resources available in the logical unit.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
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