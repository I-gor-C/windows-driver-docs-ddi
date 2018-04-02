---
UID: NF:fwpsk.FwpsAleEndpointGetSecurityInfo0
title: FwpsAleEndpointGetSecurityInfo0 function
author: windows-driver-content
description: The FwpsAleEndpointGetSecurityInfo0 function retrieves security information about the application layer enforcement (ALE) endpoint enumeration session.Note  FwpsAleEndpointGetSecurityInfo0 is a specific version of FwpsAleEndpointGetSecurityInfo.
old-location: netvista\fwpsaleendpointgetsecurityinfo0.htm
old-project: netvista
ms.assetid: 0c825695-7fef-4eb1-8615-f41c526aa32d
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: FwpsAleEndpointGetSecurityInfo0, FwpsAleEndpointGetSecurityInfo0 function [Network Drivers Starting with Windows Vista], fwpsk/FwpsAleEndpointGetSecurityInfo0, netvista.fwpsaleendpointgetsecurityinfo0, wfp_ref_2_funct_3_fwps_A-B_83803cc6-94be-4b32-8b33-2d12cec31e9e.xml
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	LibDef
api_location:
-	fwpkclnt.lib
-	fwpkclnt.dll
api_name:
-	FwpsAleEndpointGetSecurityInfo0
product: Windows
targetos: Windows
req.typenames: FWPS_VSWITCH_EVENT_TYPE
---


# FwpsAleEndpointGetSecurityInfo0 function
The 
  <b>FwpsAleEndpointGetSecurityInfo0</b> function retrieves security information about the application layer
  enforcement (ALE) endpoint enumeration session.
<div class="alert"><b>Note</b>  <b>FwpsAleEndpointGetSecurityInfo0</b> is a specific version of <b>FwpsAleEndpointGetSecurityInfo</b>. See <a href="https://msdn.microsoft.com/FBDF53E5-F7DE-4DEB-AC18-6D2BB59FE670">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div><div> </div>

## Syntax

```
NTSTATUS FwpsAleEndpointGetSecurityInfo0(
  HANDLE               engineHandle,
  SECURITY_INFORMATION securityInfo,
  PSID                 *sidOwner,
  PSID                 *sidGroup,
  PACL                 *dacl,
  PACL                 *sacl,
  PSECURITY_DESCRIPTOR *securityDescriptor
);
```

## Parameters

`engineHandle`

A handle for an open session with the filter engine. This handle is obtained when a session is
     opened by calling 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff550075">FwpmEngineOpen0</a>.

`securityInfo`

A set of security information flags. For more information, see the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff556635">SECURITY_INFORMATION</a> description in the
     Installable File Systems driver documentation.

`sidOwner`

The security identifier of the security owner.

`sidGroup`

The security identifier of the security group.

`dacl`

The discretionary access control list.

`sacl`

The system access control list.

`securityDescriptor`

The security descriptor structure.


## Return Value

The 
     <b>FwpsAleEndpointGetSecurityInfo0</b> function returns one of the following NTSTATUS codes.

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
The function succeeded.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>Other status codes</b></dt>
</dl>
</td>
<td width="60%">
An error occurred.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 7.  |
| **Target Platform** | Universal |
| **Header** | fwpsk.h (include Fwpsk.h) |
| **Library** | Fwpkclnt.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551126">FwpsAleEndpointEnum0</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551128">FwpsAleEndpointGetById0</a>



<a href="https://msdn.microsoft.com/7b7fed83-dcf8-466d-8bd7-42a5ed15cced">
   FwpsAleEndpointSetSecurityInfo0</a>