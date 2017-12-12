---
UID: NF.ntifs.FsRtlGetSupportedFeatures
title: FsRtlGetSupportedFeatures function
author: windows-driver-content
description: The FsRtlGetSupportedFeatures routine returns the supported features of a volume attached to the specified device object.
old-location: ifsk\fsrtlgetsupportedfeatures.htm
old-project: ifsk
ms.assetid: 24852B9A-5156-41BB-87F9-81B147A85AC2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlGetSupportedFeatures
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlGetSupportedFeatures
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
---

# FsRtlGetSupportedFeatures function



## -description
The <b>FsRtlGetSupportedFeatures</b> routine returns the supported features of a volume attached to the specified device object.



## -syntax

````
NTSTATUS FsRtlGetSupportedFeatures(
  _In_  PDEVICE_OBJECT DeviceObject,
  _Out_ PULONG         SupportedFeatures
);
````


## -parameters

### -param DeviceObject [in]

The target device object attached to a volume.


### -param SupportedFeatures [out]

A pointer to a caller supplied <b>ULONG</b> value. On return, this value contains the supported feature flags for the attached volume.


The supported features are a bitwise OR combination of the following flags.



<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

### -param SUPPORTED_FS_FEATURES_OFFLOAD_READ
### -param 0x00000001

</td>
<td width="60%">
The volume supports offloaded read operations.

</td>
</tr>
<tr>

### -param SUPPORTED_FS_FEATURES_OFFLOAD_WRITE
### -param 0x00000002

</td>
<td width="60%">
The volume supports offloaded write operations.

</td>
</tr>
</table>
 


## -returns
<b>FsRtlGetSupportedFeatures</b> returns <b>STATUS_SUCCESS</b> if the supported features for the volume attached to <i>DeviceObject</i> are returned successfully. Otherwise, one of the following <b>NTSTATUS</b> values is returned.
<dl>
<dt><b>STATUS_FLT_VOLUME_NOT_FOUND</b></dt>
</dl>No volume is found for <i>DeviceObject</i>.
<dl>
<dt><b>STATUS_FLT_INTERNAL_ERROR</b></dt>
</dl>The device object specified by <i>DeviceObject</i> is not in a file system device stack.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in starting with Windows 8.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= APC_LEVEL

</td>
</tr>
</table>