---
UID: NF:ntifs.SeTokenGetNoChildProcessRestricted
title: SeTokenGetNoChildProcessRestricted function
author: windows-driver-content
description: The SeTokenGetNoChildProcessRestricted routine determines the state of the no child process mitigation. It is not possible to be enforced and audit-only at the same time.
old-location: ifsk\setokengetnochildprocessrestricted.htm
old-project: ifsk
ms.assetid: 6C42E6C4-91EB-44A3-84E1-CAFDBD5CD724
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: SeTokenGetNoChildProcessRestricted, SeTokenGetNoChildProcessRestricted function [Installable File System Drivers], ifsk.setokengetnochildprocessrestricted, ntifs/SeTokenGetNoChildProcessRestricted
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
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
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	NtosKrnl.exe
api_name:
-	SeTokenGetNoChildProcessRestricted
product:
- Windows
targetos: Windows
req.typenames: TOKEN_TYPE
---


# SeTokenGetNoChildProcessRestricted function
The <b>SeTokenGetNoChildProcessRestricted</b> routine determines the state of the no child process mitigation.  It is
    not possible to be enforced and audit-only at the same time.

## Syntax

```
NTKERNELAPI VOID SeTokenGetNoChildProcessRestricted(
  PACCESS_TOKEN Token,
  PBOOLEAN      Enforced,
  PBOOLEAN      UnlessSecure,
  PBOOLEAN      AuditOnly
);
```

## Parameters

`Token`

Specifies a pointer to the access token.

`Enforced`

A pointer to a boolean that returns whether the mitigation is in enforcement mode.

`UnlessSecure`

A pointer to a boolean that returns whether secure process creation is enabled even if
        process creation is restricted.

`AuditOnly`

A pointer to a boolean that returns whether the mitigation is in audit-only mode.


## Return Value

This function does not return a value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 10, version 1709.  |
| **Target Platform** | Windows |
| **Header** | ntifs.h (include Ntifs.h) |
| **Library** | NtosKrnl.lib |
| **DLL** | NtosKrnl.exe |

## See Also

<a href="https://msdn.microsoft.com/FCFCBF4C-CBAA-4284-A6F4-67630608CF19">SeTokenSetNoChildProcessRestricted</a>