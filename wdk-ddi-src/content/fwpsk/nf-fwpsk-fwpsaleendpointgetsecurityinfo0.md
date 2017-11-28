---
UID: NF.fwpsk.FwpsAleEndpointGetSecurityInfo0
title: FwpsAleEndpointGetSecurityInfo0
author: windows-driver-content
description: The FwpsAleEndpointGetSecurityInfo0 function retrieves security information about the application layer enforcement (ALE) endpoint enumeration session.Note  FwpsAleEndpointGetSecurityInfo0 is a specific version of FwpsAleEndpointGetSecurityInfo.
old-location: netvista\fwpsaleendpointgetsecurityinfo0.htm
old-project: netvista
ms.assetid: 0c825695-7fef-4eb1-8615-f41c526aa32d
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpsAleEndpointGetSecurityInfo0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsAleEndpointGetSecurityInfo0
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FwpsAleEndpointGetSecurityInfo0 function



## -description
<p>The 
  <b>FwpsAleEndpointGetSecurityInfo0</b> function retrieves security information about the application layer
  enforcement (ALE) endpoint enumeration session.</p>


## -syntax

````
NTSTATUS NTAPI FwpsAleEndpointGetSecurityInfo0(
  _In_  HANDLE               engineHandle,
  _In_  SECURITY_INFORMATION securityInfo,
  _Out_ PSID                 *sidOwner,
  _Out_ PSID                 *sidGroup,
  _Out_ PACL                 *dacl,
  _Out_ PACL                 *sacl,
  _Out_ PSECURITY_DESCRIPTOR *securityDescriptor
);
````


## -parameters
<dl>

### -param <i>engineHandle</i> [in]

<dd>
<p>A handle for an open session with the filter engine. This handle is obtained when a session is
     opened by calling 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff550075">FwpmEngineOpen0</a>.</p>
</dd>

### -param <i>securityInfo</i> [in]

<dd>
<p>A set of security information flags. For more information, see the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff556635">SECURITY_INFORMATION</a> description in the
     Installable File Systems driver documentation.</p>
</dd>

### -param <i>sidOwner</i> [out]

<dd>
<p>The security identifier of the security owner.</p>
</dd>

### -param <i>sidGroup</i> [out]

<dd>
<p>The security identifier of the security group.</p>
</dd>

### -param <i>dacl</i> [out]

<dd>
<p>The discretionary access control list.</p>
</dd>

### -param <i>sacl</i> [out]

<dd>
<p>The system access control list.</p>
</dd>

### -param <i>securityDescriptor</i> [out]

<dd>
<p>The security descriptor structure.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsAleEndpointGetSecurityInfo0</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

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
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 7.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551126">FwpsAleEndpointEnum0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551128">FwpsAleEndpointGetById0</a>
</dt>
<dt>
<a href="..\fwpsk\nf-fwpsk-fwpsaleendpointsetsecurityinfo0.md">
   FwpsAleEndpointSetSecurityInfo0</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsAleEndpointGetSecurityInfo0 function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
