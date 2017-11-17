---
UID: NS.ntifs._ECP_OPEN_PARAMETERS
title: ECP_OPEN_PARAMETERS
author: windows-driver-content
description: The ECP_OPEN_PARAMETERS structure allows a caller to specify the purpose of opening of a file without interfering with existing handles and/or oplocks on the file.
old-location: ifsk\ecp_open_parameters.htm
ms.assetid: 1223C77A-EAEC-4FCF-B2CC-F1E2935AF5CB
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
req.alt-api: ECP_OPEN_PARAMETERS
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
ms.keywords: ECP_OPEN_PARAMETERS, ECP_OPEN_PARAMETERS, *PECP_OPEN_PARAMETERS
req.iface: 
---

# ECP_OPEN_PARAMETERS structure



## -description
<p>The <b>ECP_OPEN_PARAMETERS</b> structure allows a caller to specify the purpose of opening of a file without interfering with existing handles and/or oplocks on the file. </p>


## -syntax

````
typedef struct _ECP_OPEN_PARAMETERS {
  USHORT Size;
  USHORT Reserved;
  ULONG  Flags;
} ECP_OPEN_PARAMETERS, *PECP_OPEN_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size of this context structure, in bytes.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use. This must be initialized to 0.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Flags that Specify the parameters or purpose for opening a file. Contains one of the following values:</p>
<table>
<tr>
<th>Name</th>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>ECP_OPEN_PARAMETERS_FLAG_OPEN_FOR_READ </td>
<td>0x01</td>
<td>Opening file to read it.</td>
</tr>
<tr>
<td>ECP_OPEN_PARAMETERS_FLAG_OPEN_FOR_WRITE</td>
<td>0x02</td>
<td>Opening file to write to it.</td>
</tr>
<tr>
<td>ECP_OPEN_PARAMETERS_FLAG_OPEN_FOR_DELETE</td>
<td>0x04</td>
<td>Opening file to delete it.</td>
</tr>
</table>
<p> </p>
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