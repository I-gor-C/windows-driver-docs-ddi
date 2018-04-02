---
UID: NS:ntifs._SRV_OPEN_ECP_CONTEXT
title: "_SRV_OPEN_ECP_CONTEXT"
author: windows-driver-content
description: The SRV_OPEN_ECP_CONTEXT structure is used by a server to conditionally open files in response to client requests.
old-location: ifsk\srv_open_ecp_context.htm
old-project: ifsk
ms.assetid: 6860f512-758d-4a75-88e4-17310b3e6349
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PSRV_OPEN_ECP_CONTEXT, ECP_Structures_1a5afc2a-f4a5-4f86-ac30-2e206778acc0.xml, PSRV_OPEN_ECP_CONTEXT, PSRV_OPEN_ECP_CONTEXT structure pointer [Installable File System Drivers], SRV_OPEN_ECP_CONTEXT, SRV_OPEN_ECP_CONTEXT structure [Installable File System Drivers], _SRV_OPEN_ECP_CONTEXT, ifsk.srv_open_ecp_context, ntifs/PSRV_OPEN_ECP_CONTEXT, ntifs/SRV_OPEN_ECP_CONTEXT"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Windows 7.
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
-	SRV_OPEN_ECP_CONTEXT
product: Windows
targetos: Windows
req.typenames: SRV_OPEN_ECP_CONTEXT, *PSRV_OPEN_ECP_CONTEXT
---

# _SRV_OPEN_ECP_CONTEXT structure
The SRV_OPEN_ECP_CONTEXT structure is used by a server to conditionally open files in response to client requests.

## Syntax
```
typedef struct _SRV_OPEN_ECP_CONTEXT {
  PUNICODE_STRING       ShareName;
  PSOCKADDR_STORAGE_NFS SocketAddress;
  BOOLEAN               OplockBlockState;
  BOOLEAN               OplockAppState;
  BOOLEAN               OplockFinalState;
  USHORT                Version;
  SRV_INSTANCE_TYPE     InstanceType;
} SRV_OPEN_ECP_CONTEXT, *PSRV_OPEN_ECP_CONTEXT;
```

## Members


`ShareName`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that supplies the share name for the server that contains the files to be open.

`SocketAddress`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570825">SOCKADDR_STORAGE</a> structure that specifies the transport address of a client computer. This client originates the open file request.

`OplockBlockState`

A Boolean value that indicates whether the Server Message Block (SMB) server blocks the open thread that is waiting for the oplock break. <b>TRUE</b> indicates that the open thread is in the blocking state and <b>FALSE</b> otherwise.

`OplockAppState`

A Boolean value that indicates whether the SMB server requests an oplock with the current open thread. Set to <b>TRUE</b> to request the oplock and <b>FALSE</b> otherwise.

`OplockFinalState`

A Boolean value that indicates whether a file-open operation is the final file-open operation to request the oplock. <b>TRUE</b> indicates the final file-open operation to obtain the oplock and <b>FALSE</b> indicates otherwise.

`Version`



`InstanceType`



## Remarks
The file-system stack can determine whether SRV_OPEN_ECP_CONTEXT is attached to the create file request. The file-system stack can then use the information in SRV_OPEN_ECP_CONTEXT to determine which client requested that the file be opened, and why it requested it. For information about how to retrieve the SRV_OPEN_ECP_CONTEXT extra information that is attached to a create file request, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/ifs/using-ecps-to-process-irp-mj-create-operations-in-a-file-system-filter">Retrieving ECPs</a>. 

The SRV_OPEN_ECP_CONTEXT structure is read-only. You should use it to retrieve information about a server open ECP only. For more information about this issue, see <a href="https://msdn.microsoft.com/6acb4be4-a7aa-431d-b2d8-3ef6d41cb4ef">System-Defined ECPs</a>.

The oplock state values (<b>OplockBlockState</b>, <b>OplockAppState</b>, and <b>OplockFinalState</b>) are used with oplock breaking logic for system management for SMB and SMB2.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | This structure is available starting with Windows 7. This structure is available starting with Windows 7. |
| **Header** | ntifs.h (include Ntifs.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff570825">SOCKADDR_STORAGE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>