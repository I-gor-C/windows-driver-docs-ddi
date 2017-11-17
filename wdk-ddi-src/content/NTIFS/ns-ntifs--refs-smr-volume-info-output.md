---
UID: NS.ntifs._REFS_SMR_VOLUME_INFO_OUTPUT
title: REFS_SMR_VOLUME_INFO_OUTPUT
author: windows-driver-content
description: The REFS_SMR_VOLUME_INFO_OUTPUT structure describes a Shingled Magnetic Recording (SMR) volume's current state on space and garbage collection activities.
old-location: ifsk\refs_smr_volume_info_output.htm
ms.assetid: 0DCBAF5F-AEBC-4C4B-9DBD-F7A6FD6C7712
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: REFS_SMR_VOLUME_INFO_OUTPUT
req.alt-loc: Ntifs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: REFS_SMR_VOLUME_INFO_OUTPUT, REFS_SMR_VOLUME_INFO_OUTPUT, *PREFS_SMR_VOLUME_INFO_OUTPUT
req.iface: 
---

# REFS_SMR_VOLUME_INFO_OUTPUT structure



## -description
<p>The <b>REFS_SMR_VOLUME_INFO_OUTPUT</b> structure describes a Shingled Magnetic Recording (SMR) volume's  current  state on space and garbage collection activities.</p>


## -syntax

````
typedef struct _REFS_SMR_VOLUME_INFO_OUTPUT {
  ULONG                    Version;
  ULONG                    Flags;
  LARGE_INTEGER            SizeOfRandomlyWritableTier;
  LARGE_INTEGER            FreeSpaceInRandomlyWritableTier;
  LARGE_INTEGER            SizeofSMRTier;
  LARGE_INTEGER             FreeSpaceInSMRTier;
  LARGE_INTEGER            UsableFreeSpaceInSMRTier;
  REFS_SMR_VOLUME_GC_STATE VolumeGcState;
  NTSTATUS                 VolumeGcLastStatus;
  ULONGLONG                Unused[7];
} REFS_SMR_VOLUME_INFO_OUTPUT, *PREFS_SMR_VOLUME_INFO_OUTPUT;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Currently ignored.  Will be set to zero for now.  </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Currently ignored. Will be set to zero for now.</p>
</dd>

### -field <b>SizeOfRandomlyWritableTier</b>

<dd>
<p>Specifies the total size of the randomly writable tier.</p>
</dd>

### -field <b>FreeSpaceInRandomlyWritableTier</b>

<dd>
<p>Specifies the free space within the randomly writable tier.</p>
</dd>

### -field <b>SizeofSMRTier</b>

<dd>
<p>Specifies the total size of the Shingled Magnetic Recording (SMR) tier.</p>
</dd>

### -field <b> FreeSpaceInSMRTier</b>

<dd>
<p>Specifies the free space the Shingled Magnetic Recording (SMR) tier.</p>
</dd>

### -field <b>UsableFreeSpaceInSMRTier</b>

<dd>
<p>Specifies the usable space the Shingled Magnetic Recording (SMR) tier.</p>
</dd>

### -field <b>VolumeGcState</b>

<dd>
<p>Specifies the current state of the garbage collector.</p>
</dd>

### -field <b>VolumeGcLastStatus</b>

<dd>
<p>Specifies the status of the last garbage collection using the specified method in <a href="https://msdn.microsoft.com/6C58EFD4-B5F9-4E2B-AF76-E9614218E0DC">REFS_SMR_VOLUME_GC_METHOD</a>.</p>
</dd>

### -field <b>Unused</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10, version 1709.</p>
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
</table>