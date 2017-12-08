---
UID: NS.BTHSDPDDI._BTHDDI_SDP_NODE_INTERFACE
title: _BTHDDI_SDP_NODE_INTERFACE
author: windows-driver-content
description: The BTHDDI_SDP_NODE_INTERFACE structure provides functions for manipulating SDP records, including converting them to and from a tree representation that profile drivers can more easily parse.
old-location: bltooth\bthddi_sdp_node_interface.htm
old-project: bltooth
ms.assetid: c9aeaaed-f017-4b23-b867-d704c4f8afb6
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: _BTHDDI_SDP_NODE_INTERFACE, *PBTHDDI_SDP_NODE_INTERFACE, BTHDDI_SDP_NODE_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bthsdpddi.h
req.include-header: BthSdpddi.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows Vista, and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BTHDDI_SDP_NODE_INTERFACE
req.alt-loc: bthsdpddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= PASSIVE_LEVEL
---

# _BTHDDI_SDP_NODE_INTERFACE structure



## -description
The BTHDDI_SDP_NODE_INTERFACE structure provides functions for manipulating SDP records, including
  converting them to and from a tree representation that profile drivers can more easily parse.


## -syntax

````
typedef struct _BTHDDI_SDP_NODE_INTERFACE {
  INTERFACE                  Interface;
  PCREATENODETREEROOT        SdpCreateNodeTree;
  PFREETREE                  SdpFreeTree;
  PCREATENODENIL             SdpCreateNodeNil;
  PCREATENODEBOOLEAN         SdpCreateNodeBoolean;
  PCREATENODEUINT8           SdpCreateNodeUint8;
  PCREATENODEUINT16          SdpCreateNodeUint16;
  PCREATENODEUINT32          SdpCreateNodeUint32;
  PCREATENODEUINT64          SdpCreateNodeUint64;
  PCREATENODEUINT128         SdpCreateNodeUint128;
  PCREATENODEINT8            SdpCreateNodeInt8;
  PCREATENODEINT16           SdpCreateNodeInt16;
  PCREATENODEINT32           SdpCreateNodeInt32;
  PCREATENODEINT64           SdpCreateNodeInt64;
  PCREATENODEINT128          SdpCreateNodeInt128;
  PCREATENODEUUID16          SdpCreateNodeUuid16;
  PCREATENODEUUID32          SdpCreateNodeUuid32;
  PCREATENODEUUID128         SdpCreateNodeUuid128;
  PCREATENODESTRING          SdpCreateNodeString;
  PCREATENODEURL             SdpCreateNodeUrl;
  PCREATENODEALTERNATIVE     SdpCreateNodeAlternative;
  PCREATENODESEQUENCE        SdpCreateNodeSequence;
  PADDATTRIBUTETOTREEE       SdpAddAttributeToTree;
  PAPPENDNODETOCONTAINERNODE SdpAppendNodeToContainerNode;
} BTHDDI_SDP_NODE_INTERFACE, *PBTHDDI_SDP_NODE_INTERFACE;
````


## -struct-fields

### -field Interface

A structure that describes the 
     <b>BTHDDI_SDP_NODE_INTERFACE</b> interface for use by profile drivers. For more information about this
     structure, see 
     <a href="kernel.interface">INTERFACE</a>.

### -field SdpCreateNodeTree

A pointer to the 
     <a href="bltooth.sdpcreatenodetree">SdpCreateNodeTree</a> function.

### -field SdpFreeTree

A pointer to the 
     <a href="bltooth.sdpfreetree">SdpFreeTree</a> function
     <i>.</i>

### -field SdpCreateNodeNil

A pointer to the 
     <a href="bltooth.sdpcreatenodenil">SdpCreateNodeNil</a> function.

### -field SdpCreateNodeBoolean

A pointer to the 
     <a href="bltooth.sdpcreatenodeboolean">SdpCreateNodeBoolean</a> function.

### -field SdpCreateNodeUint8

A pointer to the 
     <a href="bltooth.sdpcreatenodeuint8">SdpCreateNodeUInt8</a> function.

### -field SdpCreateNodeUint16

A pointer to the 
     <a href="bltooth.sdpcreatenodeuint16">SdpCreateNodeUInt16</a> function.

### -field SdpCreateNodeUint32

A pointer to the 
     <a href="bltooth.sdpcreatenodeuint32">SdpCreateNodeUInt32</a> function.

### -field SdpCreateNodeUint64

A pointer to the 
     <a href="bltooth.sdpcreatenodeuint64">SdpCreateNodeUInt64</a> function.

### -field SdpCreateNodeUint128

A pointer to the 
     <a href="bltooth.sdpcreatenodeuint128">SdpCreateNodeUInt128</a> function.

### -field SdpCreateNodeInt8

A pointer to the 
     <a href="bltooth.sdpcreatenodeuint128">SdpCreateNodeInt8</a> function.

### -field SdpCreateNodeInt16

A pointer to the 
     <a href="bltooth.sdpcreatenodeint16">SdpCreateNodeInt16</a> function.

### -field SdpCreateNodeInt32

A pointer to the 
     <a href="bltooth.sdpcreatenodeint32">SdpCreateNodeInt32</a> function.

### -field SdpCreateNodeInt64

A pointer to the 
     <a href="bltooth.sdpcreatenodeint64">SdpCreateNodeInt64</a> function.

### -field SdpCreateNodeInt128

A pointer to the 
     <a href="bltooth.sdpcreatenodeint128">SdpCreateNodeInt128</a> function.

### -field SdpCreateNodeUuid16

A pointer to the 
     <a href="bltooth.sdpcreatenodeuuid16">SdpCreateNodeUUID16</a> function.

### -field SdpCreateNodeUuid32

A pointer to the 
     <a href="bltooth.sdpcreatenodeuuid32">SdpCreateNodeUUID32</a> function.

### -field SdpCreateNodeUuid128

A pointer to the 
     <a href="bltooth.sdpcreatenodeuuid128">SdpCreateNodeUUID128</a> function.

### -field SdpCreateNodeString

A pointer to the 
     <a href="bltooth.sdpcreatenodestring">SdpCreateNodeString</a> function.

### -field SdpCreateNodeUrl

A pointer to the 
     <a href="bltooth.sdpcreatenodeurl">SdpCreateNodeUrl</a> function.

### -field SdpCreateNodeAlternative

A pointer to the 
     <a href="bltooth.sdpcreatenodealternative">
     SdpCreateNodeAlternative</a> function.

### -field SdpCreateNodeSequence

A pointer to the 
     <a href="bltooth.sdpcreatenodesequence">
     SdpCreateNodeSequence</a> function.

### -field SdpAddAttributeToTree

A pointer to the 
     <a href="bltooth.sdpaddattributetotree">
     SdpAddAttributeToTree</a> function.

### -field SdpAppendNodeToContainerNode

A pointer to the 
     <a href="bltooth.sdpappendnodetocontainernode">
     SdpAppendNodeToContainerNode</a> function.

## -remarks
Profile drivers should specify the 
    <b>GUID_BTHDDI_SDP_NODE_INTERFACE</b> GUID to query for an instance of the BTHDDI_SDP_NODE_INTERFACE
    structure from the Bluetooth driver stack.

All the members of this structure, other than the 
    <b>Interface</b> member, are function pointers.

## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Versions: Supported in Windows Vista, and later.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Bthsdpddi.h (include BthSdpddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.interface">INTERFACE</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodetree">SdpCreateNodeTree</a>
</dt>
<dt>
<a href="bltooth.sdpfreetree">SdpFreeTree</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodenil">SdpCreateNodeNil</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeboolean">SdpCreateNodeBoolean</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeuint8">SdpCreateNodeUInt8</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeuint16">SdpCreateNodeUInt16</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeuint32">SdpCreateNodeUInt32</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeuint64">SdpCreateNodeUInt64</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeuint128">SdpCreateNodeUInt128</a>
</dt>
<dt><b>SdpCreateNodeInt8</b></dt>
<dt>
<a href="bltooth.sdpcreatenodeint16">SdpCreateNodeInt16</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeint32">SdpCreateNodeInt32</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeint64">SdpCreateNodeInt64</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeint128">SdpCreateNodeInt128</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeuuid16">SdpCreateNodeUUID16</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeuuid32">SdpCreateNodeUUID32</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeuuid128">SdpCreateNodeUUID128</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodestring">SdpCreateNodeString</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodeurl">SdpCreateNodeUrl</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodealternative">SdpCreateNodeAlternative</a>
</dt>
<dt>
<a href="bltooth.sdpcreatenodesequence">SdpCreateNodeSequence</a>
</dt>
<dt>
<a href="bltooth.sdpaddattributetotree">SdpAddAttributeToTree</a>
</dt>
<dt>
<a href="bltooth.sdpappendnodetocontainernode">SdpAppendNodeToContainerNode</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20BTHDDI_SDP_NODE_INTERFACE structure%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
