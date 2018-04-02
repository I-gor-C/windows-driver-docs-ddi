---
UID: NF:ntifs.RtlSelfRelativeToAbsoluteSD
title: RtlSelfRelativeToAbsoluteSD function
author: windows-driver-content
description: The RtlSelfRelativeToAbsoluteSD routine creates a new security descriptor in absolute format by using a security descriptor in self-relative format as a template.
old-location: ifsk\rtlselfrelativetoabsolutesd.htm
old-project: ifsk
ms.assetid: 31565c5f-a1f2-4a81-bb91-e30e13f45050
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: RtlSelfRelativeToAbsoluteSD, RtlSelfRelativeToAbsoluteSD routine [Installable File System Drivers], ifsk.rtlselfrelativetoabsolutesd, ntifs/RtlSelfRelativeToAbsoluteSD, rtlref_84aae1db-020b-440b-ab32-ade50a4b47bb.xml
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
-	RtlSelfRelativeToAbsoluteSD
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# RtlSelfRelativeToAbsoluteSD function
The <b>RtlSelfRelativeToAbsoluteSD</b> routine creates a new security descriptor in absolute format by using a security descriptor in self-relative format as a template.

## Syntax

```
NTSYSAPI NTSTATUS RtlSelfRelativeToAbsoluteSD(
  PSECURITY_DESCRIPTOR SelfRelativeSecurityDescriptor,
  PSECURITY_DESCRIPTOR AbsoluteSecurityDescriptor,
  PULONG               AbsoluteSecurityDescriptorSize,
  PACL                 Dacl,
  PULONG               DaclSize,
  PACL                 Sacl,
  PULONG               SaclSize,
  PSID                 Owner,
  PULONG               OwnerSize,
  PSID                 PrimaryGroup,
  PULONG               PrimaryGroupSize
);
```

## Parameters

`SelfRelativeSecurityDescriptor`

Pointer to a caller-allocated buffer that contains a SECURITY_DESCRIPTOR structure in self-relative format. <b>RtlSelfRelativeToAbsoluteSD</b> creates a version of this security descriptor in absolute format without modifying the original.

`AbsoluteSecurityDescriptor`

Pointer to a caller-allocated buffer that receives the main body of an absolute-format security descriptor. This information is formatted as a SECURITY_DESCRIPTOR structure.

`AbsoluteSecurityDescriptorSize`

Pointer to a caller-allocated variable that specifies the size, in bytes, of the buffer pointed to by the <i>AbsoluteSecurityDescriptor</i> parameter. If the buffer is not large enough to hold the security descriptor, <b>RtlSelfRelativeToAbsoluteSD</b> returns STATUS_BUFFER_TOO_SMALL and sets this variable to the minimum required size.

`Dacl`

Pointer to a caller-allocated buffer that receives the DACL of the absolute-format security descriptor. The main body of the absolute-format security descriptor references this pointer.

`DaclSize`

Pointer to a caller-allocated variable that specifies the size, in bytes, of the buffer pointed to by the <i>Dacl</i> parameter. If the buffer is not large enough to hold the DACL, <b>RtlSelfRelativeToAbsoluteSD</b> returns STATUS_BUFFER_TOO_SMALL and sets this variable to the minimum required size.

`Sacl`

Pointer to a caller-allocated buffer that receives the SACL of the absolute-format security descriptor. The main body of the absolute-format security descriptor references this pointer.

`SaclSize`

Pointer to a caller-allocated variable that specifies the size, in bytes, of the buffer pointed to by the <i>Sacl</i> parameter. If the buffer is not large enough to hold the SACL, <b>RtlSelfRelativeToAbsoluteSD</b> returns STATUS_BUFFER_TOO_SMALL and sets this variable to the minimum required size.

`Owner`

Pointer to a caller-allocated buffer that receives the SID of the owner of the absolute-format security descriptor. The main body of the absolute-format security descriptor references this pointer.

`OwnerSize`

Pointer to a caller-allocated variable that specifies the size, in bytes, of the buffer pointed to by the <i>Owner</i> parameter. If the buffer is not large enough to hold the SID, <b>RtlSelfRelativeToAbsoluteSD</b> returns STATUS_BUFFER_TOO_SMALL and sets this variable to the minimum required size.

`PrimaryGroup`

Pointer to a caller-allocated buffer that receives the SID of the primary group of the absolute-format security descriptor. The main body of the absolute-format security descriptor references this pointer.

`PrimaryGroupSize`

Pointer to a caller-allocated variable that specifies the size, in bytes, of the buffer pointed to by the <i>PrimaryGroup</i> parameter. If the buffer is not large enough to hold the SID, <b>RtlSelfRelativeToAbsoluteSD</b> returns STATUS_BUFFER_TOO_SMALL and sets this variable to the minimum required size.


## Return Value

<b>RtlSelfRelativeToAbsoluteSD</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as one of the following:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_BAD_DESCRIPTOR_FORMAT</b></dt>
</dl>
</td>
<td width="60%">
The buffer pointed to by the <i>AbsoluteSecurityDescriptor</i> parameter did not contain a SECURITY_DESCRIPTOR structure in absolute format. STATUS_BAD_DESCRIPTOR_FORMAT is an error code. 

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl>
</td>
<td width="60%">
The buffer pointed to by the <i>AbsoluteSecurityDescriptor</i> , <i>Dacl</i>, <i>Sacl</i>, <i>Owner</i>, or <i>PrimaryGroup</i> parameter was too small. STATUS_BUFFER_TOO_SMALL is an error code. 

</td>
</tr>
</table>

## Remarks

A security descriptor in absolute format contains pointers to the information, rather than containing the information itself. A security descriptor in self-relative format contains the information in a contiguous block of memory. In a self-relative security descriptor, a SECURITY_DESCRIPTOR structure always starts the information, but the security descriptor's other components can follow the SECURITY_DESCRIPTOR structure in any order. Instead of using memory addresses, the components of the security descriptor are identified by offsets from the beginning of the security descriptor. This format is useful when a security descriptor must be stored on a floppy disk or transmitted by means of a communications protocol. 

Note that the <i>AbsoluteSecurityDescriptor</i> parameter receives only the main body of the absolute security descriptor. The entire absolute security descriptor consists of this main body, plus all of the security descriptor components returned in the <i>Dacl</i>, <i>Sacl</i>, <i>Owner</i>, and <i>PrimaryGroup</i> buffers. Thus, the caller cannot free these buffers after calling <b>RtlSelfRelativeToAbsoluteSD</b>, because doing so would invalidate the absolute security descriptor. 

To create a new security descriptor in self-relative format by using a security descriptor in absolute format as a template, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff552089">RtlAbsoluteToSelfRelativeSD</a>. 

For more information about security and access control, see the Microsoft Windows SDK documentation.

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



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552089">RtlAbsoluteToSelfRelativeSD</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff561827">RtlCreateSecurityDescriptor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562025">RtlLengthSecurityDescriptor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff562781">RtlSetDaclSecurityDescriptor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff553220">RtlSetOwnerSecurityDescriptor</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563024">RtlValidSecurityDescriptor</a>