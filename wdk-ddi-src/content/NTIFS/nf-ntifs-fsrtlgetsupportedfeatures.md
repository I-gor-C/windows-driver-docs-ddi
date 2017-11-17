---
UID: NF.ntifs.FsRtlGetSupportedFeatures
title: FsRtlGetSupportedFeatures
author: windows-driver-content
description: The FsRtlGetSupportedFeatures routine returns the supported features of a volume attached to the specified device object.
old-location: ifsk\fsrtlgetsupportedfeatures.htm
ms.assetid: 24852B9A-5156-41BB-87F9-81B147A85AC2
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
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
ms.keywords: FsRtlGetSupportedFeatures
req.iface: 
---

# FsRtlGetSupportedFeatures function



## -description
<p>The <b>FsRtlGetSupportedFeatures</b> routine returns the supported features of a volume attached to the specified device object.</p>


## -syntax

````
NTSTATUS FsRtlGetSupportedFeatures(
  _In_  PDEVICE_OBJECT DeviceObject,
  _Out_ PULONG         SupportedFeatures
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>The target device object attached to a volume.</p>
</dd>

### -param <i>SupportedFeatures</i> [out]

<dd>
<p>A pointer to a caller supplied <b>ULONG</b> value. On return, this value contains the supported feature flags for the attached volume.</p>
<p>
<p>The supported features are a bitwise OR combination of the following flags.</p>
</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="SUPPORTED_FS_FEATURES_OFFLOAD_READ"></a><a id="supported_fs_features_offload_read"></a><dl>

### -param <b>SUPPORTED_FS_FEATURES_OFFLOAD_READ</b>


### -param 0x00000001

</dl>
</td>
<td width="60%">
<p>The volume supports offloaded read operations.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SUPPORTED_FS_FEATURES_OFFLOAD_WRITE"></a><a id="supported_fs_features_offload_write"></a><dl>

### -param <b>SUPPORTED_FS_FEATURES_OFFLOAD_WRITE</b>


### -param 0x00000002

</dl>
</td>
<td width="60%">
<p>The volume supports offloaded write operations.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>FsRtlGetSupportedFeatures</b> returns <b>STATUS_SUCCESS</b> if the supported features for the volume attached to <i>DeviceObject</i> are returned successfully. Otherwise, one of the following <b>NTSTATUS</b> values is returned.</p><dl>
<dt><b>STATUS_FLT_VOLUME_NOT_FOUND</b></dt>
</dl><p>No volume is found for <i>DeviceObject</i>.</p><dl>
<dt><b>STATUS_FLT_INTERNAL_ERROR</b></dt>
</dl><p>The device object specified by <i>DeviceObject</i> is not in a file system device stack.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>