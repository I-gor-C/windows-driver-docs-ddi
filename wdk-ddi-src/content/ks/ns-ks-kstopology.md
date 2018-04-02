---
UID: NS:ks.KSTOPOLOGY
title: KSTOPOLOGY
author: windows-driver-content
description: The KSTOPOLOGY structure describes the topology of pins and nodes.
old-location: stream\kstopology.htm
old-project: stream
ms.assetid: 8dbd37ed-5d71-43bd-a3ca-caa5b0d08075
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKSTOPOLOGY, KSTOPOLOGY, KSTOPOLOGY structure [Streaming Media Devices], PKSTOPOLOGY, PKSTOPOLOGY structure pointer [Streaming Media Devices], ks-struct_1d55c5f9-18d4-43d0-9fe9-291134e84115.xml, ks/KSTOPOLOGY, ks/PKSTOPOLOGY, stream.kstopology"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
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
-	ks.h
api_name:
-	KSTOPOLOGY
product:
- Windows
targetos: Windows
req.typenames: KSTOPOLOGY, *PKSTOPOLOGY
---

# KSTOPOLOGY structure
The KSTOPOLOGY structure describes the topology of pins and nodes.

## Syntax
```
typedef struct KSTOPOLOGY {
  ULONG                       CategoriesCount;
  const GUID                  *Categories;
  ULONG                       TopologyNodesCount;
  const GUID                  *TopologyNodes;
  ULONG                       TopologyConnectionsCount;
  const KSTOPOLOGY_CONNECTION *TopologyConnections;
  const GUID                  *TopologyNodesNames;
  ULONG                       Reserved;
} *PKSTOPOLOGY, KSTOPOLOGY;
```

## Members


`CategoriesCount`

Specifies the number of functional categories that the driver supports.

`Categories`

Points to the beginning of the array of functional categories that the driver supports.

`TopologyNodesCount`

Specifies the number of nodes that the driver supports.

`TopologyNodes`

Points to the beginning of the array of GUIDs that describe the type of each node. For a list of video kernel streaming related nodes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560886">Kernel Streaming Topology Nodes</a>. For a list of audio kernel streaming related nodes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536219">Audio Topology Nodes</a>.

`TopologyConnectionsCount`

Specifies the number of entries in the array pointed to by <b>TopologyConnections</b>. The node numbers of each entry must correspond to the array offset of the node within <b>TopologyNodes</b>. When this structure is a part of a streaming minidriver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559690">HW_STREAM_HEADER</a>, the pin numbers must correspond to the offsets within the array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff559692">HW_STREAM_INFORMATION</a> structures in the minidriver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff559686">HW_STREAM_DESCRIPTOR</a> structure.

`TopologyConnections`

Points to the beginning of the array of topology connections for this structure.

`TopologyNodesNames`

Specifies the GUID of the localized Unicode string name for the node, stored in the registry.

`Reserved`

Reserved for system use. Drivers should set this to zero.

## Remarks
A stream class minidriver creates and passes this structure as part of its <a href="https://msdn.microsoft.com/library/windows/hardware/ff559690">HW_STREAM_HEADER</a> structure. The class driver uses this structure to process topology property requests. The property data that the class driver returns is determined from the KSTOPOLOGY structure as follows:

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559686">HW_STREAM_DESCRIPTOR</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559690">HW_STREAM_HEADER</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff559692">HW_STREAM_INFORMATION</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff567148">KSTOPOLOGY_CONNECTION</a>