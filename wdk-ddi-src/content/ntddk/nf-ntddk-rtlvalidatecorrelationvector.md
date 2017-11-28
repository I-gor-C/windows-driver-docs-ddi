---
UID: NF.ntddk.RtlValidateCorrelationVector
title: RtlValidateCorrelationVector
author: windows-driver-content
description: Validates the specified correlation vector to check whether it conforms to the Correlation Vector Specification (v2).
old-location: kernel\rtlvalidatecorrelationvector.htm
old-project: kernel
ms.assetid: a73ab33b-3e8c-43d8-8547-1483bcd2af52
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlValidateCorrelationVector
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlValidateCorrelationVector
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode)
req.irql: PASSIVE_LEVEL
req.iface: 
---

# RtlValidateCorrelationVector function



## -description
<p>Validates the specified correlation vector to check whether it conforms to the Correlation Vector Specification (v2).
    The function specifically checks if the first 22 bytes are a valid base64 representation of a 16 byte
        buffer
         and the remaining characters match the (\.\d+)+  regular expression.
			
            </p>


## -syntax

````
 NTSTATUS  RtlValidateCorrelationVector(
  _Inout_ PCORRELATION_VECTOR CorrelationVector
);
````


## -parameters
<dl>

### -param <i>CorrelationVector</i> [in, out]

<dd>
<p>A pointer to a  <a href="..\ntddk\ns-ntddk-correlation-vector.md">CORRELATION_VECTOR</a> structure that represents the correlation vector to be validated.</p>
</dd>
</dl>

## -returns
<p>
Returns an NTSTATUS value that indicates the success of failure of the operation. </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The correlation vector is valid.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The supplied correlation vector is invalid.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
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
<dt>NtosKrnl.exe (kernel mode)</dt>
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