---
UID: NS.ufs.PUFS_GEOMETRY_DESCRIPTOR
title: PUFS_GEOMETRY_DESCRIPTOR
author: windows-driver-content
description: UFS_GEOMETRY_DESCRIPTOR describes a device's geometric parameters.
old-location: storage\ufs_geometry_descriptor.htm
old-project: storage
ms.assetid: DD3AEB66-E36B-4F18-AFEC-D344132D4B8C
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PUFS_GEOMETRY_DESCRIPTOR, UFS_GEOMETRY_DESCRIPTOR, *PUFS_GEOMETRY_DESCRIPTOR
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
req.alt-api: UFS_GEOMETRY_DESCRIPTOR
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

# PUFS_GEOMETRY_DESCRIPTOR structure



## -description
<p><b>UFS_GEOMETRY_DESCRIPTOR</b> describes a device's geometric parameters.</p>


## -syntax

````
typedef struct _UFS_GEOMETRY_DESCRIPTOR {
  UCHAR bLength;
  UCHAR bDescriptorIDN;
  UCHAR bMediaTechnology;
  UCHAR Reserved1;
  UCHAR  qTotalRawDeviceCapacity[8];
  UCHAR bMaxNumberLU;
  UCHAR dSegmentSize[4];
  UCHAR bAllocationUnitSize;
  UCHAR bMinAddrBlockSize;
  UCHAR bOptimalReadBlockSize;
  UCHAR bOptimalWriteBlockSize;
  UCHAR bMaxInBufferSize;
  UCHAR bMaxOutBufferSize;
  UCHAR bRPMB_ReadWriteSize;
  UCHAR bDynamicCapacityResourcePolicy;
  UCHAR bDataOrdering;
  UCHAR bMaxContexIDNumber;
  UCHAR bSysDataTagUnitSize;
  UCHAR bSysDataTagResSize;
  UCHAR bSupportedSecRTypes;
  UCHAR wSupportedMemoryTypes[2];
  UCHAR dSystemCodeMaxNAllocU[4];
  UCHAR wSystemCodeCapAdjFac[2];
  UCHAR dNonPersistMaxNAllocU[4];
  UCHAR wNonPersistCapAdjFac[2];
  UCHAR dEnhanced1MaxNAllocU[4];
  UCHAR wEnhanced1CapAdjFac[2];
  UCHAR dEnhanced2MaxNAllocU[4];
  UCHAR wEnhanced2CapAdjFac[2];
  UCHAR dEnhanced3MaxNAllocU[4];
  UCHAR wEnhanced3CapAdjFac[2];
  UCHAR dEnhanced4MaxNAllocU[4];
  UCHAR wEnhanced4CapAdjFac[2];
  UCHAR dOptimalLogicalBlockSize[4];
} UFS_GEOMETRY_DESCRIPTOR, *PUFS_GEOMETRY_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>bLength</b>

<dd>
<p>Specifies the length of the descriptor.</p>
</dd>

### -field <b>bDescriptorIDN</b>

<dd>
<p>Specifies the type of the descriptor. This descriptor will have a value of<b> UFS_DESC_GEOMETRY_IDN</b>.

</p>
</dd>

### -field <b>bMediaTechnology</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b> qTotalRawDeviceCapacity</b>

<dd>
<p>Specifies the total raw device capacity. Expressed in units of 512 bytes.</p>
</dd>

### -field <b>bMaxNumberLU</b>

<dd>
<p>Specifies the maximum number of logical unit(s) supported by the UFS (Universal Flash Storage). Contains one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>8 logical units.</td>
</tr>
<tr>
<td>0x01</td>
<td>32 logical units.</td>
</tr>
<tr>
<td>Other Values</td>
<td>Reserved for future use.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dSegmentSize</b>

<dd>
<p>Specifies the segment size of the device in units of 512 bytes.</p>
</dd>

### -field <b>bAllocationUnitSize</b>

<dd>
<p>Specifies the allocation unit size in number of segments.</p>
</dd>

### -field <b>bMinAddrBlockSize</b>

<dd>
<p>Specifies the minimum addressable block size in units of 512 bytes. The minium size is 4 KB or a value of 0x08.</p>
</dd>

### -field <b>bOptimalReadBlockSize</b>

<dd>
<p>Specifies the optimal read block size in units of 512 bytes.</p>
</dd>

### -field <b>bOptimalWriteBlockSize</b>

<dd>
<p>Specifies the optimal write block size in units of 512 bytes. <b>bOptimalWriteBlockSize</b> is equal to or greater than <b>bMinAddrBlockSize</b>.</p>
</dd>

### -field <b>bMaxInBufferSize</b>

<dd>
<p>Specifies the max size of the data-in buffer in units of 512 bytes. The minium size is 4 KB or a value of 0x08.</p>
</dd>

### -field <b>bMaxOutBufferSize</b>

<dd>
<p>Specifies the max size of the data-out buffer in units of 512 bytes. The minium size is 4 KB or a value of 0x08.</p>
</dd>

### -field <b>bRPMB_ReadWriteSize</b>

<dd>
<p>Specifies the maximum number of Replay Protected Memory Block (RPMB) frames allowed in Security Protocol In and Security
Protocol Out. Each frame is 256-bytes. </p>
</dd>

### -field <b>bDynamicCapacityResourcePolicy</b>

<dd>
<p>Specifies a device's spare blocks
resource management policy. Contains one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>Spare blocks resource management policy is
per logical unit.</td>
</tr>
<tr>
<td>0x01</td>
<td>Spare blocks resource management policy is
per memory type.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>bDataOrdering</b>

<dd>
<p>Specifies if a device supports out-of-order data transfer. Contains one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>0x00</td>
<td>Out-of-order data transfer is not supported.</td>
</tr>
<tr>
<td>0x01</td>
<td>Out-of-order data transfer is supported.</td>
</tr>
<tr>
<td>All other values</td>
<td>Reserved for future use.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>bMaxContexIDNumber</b>

<dd>
<p>Specifies the max number of contexts supported by a device. This number must be greater than 5.</p>
</dd>

### -field <b>bSysDataTagUnitSize</b>

<dd>
<p>Specifies the system data tag
unit size.</p>
</dd>

### -field <b>bSysDataTagResSize</b>

<dd>
<p>Specifies the maximum size in bytes allocated by
the device to handle system data.</p>
</dd>

### -field <b>bSupportedSecRTypes</b>

<dd>
<p>Specifies the supported Secure Removal types. The first 3 bits of the variable are flags that represent different supported Secure Removal types. </p>
<table>
<tr>
<th>Bit</th>
<th>Description</th>
</tr>
<tr>
<td>0</td>
<td>Information removed with an erase of the physical memory. </td>
</tr>
<tr>
<td>1</td>
<td>Information removed by overwriting the
addressed locations with a single character
followed by an erase.</td>
</tr>
<tr>
<td>2</td>
<td>Information removed by overwriting the
addressed locations with a character, its
complement, then a random character.</td>
</tr>
<tr>
<td>3</td>
<td>Information removed using a vendor-defined
mechanism.</td>
</tr>
<tr>
<td>4-7</td>
<td>Reserved for future use.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>wSupportedMemoryTypes</b>

<dd>
<p>Specifies the supported memory types in a bitmap.</p>
<table>
<tr>
<th>Bit</th>
<th>Description</th>
</tr>
<tr>
<td>0</td>
<td>A normal memory type is supported.</td>
</tr>
<tr>
<td>1</td>
<td>A system code memory type is supported.</td>
</tr>
<tr>
<td>2</td>
<td>A non-persistent memory type is supported.</td>
</tr>
<tr>
<td>3</td>
<td>Enhanced memory type 1 is supported.</td>
</tr>
<tr>
<td>4</td>
<td>Enhanced memory type 2 is supported.</td>
</tr>
<tr>
<td>5</td>
<td>Enhanced memory type 3 is supported.</td>
</tr>
<tr>
<td>6</td>
<td>Enhanced memory type 4 is supported.</td>
</tr>
<tr>
<td>7-14</td>
<td>Reserved for future use.</td>
</tr>
<tr>
<td>15</td>
<td>A RPMB memory type is supported.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dSystemCodeMaxNAllocU</b>

<dd>
<p>Specifies the maximum number of allocation units for the System Code for a device.</p>
</dd>

### -field <b>wSystemCodeCapAdjFac</b>

<dd>
<p>Species the Capacity Adjustment Factor for the System Code
memory type.</p>
</dd>

### -field <b>dNonPersistMaxNAllocU</b>

<dd>
<p>Species the maximum number of Allocation Units for a non-persistent memory type.</p>
</dd>

### -field <b>wNonPersistCapAdjFac</b>

<dd>
<p>Specifies the capacity adjustment factor for the non-persistent memory type.</p>
</dd>

### -field <b>dEnhanced1MaxNAllocU</b>

<dd>
<p>specifies the max number of Allocation Units for the enhanced
memory type 1.</p>
</dd>

### -field <b>wEnhanced1CapAdjFac</b>

<dd>
<p>specifies the Capacity Adjustment Factor for the enhanced
memory type 1.</p>
</dd>

### -field <b>dEnhanced2MaxNAllocU</b>

<dd>
<p>specifies the max number of Allocation Units for the enhanced
memory type 2.</p>
</dd>

### -field <b>wEnhanced2CapAdjFac</b>

<dd>
<p>specifies the Capacity Adjustment Factor for the enhanced
memory type 2.</p>
</dd>

### -field <b>dEnhanced3MaxNAllocU</b>

<dd>
<p>specifies the max number of Allocation Units for the enhanced
memory type 3.</p>
</dd>

### -field <b>wEnhanced3CapAdjFac</b>

<dd>
<p>specifies the Capacity Adjustment Factor for the enhanced
memory type 3.</p>
</dd>

### -field <b>dEnhanced4MaxNAllocU</b>

<dd>
<p>specifies the max number of Allocation Units for the enhanced
memory type 4.</p>
</dd>

### -field <b>wEnhanced4CapAdjFac</b>

<dd>
<p>specifies the Capacity Adjustment Factor for the enhanced
memory type 4.</p>
</dd>

### -field <b>dOptimalLogicalBlockSize</b>

<dd>
<p>Specifies the optimal logical block size.</p>
</dd>
</dl>

## -remarks
<p>If the size of the data transferred exceeds the number of frames <b>bRPMB_ReadWriteSize</b>, it will be done in multiple Security commands.</p>

<p>The Capacity Adjustment Factor value for a normal memory type is equal to 1.</p>

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