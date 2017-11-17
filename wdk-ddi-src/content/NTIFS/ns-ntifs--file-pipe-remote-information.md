---
UID: NS.ntifs._FILE_PIPE_REMOTE_INFORMATION
title: FILE_PIPE_REMOTE_INFORMATION
author: windows-driver-content
description: The FILE_PIPE_REMOTE_INFORMATION structure contains information about the remote end of a named pipe.
old-location: ifsk\file_pipe_remote_information.htm
ms.assetid: e0e62227-5e84-45bd-9127-f5bbb30ba6f3
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_PIPE_REMOTE_INFORMATION
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
ms.keywords: FILE_PIPE_REMOTE_INFORMATION, FILE_PIPE_REMOTE_INFORMATION, *PFILE_PIPE_REMOTE_INFORMATION
req.iface: 
---

# FILE_PIPE_REMOTE_INFORMATION structure



## -description
<p>The <b>FILE_PIPE_REMOTE_INFORMATION</b> structure contains information about the remote end of a named pipe.</p>


## -syntax

````
typedef struct _FILE_PIPE_REMOTE_INFORMATION {
  LARGE_INTEGER CollectDataTime;
  ULONG         MaximumCollectionCount;
} FILE_PIPE_REMOTE_INFORMATION, *PFILE_PIPE_REMOTE_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>CollectDataTime</b>

<dd>
<p>The maximum amount of time, in 100-nanosecond intervals, that elapses before transmission of data from the client machine to the server.</p>
</dd>

### -field <b>MaximumCollectionCount</b>

<dd>
<p>The maximum size, in bytes, of data that will be collected on the client machine before transmission to the server.</p>
</dd>
</dl>

## -remarks
<p>Remote information is not available for local pipes or for the server end of a remote pipe.</p>

<p>For information about pipes, see <a href="base.pipes">Pipes</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 2000 and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>