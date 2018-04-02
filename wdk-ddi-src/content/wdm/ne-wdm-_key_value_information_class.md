---
UID: NE:wdm._KEY_VALUE_INFORMATION_CLASS
title: "_KEY_VALUE_INFORMATION_CLASS"
author: windows-driver-content
description: The KEY_VALUE_INFORMATION_CLASS enumeration type specifies the type of information to supply about the value of a registry key.
old-location: kernel\key_value_information_class.htm
old-project: kernel
ms.assetid: 99a34b06-3352-47a6-95bc-051a5dfdd82e
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: KEY_VALUE_INFORMATION_CLASS, KEY_VALUE_INFORMATION_CLASS enumeration [Kernel-Mode Driver Architecture], KeyValueBasicInformation, KeyValueFullInformation, KeyValueFullInformationAlign64, KeyValuePartialInformation, KeyValuePartialInformationAlign64, MaxKeyValueInfoClass, _KEY_VALUE_INFORMATION_CLASS, kernel.key_value_information_class, sysenum_ee3730f5-18b6-45ff-bb9b-4ec2e71586fc.xml, wdm/KEY_VALUE_INFORMATION_CLASS, wdm/KeyValueBasicInformation, wdm/KeyValueFullInformation, wdm/KeyValueFullInformationAlign64, wdm/KeyValuePartialInformation, wdm/KeyValuePartialInformationAlign64, wdm/MaxKeyValueInfoClass
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
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
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Wdm.h
api_name:
-	KEY_VALUE_INFORMATION_CLASS
product:
- Windows
targetos: Windows
req.typenames: KEY_VALUE_INFORMATION_CLASS
req.product: Windows 10 or later.
---

# _KEY_VALUE_INFORMATION_CLASS Enumeration
The <b>KEY_VALUE_INFORMATION_CLASS</b> enumeration type specifies the type of information to supply about the value of a registry key.

## Syntax
```
typedef enum _KEY_VALUE_INFORMATION_CLASS {
  KeyValueBasicInformation           ,
  KeyValueFullInformation            ,
  KeyValuePartialInformation         ,
  KeyValueFullInformationAlign64     ,
  KeyValuePartialInformationAlign64  ,
  KeyValueLayerInformation           ,
  MaxKeyValueInfoClass
} KEY_VALUE_INFORMATION_CLASS;
```

## Constants

<table>
            
                <tr>
                    <td>KeyValueBasicInformation</td>
                    <td>The information is stored as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553410">KEY_VALUE_BASIC_INFORMATION</a> structure.</td>
                </tr>
            
                <tr>
                    <td>KeyValueFullInformation</td>
                    <td>The information is stored as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554217">KEY_VALUE_FULL_INFORMATION</a> structure.</td>
                </tr>
            
                <tr>
                    <td>KeyValuePartialInformation</td>
                    <td>The information is stored as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554220">KEY_VALUE_PARTIAL_INFORMATION</a> structure.</td>
                </tr>
            
                <tr>
                    <td>KeyValueFullInformationAlign64</td>
                    <td>The information is stored as a <b>KEY_VALUE_FULL_INFORMATION</b> structure that is aligned to a 64-bit (that is, 8-byte) boundary in memory. If the caller-supplied buffer does not start on a 64-bit boundary, the information is stored starting at the first 64-bit boundary in the buffer.</td>
                </tr>
            
                <tr>
                    <td>KeyValuePartialInformationAlign64</td>
                    <td>The information is stored as a <b>KEY_VALUE_PARTIAL_INFORMATION</b> structure that is aligned to a 64-bit (that is, 8-byte) boundary in memory. If the caller-supplied buffer does not start on a 64-bit boundary, the information is stored starting at the first 64-bit boundary in the buffer.</td>
                </tr>
            
                <tr>
                    <td>KeyValueLayerInformation</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>MaxKeyValueInfoClass</td>
                    <td>The maximum value in this enumeration type.</td>
                </tr>
</table>

## Remarks

Use the <b>KEY_VALUE_INFORMATION_CLASS</b> values to specify the type of data to be supplied by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566453">ZwEnumerateValueKey</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567069">ZwQueryValueKey</a> routines.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553410">KEY_VALUE_BASIC_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554217">KEY_VALUE_FULL_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff554220">KEY_VALUE_PARTIAL_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff566453">ZwEnumerateValueKey</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567069">ZwQueryValueKey</a>