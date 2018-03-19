---
UID: NS:wdm._REG_ENUMERATE_VALUE_KEY_INFORMATION
title: "_REG_ENUMERATE_VALUE_KEY_INFORMATION"
author: windows-driver-content
description: The REG_ENUMERATE_VALUE_KEY_INFORMATION structure describes one value entry of a key whose value entries are being enumerated.
old-location: kernel\reg_enumerate_value_key_information.htm
old-project: kernel
ms.assetid: 0d5566ca-b71c-429e-bb7d-db3eb09f0472
ms.author: windowsdriverdev
ms.date: 3/1/2018
ms.keywords: "*PREG_ENUMERATE_VALUE_KEY_INFORMATION, PREG_ENUMERATE_VALUE_KEY_INFORMATION, PREG_ENUMERATE_VALUE_KEY_INFORMATION structure pointer [Kernel-Mode Driver Architecture], REG_ENUMERATE_VALUE_KEY_INFORMATION, REG_ENUMERATE_VALUE_KEY_INFORMATION structure [Kernel-Mode Driver Architecture], _REG_ENUMERATE_VALUE_KEY_INFORMATION, kernel.reg_enumerate_value_key_information, kstruct_d_126313cd-66b7-4239-8c2a-23c475d575cf.xml, wdm/PREG_ENUMERATE_VALUE_KEY_INFORMATION, wdm/REG_ENUMERATE_VALUE_KEY_INFORMATION"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available on Microsoft Windows XP and later versions of the Windows operating system.
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
-	Wdm.h
api_name:
-	REG_ENUMERATE_VALUE_KEY_INFORMATION
product: Windows
targetos: Windows
req.typenames: REG_ENUMERATE_VALUE_KEY_INFORMATION, *PREG_ENUMERATE_VALUE_KEY_INFORMATION
req.product: Windows 10 or later.
---

# _REG_ENUMERATE_VALUE_KEY_INFORMATION structure
The <b>REG_ENUMERATE_VALUE_KEY_INFORMATION</b> structure describes one value entry of a key whose value entries are being enumerated.

## Syntax
````
typedef struct _REG_ENUMERATE_VALUE_KEY_INFORMATION {
  PVOID                       Object;
  ULONG                       Index;
  KEY_VALUE_INFORMATION_CLASS KeyValueInformationClass;
  PVOID                       KeyValueInformation;
  ULONG                       Length;
  PULONG                      ResultLength;
  PVOID                       CallContext;
  PVOID                       ObjectContext;
  PVOID                       Reserved;
} REG_ENUMERATE_VALUE_KEY_INFORMATION, *PREG_ENUMERATE_VALUE_KEY_INFORMATION;
````

## Members


`Object`

A pointer to the registry key object for the key whose value entries are being enumerated.

`Index`

The zero-based index of the subkey within the key.

`KeyValueInformationClass`

The <a href="..\wdm\ne-wdm-_key_value_information_class.md">KEY_VALUE_INFORMATION_CLASS</a> value that indicates the type of information to be returned by the system in the <b>KeyValueInformation</b> buffer.

`KeyValueInformation`

A pointer to a buffer that contains the information to be returned by the system. The format of the buffer depends on the value of <b>KeyValueInformationClass</b>. For more information see <a href="..\wdm\ne-wdm-_key_value_information_class.md">KEY_VALUE_INFORMATION_CLASS</a>.

`Length`

The size, in bytes, of the <b>KeyValueInformation</b> buffer.

`ResultLength`

A pointer to a variable that receives (from the system) the amount of valid data, in bytes, in the <b>KeyValueInformation</b> buffer.

`CallContext`

Optional driver-defined context information that the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine can supply. This member is defined for Windows Vista and later versions of the Windows operating system.

`ObjectContext`

A pointer to driver-defined context information that the driver has associated with a registry object by calling <a href="..\wdm\nf-wdm-cmsetcallbackobjectcontext.md">CmSetCallbackObjectContext</a>. This member is defined for Windows Vista and later versions of the Windows operating system.

`Reserved`

This member is reserved for future use. This member is defined for Windows Vista and later versions of the Windows operating system.

## Remarks
The system passes this structure to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine every time a thread attempts to enumerate a value entry of a key—for example, when a user-mode thread calls <b>RegEnumValue</b> or when a driver calls <a href="..\wdm\nf-wdm-zwenumeratevaluekey.md">ZwEnumerateValueKey</a>.

For more information about registry filtering operations, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff545879">Filtering Registry Calls</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available on Microsoft Windows XP and later versions of the Windows operating system. Available on Microsoft Windows XP and later versions of the Windows operating system. |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="..\wdm\ne-wdm-_key_value_information_class.md">KEY_VALUE_INFORMATION_CLASS</a>



<a href="..\wdm\nf-wdm-cmsetcallbackobjectcontext.md">CmSetCallbackObjectContext</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>



<a href="..\wdm\nf-wdm-zwenumeratevaluekey.md">ZwEnumerateValueKey</a>