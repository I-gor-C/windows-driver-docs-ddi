---
UID: NE:wdm._KEY_SET_INFORMATION_CLASS
title: "_KEY_SET_INFORMATION_CLASS"
author: windows-driver-content
description: The KEY_SET_INFORMATION_CLASS enumeration type represents the type of information to set for a registry key.
old-location: kernel\key_set_information_class.htm
old-project: kernel
ms.assetid: 95a8f683-642c-4f33-9536-08f497567f87
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: KEY_SET_INFORMATION_CLASS, KEY_SET_INFORMATION_CLASS enumeration [Kernel-Mode Driver Architecture], KeyControlFlagsInformation, KeySetDebugInformation, KeySetHandleTagsInformation, KeySetVirtualizationInformation, KeyWow64FlagsInformation, KeyWriteTimeInformation, MaxKeySetInfoClass, _KEY_SET_INFORMATION_CLASS, kernel.key_set_information_class, sysenum_b2121228-e221-424c-8e84-cd213d91716b.xml, wdm/KEY_SET_INFORMATION_CLASS, wdm/KeyControlFlagsInformation, wdm/KeySetDebugInformation, wdm/KeySetHandleTagsInformation, wdm/KeySetVirtualizationInformation, wdm/KeyWow64FlagsInformation, wdm/KeyWriteTimeInformation, wdm/MaxKeySetInfoClass
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows XP.
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
-	KEY_SET_INFORMATION_CLASS
product:
- Windows
targetos: Windows
req.typenames: KEY_SET_INFORMATION_CLASS
req.product: Windows 10 or later.
---

# _KEY_SET_INFORMATION_CLASS Enumeration
The <b>KEY_SET_INFORMATION_CLASS</b> enumeration type represents the type of information to set for a registry key.

## Syntax
```
typedef enum _KEY_SET_INFORMATION_CLASS {
  KeyWriteTimeInformation          ,
  KeyWow64FlagsInformation         ,
  KeyControlFlagsInformation       ,
  KeySetVirtualizationInformation  ,
  KeySetDebugInformation           ,
  KeySetHandleTagsInformation      ,
  KeySetLayerInformation           ,
  MaxKeySetInfoClass
} KEY_SET_INFORMATION_CLASS;
```

## Constants

<table>
            
                <tr>
                    <td>KeyWriteTimeInformation</td>
                    <td>Indicates that a <a href="https://msdn.microsoft.com/library/windows/hardware/ff554226">KEY_WRITE_TIME_INFORMATION</a> structure is supplied.</td>
                </tr>
            
                <tr>
                    <td>KeyWow64FlagsInformation</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>KeyControlFlagsInformation</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>KeySetVirtualizationInformation</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>KeySetDebugInformation</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>KeySetHandleTagsInformation</td>
                    <td>Reserved for system use.</td>
                </tr>
            
                <tr>
                    <td>KeySetLayerInformation</td>
                    <td></td>
                </tr>
            
                <tr>
                    <td>MaxKeySetInfoClass</td>
                    <td>This member constant is always the maximum value in the enumeration.</td>
                </tr>
</table>

## Remarks

A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a> routine can receive a pointer to a <b>KEY_SET_INFORMATION_CLASS</b> structure as an input parameter.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows XP. Available starting with Windows XP. |
| **Header** | wdm.h (include Wdm.h, Ntddk.h, Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff554226">KEY_WRITE_TIME_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560903">RegistryCallback</a>