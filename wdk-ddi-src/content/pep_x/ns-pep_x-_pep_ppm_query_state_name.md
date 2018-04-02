---
UID: NS:pep_x._PEP_PPM_QUERY_STATE_NAME
title: "_PEP_PPM_QUERY_STATE_NAME"
author: windows-driver-content
description: The PEP_PPM_QUERY_STATE_NAME structure contains information about a specific coordinated or platform idle state.
old-location: kernel\pep_ppm_query_state_name.htm
old-project: kernel
ms.assetid: CE0C4DAA-0B14-4CC3-B75A-66329A5830E7
ms.author: windowsdriverdev
ms.date: 3/28/2018
ms.keywords: "*PPEP_PPM_QUERY_STATE_NAME, PEP_PPM_QUERY_STATE_NAME, PEP_PPM_QUERY_STATE_NAME structure [Kernel-Mode Driver Architecture], PPEP_PPM_QUERY_STATE_NAME, PPEP_PPM_QUERY_STATE_NAME structure pointer [Kernel-Mode Driver Architecture], _PEP_PPM_QUERY_STATE_NAME, kernel.pep_ppm_query_state_name, pepfx/PEP_PPM_QUERY_STATE_NAME, pepfx/PPEP_PPM_QUERY_STATE_NAME"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pep_x.h
req.include-header: Pep_x.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
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
-	pepfx.h
api_name:
-	PEP_PPM_QUERY_STATE_NAME
product:
- Windows
targetos: Windows
req.typenames: PEP_PPM_QUERY_STATE_NAME, *PPEP_PPM_QUERY_STATE_NAME, PEP_PPM_QUERY_STATE_NAME, *PPEP_PPM_QUERY_STATE_NAME
---

# _PEP_PPM_QUERY_STATE_NAME structure
The <b>PEP_PPM_QUERY_STATE_NAME</b> structure contains information about a specific coordinated or platform idle state.

## Syntax
```
typedef struct _PEP_PPM_QUERY_STATE_NAME {
  ULONG  StateIndex;
  USHORT NameSize;
  PWSTR  Name;
} PEP_PPM_QUERY_STATE_NAME, *PPEP_PPM_QUERY_STATE_NAME;
```

## Members


`StateIndex`

[in] The index of the state that the OS is querying about.

`NameSize`

[in/out] If <b>Name</b> is <b>NULL</b>, returns the size of the buffer required to hold <b>Name</b> (including the trailing <b>UNICODE_NULL</b> character), in WCHARs.
If <b>Name</b> is not <b>NULL</b>, supplies the size of the <b>Name</b> buffer, in WCHARs.

`Name`

[in] A pointer to a buffer to copy the name of the state to, or <b>NULL</b>.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with Windows 10. Supported starting with Windows 10. |
| **Header** | pep_x.h (include Pep_x.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt186778">PEP_NOTIFY_PPM_QUERY_COORDINATED_STATE_NAME notification</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/mt186786">PEP_NOTIFY_PPM_QUERY_PROCESSOR_STATE_NAME notification</a>