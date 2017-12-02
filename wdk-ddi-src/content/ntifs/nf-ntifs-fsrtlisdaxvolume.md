---
UID: NF.ntifs.FsRtlIsDaxVolume
title: FsRtlIsDaxVolume
author: windows-driver-content
description: This routine queries if the specified file is on a direct access (DAX) volume.
old-location: ifsk\fsrtlisdaxvolume.htm
old-project: ifsk
ms.assetid: FFCD2329-FD6A-48AE-8E9D-56AA7D79B174
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlIsDaxVolume
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlIsDaxVolume
req.alt-loc: ntifs.h
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
req.iface: 
---

# FsRtlIsDaxVolume function



## -description
<p>This routine queries if the specified file is on a  direct access (DAX) volume.</p>


## -syntax

````
BOOLEAN FsRtlIsDaxVolume(
  _In_ PFILE_OBJECT FileObject
);
````


## -parameters
<dl>

### -param FileObject [in]

<dd>
<p>A file object for a file, on the volume which is being queried.</p>
</dd>
</dl>

## -returns
<p>Returns <b>true</b> if the file is on a DAX volume; otherwise, <b>false</b>.</p>

## -remarks
<p>In DAX volumes,  user files
    are mapped directly to the persistent memory device.  Files are
    then accessed using the memory bus, to help boost system performance.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1607</p>
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
<dt>Ntifs.h</dt>
</dl>
</td>
</tr>
</table>