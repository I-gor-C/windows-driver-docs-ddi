---
UID: NS.1394._TOPOLOGY_MAP
title: TOPOLOGY_MAP
author: windows-driver-content
description: The TOPOLOGY_MAP structure is used to store an IEEE 1394 bus topology map. The relations between devices are found in the port members of the entries in TOP_Self_ID_Array.
old-location: ieee\topology_map.htm
ms.assetid: 0a4c7ffc-94f9-4068-b650-1da43e45d0ad
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: IEEE
req.header: 1394.h
req.include-header: 1394.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TOPOLOGY_MAP
req.alt-loc: 1394.h
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
ms.keywords: TOPOLOGY_MAP, TOPOLOGY_MAP, *PTOPOLOGY_MAP
---

# TOPOLOGY_MAP structure



## -description
<p>The TOPOLOGY_MAP structure is used to store an IEEE 1394 bus topology map. The relations between devices are found in the port members of the entries in <b>TOP_Self_ID_Array</b>.</p>


## -syntax

````
typedef struct _TOPOLOGY_MAP {
  USHORT  TOP_Length;
  USHORT  TOP_CRC;
  ULONG   TOP_Generation;
  USHORT  TOP_Node_Count;
  USHORT  TOP_Self_ID_Count;
  SELF_ID TOP_Self_ID_Array[1];
} TOPOLOGY_MAP, *PTOPOLOGY_MAP;
````


## -struct-fields
<dl>

### -field <b>TOP_Length</b>

<dd>
<p>Specifies the length in quadlets of the topology map.</p>
</dd>

### -field <b>TOP_CRC</b>

<dd>
<p>Specifies the CRC value for the topology map.</p>
</dd>

### -field <b>TOP_Generation</b>

<dd>
<p>Specifies the bus reset generation for which the topology map was created.</p>
</dd>

### -field <b>TOP_Node_Count</b>

<dd>
<p>Specifies the number of nodes in the topology map.</p>
</dd>

### -field <b>TOP_Self_ID_Count</b>

<dd>
<p>Specifies the number of entries in <b>TOP_Self_ID_Array</b>.</p>
</dd>

### -field <b>TOP_Self_ID_Array</b>

<dd>
<p>Pointer to an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff538073">SELF_ID</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff538080">SELF_ID_MORE</a> structures (the two structures are the same size).</p>
</dd>
</dl>

## -remarks
<p>All data will be in big-endian format.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h (include 1394.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537646">REQUEST_GET_SPEED_TOPOLOGY_MAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20TOPOLOGY_MAP structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
