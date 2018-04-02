---
UID: NS:ntddsysenv._XVARIABLE_NAME_AND_VALUE
title: "_XVARIABLE_NAME_AND_VALUE"
author: windows-driver-content
description: Stores the name and value of a system environment variable using SysEnv device. This structure is used in the IOCTL_SYSENV_ENUM_VARIABLES and IOCTL_SYSENV_SET_VARIABLE requests.
old-location: kernel\xvariable_name_and_value.htm
old-project: kernel
ms.assetid: 46E892A7-2813-4C50-BE91-B5267696E2A5
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PSYSENV_VARIABLE_AND_VALUE, *PXVARIABLE_NAME_AND_VALUE, PXVARIABLE_NAME_AND_VALUE, PXVARIABLE_NAME_AND_VALUE structure pointer [Kernel-Mode Driver Architecture], SYSENV_VARIABLE_AND_VALUE, XVARIABLE_NAME_AND_VALUE, XVARIABLE_NAME_AND_VALUE structure [Kernel-Mode Driver Architecture], _XVARIABLE_NAME_AND_VALUE, kernel.xvariable_name_and_value, ntddsysenv/PXVARIABLE_NAME_AND_VALUE, ntddsysenv/XVARIABLE_NAME_AND_VALUE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddsysenv.h
req.include-header: 
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
-	Ntddsysenv.h
api_name:
-	XVARIABLE_NAME_AND_VALUE
product: Windows
targetos: Windows
req.typenames: XVARIABLE_NAME_AND_VALUE, *PXVARIABLE_NAME_AND_VALUE
---

# _XVARIABLE_NAME_AND_VALUE structure
Stores the name and value of a system environment variable using
    SysEnv device. This structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/mt791525">IOCTL_SYSENV_ENUM_VARIABLES</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/mt791528">IOCTL_SYSENV_SET_VARIABLE</a> requests.

## Syntax
```
typedef struct _XVARIABLE_NAME_AND_VALUE {
  ULONG NextEntryOffset;
  ULONG ValueOffset;
  ULONG ValueLength;
  ULONG Attributes;
  GUID  VendorGuid;
  WCHAR Name[ANYSIZE_ARRAY];
} *PXVARIABLE_NAME_AND_VALUE, XVARIABLE_NAME_AND_VALUE;
```

## Members


`NextEntryOffset`

The location of the next entry in the array of XVARIABLE_NAME structures reprieved by the  <a href="https://msdn.microsoft.com/library/windows/hardware/mt791525">IOCTL_SYSENV_ENUM_VARIABLES</a> request.

`ValueOffset`

The value of the system environment variable.

`ValueLength`

The length of the value.

`Attributes`

Attributes of the system environment variable.

`VendorGuid`

The vendor GUID.

`Name`

Name of the system environment variable.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddsysenv.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt791525">IOCTL_SYSENV_ENUM_VARIABLES</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt791528">IOCTL_SYSENV_SET_VARIABLE</a>