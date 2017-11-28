---
UID: NS.ntifs._FILE_PIPE_LOCAL_INFORMATION
title: FILE_PIPE_LOCAL_INFORMATION
author: windows-driver-content
description: The FILE_PIPE_LOCAL_INFORMATION structure contains information about the local end of a named pipe.
old-location: ifsk\file_pipe_local_information.htm
old-project: ifsk
ms.assetid: 7ca66b75-e5ff-46a6-8a40-47aa53bf0f6f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FILE_PIPE_LOCAL_INFORMATION, FILE_PIPE_LOCAL_INFORMATION, *PFILE_PIPE_LOCAL_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FILE_PIPE_LOCAL_INFORMATION
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

# FILE_PIPE_LOCAL_INFORMATION structure



## -description
<p>The <b>FILE_PIPE_LOCAL_INFORMATION</b> structure contains information about the local end of a named pipe.</p>


## -syntax

````
typedef struct _FILE_PIPE_LOCAL_INFORMATION {
  ULONG NamedPipeType;
  ULONG NamedPipeConfiguration;
  ULONG MaximumInstances;
  ULONG CurrentInstances;
  ULONG InboundQuota;
  ULONG ReadDataAvailable;
  ULONG OutboundQuota;
  ULONG WriteQuotaAvailable;
  ULONG NamedPipeState;
  ULONG NamedPipeEnd;
} FILE_PIPE_LOCAL_INFORMATION, *PFILE_PIPE_LOCAL_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>NamedPipeType</b>

<dd>
<p>One of the following named pipe types. </p>
<table>
<tr>
<th>Value </th>
<th>Meaning </th>
</tr>
<tr>
<td>FILE_PIPE_BYTE_STREAM_TYPE (0x00000000)</td>
<td>Data is read from the pipe as a stream of bytes.</td>
</tr>
<tr>
<td>FILE_PIPE_MESSAGE_TYPE (0x00000001)</td>
<td>Data is read from the pipe as a stream of messages.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>NamedPipeConfiguration</b>

<dd>
<p>One of the following named pipe configurations.
</p>
<table>
<tr>
<th>Value </th>
<th>Meaning </th>
</tr>
<tr>
<td>FILE_PIPE_INBOUND
(0x00000000)
</td>
<td>The flow of data in the pipe goes from client to server only.</td>
</tr>
<tr>
<td>FILE_PIPE_OUTBOUND
(0x00000001)
</td>
<td>The flow of data in the pipe goes from server to client only.</td>
</tr>
<tr>
<td>FILE_PIPE_FULL_DUPLEX
(0x00000002)
</td>
<td>The pipe is bidirectional; both server and client processes can read from and write to the pipe. </td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>MaximumInstances</b>

<dd>
<p>
The maximum number of instances that can be created for this pipe. The first instance of the pipe must specify this value.
</p>
</dd>

### -field <b>CurrentInstances</b>

<dd>
<p>
The number of current named pipe instances.
</p>
</dd>

### -field <b>InboundQuota</b>

<dd>
<p> 
The inbound quota, in bytes, for the named pipe.
</p>
</dd>

### -field <b>ReadDataAvailable</b>

<dd>
<p>
The amount of data available, in bytes, to be read from the named pipe.</p>
</dd>

### -field <b>OutboundQuota</b>

<dd>
<p>
The outbound quota, in bytes, for the named pipe.
</p>
</dd>

### -field <b>WriteQuotaAvailable</b>

<dd>
<p>

The write quota, in bytes, for the named pipe.</p>
</dd>

### -field <b>NamedPipeState</b>

<dd>
<p>The connection status for the named pipe. This state has one of the following values.</p>
<table>
<tr>
<th>Value </th>
<th>Meaning </th>
</tr>
<tr>
<td>FILE_PIPE_DISCONNECTED_STATE
(0x00000001)
</td>
<td>Named pipe is disconnected.</td>
</tr>
<tr>
<td>FILE_PIPE_LISTENING_STATE
(0x00000002)</td>
<td>Named pipe is waiting to establish a connection.</td>
</tr>
<tr>
<td>FILE_PIPE_CONNECTED_STATE
(0x00000003)</td>
<td>Named pipe is connected.</td>
</tr>
<tr>
<td>FILE_PIPE_CLOSING_STATE
(0x00000004)</td>
<td>Named pipe is in the process of being closed.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>NamedPipeEnd</b>

<dd>
<p>The type of the named pipe end, which specifies whether this is the client or the server side of a named pipe.</p>
<table>
<tr>
<th>Value </th>
<th>Meaning </th>
</tr>
<tr>
<td>FILE_PIPE_CLIENT_END
(0x00000000)</td>
<td>This is the client end of a named pipe.</td>
</tr>
<tr>
<td>FILE_PIPE_SERVER_END
(0x00000001)</td>
<td>This is the server end of a named pipe.</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks
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