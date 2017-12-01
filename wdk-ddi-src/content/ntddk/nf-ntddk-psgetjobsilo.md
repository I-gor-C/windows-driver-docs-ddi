---
UID: NF.ntddk.PsGetJobSilo
title: PsGetJobSilo
author: windows-driver-content
description: This routine returns the first job in the hierarchy that is a Silo. The returned pointer is valid as long as the supplied Job object remains referenced.
old-location: kernel\psgetjobsilo.htm
old-project: kernel
ms.assetid: 1032282B-7CA3-4162-8FC2-1A4A683E9DEF
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsGetJobSilo
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
req.alt-api: PsGetJobSilo
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

# PsGetJobSilo function



## -description
<p>This routine returns the first job in the hierarchy that is a <i>Silo</i>.  The returned pointer is valid as long as the supplied <i>Job</i> object remains referenced.</p>
<p>
<div class="alert"><b>Note</b>  This returns both app silos and server silos, whichever is first.</div>
<div> </div>
</p>


## -syntax

````
NTSTATUS PsGetJobSilo(
  _In_  PEJOB  Job,
  _Out_ PESILO *Silo
);
````


## -parameters
<dl>

### -param <i>Job</i> [in]

<dd>
<p>A job object.</p>
</dd>

### -param <i>Silo</i> [out]

<dd>
<p> A pointer that receives the silo for the job.</p>
</dd>
</dl>

## -returns
<p>The following NT status codes are returned.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>Job</i> parameter is <b>NULL</b>.</p><dl>
<dt><b>STATUS_JOB_NO_CONTAINER</b></dt>
</dl><p>No silo is present.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>A PESILO is returned successfully.</p>

<p> </p>

## -remarks


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