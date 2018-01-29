---
UID : NF:ntifs.SecLookupWellKnownSid
title : SecLookupWellKnownSid function
author : windows-driver-content
description : SecLookupWellKnownSid accepts a well-known security identifier (SID) type as input and retrieves the local security identifier (SID) for this well known SID.
old-location : ifsk\seclookupwellknownsid.htm
old-project : ifsk
ms.assetid : fbf06a28-d6f8-424c-95e0-ce24653cac64
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : ifsk.seclookupwellknownsid, ksecddref_4c0053b3-cdaa-4cdc-a4d3-6329ccf64f98.xml, ntifs/SecLookupWellKnownSid, SecLookupWellKnownSid function [Installable File System Drivers], SecLookupWellKnownSid
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Universal
req.target-min-winverclnt : This SecLookupWellKnownSid function is only available starting with Windows Server 2003.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ksecdd.lib
req.dll : 
req.irql : <= APC_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : TOKEN_TYPE
---


# SecLookupWellKnownSid function
<b>SecLookupWellKnownSid</b> accepts a well-known security identifier (SID) type as input and retrieves the local security identifier (SID) for this well known SID.

## Syntax

````
NTSTATUS SecLookupWellKnownSid(
  _In_    WELL_KNOWN_SID_TYPE SidType,
  _Out_   PSID                Sid,
  _In_    ULONG               SidBufferSize,
  _Inout_ PULONG              SidSize
);
````

## Parameters

`SidType`

An enumerated type that indicates the type of security identifier (SID) the function returns. This parameter can be one of the following enumerations for WELL_KNOWN_SID_TYPE:

`Sid`

A pointer to a buffer that receives the SID structure that corresponds to the <i>SidType</i> parameter. If this parameter is <b>NULL</b>, <i>SidBufferSize</i> must be zero.

`SidBufferSize`

A variable that specifies the size of the <i>Sid</i> buffer in bytes.

`OPTIONAL`

TBD


## Return Value

<b>SecLookupWellKnownSid</b> returns STATUS_SUCCESS on success or one of the following error codes on failure: 
<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>SEC_E_INTERNAL_ERROR</b></dt>
</dl>
</td>
<td width="60%">
An internal error occurred while trying to connect to the Local System Authority (LSA) or the local procedure call (LPC) to the security provider failed. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl>
</td>
<td width="60%">
The process ID associated with the currently executing thread does not match the current process ID. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl>
</td>
<td width="60%">
The buffer size for the <i>Sid</i>, the <i>SidBufferSize</i> parameter, was too small.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
A <b>NULL</b> pointer was passed for <i>Sid</i> parameter or a well-known SID could not be found for the <i>SidType</i> specified. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_PROCESS_IS_TERMINATING</b></dt>
</dl>
</td>
<td width="60%">
This process has terminated so it is not possible to establish a local procedure call (LPC) connection.

</td>
</tr>
</table>

## Remarks

<b>SecLookupWellKnownSid</b> attempts to find a well known SID using a <i>SidType</i> parameter. In addition to looking up well-known SIDs on the local machine, <b>SecLookupWellKnownSid</b> can look up well-known SIDs on the local domain. <b>SecLookupWellKnownSid</b>first checks a list of well-known local SIDs. If the <i>SidType</i> does not correspond to a local well-known SID, the function checks for well-known SIDs on the primary domain. 

If the function cannot find the well known SID for the <i>SidType</i> specified, <b>SecLookupWellKnownSid</b> fails. This can occur if a network time-out prevents the function from finding the SID on the primary domain. It also occurs for a <i>SidType</i> that has no corresponding well-known SID.

<b>SecLookupWellKnownSid</b> is equivalent to the Win32   <b>CreateWellKnownSid</b> function. For user-mode applications, the WELL_KNOWN_SID_TYPE enumeration is defined in <i>winbase.h</i>.

<b>SecLookupWellKnownSid</b> is exported by the ksecdd driver, which implements this function by using user-mode helper services. Accordingly, the use of this function within file systems must obey the usual rules for communication with user-mode services. <b>SecLookupWellKnownSid</b> cannot be used during paging file I/O.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** |  |
| **IRQL** | <= APC_LEVEL |
| **DDI compliance rules** |  |

## See Also

<a href="..\ntifs\nf-ntifs-seclookupaccountsid.md">SecLookupAccountSid</a>

<a href="..\ntifs\nf-ntifs-seclookupaccountname.md">SecLookupAccountName</a>

<a href="..\ntifs\ns-ntifs-_sid.md">SID</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20SecLookupWellKnownSid function%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>