---
UID: NS:bthsdpddi._BTHDDI_SDP_NODE_INTERFACE
title: "_BTHDDI_SDP_NODE_INTERFACE"
author: windows-driver-content
description: The BTHDDI_SDP_NODE_INTERFACE structure provides functions for manipulating SDP records, including converting them to and from a tree representation that profile drivers can more easily parse.
old-location: bltooth\bthddi_sdp_node_interface.htm
old-project: bltooth
ms.assetid: c9aeaaed-f017-4b23-b867-d704c4f8afb6
ms.author: windowsdriverdev
ms.date: 2/15/2018
ms.keywords: "*PBTHDDI_SDP_NODE_INTERFACE, BTHDDI_SDP_NODE_INTERFACE, BTHDDI_SDP_NODE_INTERFACE structure [Bluetooth Devices], PBTHDDI_SDP_NODE_INTERFACE, PBTHDDI_SDP_NODE_INTERFACE structure pointer [Bluetooth Devices], _BTHDDI_SDP_NODE_INTERFACE, bltooth.bthddi_sdp_node_interface, bth_structs_54f8f76d-9f12-491d-b189-c4e2fdd9b364.xml, bthsdpddi/BTHDDI_SDP_NODE_INTERFACE, bthsdpddi/PBTHDDI_SDP_NODE_INTERFACE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthsdpddi.h
req.include-header: BthSdpddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions:\_Supported in Windows Vista, and later.
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
req.irql: "<= PASSIVE_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	bthsdpddi.h
api_name:
-	BTHDDI_SDP_NODE_INTERFACE
product: Windows
targetos: Windows
req.typenames: BTHDDI_SDP_NODE_INTERFACE, *PBTHDDI_SDP_NODE_INTERFACE
---

# _BTHDDI_SDP_NODE_INTERFACE structure
The BTHDDI_SDP_NODE_INTERFACE structure provides functions for manipulating SDP records, including
  converting them to and from a tree representation that profile drivers can more easily parse.

## Syntax
```
typedef struct _BTHDDI_SDP_NODE_INTERFACE {
  INTERFACE                  Interface;
  PCREATENODETREEROOT        SdpCreateNodeTree;
  PFREETREE                  SdpFreeTree;
  PCREATENODENIL             SdpCreateNodeNil;
  PCREATENODEBOOLEAN         SdpCreateNodeBoolean;
  PCREATENODEUINT8           SdpCreateNodeUint8;
  PCREATENODEUINT16          SdpCreateNodeUint16;
  PCREATENODEUINT32          SdpCreateNodeUint32;
  PCREATENODEUINT64          SdpCreateNodeUint64;
  PCREATENODEUINT128         SdpCreateNodeUint128;
  PCREATENODEINT8            SdpCreateNodeInt8;
  PCREATENODEINT16           SdpCreateNodeInt16;
  PCREATENODEINT32           SdpCreateNodeInt32;
  PCREATENODEINT64           SdpCreateNodeInt64;
  PCREATENODEINT128          SdpCreateNodeInt128;
  PCREATENODEUUID16          SdpCreateNodeUuid16;
  PCREATENODEUUID32          SdpCreateNodeUuid32;
  PCREATENODEUUID128         SdpCreateNodeUuid128;
  PCREATENODESTRING          SdpCreateNodeString;
  PCREATENODEURL             SdpCreateNodeUrl;
  PCREATENODEALTERNATIVE     SdpCreateNodeAlternative;
  PCREATENODESEQUENCE        SdpCreateNodeSequence;
  PADDATTRIBUTETOTREEE       SdpAddAttributeToTree;
  PAPPENDNODETOCONTAINERNODE SdpAppendNodeToContainerNode;
} *PBTHDDI_SDP_NODE_INTERFACE, BTHDDI_SDP_NODE_INTERFACE;
```

## Members


`Interface`

A structure that describes the 
     <b>BTHDDI_SDP_NODE_INTERFACE</b> interface for use by profile drivers. For more information about this
     structure, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a>.

`SdpCreateNodeTree`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536818">SdpCreateNodeTree</a> function.

`SdpFreeTree`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536839">SdpFreeTree</a> function
     <i>.</i>

`SdpCreateNodeNil`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536812">SdpCreateNodeNil</a> function.

`SdpCreateNodeBoolean`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536801">SdpCreateNodeBoolean</a> function.

`SdpCreateNodeUint8`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536828">SdpCreateNodeUInt8</a> function.

`SdpCreateNodeUint16`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536822">SdpCreateNodeUInt16</a> function.

`SdpCreateNodeUint32`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536824">SdpCreateNodeUInt32</a> function.

`SdpCreateNodeUint64`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536827">SdpCreateNodeUInt64</a> function.

`SdpCreateNodeUint128`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536819">SdpCreateNodeUInt128</a> function.

`SdpCreateNodeInt8`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536811">SdpCreateNodeInt8</a> function.

`SdpCreateNodeInt16`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536804">SdpCreateNodeInt16</a> function.

`SdpCreateNodeInt32`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536806">SdpCreateNodeInt32</a> function.

`SdpCreateNodeInt64`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536808">SdpCreateNodeInt64</a> function.

`SdpCreateNodeInt128`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536802">SdpCreateNodeInt128</a> function.

`SdpCreateNodeUuid16`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536835">SdpCreateNodeUUID16</a> function.

`SdpCreateNodeUuid32`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536836">SdpCreateNodeUUID32</a> function.

`SdpCreateNodeUuid128`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536833">SdpCreateNodeUUID128</a> function.

`SdpCreateNodeString`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536816">SdpCreateNodeString</a> function.

`SdpCreateNodeUrl`

A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff536831">SdpCreateNodeUrl</a> function.

`SdpCreateNodeAlternative`

A pointer to the 
     <a href="https://msdn.microsoft.com/1e6b922d-01a2-4a67-91cb-74956d40d769">
     SdpCreateNodeAlternative</a> function.

`SdpCreateNodeSequence`

A pointer to the 
     <a href="https://msdn.microsoft.com/9e02f32b-cd39-4953-9698-a1800bedf0e2">
     SdpCreateNodeSequence</a> function.

`SdpAddAttributeToTree`

A pointer to the 
     <a href="https://msdn.microsoft.com/f5b72de2-c2e9-44ac-a2a7-04271e9253d3">
     SdpAddAttributeToTree</a> function.

`SdpAppendNodeToContainerNode`

A pointer to the 
     <a href="https://msdn.microsoft.com/beec5516-6191-4b70-8c80-ddbaedbad5c0">
     SdpAppendNodeToContainerNode</a> function.

## Remarks
Profile drivers should specify the 
    <b>GUID_BTHDDI_SDP_NODE_INTERFACE</b> GUID to query for an instance of the BTHDDI_SDP_NODE_INTERFACE
    structure from the Bluetooth driver stack.

All the members of this structure, other than the 
    <b>Interface</b> member, are function pointers.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Versions:\_Supported in Windows Vista, and later. Versions:\_Supported in Windows Vista, and later. |
| **Header** | bthsdpddi.h (include BthSdpddi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn895657">INTERFACE</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536784">SdpAddAttributeToTree</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536786">SdpAppendNodeToContainerNode</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536798">SdpCreateNodeAlternative</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536801">SdpCreateNodeBoolean</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536802">SdpCreateNodeInt128</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536804">SdpCreateNodeInt16</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536806">SdpCreateNodeInt32</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536808">SdpCreateNodeInt64</a>



<b>SdpCreateNodeInt8</b>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536812">SdpCreateNodeNil</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536814">SdpCreateNodeSequence</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536816">SdpCreateNodeString</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536818">SdpCreateNodeTree</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536819">SdpCreateNodeUInt128</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536822">SdpCreateNodeUInt16</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536824">SdpCreateNodeUInt32</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536827">SdpCreateNodeUInt64</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536828">SdpCreateNodeUInt8</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536833">SdpCreateNodeUUID128</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536835">SdpCreateNodeUUID16</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536836">SdpCreateNodeUUID32</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536831">SdpCreateNodeUrl</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536839">SdpFreeTree</a>