---
UID: NS:ntddndis._NDIS_NDK_LOCAL_ENDPOINT_ENTRY
title: "_NDIS_NDK_LOCAL_ENDPOINT_ENTRY"
author: windows-driver-content
description: The NDIS_NDK_LOCAL_ENDPOINT_ENTRY structure specifies an ND local endpoint entry for an ND local endpoint on a miniport adapter.
old-location: netvista\ndis_ndk_local_endpoint_entry.htm
old-project: netvista
ms.assetid: 83B88D3D-8FBF-4DC1-8A73-FAB306281F36
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: NDIS_NDK_LOCAL_ENDPOINT_ENTRY, NDIS_NDK_LOCAL_ENDPOINT_ENTRY structure [Network Drivers Starting with Windows Vista], _NDIS_NDK_LOCAL_ENDPOINT_ENTRY, netvista.ndis_ndk_local_endpoint_entry, ntddndis/NDIS_NDK_LOCAL_ENDPOINT_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
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
-	ntddndis.h
api_name:
-	NDIS_NDK_LOCAL_ENDPOINT_ENTRY
product: Windows
targetos: Windows
req.typenames: NDIS_NDK_LOCAL_ENDPOINT_ENTRY
---

# _NDIS_NDK_LOCAL_ENDPOINT_ENTRY structure
The <b>NDIS_NDK_LOCAL_ENDPOINT_ENTRY</b> structure specifies an ND  local endpoint entry for an ND  local endpoint on a miniport adapter.

## Syntax
````
typedef struct _NDIS_NDK_LOCAL_ENDPOINT_ENTRY {
  SOCKADDR_INET Local;
  BOOLEAN       UserModeOwner;
  BOOLEAN       Listener;
  ULONG         OwnerPid;
} NDIS_NDK_LOCAL_ENDPOINT_ENTRY;
````

## Members


`Local`

The local IP address and port.

`UserModeOwner`

A BOOLEAN value that is TRUE if the connection is an NDS user-mode connection, or FALSE if it is an NDK kernel-mode connection.

`Listener`

A BOOLEAN value that  is TRUE if the connection is a listener or FALSE if it is a shared endpoint.

`OwnerPid`

A process identifier for an NDS user-mode connection.

## Remarks
The NDIS_NDK_LOCAL_ENDPOINT_ENTRY structure is used in the <a href="..\ntddndis\ns-ntddndis-_ndis_ndk_local_endpoints.md">NDIS_NDK_LOCAL_ENDPOINTS</a> structure to specify an array of local endpoints.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | None supported,Supported in NDIS 6.30 and later. None supported,Supported in NDIS 6.30 and later. |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="..\ntddndis\ns-ntddndis-_ndis_ndk_local_endpoints.md">NDIS_NDK_LOCAL_ENDPOINTS</a>