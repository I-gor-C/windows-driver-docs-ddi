---
UID: NS:ntddndis._NDIS_NDK_PERFORMANCE_COUNTERS
title: "_NDIS_NDK_PERFORMANCE_COUNTERS"
author: windows-driver-content
description: The NDIS_NDK_PERFORMANCE_COUNTERS structure contains the NDK performance counters.
old-location: netvista\ndis_ndk_performance_counters.htm
old-project: netvista
ms.assetid: DA752989-B49B-4832-8821-8B45AB3304CD
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*PNDIS_NDK_PERFORMANCE_COUNTERS, NDIS_NDK_PERFORMANCE_COUNTERS, NDIS_NDK_PERFORMANCE_COUNTERS structure [Network Drivers Starting with Windows Vista], PNDIS_NDK_PERFORMANCE_COUNTERS, PNDIS_NDK_PERFORMANCE_COUNTERS structure pointer [Network Drivers Starting with Windows Vista], _NDIS_NDK_PERFORMANCE_COUNTERS, netvista.ndis_ndk_performance_counters, ntddndis/NDIS_NDK_PERFORMANCE_COUNTERS, ntddndis/PNDIS_NDK_PERFORMANCE_COUNTERS"
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
-	NDIS_NDK_PERFORMANCE_COUNTERS
product: Windows
targetos: Windows
req.typenames: NDIS_NDK_PERFORMANCE_COUNTERS, *PNDIS_NDK_PERFORMANCE_COUNTERS
---

# _NDIS_NDK_PERFORMANCE_COUNTERS structure
The <b>NDIS_NDK_PERFORMANCE_COUNTERS</b> structure contains the NDK performance counters.

## Syntax
```
typedef struct _NDIS_NDK_PERFORMANCE_COUNTERS {
  ULONG64 Connect;
  ULONG64 Accept;
  ULONG64 ConnectFailure;
  ULONG64 ConnectionError;
  ULONG64 ActiveConnection;
  ULONG64 Reserved01;
  ULONG64 Reserved02;
  ULONG64 Reserved03;
  ULONG64 Reserved04;
  ULONG64 Reserved05;
  ULONG64 Reserved06;
  ULONG64 Reserved07;
  ULONG64 Reserved08;
  ULONG64 Reserved09;
  ULONG64 Reserved10;
  ULONG64 Reserved11;
  ULONG64 Reserved12;
  ULONG64 Reserved13;
  ULONG64 Reserved14;
  ULONG64 Reserved15;
  ULONG64 Reserved16;
  ULONG64 Reserved17;
  ULONG64 Reserved18;
  ULONG64 Reserved19;
  ULONG64 Reserved20;
  ULONG64 CQError;
  ULONG64 RDMAInOctets;
  ULONG64 RDMAOutOctets;
  ULONG64 RDMAInFrames;
  ULONG64 RDMAOutFrames;
} NDIS_NDK_PERFORMANCE_COUNTERS, *PNDIS_NDK_PERFORMANCE_COUNTERS;
```

## Members


`Connect`

The number of outbound connections established. In a bitmask of counters (for example, <b>MissingCounterMask</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451560">NDIS_NDK_CAPABILITIES</a> structure), this is counter 0.

`Accept`

The number of inbound <i>RDMA</i> connections established. In a bitmask of counters (for example, <b>MissingCounterMask</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451560">NDIS_NDK_CAPABILITIES</a> structure), this is counter 1.

`ConnectFailure`

The  number of inbound and outbound <i>RDMA</i> connect attempts that  failed. In a bitmask of counters, this is counter 2.

`ConnectionError`

The number of established connections with  an error before a consumer disconnected the connection. In a bitmask of counters, this is counter 3.

`ActiveConnection`

The number of  active <i>RDMA</i> connections. In a bitmask of counters, this is counter 4.

`Reserved01`

Reserved.

`Reserved02`

Reserved.

`Reserved03`

Reserved.

`Reserved04`

Reserved.

`Reserved05`

Reserved.

`Reserved06`

Reserved.

`Reserved07`

Reserved.

`Reserved08`

Reserved.

`Reserved09`

Reserved.

`Reserved10`

Reserved.

`Reserved11`

Reserved.

`Reserved12`

Reserved.

`Reserved13`

Reserved.

`Reserved14`

Reserved.

`Reserved15`

Reserved.

`Reserved16`

Reserved.

`Reserved17`

Reserved.

`Reserved18`

Reserved.

`Reserved19`

Reserved.

`Reserved20`

Reserved.

`CQError`

The number of <i>RDMA</i> completion queue (CQs) that went into an error state. In a bitmask of counters, this is counter 25.

`RDMAInOctets`

The number of bytes  for all incoming <i>RDMA</i> traffic. This should include additional layer two protocol overhead.  In a bitmask of counters, this is counter 26.

`RDMAOutOctets`

The number of bytes  for all outgoing <i>RDMA</i> traffic.  This should include additional layer two protocol overhead.  In a bitmask of counters, this is counter 27.

`RDMAInFrames`

The number, in frames,  of layer two frames that carry incoming <i>RDMA</i> traffic. In a bitmask of counters, this is counter 28.

`RDMAOutFrames`

The number, in frames,  of layer two frames that carry outgoing <i>RDMA</i> traffic. In a bitmask of counters, this is counter 29.

## Remarks
The <b>NDIS_NDK_PERFORMANCE_COUNTERS</b> structure is used in the <b>CounterSet</b>  member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451567">NDIS_NDK_STATISTICS_INFO</a> structure. 

NDK providers are required to support all the performance counters that are included
    in the <b>NDIS_NDK_PERFORMANCE_COUNTERS</b> structure. However, in the rare case that
    a provider cannot support a counter due to extreme implementation difficulties,
    the provider must indicate any unsupported counters with the mask value for the
    counter which it cannot support. The <b>MissingCounterMask</b>  parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451560">NDIS_NDK_CAPABILITIES</a> structure specifies a bitmask that identifies counters that an NDK provider does not support.

All <b>ReservedXX</b> counters must be set to zero by providers and are ignored by NDIS. The term <i>RDMA</i> refers to all NDKPI and NDSPI activity as well as activity through any other RDMA programming interface that might be exposed by the provider. All providers must report the NDKPI and NDSPI activity with these counters, but reporting activity for other RDMA programming interfaces is not a strict requirement. The term <i>RDMA traffic</i> for the RDMA in, out, byte, and frame counters refers to all RDMA activity originating from NDKPI, NDSPI, and other RDMA programming interfaces (if any). This includes reads and writes (that is, direct data placement) as well as sends and receives. This also should also include all of the associated layer two protocol overhead. That is, <i>RDMA traffic</i> on an NDK-capable adapter includes all traffic through the adapter except for traffic that is  delivered through the standard NDIS send and receive interface and TCP chimney by NDIS protocol drivers.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | None supported,Supported in NDIS 6.30 and later. None supported,Supported in NDIS 6.30 and later. |
| **Header** | ntddndis.h (include Ndis.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh451560">NDIS_NDK_CAPABILITIES</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/hh451567">NDIS_NDK_STATISTICS_INFO</a>