---
UID: NF.ntifs.FsRtlSetEcpListIntoIrp
title: FsRtlSetEcpListIntoIrp
author: windows-driver-content
description: The FsRtlSetEcpListIntoIrp routine attaches an extra create parameter (ECP) context structure list to an IRP_MJ_CREATE operation.
old-location: ifsk\fsrtlsetecplistintoirp.htm
old-project: ifsk
ms.assetid: 370da53a-3c20-4e45-8732-8f08aa2d96ae
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlSetEcpListIntoIrp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: FsRtlSetEcpListIntoIrp is available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlSetEcpListIntoIrp
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

# FsRtlSetEcpListIntoIrp function



## -description
<p>The <b>FsRtlSetEcpListIntoIrp</b> routine attaches an extra create parameter (ECP) context structure list to an IRP_MJ_CREATE operation. </p>


## -syntax

````
NTSTATUS FsRtlSetEcpListIntoIrp(
  _Inout_ PIRP      Irp,
  _In_    PECP_LIST EcpList
);
````


## -parameters
<dl>

### -param Irp [in, out]

<dd>
<p>A pointer to the IRP for an IRP_MJ_CREATE operation to which the ECP context structure list is to be attached.</p>
</dd>

### -param EcpList [in]

<dd>
<p>Pointer to an ECP list that contains one or more ECP context structures. These structures will be attached to the IRP to which the <i>Irp</i> parameter points. </p>
</dd>
</dl>

## -returns
<p><b>FsRtlSetEcpListIntoIrp</b> returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The given ECP list was successfully attached to the given IRP. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>The given IRP was not an IRP-based IRP_MJ_CREATE operation. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER_3</b></dt>
</dl><p>An ECP list has already been attached to the given IRP. </p>

<p> </p>

## -remarks
<p>The <b>FsRtlSetEcpListIntoIrp</b> routine provides a mechanism for passing extra create parameters down the file system filter stack to underlying filter drivers.</p>

<p>To retrieve an ECP list that is associated with a given IRP_MJ_CREATE operation, use the <a href="..\ntifs\nf-ntifs-fsrtlgetecplistfromirp.md">FsRtlGetEcpListFromIrp</a> routine.</p>

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
<p>FsRtlSetEcpListIntoIrp is available starting with Windows Vista. </p>
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
<a href="ifsk.ecp_list">ECP_LIST</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlgetecplistfromirp.md">FsRtlGetEcpListFromIrp</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlSetEcpListIntoIrp routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
