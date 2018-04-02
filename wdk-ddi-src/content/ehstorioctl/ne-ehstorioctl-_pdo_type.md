---
UID: NE:ehstorioctl._PDO_TYPE
title: "_PDO_TYPE"
author: windows-driver-content
description: This enumeration describes the types of Physical Device Objects (PDOs).
old-location: storage\pdo_type.htm
old-project: storage
ms.assetid: 9695d55c-a214-4bba-aba9-38dfa7f54ec9
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: PDO_TYPE, PDO_TYPE enumeration [Storage Devices], PDO_TYPE_CONTROL, PDO_TYPE_DISK, PDO_TYPE_SILO, PDO_TYPE_THIS, PDO_TYPE_UNDEFINED, _PDO_TYPE, ehstorioctl/PDO_TYPE, ehstorioctl/PDO_TYPE_CONTROL, ehstorioctl/PDO_TYPE_DISK, ehstorioctl/PDO_TYPE_SILO, ehstorioctl/PDO_TYPE_THIS, ehstorioctl/PDO_TYPE_UNDEFINED, storage.pdo_type, structs-silo_9ef418bc-5275-4fcf-a49b-804ace353da8.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ehstorioctl.h
req.include-header: EhStorIoctl.h
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
-	EhStorIoctl.h
api_name:
-	PDO_TYPE
product:
- Windows
targetos: Windows
req.typenames: PDO_TYPE
---

# _PDO_TYPE Enumeration
This enumeration describes the types of Physical Device Objects (PDOs).

## Syntax
```
typedef enum _PDO_TYPE {
  PDO_TYPE_UNDEFINED  ,
  PDO_TYPE_DISK       ,
  PDO_TYPE_CONTROL    ,
  PDO_TYPE_SILO       ,
  PDO_TYPE_THIS
} PDO_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>PDO_TYPE_UNDEFINED</td>
                    <td>Types either enumerated or provided as filter parameter to <a href="https://msdn.microsoft.com/library/windows/hardware/hh451409">IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS</a></td>
                </tr>
            
                <tr>
                    <td>PDO_TYPE_DISK</td>
                    <td>This value indicates the PDO is for a logical disk device.</td>
                </tr>
            
                <tr>
                    <td>PDO_TYPE_CONTROL</td>
                    <td>This value indicates the PDO is for a logical control device.</td>
                </tr>
            
                <tr>
                    <td>PDO_TYPE_SILO</td>
                    <td>This value indicates the PDO is for a logical silo device.</td>
                </tr>
            
                <tr>
                    <td>PDO_TYPE_THIS</td>
                    <td></td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ehstorioctl.h (include EhStorIoctl.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451409">IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS</a>