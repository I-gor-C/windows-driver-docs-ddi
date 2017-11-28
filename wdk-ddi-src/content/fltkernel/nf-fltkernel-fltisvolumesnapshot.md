---
UID: NF.fltkernel.FltIsVolumeSnapshot
title: FltIsVolumeSnapshot
author: windows-driver-content
description: The FltIsVolumeSnapshot routine determines whether a volume or minifilter driver instance is attached to a snapshot volume.
old-location: ifsk\fltisvolumesnapshot.htm
old-project: ifsk
ms.assetid: eb35e108-577e-4897-8f8c-f3c54753c1f7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltIsVolumeSnapshot
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltIsVolumeSnapshot
req.alt-loc: FltMgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fltmgr.lib
req.dll: FltMgr.sys
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FltIsVolumeSnapshot function



## -description
<p>The <b>FltIsVolumeSnapshot</b> routine determines whether a volume or minifilter driver instance is attached to a snapshot volume.</p>


## -syntax

````
NTSTATUS FltIsVolumeSnapshot(
  _In_  PVOID    FltObject,
  _Out_ PBOOLEAN IsSnapshotVolume
);
````


## -parameters
<dl>

### -param <i>FltObject</i> [in]

<dd>
<p>An opaque pointer to the volume or instance.</p>
</dd>

### -param <i>IsSnapshotVolume</i> [out]

<dd>
<p>A pointer to a caller-allocated Boolean variable that receives <b>TRUE</b> if the volume or instance is attached to a snapshot volume. Otherwise, the variable receives <b>FALSE</b>.</p>
</dd>
</dl>

## -returns
<p><b>FltIsVolumeSnapshot</b> returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p><b>FltIsVolumeSnapshot</b> determined whether <i>FltObject</i> is a snapshot.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p><i>FltObject </i>specifies something besides a volume or an instance. This is an error code.</p><dl>
<dt><b>STATUS_FLT_NO_DEVICE_OBJECT</b></dt>
</dl><p><i>FltObject</i> does not have an associated disk device object. This can occur if <i>FltObject</i> is associated with a network drive. This is an error code.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>FltIsVolumeSnapshot</b> encountered a memory allocation failure. This is an error code.</p>

<p> </p>

## -remarks
<p>If the volume or instance object does not support snapshots, <b>FltIsVolumeSnapshot</b> returns STATUS_SUCCESS and <i>IsSnapshotVolume</i> is <b>FALSE</b>.</p>

<p>If the volume or instance object does not support snapshots, <b>FltIsVolumeSnapshot</b> returns STATUS_SUCCESS and <i>IsSnapshotVolume</i> is <b>FALSE</b>.</p>

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
<p>Available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>