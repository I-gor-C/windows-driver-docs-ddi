---
UID: NF.fwpsk.FwpsAleEndpointGetSecurityInfo0
title: FwpsAleEndpointGetSecurityInfo0 function
author: windows-driver-content
description: The FwpsAleEndpointGetSecurityInfo0 function retrieves security information about the application layer enforcement (ALE) endpoint enumeration session.Note  FwpsAleEndpointGetSecurityInfo0 is a specific version of FwpsAleEndpointGetSecurityInfo.
old-location: netvista\fwpsaleendpointgetsecurityinfo0.htm
old-project: netvista
ms.assetid: 0c825695-7fef-4eb1-8615-f41c526aa32d
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
---

# FwpsAleEndpointGetSecurityInfo0 function



## -description
The 
  <b>FwpsAleEndpointGetSecurityInfo0</b> function retrieves security information about the application layer
  enforcement (ALE) endpoint enumeration session.


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

### -param engineHandle [in]

A handle for an open session with the filter engine. This handle is obtained when a session is
     opened by calling 
     <a href="netvista.fwpmengineopen0">FwpmEngineOpen0</a>.

### -param securityInfo [in]

A set of security information flags. For more information, see the 
     <a href="ifsk.security_information">SECURITY_INFORMATION</a> description in the
     Installable File Systems driver documentation.

### -param sidOwner [out]

The security identifier of the security owner.

### -param sidGroup [out]

The security identifier of the security group.

### -param dacl [out]

The discretionary access control list.

### -param sacl [out]

The system access control list.

### -param securityDescriptor [out]

The security descriptor structure.

## -returns
The 
     <b>FwpsAleEndpointGetSecurityInfo0</b> function returns one of the following NTSTATUS codes.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The function succeeded.
<dl>
<dt><b>Other status codes</b></dt>
</dl>An error occurred.

 

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available starting with Windows 7.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.fwpsaleendpointenum0">FwpsAleEndpointEnum0</a>
</dt>
<dt>
<a href="netvista.fwpsaleendpointgetbyid0">FwpsAleEndpointGetById0</a>
</dt>
<dt>
<a href="netvista.fwpsaleendpointsetsecurityinfo0">
   FwpsAleEndpointSetSecurityInfo0</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsAleEndpointGetSecurityInfo0 function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
