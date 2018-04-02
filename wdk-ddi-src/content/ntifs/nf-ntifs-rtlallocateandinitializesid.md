---
UID: NF:ntifs.RtlAllocateAndInitializeSid
title: RtlAllocateAndInitializeSid function
author: windows-driver-content
description: Reserved for system use.
old-location: ifsk\rtlallocateandinitializesid.htm
old-project: ifsk
ms.assetid: c58f4448-06f5-4eda-a254-e453defd1d6c
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: RtlAllocateAndInitializeSid, RtlAllocateAndInitializeSid function [Installable File System Drivers], ifsk.rtlallocateandinitializesid, ntifs/RtlAllocateAndInitializeSid, rtlref_74879713-f57f-4d67-a779-995c150bc7ea.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntifs.h
api_name:
-	RtlAllocateAndInitializeSid
product: Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# RtlAllocateAndInitializeSid function
The <b>RtlAllocateAndInitializeSid</b> routine is reserved for system use. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff552146">RtlCopySid</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff552998">RtlInitializeSid</a>.

## Syntax

```
NTSYSAPI NTSTATUS RtlAllocateAndInitializeSid(
  PSID_IDENTIFIER_AUTHORITY IdentifierAuthority,
  UCHAR                     SubAuthorityCount,
  ULONG                     SubAuthority0,
  ULONG                     SubAuthority1,
  ULONG                     SubAuthority2,
  ULONG                     SubAuthority3,
  ULONG                     SubAuthority4,
  ULONG                     SubAuthority5,
  ULONG                     SubAuthority6,
  ULONG                     SubAuthority7,
  PSID                      *Sid
);
```

## Parameters

`IdentifierAuthority`

TBD

`SubAuthorityCount`

TBD

`SubAuthority0`

TBD

`SubAuthority1`

TBD

`SubAuthority2`

TBD

`SubAuthority3`

TBD

`SubAuthority4`

TBD

`SubAuthority5`

TBD

`SubAuthority6`

TBD

`SubAuthority7`

TBD

`Sid`

TBD


## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ntifs.h (include Ntifs.h) |