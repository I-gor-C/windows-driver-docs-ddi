---
UID: NF:ntifs.RtlGetSaclSecurityDescriptor
title: RtlGetSaclSecurityDescriptor function
author: windows-driver-content
description: The RtlGetSaclSecurityDescriptor routine returns a pointer to the system ACL (SACL) for a security descriptor.
old-location: ifsk\rtlgetsaclsecuritydescriptor.htm
old-project: ifsk
ms.assetid: 5dd4b15a-63e1-4b80-a156-bc44aeeafb0e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: RtlGetSaclSecurityDescriptor, RtlGetSaclSecurityDescriptor routine [Installable File System Drivers], ifsk.rtlgetsaclsecuritydescriptor, ntifs/RtlGetSaclSecurityDescriptor, rtlref_708c4a48-6840-426d-9c64-1eff896e8446.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows Server 2003 SP1 and later.
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
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: "<= APC_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	RtlGetSaclSecurityDescriptor
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# RtlGetSaclSecurityDescriptor function
The <b>RtlGetSaclSecurityDescriptor</b> routine returns a pointer to the system ACL (SACL) for a security descriptor.

## Syntax

```
NTSYSAPI NTSTATUS RtlGetSaclSecurityDescriptor(
  PSECURITY_DESCRIPTOR SecurityDescriptor,
  PBOOLEAN             SaclPresent,
  PACL                 *Sacl,
  PBOOLEAN             SaclDefaulted
);
```

## Parameters

`SecurityDescriptor`

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a> whose SACL is to be returned.

`SaclPresent`

Pointer to a Boolean variable that indicates the presence of a SACL in the specified security descriptor. If this variable receives <b>TRUE</b>, the security descriptor contains a SACL, and the remaining output parameters receive valid values. If this variable receives <b>FALSE</b>, the security descriptor does not contain a SACL, and the remaining output parameters do not receive valid values.

`Sacl`

Pointer to a variable that receives the address of the SACL for the security descriptor. If the security descriptor does not have a SACL, this variable does not receive a value. If the security descriptor has a <b>NULL</b> SACL, this variable receives <b>NULL</b>.

`SaclDefaulted`

Pointer to a Boolean variable that receives the value of the SE_SACL_DEFAULTED flag in the security descriptor's SECURITY_DESCRIPTOR_CONTROL structure if a SACL exists for the security descriptor.


## Return Value

<b>RtlGetSaclSecurityDescriptor</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_UNKNOWN_REVISION</b></dt>
</dl>
</td>
<td width="60%">
The security descriptor's revision level is unknown or is not supported. This is an error code.

</td>
</tr>
</table>

## Remarks

For more information about security and access control, see the documentation for these topics in the Microsoft Windows SDK.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This routine is available on Microsoft Windows Server 2003 SP1 and later.  |
| **Target Platform** | Universal |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |
| **IRQL** | "<= APC_LEVEL" |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff538866">ACL</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561827">RtlCreateSecurityDescriptor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552292">RtlGetDaclSecurityDescriptor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562025">RtlLengthSecurityDescriptor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562781">RtlSetDaclSecurityDescriptor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563024">RtlValidSecurityDescriptor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563689">SECURITY_DESCRIPTOR</a>