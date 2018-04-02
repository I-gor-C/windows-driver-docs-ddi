---
UID: NE:ntddstor._STORAGE_PROTOCOL_UFS_DATA_TYPE
title: "_STORAGE_PROTOCOL_UFS_DATA_TYPE"
author: windows-driver-content
description: The UFS (Universal Flash Storage) data type. Describes the type of UFS specific data that's to be queried during an IOCTL_STORAGE_QUERY_PROPERTY request.
old-location: storage\storage_protocol_ufs_data_type.htm
old-project: storage
ms.assetid: A4324FAD-A925-4D65-9697-9CC2878DBE0B
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PSTORAGE_PROTOCOL_UFS_DATA_TYPE, STORAGE_PROTOCOL_UFS_DATA_TYPE, STORAGE_PROTOCOL_UFS_DATA_TYPE enumeration [Storage Devices], UfsDataTypeMax, UfsDataTypeQueryDescriptor, UfsDataTypeUnknown, _STORAGE_PROTOCOL_UFS_DATA_TYPE, ntddstor/ UfsDataTypeMax, ntddstor/ UfsDataTypeQueryDescriptor, ntddstor/STORAGE_PROTOCOL_UFS_DATA_TYPE, ntddstor/UfsDataTypeUnknown, storage.storage_protocol_ufs_data_type"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: Ntddstor.h
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
-	Ntddstor.h
api_name:
-	STORAGE_PROTOCOL_UFS_DATA_TYPE
product: Windows
targetos: Windows
req.typenames: STORAGE_PROTOCOL_UFS_DATA_TYPE, *PSTORAGE_PROTOCOL_UFS_DATA_TYPE
---

# _STORAGE_PROTOCOL_UFS_DATA_TYPE Enumeration
The UFS (Universal Flash Storage) data type. Describes the type of UFS specific data that's to be queried during an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> request.

## Syntax
```
typedef enum _STORAGE_PROTOCOL_UFS_DATA_TYPE {
  UfsDataTypeUnknown          ,
  UfsDataTypeQueryDescriptor  ,
  UfsDataTypeMax
} STORAGE_PROTOCOL_UFS_DATA_TYPE, *PSTORAGE_PROTOCOL_UFS_DATA_TYPE;
```

## Constants

<table>
            
                <tr>
                    <td>UfsDataTypeUnknown</td>
                    <td>Unknown data type.</td>
                </tr>
            
                <tr>
                    <td>UfsDataTypeQueryDescriptor</td>
                    <td>Query Descriptor data type. Retrieved by command UfsSrbQueryProtocolQueryDescriptor.</td>
                </tr>
            
                <tr>
                    <td>UfsDataTypeMax</td>
                    <td>Max size of data type.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddstor.h (include Ntddstor.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn931815">STORAGE_PROTOCOL_DATA_DESCRIPTOR</a>