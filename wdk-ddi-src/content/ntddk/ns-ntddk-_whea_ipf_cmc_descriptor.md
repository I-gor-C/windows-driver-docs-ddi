---
UID: NS:ntddk._WHEA_IPF_CMC_DESCRIPTOR
title: "_WHEA_IPF_CMC_DESCRIPTOR"
author: windows-driver-content
description: The WHEA_IPF_CMC_DESCRIPTOR structure describes a corrected machine check (CMC) error source for an Itanium processor.
old-location: whea\whea_ipf_cmc_descriptor.htm
old-project: whea
ms.assetid: 570a1dfa-d6dc-4886-ad13-0f3e1f88ddde
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: "*PWHEA_IPF_CMC_DESCRIPTOR, PWHEA_IPF_CMC_DESCRIPTOR, PWHEA_IPF_CMC_DESCRIPTOR structure pointer [WHEA Drivers and Applications], WHEA_IPF_CMC_DESCRIPTOR, WHEA_IPF_CMC_DESCRIPTOR structure [WHEA Drivers and Applications], _WHEA_IPF_CMC_DESCRIPTOR, ntddk/PWHEA_IPF_CMC_DESCRIPTOR, ntddk/WHEA_IPF_CMC_DESCRIPTOR, whea.whea_ipf_cmc_descriptor, whearef_825e6302-2ef1-4277-9fd5-4855d64fce9d.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
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
-	ntddk.h
api_name:
-	WHEA_IPF_CMC_DESCRIPTOR
product: Windows
targetos: Windows
req.typenames: WHEA_IPF_CMC_DESCRIPTOR, *PWHEA_IPF_CMC_DESCRIPTOR
---

# _WHEA_IPF_CMC_DESCRIPTOR structure
The WHEA_IPF_CMC_DESCRIPTOR structure describes a corrected machine check (CMC) error source for an Itanium processor.

## Syntax
````
typedef struct _WHEA_IPF_CMC_DESCRIPTOR {
  USHORT Type;
  UCHAR  Enabled;
  UCHAR  Reserved;
} WHEA_IPF_CMC_DESCRIPTOR, *PWHEA_IPF_CMC_DESCRIPTOR;
````

## Members


`Type`

The type of error source descriptor. This member is always set to WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_IPFCMC.

`Enabled`

A Boolean value that indicates if the error source is enabled.

`Reserved`

Reserved for system use.

## Remarks
A WHEA_IPF_CMC_DESCRIPTOR structure is contained within the <a href="..\ntddk\ns-ntddk-_whea_error_source_descriptor.md">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows. |
| **Header** | ntddk.h (include Ntddk.h) |

## See Also

<a href="..\ntddk\ns-ntddk-_whea_error_source_descriptor.md">WHEA_ERROR_SOURCE_DESCRIPTOR</a>