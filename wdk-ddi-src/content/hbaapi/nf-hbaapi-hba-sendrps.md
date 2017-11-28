---
UID: NF.hbaapi.HBA_SendRPS
title: HBA_SendRPS
author: windows-driver-content
description: The HBA_SendRPS routine sends a read port status block (RPS) request to the indicated agent port or domain controller.
old-location: storage\hba_sendrps.htm
old-project: storage
ms.assetid: 6a79896a-0591-40dd-8e2d-6e3796556564
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: HBA_SendRPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_SendRPS
req.alt-loc: Hbaapi.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hbaapi.lib
req.dll: Hbaapi.dll
req.irql: 
req.iface: 
---

# HBA_SendRPS function



## -description
<p>The <b>HBA_SendRPS</b> routine sends a read port status block (RPS) request to the indicated agent port or domain controller. </p>


## -syntax

````
HBA_STATUS HBA_API HBA_SendRPS(
  _In_    HBA_HANDLE Handle,
  _In_    HBA_WWN    hbaPortWWN,
  _In_    HBA_WWN    agent_wwn,
  _In_    HBA_UINT32 agent_domain,
  _In_    HBA_WWN    object_wwn,
  _In_    HBA_UINT32 object_port_number,
  _Out_   void       *pRspBuffer,
  _Inout_ HBA_UINT32 *RspBufferSize
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Contains a value returned by the routine <a href="https://msdn.microsoft.com/library/windows/hardware/ff557097">HBA_OpenAdapter</a> that identifies the local HBA through which the request is sent. </p>
</dd>

### -param <i>hbaPortWWN</i> [in]

<dd>
<p>Contains a 64-bit worldwide name (WWN) that uniquely identifies the local port through which the RPS request is sent. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification. </p>
</dd>

### -param <i>agent_wwn</i> [in]

<dd>
<p>Contains, when non-<b>NULL</b>, a 64-bit WWN that uniquely identifies the port to query for the status of the port referenced by <i>object_wwn. </i>If this member is <b>NULL</b>, it is ignored, and the domain controller identified by <i>agent_domain </i>is queried. </p>
</dd>

### -param <i>agent_domain</i> [in]

<dd>
<p>Contains the domain number for the domain controller to query for the status of the port referenced by <i>object_wwn. </i>If <i>agent_wwn </i>is non-<b>NULL</b>, this member is ignored.</p>
</dd>

### -param <i>object_wwn</i> [in]

<dd>
<p>Contains a 64-bit WWN that uniquely identifies the port for which status information is retrieved. If this member is <b>NULL</b>, it is ignored, and status information is retrieved for the port identified by <i>object_port_number</i>. </p>
</dd>

### -param <i>object_port_number</i> [in]

<dd>
<p>Contains the relative port number of the port for which status information is retrieved. The meaning of the relative port number is defined by the hardware vendor that contains the port, and it is the responsibility of the software that receives the status query to interpret this number. If <i>object_wwn </i>is non-<b>NULL</b>, this member is ignored.</p>
</dd>

### -param <i>pRspBuffer</i> [out]

<dd>
<p>Pointer to a buffer that receives the results of the RPS request, if the request succeeds. If the destination port or domain controller rejects the request, this buffer holds the link service reject (LS_RJT) payload data. If the amount of returned data exceeds the buffer size specified in <i>RspBufferSize</i>, the data is truncated to the buffer size<i>. </i>The payload data is in big-endian format (higher order bytes are in lower addresses). </p>
</dd>

### -param <i>RspBufferSize</i> [in, out]

<dd>
<p>On input, indicates the size, in bytes, of the buffer pointed to by <i>pRspBuffer</i>. On return, this member indicates the size, in bytes, of the response data. A buffer size of 56 bytes is sufficient for the largest response. </p>
</dd>
</dl>

## -returns
<p>The <b>HBA_SendRPS</b> routine returns a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a> that indicates the status of the HBA. In particular, <b>HBA_SendRPS</b> returns one of the following values.</p><dl>
<dt><b>HBA_STATUS_OK</b></dt>
</dl><p>Returned if the complete payload of a reply to the RPS request was successfully retrieved. </p><dl>
<dt><b>HBA_STATUS_ERROR_ILLEGAL_WWN</b></dt>
</dl><p>Returned if the HBA referenced by <i>handle</i> does not contain a port with a name that matches <i>hbaPortWWN</i>. </p><dl>
<dt><b>HBA_STATUS_ERROR_ELS_REJECT</b></dt>
</dl><p>Returned if the destination port referenced by <i>agent_wwn </i>or the domain controller referenced by <i>agent_domain </i>rejected the request node identification information data (RNID) that identifies the source HBA. </p><dl>
<dt><b>HBA_STATUS_ERROR</b></dt>
</dl><p>Returned if an unspecified error occurred that prevented the execution of the RPS request. </p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557097">HBA_OpenAdapter</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20HBA_SendRPS routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
