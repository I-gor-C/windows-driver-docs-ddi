---
UID: NE:ntddcdvd.DVD_STRUCTURE_FORMAT
title: DVD_STRUCTURE_FORMAT
author: windows-driver-content
description: The DVD_STRUCTURE_FORMAT enumeration type is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request and the DVD_READ_STRUCTURE structure to retrieve a DVD descriptor.
old-location: storage\dvd_structure_format.htm
old-project: storage
ms.assetid: 0f3ca59b-f7e9-4bd7-a652-f7f0a6075d80
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PDVD_STRUCTURE_FORMAT, DVD_STRUCTURE_FORMAT, DVD_STRUCTURE_FORMAT enumeration [Storage Devices], DvdBCADescriptor, DvdCopyrightDescriptor, DvdDiskKeyDescriptor, DvdManufacturerDescriptor, DvdMaxDescriptor, DvdPhysicalDescriptor, PDVD_STRUCTURE_FORMAT, PDVD_STRUCTURE_FORMAT enumeration pointer [Storage Devices], ntddcdvd/DVD_STRUCTURE_FORMAT, ntddcdvd/DvdBCADescriptor, ntddcdvd/DvdCopyrightDescriptor, ntddcdvd/DvdDiskKeyDescriptor, ntddcdvd/DvdManufacturerDescriptor, ntddcdvd/DvdMaxDescriptor, ntddcdvd/DvdPhysicalDescriptor, ntddcdvd/PDVD_STRUCTURE_FORMAT, storage.dvd_structure_format, structs-DVD_299fec4b-1ed0-43ea-a522-716c1a585d0e.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
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
-	ntddcdvd.h
api_name:
-	DVD_STRUCTURE_FORMAT
product:
- Windows
targetos: Windows
req.typenames: DVD_STRUCTURE_FORMAT, *PDVD_STRUCTURE_FORMAT
---

# DVD_STRUCTURE_FORMAT Enumeration
The DVD_STRUCTURE_FORMAT enumeration type is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560426">IOCTL_DVD_READ_STRUCTURE</a> request and the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553738">DVD_READ_STRUCTURE</a> structure to retrieve a DVD descriptor.

## Syntax
```
typedef enum DVD_STRUCTURE_FORMAT {
  DvdPhysicalDescriptor      ,
  DvdCopyrightDescriptor     ,
  DvdDiskKeyDescriptor       ,
  DvdBCADescriptor           ,
  DvdManufacturerDescriptor  ,
  DvdMaxDescriptor
}  *PDVD_STRUCTURE_FORMAT;
```

## Constants

<table>
            
                <tr>
                    <td>DvdPhysicalDescriptor</td>
                    <td>Indicates that caller is requesting a DVD physical descriptor.</td>
                </tr>
            
                <tr>
                    <td>DvdCopyrightDescriptor</td>
                    <td>Indicates that caller is requesting a DVD copyright descriptor containing copyright information from the DVD lead-in area.</td>
                </tr>
            
                <tr>
                    <td>DvdDiskKeyDescriptor</td>
                    <td>Indicates that caller is requesting a DVD key descriptor containing the disc key obfuscated using the bus key.</td>
                </tr>
            
                <tr>
                    <td>DvdBCADescriptor</td>
                    <td>Indicates that caller is requesting a DVD burst cutting area (BCA) descriptor.</td>
                </tr>
            
                <tr>
                    <td>DvdManufacturerDescriptor</td>
                    <td>Indicates that caller is requesting a DVD manufacturer descriptor containing disc manufacturing information from the DVD lead-in area.</td>
                </tr>
            
                <tr>
                    <td>DvdMaxDescriptor</td>
                    <td>Indicates that caller is requesting a DVD max descriptor.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddcdvd.h (include Ntddcdvd.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff553738">DVD_READ_STRUCTURE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff560426">IOCTL_DVD_READ_STRUCTURE</a>