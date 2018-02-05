---
UID : NE:ufs.UFS_FLAGS_DESCRIPTOR
title : UFS_FLAGS_DESCRIPTOR
author : windows-driver-content
description : UFS_FLAGS_DESCRIPTOR describes the different types of flags used by Universal Flash Storage (UFS) descriptors.
old-location : storage\ufs_flags_descriptor.htm
old-project : storage
ms.assetid : D530355F-5824-4F7C-84C4-57D3D03A7116
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : UFS_FLAGS_DESCRIPTOR, ufs/UFS_Reserved3, UFS_fBackgroundOpsEn, ufs/UFS_fPurgeEnable, UFS_fPowerOnWPEn, ufs/UFS_Reserved1, UFS_fPermanentWPEn, storage.ufs_flags_descriptor, UFS_fBusyRTC, ufs/UFS_fPermanentlyDisableFwUpdate, ufs/UFS_fBackgroundOpsEn, UFS_Reserved1, UFS_Reserved2, UFS_fPermanentlyDisableFwUpdate, ufs/UFS_Reserved4, ufs/UFS_fBusyRTC, ufs/UFS_FLAGS_DESCRIPTOR, UFS_Reserved5, ufs/UFS_Reserved2, UFS_fPurgeEnable, ufs/UFS_fPhyResourceRemoval, UFS_fDeviceInit, UFS_fDeviceLifeSpanModeEn, UFS_Reserved3, ufs/UFS_fDeviceLifeSpanModeEn, ufs/UFS_fPermanentWPEn, UFS_Reserved4, UFS_FLAGS_DESCRIPTOR enumeration [Storage Devices], ufs/UFS_Reserved5, ufs/UFS_fDeviceInit, UFS_fPhyResourceRemoval, ufs/UFS_fPowerOnWPEn
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ufs.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : Windows 10, version 1709
req.target-min-winversvr : Windows Server 2016
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : UFS_FLAGS_DESCRIPTOR
req.product : Windows 10 or later.
---

# UFS_FLAGS_DESCRIPTOR Enumeration
<b>UFS_FLAGS_DESCRIPTOR</b> describes the different types of flags used by Universal Flash Storage (UFS) descriptors.

## Syntax
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

## Constants

<table>

<tr>
<td>UFS_fBackgroundOpsEn</td>
<td>Indicates the device is permitted to run
background operations.</td>
</tr>

<tr>
<td>UFS_fBusyRTC</td>
<td>Indicates the device is executing internal
operation related to Real Time Clock.</td>
</tr>

<tr>
<td>UFS_fDeviceInit</td>
<td>Indicates the device initialization is in progress.</td>
</tr>

<tr>
<td>UFS_fDeviceLifeSpanModeEn</td>
<td>Indicates Device Life Span Mode is enabled.</td>
</tr>

<tr>
<td>UFS_fPermanentlyDisableFwUpdate</td>
<td>Indicates the UFS device will permanently
disallow future firmware updates to
the Universal Flash Storage (UFS) device.</td>
</tr>

<tr>
<td>UFS_fPermanentWPEn</td>
<td>Indicates permanent write protection is enabled.</td>
</tr>

<tr>
<td>UFS_fPhyResourceRemoval</td>
<td>Indicates
that the dynamic capacity operation occurs on the device's EndPointReset or
a hardware reset. The host cannot reset this flag.</td>
</tr>

<tr>
<td>UFS_fPowerOnWPEn</td>
<td>Indicates power on write protection is enabled.</td>
</tr>

<tr>
<td>UFS_fPurgeEnable</td>
<td>Indicates Purge Operation is enabled.</td>
</tr>

<tr>
<td>UFS_Reserved1</td>
<td>Reserved for future use.</td>
</tr>

<tr>
<td>UFS_Reserved2</td>
<td>Reserved for future use.</td>
</tr>

<tr>
<td>UFS_Reserved3</td>
<td>Reserved for the Unified Memory Extension standard..</td>
</tr>

<tr>
<td>UFS_Reserved4</td>
<td>Reserved for the Unified Memory Extension standard.</td>
</tr>

<tr>
<td>UFS_Reserved5</td>
<td>Reserved for the Unified Memory Extension standard.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10, version 1709 Windows 10, version 1709 |
| **Header** | ufs.h |