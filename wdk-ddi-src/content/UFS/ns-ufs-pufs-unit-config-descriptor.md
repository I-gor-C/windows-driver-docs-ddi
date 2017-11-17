---
UID: NS.ufs.PUFS_UNIT_CONFIG_DESCRIPTOR
title: PUFS_UNIT_CONFIG_DESCRIPTOR
author: windows-driver-content
description: The UFS_UNIT_CONFIG_DESCRIPTOR structure describes the user configurable parameters within the UFS_CONFIG_DESCRIPTOR.
old-location: storage\ufs_unit_config_descriptor.htm
ms.assetid: 09CBAD0A-CBDC-464E-908C-BF142D515969
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
req.alt-api: UFS_UNIT_CONFIG_DESCRIPTOR
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
ms.keywords: PUFS_UNIT_CONFIG_DESCRIPTOR, UFS_UNIT_CONFIG_DESCRIPTOR, *PUFS_UNIT_CONFIG_DESCRIPTOR
req.iface: 
req.product: Windows 10 or later.
---

# PUFS_UNIT_CONFIG_DESCRIPTOR structure



## -description
<p>The <b>UFS_UNIT_CONFIG_DESCRIPTOR</b> structure describes the user configurable parameters within the <a href="https://msdn.microsoft.com/B65A2268-6959-4630-97DA-C0CFD37D9174">UFS_CONFIG_DESCRIPTOR</a>.</p>


## -syntax

````
typedef struct _UFS_UNIT_CONFIG_DESCRIPTOR {
  UCHAR bLUEnable;
  UCHAR bBootLunID;
  UCHAR bLUWriteProtect;
  UCHAR bMemoryType;
  UCHAR dNumAllocUnits[4];
  UCHAR bDataReliability;
  UCHAR bLogicalBlockSize;
  UCHAR bProvisioningType;
  UCHAR wContextCapabilities[2];
  UCHAR Reserved[3];
} UFS_UNIT_CONFIG_DESCRIPTOR, *PUFS_UNIT_CONFIG_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>bLUEnable</b>

<dd>
<p>Specifies if the logical unit is enabled.</p>
</dd>

### -field <b>bBootLunID</b>

<dd>
<p>Specifies if the logical unit is a bootable logical unit.</p>
</dd>

### -field <b>bLUWriteProtect</b>

<dd>
<p>Specifies if the Logical Unit is write protected.</p>
</dd>

### -field <b>bMemoryType</b>

<dd>
<p>Specifies the Memory type of the device.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>Normal Memory type</td>
</tr>
<tr>
<td>0x01</td>
<td>System code memory type</td>
</tr>
<tr>
<td>0x02</td>
<td>Non-Persistent memory type</td>
</tr>
<tr>
<td>0x03</td>
<td>Enhanced memory type 1</td>
</tr>
<tr>
<td>0x04</td>
<td>Enhanced memory type 2</td>
</tr>
<tr>
<td>0x05</td>
<td>Enhanced memory type 3</td>
</tr>
<tr>
<td>0x06</td>
<td>Enhanced memory type 4</td>
</tr>
<tr>
<td>All other values</td>
<td>Reserved for future use.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dNumAllocUnits</b>

<dd>
<p>Specifies the number of allocation units assigned to the logical unit.</p>
</dd>

### -field <b>bDataReliability</b>

<dd>
<p><b>bDataReliability</b> defines the device behavior
when a power failure occurs during a write
operation to the logical unit:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>The logical unit is not protected. Logical
unit's entire data may be lost as a result
of a power failure during a write
operation</td>
</tr>
<tr>
<td>0x01</td>
<td>The logical unit is protected. Logical unit's
data is protected against power failure.</td>
</tr>
<tr>
<td>All other values</td>
<td>Reserved for future use.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>bLogicalBlockSize</b>

<dd>
<p>Specifies the logical block size.</p>
</dd>

### -field <b>bProvisioningType</b>

<dd>
<p>Specifies the provisioning type.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>Thin Provisioning is disabled (default)</td>
</tr>
<tr>
<td>0x02</td>
<td>Thin Provisioning is enabled and Thin Provisioning Read Zeros (TPRZ)
= 0</td>
</tr>
<tr>
<td>0x03</td>
<td>Thin Provisioning is enabled and TPRZ
= 1</td>
</tr>
<tr>
<td>All other values</td>
<td>Reserved for future use.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>wContextCapabilities</b>

<dd>
<p>Specifies the Context Capabilities.</p>
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