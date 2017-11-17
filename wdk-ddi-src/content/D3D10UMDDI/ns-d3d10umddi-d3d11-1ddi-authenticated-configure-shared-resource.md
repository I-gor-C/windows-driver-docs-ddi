---
UID: NS.d3d10umddi.D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE
title: D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE
author: windows-driver-content
description: Contains input data for a call to the ConfigureAuthenticatedChannel(D3D11_1) function when D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT.ConfigureType has a GUID value of D3D11_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE.
old-location: display\d3d11_1ddi_authenticated_configure_shared_resource.htm
ms.assetid: 004046d1-552e-43a5-94b1-30b113e8b40e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE
req.alt-loc: D3d10umddi.h
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
ms.keywords: D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE, D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE
req.iface: 
---

# D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE structure



## -description
<p>Contains input data for a call to the <a href="https://msdn.microsoft.com/28d32813-15f5-4b9c-9bdb-5ad9b47bbe3b">ConfigureAuthenticatedChannel(D3D11_1)</a> function when <a href="https://msdn.microsoft.com/library/windows/hardware/hh406358">D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT</a>.<b>ConfigureType</b> has a GUID value of <b>D3D11_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE</b>.</p>


## -syntax

````
typedef struct D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE {
  D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT         Parameters;
  D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE ProcessType;
  HANDLE                                           ProcessHandle;
  BOOL                                             AllowAccess;
} D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE;
````


## -struct-fields
<dl>

### -field <b>Parameters</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh406358">D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT</a> structure that contains the command GUID and other data. </p>
</dd>

### -field <b>ProcessType</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/hh406372">D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE</a> value that specifies the type of process. To specify the DWM process, set this member to <b>D3D11_1DDI_PROCESSIDTYPE_DWM</b>. Otherwise, set this member to <b>D3D11_1DDI_PROCESSIDTYPE_HANDLE</b> and set the <b>ProcessHandle</b> member to a valid handle.</p>
</dd>

### -field <b>ProcessHandle</b>

<dd>
<p>A process handle. If the <b>ProcessType</b> member equals <b>D3D11_1DDI_PROCESSIDTYPE_HANDLE</b>, the <b>ProcessHandle</b> member specifies a handle to a process. Otherwise, the value is ignored.</p>
</dd>

### -field <b>AllowAccess</b>

<dd>
<p>If <b>TRUE</b>, the specified process has access to restricted shared resources.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/28d32813-15f5-4b9c-9bdb-5ad9b47bbe3b">ConfigureAuthenticatedChannel(D3D11_1)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406358">D3D11_1DDI_AUTHENTICATED_CONFIGURE_INPUT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406372">D3D11_1DDI_AUTHENTICATED_PROCESS_IDENTIFIER_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D11_1DDI_AUTHENTICATED_CONFIGURE_SHARED_RESOURCE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
