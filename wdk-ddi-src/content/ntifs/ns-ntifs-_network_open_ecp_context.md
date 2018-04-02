---
UID: NS:ntifs._NETWORK_OPEN_ECP_CONTEXT
title: "_NETWORK_OPEN_ECP_CONTEXT"
author: windows-driver-content
description: The NETWORK_OPEN_ECP_CONTEXT structure is used to interpret network ECP contexts on files.
old-location: ifsk\network_open_ecp_context.htm
old-project: ifsk
ms.assetid: 583fe92d-ce81-47b4-bd75-5566a5379790
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PNETWORK_OPEN_ECP_CONTEXT, ECP_Structures_9cdb7dab-17df-47f3-b994-fca989b3442e.xml, NETWORK_OPEN_ECP_CONTEXT, NETWORK_OPEN_ECP_CONTEXT structure [Installable File System Drivers], PNETWORK_OPEN_ECP_CONTEXT, PNETWORK_OPEN_ECP_CONTEXT structure pointer [Installable File System Drivers], _NETWORK_OPEN_ECP_CONTEXT, ifsk.network_open_ecp_context, ntifs/NETWORK_OPEN_ECP_CONTEXT, ntifs/PNETWORK_OPEN_ECP_CONTEXT"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Windows Vista.
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
-	ntifs.h
api_name:
-	NETWORK_OPEN_ECP_CONTEXT
product:
- Windows
targetos: Windows
req.typenames: NETWORK_OPEN_ECP_CONTEXT, *PNETWORK_OPEN_ECP_CONTEXT, NETWORK_OPEN_ECP_CONTEXT, *PNETWORK_OPEN_ECP_CONTEXT
---

# _NETWORK_OPEN_ECP_CONTEXT structure
The <b>NETWORK_OPEN_ECP_CONTEXT</b> structure is used to interpret network ECP contexts on files.

## Syntax
```
typedef struct _NETWORK_OPEN_ECP_CONTEXT {
  USHORT Size;
  USHORT Reserved;
  struct {
    struct {
      NETWORK_OPEN_LOCATION_QUALIFIER  Location;
      NETWORK_OPEN_INTEGRITY_QUALIFIER Integrity;
      NETWORK_OPEN_IN_FLAGS            Flags;
    } in;
    struct {
      NETWORK_OPEN_LOCATION_QUALIFIER  Location;
      NETWORK_OPEN_INTEGRITY_QUALIFIER Integrity;
      NETWORK_OPEN_OUT_FLAGS           Flags;
    } out;
  } DUMMYSTRUCTNAME;
} *PNETWORK_OPEN_ECP_CONTEXT, NETWORK_OPEN_ECP_CONTEXT;
```

## Members


`Size`

The size, in bytes, of this structure.

`Reserved`

Reserved. Must be set to zero.

`DUMMYSTRUCTNAME`



## Remarks
For information about how to use ECPs to associate extra information with a file when the file is created, see <a href="https://msdn.microsoft.com/e32aeec6-1a0a-4d21-8358-89d9fc0a15eb">Using Extra Create Parameters with an IRP_MJ_CREATE Operation</a>. 

The NETWORK_OPEN_ECP_CONTEXT structure is read-only. You should use it to retrieve information about the network ECP context on a file only. For more information about this issue, see <a href="https://msdn.microsoft.com/6acb4be4-a7aa-431d-b2d8-3ef6d41cb4ef">System-Defined ECPs</a>.

If a caller must verify that the file system acknowledged the <b>NETWORK_OPEN_ECP_CONTEXT</b> context structure, the caller should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543321">FltIsEcpAcknowledged</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546808">FsRtlIsEcpAcknowledged</a> routine on the ECP after the operation is complete.

Drivers that run on Windows 7 and later versions of Windows and that must interpret network ECP contexts on files that reside on Windows Vista must use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550899">NETWORK_OPEN_ECP_CONTEXT_V0</a> structure instead. Drivers that run on Windows Vista and later versions of Windows use the <b>NETWORK_OPEN_ECP_CONTEXT</b> structure to interpret network ECP contexts on files. However, the <b>DUMMYSTRUCTNAME.in.Flags</b> and <b>DUMMYSTRUCTNAME.out.Flags</b> members are only supported starting with Windows 7.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This structure is available starting with Windows Vista. This structure is available starting with Windows Vista. |
| **Header** | ntifs.h (include Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff550899">NETWORK_OPEN_ECP_CONTEXT_V0</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550902">NETWORK_OPEN_INTEGRITY_QUALIFIER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff550908">NETWORK_OPEN_LOCATION_QUALIFIER</a>