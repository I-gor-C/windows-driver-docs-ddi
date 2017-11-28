---
UID: NF.ntddk.PsGetJobServerSilo
title: PsGetJobServerSilo
author: windows-driver-content
description: This routine returns the effective ServerSilo for the job. The returned pointer is valid as long as the supplied Job object remains referenced.
old-location: kernel\psgetjobserversilo.htm
old-project: kernel
ms.assetid: 8EBCBC06-8373-43EA-91F5-6C8A439C0EAD
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PsGetJobServerSilo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsGetJobServerSilo
req.alt-loc: ntddk.h
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

# PsGetJobServerSilo function



## -description
<p>This routine returns the effective <i>ServerSilo</i> for the job. The returned pointer is valid as long as the supplied <i>Job</i> object remains referenced.</p>
<p>
<div class="alert"><b>Note</b>  This returns a <i>ServerSilo</i> or a value indicating the host silo. Unlike <a href="https://msdn.microsoft.com/library/windows/hardware/mt735068">PsGetJobSilo</a>, it will not return an app silo, even if one is present.</div>
<div> </div>
</p>


## -syntax

````
NTSTATUS PsGetJobServerSilo(
  _In_opt_ PEJOB  Job,
  _Out_    PESILO *ServerSilo
);
````


## -parameters
<dl>

### -param <i>Job</i> [in, optional]

<dd>
<p>A job object.</p>
</dd>

### -param <i>ServerSilo</i> [out]

<dd>
<p> A pointer that receives the server silo for the job.</p>
</dd>
</dl>

## -returns
<p>The following NT status codes are returned.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>Job</i> parameter is <b>NULL</b>.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>A PESILO is returned successfully.</p>

<p> </p>

## -remarks
<p><b>STATUS_SUCCESS</b> is returned even if a server silo is not in effect for the job. In that case, it will return the default host silo.</p>

<p><b>STATUS_SUCCESS</b> is returned even if a server silo is not in effect for the job. In that case, it will return the default host silo.</p>

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
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
</table>