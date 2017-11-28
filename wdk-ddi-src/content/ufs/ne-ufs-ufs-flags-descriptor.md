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

### -field <a id="UFS_Reserved1"></a><a id="ufs_reserved1"></a><a id="UFS_RESERVED1"></a><b>UFS_Reserved1</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <a id="UFS_fDeviceInit"></a><a id="ufs_fdeviceinit"></a><a id="UFS_FDEVICEINIT"></a><b>UFS_fDeviceInit</b>

<dd>
<p>Indicates the device initialization is in progress.</p>
</dd>

### -field <a id="UFS_fPermanentWPEn"></a><a id="ufs_fpermanentwpen"></a><a id="UFS_FPERMANENTWPEN"></a><b>UFS_fPermanentWPEn</b>

<dd>
<p>Indicates permanent write protection is enabled.</p>
</dd>

### -field <a id="UFS_fPowerOnWPEn"></a><a id="ufs_fpoweronwpen"></a><a id="UFS_FPOWERONWPEN"></a><b>UFS_fPowerOnWPEn</b>

<dd>
<p>Indicates power on write protection is enabled.</p>
</dd>

### -field <a id="UFS_fBackgroundOpsEn"></a><a id="ufs_fbackgroundopsen"></a><a id="UFS_FBACKGROUNDOPSEN"></a><b>UFS_fBackgroundOpsEn</b>

<dd>
<p>Indicates the device is permitted to run
background operations.</p>
</dd>

### -field <a id="UFS_fDeviceLifeSpanModeEn"></a><a id="ufs_fdevicelifespanmodeen"></a><a id="UFS_FDEVICELIFESPANMODEEN"></a><b>UFS_fDeviceLifeSpanModeEn</b>

<dd>
<p>Indicates Device Life Span Mode is enabled.</p>
</dd>

### -field <a id="UFS_fPurgeEnable"></a><a id="ufs_fpurgeenable"></a><a id="UFS_FPURGEENABLE"></a><b>UFS_fPurgeEnable</b>

<dd>
<p>Indicates Purge Operation is enabled.</p>
</dd>

### -field <a id="UFS_Reserved2"></a><a id="ufs_reserved2"></a><a id="UFS_RESERVED2"></a><b>UFS_Reserved2</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <a id="UFS_fPhyResourceRemoval"></a><a id="ufs_fphyresourceremoval"></a><a id="UFS_FPHYRESOURCEREMOVAL"></a><b>UFS_fPhyResourceRemoval</b>

<dd>
<p>Indicates
that the dynamic capacity operation occurs on the device's EndPointReset or
a hardware reset. The host cannot reset this flag.</p>
</dd>

### -field <a id="UFS_fBusyRTC"></a><a id="ufs_fbusyrtc"></a><a id="UFS_FBUSYRTC"></a><b>UFS_fBusyRTC</b>

<dd>
<p>Indicates the device is executing internal
operation related to Real Time Clock.</p>
</dd>

### -field <a id="UFS_Reserved3"></a><a id="ufs_reserved3"></a><a id="UFS_RESERVED3"></a><b>UFS_Reserved3</b>

<dd>
<p>Reserved for the Unified Memory Extension standard..</p>
</dd>

### -field <a id="UFS_fPermanentlyDisableFwUpdate"></a><a id="ufs_fpermanentlydisablefwupdate"></a><a id="UFS_FPERMANENTLYDISABLEFWUPDATE"></a><b>UFS_fPermanentlyDisableFwUpdate</b>

<dd>
<p>Indicates the UFS device will permanently
disallow future firmware updates to
the Universal Flash Storage (UFS) device.</p>
</dd>

### -field <a id="UFS_Reserved4"></a><a id="ufs_reserved4"></a><a id="UFS_RESERVED4"></a><b>UFS_Reserved4</b>

<dd>
<p>Reserved for the Unified Memory Extension standard.</p>
</dd>

### -field <a id="UFS_Reserved5"></a><a id="ufs_reserved5"></a><a id="UFS_RESERVED5"></a><b>UFS_Reserved5</b>

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