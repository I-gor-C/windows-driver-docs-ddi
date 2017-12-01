---
UID: NF.ntddk.RtlInitializeCorrelationVector
title: RtlInitializeCorrelationVector
author: windows-driver-content
description: Initializes the specified correlation vector with the supplied GUID.
old-location: kernel\rtlinitializecorrelationvector.htm
old-project: kernel
ms.assetid: ebf5ccbe-3325-4d3d-86c9-230776f2c9ef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlInitializeCorrelationVector
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
req.alt-api: RtlInitializeCorrelationVector
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

# RtlInitializeCorrelationVector function



## -description
<p>
			
              Initializes the specified correlation vector with
    the supplied GUID.</p>


## -syntax

````
 NTSTATUS  RtlInitializeCorrelationVector(
  _Inout_ PCORRELATION_VECTOR CorrelationVector,
  _In_    int                 Version,
  _In_    const GUID          Guid
);
````


## -parameters
<dl>

### -param <i>CorrelationVector</i> [in, out]

<dd>
<p>A pointer to a  <a href="..\ntddk\ns-ntddk-correlation-vector.md">CORRELATION_VECTOR</a> structure that represents the correlation vector to be initialized.</p>
</dd>

### -param <i>Version</i> [in]

<dd>
<p>The version of the correlation vector. Possible values are: </p>
<ul>
<li>RTL_CORRELATION_VECTOR_VERSION_1</li>
<li>RTL_CORRELATION_VECTOR_VERSION_2</li>
<li>RTL_CORRELATION_VECTOR_VERSION_CURRENT</li>
</ul>
</dd>

### -param <i>Guid</i> [in]

<dd>
<p>The GUID to initialize the correlation vector. The first 22 bytes
            of the correlation vector are a base64 representation of the GUID. This value must not be NULL.</p>
</dd>
</dl>

## -returns
<p>
Returns an NTSTATUS value that indicates the success of failure of the operation. </p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The correlation vector was successfully initialized.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The supplied GUID is null.</p>

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

## -see-also
<dl>
<dt>
<a href="..\ntddk\ns-ntddk-correlation-vector.md">CORRELATION_VECTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlInitializeCorrelationVector function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
