---
UID: NF.ntifs.FsRtlGetEcpListFromIrp
title: FsRtlGetEcpListFromIrp
author: windows-driver-content
description: The FsRtlGetEcpListFromIrp routine returns a pointer to an extra create parameter (ECP) context structure list that is associated with a given IRP_MJ_CREATE operation.
old-location: ifsk\fsrtlgetecplistfromirp.htm
old-project: ifsk
ms.assetid: 9e225f00-f830-488f-8bf0-666290dc40b0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FsRtlGetEcpListFromIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlGetEcpListFromIrp
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.iface: 
---

# FsRtlGetEcpListFromIrp function



## -description
<p>The <b>FsRtlGetEcpListFromIrp </b>routine returns a pointer to an extra create parameter (ECP) context structure list that is associated with a given IRP_MJ_CREATE operation.</p>


## -syntax

````
NTSTATUS FsRtlGetEcpListFromIrp(
  _In_  PIRP      Irp,
  _Out_ PECP_LIST *EcpList
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>A pointer to the IRP for an IRP_MJ_CREATE operation from which the ECP context structure list is to be extracted.</p>
</dd>

### -param <i>EcpList</i> [out]

<dd>
<p>Receives a pointer to the ECP context structure list that is associated with the IRP.</p>
</dd>
</dl>

## -returns
<p><b>FsRtlGetEcpListFromIrp</b> returns STATUS_SUCCESS or an appropriate error status representing the final completion status of the operation. Possible error status codes include the following: </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The given IRP was not an IRP-based IRP_MJ_CREATE operation. In this case, <i>EcpList</i> is undefined. </p>

<p> </p>

## -remarks
<p>To attach an ECP context structure list to an IRP, use the <a href="..\ntifs\nf-ntifs-fsrtlsetecplistintoirp.md">FsRtlSetEcpListIntoIrp</a> routine.</p>

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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlsetecplistintoirp.md">FsRtlSetEcpListIntoIrp</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlGetEcpListFromIrp routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
