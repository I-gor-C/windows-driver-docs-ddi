---
UID: NS:ntddscsi._STORAGE_DIAGNOSTIC_MP_REQUEST
title: "_STORAGE_DIAGNOSTIC_MP_REQUEST"
author: windows-driver-content
description: Describes a diagnostic request to Miniport. The STORAGE_DIAGNOSTIC_MP_REQUEST structure is provided in the input/output buffer of an IOCTL_SCSI_MINIPORT_DIAGNOSTIC request.
old-location: storage\storage_diagnostic_mp_request.htm
old-project: storage
ms.assetid: 1F2B15A6-7C05-4FBA-B54F-EEF013FF5739
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PSTORAGE_DIAGNOSTIC_MP_REQUEST, PSTORAGE_DIAGNOSTIC_MP_REQUEST, PSTORAGE_DIAGNOSTIC_MP_REQUEST structure pointer [Storage Devices], STORAGE_DIAGNOSTIC_MP_REQUEST, STORAGE_DIAGNOSTIC_MP_REQUEST structure [Storage Devices], _STORAGE_DIAGNOSTIC_MP_REQUEST, ntddscsi/PSTORAGE_DIAGNOSTIC_MP_REQUEST, ntddscsi/STORAGE_DIAGNOSTIC_MP_REQUEST, storage.storage_diagnostic_mp_request"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddscsi.h
req.include-header: 
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ntddscsi.h
api_name:
-	STORAGE_DIAGNOSTIC_MP_REQUEST
product: Windows
targetos: Windows
req.typenames: STORAGE_DIAGNOSTIC_MP_REQUEST, *PSTORAGE_DIAGNOSTIC_MP_REQUEST
---

# _STORAGE_DIAGNOSTIC_MP_REQUEST structure
Describes  a diagnostic request to Miniport. The <b>STORAGE_DIAGNOSTIC_MP_REQUEST</b> structure is provided in the input/output buffer of an  <a href="https://msdn.microsoft.com/79E89E4A-3B06-40FA-BFA6-598331C0A330">IOCTL_SCSI_MINIPORT_DIAGNOSTIC</a> request.

## Syntax
```
typedef struct _STORAGE_DIAGNOSTIC_MP_REQUEST {
  ULONG                             Version;
  ULONG                             Size;
  MP_STORAGE_DIAGNOSTIC_TARGET_TYPE TargetType;
  MP_STORAGE_DIAGNOSTIC_LEVEL       Level;
  GUID                              ProviderId;
  ULONG                             BufferSize;
  ULONG                             Reserved;
  UCHAR                             DataBuffer[ANYSIZE_ARRAY];
} STORAGE_DIAGNOSTIC_MP_REQUEST, *PSTORAGE_DIAGNOSTIC_MP_REQUEST;
```

## Members


`Version`

Version of this structure.

`Size`

Specifies the whole size of the structure and the associated data buffer.

`TargetType`

Specifies the request target type. See definitions for <a href="https://msdn.microsoft.com/8BC338FB-7C76-49D3-96E5-0F20C4A250CE">STORAGE_DIAGNOSTIC_TARGET_TYPE</a>.

`Level`

Specifies the Diagnostic level. See definitions for <a href="https://msdn.microsoft.com/6D705DA8-7F45-4C7A-813F-5AE4F5A1D8ED">STORAGE_DIAGNOSTIC_LEVEL</a>.

`ProviderId`

Specifies the GUID of the diagnostic data provider.

`BufferSize`

Specifies the Data buffer size. As an input buffer, <i>BufferSize</i> should be set to number of bytes allocated for the <i>DataBuffer</i>. If the request is failed because of buffer too short, <i>BufferSize</i> should be set to the
       length required for <i>DataBuffer</i> by the diagnostic data provider;
       If the request is successful, it should be filled with returned data size of <i>DataBuffer</i>.       For other cases, it should be cleared to 0.

`Reserved`

Reserved for future use.

`DataBuffer`

Specifies the Diagnostic data buffer.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available starting with Windows 10, version 1709. Available starting with Windows 10, version 1709. |
| **Header** | ntddscsi.h |

## See Also

<a href="https://msdn.microsoft.com/79E89E4A-3B06-40FA-BFA6-598331C0A330">IOCTL_SCSI_MINIPORT_DIAGNOSTIC</a>



<a href="https://msdn.microsoft.com/68BC990B-DD0C-49CD-95EC-672FD1459B39">STORAGE_DIAGNOSTIC_DATA</a>



<a href="https://msdn.microsoft.com/6D705DA8-7F45-4C7A-813F-5AE4F5A1D8ED">STORAGE_DIAGNOSTIC_LEVEL</a>



<a href="https://msdn.microsoft.com/8BC338FB-7C76-49D3-96E5-0F20C4A250CE">STORAGE_DIAGNOSTIC_TARGET_TYPE</a>