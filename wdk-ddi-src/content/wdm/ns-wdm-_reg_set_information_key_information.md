---
UID: NS:wdm._REG_SET_INFORMATION_KEY_INFORMATION
title: "_REG_SET_INFORMATION_KEY_INFORMATION"
author: windows-driver-content
description: The REG_SET_INFORMATION_KEY_INFORMATION structure describes a new setting for a key's metadata.
old-location: kernel\reg_set_information_key_information.htm
old-project: kernel
ms.assetid: 30b29bda-9cd9-4fc8-b168-e66f69b82358
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PREG_SET_INFORMATION_KEY_INFORMATION, PREG_SET_INFORMATION_KEY_INFORMATION, PREG_SET_INFORMATION_KEY_INFORMATION structure pointer [Kernel-Mode Driver Architecture], REG_SET_INFORMATION_KEY_INFORMATION, REG_SET_INFORMATION_KEY_INFORMATION structure [Kernel-Mode Driver Architecture], _REG_SET_INFORMATION_KEY_INFORMATION, kernel.reg_set_information_key_information, kstruct_d_f6265b80-6f92-4856-bb8e-49cc97a1c553.xml, wdm/PREG_SET_INFORMATION_KEY_INFORMATION, wdm/REG_SET_INFORMATION_KEY_INFORMATION"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
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
req.irql: PASSIVE_LEVEL (see Remarks section)
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdm.h
api_name:
-	REG_SET_INFORMATION_KEY_INFORMATION
product: Windows
targetos: Windows
req.typenames: REG_SET_INFORMATION_KEY_INFORMATION, *PREG_SET_INFORMATION_KEY_INFORMATION
req.product: Windows 10 or later.
---

# _REG_SET_INFORMATION_KEY_INFORMATION structure
The <b>REG_SET_INFORMATION_KEY_INFORMATION</b> structure describes a new setting for a key's metadata.

## Syntax
```
typedef struct _REG_SET_INFORMATION_KEY_INFORMATION {
  PVOID                     Object;
  KEY_SET_INFORMATION_CLASS KeySetInformationClass;
  PVOID                     KeySetInformation;
  ULONG                     KeySetInformationLength;
  PVOID                     CallContext;
  PVOID                     ObjectContext;
  PVOID                     Reserved;
} *PREG_SET_INFORMATION_KEY_INFORMATION, REG_SET_INFORMATION_KEY_INFORMATION;
```

## Members


`Object`

A pointer to the registry key object for the key whose metadata is about to be changed.

`KeySetInformationClass`

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff553399">KEY_SET_INFORMATION_CLASS</a> value that indicates the type of information about to be changed.

`KeySetInformation`

A pointer to a buffer that contains the information about to be written. The format of the buffer depends on the value of <b>KeySetInformationClass</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff553399">KEY_SET_INFORMATION_CLASS</a>.

`KeySetInformationLength`

The size, in bytes, of the <b>KeySetInformation</b> buffer.

`CallContext`

Optional driver-defined context information that the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine can supply. This member is defined for Windows Vista and later versions of the Windows operating system.

`ObjectContext`

A pointer to driver-defined context information that the driver has associated with a registry object by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff541924">CmSetCallbackObjectContext</a>. This member is defined for Windows Vista and later versions of the Windows operating system.

`Reserved`

This member is reserved for future use. This member is defined for Windows Vista and later versions of the Windows operating system.

## Remarks
For more information about registry filtering operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff541924">CmSetCallbackObjectContext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>