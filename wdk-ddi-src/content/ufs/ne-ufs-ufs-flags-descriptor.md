---
UID: NE.ufs.UFS_FLAGS_DESCRIPTOR
title: UFS_FLAGS_DESCRIPTOR
author: windows-driver-content
description: UFS_FLAGS_DESCRIPTOR describes the different types of flags used by Universal Flash Storage (UFS) descriptors.
old-location: storage\ufs_flags_descriptor.htm
old-project: storage
ms.assetid: D530355F-5824-4F7C-84C4-57D3D03A7116
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: UDECX_WDF_DEVICE_CONFIG, UDECX_WDF_DEVICE_CONFIG, *PUDECX_WDF_DEVICE_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ufs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFS_FLAGS_DESCRIPTOR
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

# UFS_FLAGS_DESCRIPTOR enumeration



## -description
<p><b>UFS_FLAGS_DESCRIPTOR</b> describes the different types of flags used by Universal Flash Storage (UFS) descriptors.</p>


## -syntax

````
typedef enum _UFS_FLAGS_DESCRIPTOR { 
  UFS_Reserved1                    = 0,
  UFS_fDeviceInit,
  UFS_fPermanentWPEn,
  UFS_fPowerOnWPEn,
  UFS_fBackgroundOpsEn,
  UFS_fDeviceLifeSpanModeEn,
  UFS_fPurgeEnable,
  UFS_Reserved2,
  UFS_fPhyResourceRemoval,
  UFS_fBusyRTC,
  UFS_Reserved3,
  UFS_fPermanentlyDisableFwUpdate,
  UFS_Reserved4,
  UFS_Reserved5
} UFS_FLAGS_DESCRIPTOR;
````


## -enum-fields
<dl>

### -field UFS_Reserved1

<dd>
<p>Reserved for future use.</p>
</dd>

### -field UFS_fDeviceInit

<dd>
<p>Indicates the device initialization is in progress.</p>
</dd>

### -field UFS_fPermanentWPEn

<dd>
<p>Indicates permanent write protection is enabled.</p>
</dd>

### -field UFS_fPowerOnWPEn

<dd>
<p>Indicates power on write protection is enabled.</p>
</dd>

### -field UFS_fBackgroundOpsEn

<dd>
<p>Indicates the device is permitted to run
background operations.</p>
</dd>

### -field UFS_fDeviceLifeSpanModeEn

<dd>
<p>Indicates Device Life Span Mode is enabled.</p>
</dd>

### -field UFS_fPurgeEnable

<dd>
<p>Indicates Purge Operation is enabled.</p>
</dd>

### -field UFS_Reserved2

<dd>
<p>Reserved for future use.</p>
</dd>

### -field UFS_fPhyResourceRemoval

<dd>
<p>Indicates
that the dynamic capacity operation occurs on the device's EndPointReset or
a hardware reset. The host cannot reset this flag.</p>
</dd>

### -field UFS_fBusyRTC

<dd>
<p>Indicates the device is executing internal
operation related to Real Time Clock.</p>
</dd>

### -field UFS_Reserved3

<dd>
<p>Reserved for the Unified Memory Extension standard..</p>
</dd>

### -field UFS_fPermanentlyDisableFwUpdate

<dd>
<p>Indicates the UFS device will permanently
disallow future firmware updates to
the Universal Flash Storage (UFS) device.</p>
</dd>

### -field UFS_Reserved4

<dd>
<p>Reserved for the Unified Memory Extension standard.</p>
</dd>

### -field UFS_Reserved5

<dd>
<p>Reserved for the Unified Memory Extension standard.</p>
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