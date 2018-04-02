---
UID: NE:ntifs._OBJECT_INFORMATION_CLASS
title: "_OBJECT_INFORMATION_CLASS"
author: windows-driver-content
description: The OBJECT_INFORMATION_CLASS enumeration type represents the type of information to supply about an object.
old-location: ifsk\object_information_class.htm
old-project: ifsk
ms.assetid: fbcca01d-2dd6-405a-9ec2-709652e9dcd6
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: OBJECT_INFORMATION_CLASS, OBJECT_INFORMATION_CLASS enumeration [Installable File System Drivers], ObjectBasicInformation, ObjectTypeInformation, _OBJECT_INFORMATION_CLASS, ifsk.object_information_class, ntifs/OBJECT_INFORMATION_CLASS, ntifs/ObjectBasicInformation, ntifs/ObjectTypeInformation, objectstructures_60aa943f-6a91-429d-8c9d-1554f1bcf03e.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Microsoft Windows 2000.
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
-	ntifs.h
api_name:
-	OBJECT_INFORMATION_CLASS
product: Windows
targetos: Windows
req.typenames: OBJECT_INFORMATION_CLASS
---

# _OBJECT_INFORMATION_CLASS Enumeration
The OBJECT_INFORMATION_CLASS enumeration type represents the type of information to supply about an object.

## Syntax
```
typedef enum _OBJECT_INFORMATION_CLASS {
  ObjectBasicInformation  ,
  ObjectTypeInformation
} OBJECT_INFORMATION_CLASS;
```

## Constants

<table>
            
                <tr>
                    <td>ObjectBasicInformation</td>
                    <td>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff551944">PUBLIC_OBJECT_BASIC_INFORMATION</a> structure is supplied.</td>
                </tr>
            
                <tr>
                    <td>ObjectTypeInformation</td>
                    <td>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff551947">PUBLIC_OBJECT_TYPE_INFORMATION</a> structure is supplied.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Microsoft Windows 2000. Available starting with Microsoft Windows 2000. |
| **Header** | ntifs.h (include Ntifs.h, Fltkernel.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551944">PUBLIC_OBJECT_BASIC_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff551947">PUBLIC_OBJECT_TYPE_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567062">ZwQueryObject</a>