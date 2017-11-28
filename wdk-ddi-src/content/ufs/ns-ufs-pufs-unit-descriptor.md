---
UID: NS.ufs.PUFS_UNIT_DESCRIPTOR
title: PUFS_UNIT_DESCRIPTOR
author: windows-driver-content
description: The UFS_UNIT_DESCRIPTOR structure describes a generic unit descriptor.
old-location: storage\ufs_unit_descriptor.htm
old-project: storage
ms.assetid: 5D76C266-875A-40AC-9B26-F17978971783
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PUFS_UNIT_DESCRIPTOR, UFS_UNIT_DESCRIPTOR, *PUFS_UNIT_DESCRIPTOR
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
req.alt-api: UFS_UNIT_DESCRIPTOR
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

# PUFS_UNIT_DESCRIPTOR structure



## -description
<p>The <b>UFS_UNIT_DESCRIPTOR</b> structure describes a generic unit descriptor.</p>


## -syntax

````
typedef struct _UFS_UNIT_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR bUnitIndex;
  UCHAR bLUEnable;
  UCHAR bBootLUNID;
  UCHAR bLUWriteProtect;
  UCHAR bLUQueueDepth;
  UCHAR bPSASensitive;
  UCHAR bMemoryType;
  UCHAR bDataReliability;
  UCHAR  bLogicalBlockSize;
  UCHAR qLogicalBlockCount[8];
  UCHAR dEraseBlockSize[4];
  UCHAR bProvisioningType;
  UCHAR qPhyMemResourceCount[8];
  UCHAR wContextCapabilities[2];
  UCHAR bLargeUnitGranularity_M1;
} UFS_UNIT_DESCRIPTOR, *PUFS_UNIT_DESCRIPTOR;
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
<p>Specifies the desired memory type. The <b>wSupportedMemoryTypes</b> parameter in the <a href="storage.ufs_geometry_descriptor">UFS_GEOMETRY_DESCRIPTOR</a> indicates which memory types are supported by the device</p>
</dd>

### -field <b>bDataReliability</b>

<dd>
<p>Specifies if the device is protected against a power failure during a write operation to the logical unit. </p>
</dd>

### -field <b> bLogicalBlockSize</b>

<dd>
<p>Specifies the logical block size of the descriptor. Set the value of this equal to the corresponding value in <b>dOptimalLogicalBlockSize</b> of <a href="storage.ufs_geometry_descriptor">UFS_GEOMETRY_DESCRIPTOR</a> for the specific logical unit memory type.</p>
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

### -field <b>wContextCapabilities</b>

<dd>
<p>Specifies the number of contexts to be supported in each logical unit.</p>
</dd>

### -field <b>bLargeUnitGranularity_M1</b>

<dd>
<p>Specifies the Large Unit granularity, minus one.</p>
</dd>
</dl>

## -remarks
<p><b>bPSASensitive</b> and<b> dEraseBlockSize</b> are updated automatically after device configuration.</p>

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

## -see-also
<dl>
<dt>
<a href="storage.ufs_geometry_descriptor">UFS_GEOMETRY_DESCRIPTOR</a>
</dt>
<dt>
<a href="storage.ufs_rpmb_unit_descriptor">UFS_RPMB_UNIT_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20UFS_UNIT_DESCRIPTOR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
