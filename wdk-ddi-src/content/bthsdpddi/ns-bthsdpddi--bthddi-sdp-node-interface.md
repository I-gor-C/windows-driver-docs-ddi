---
UID: NS.bthsdpddi._BTHDDI_SDP_NODE_INTERFACE
title: BTHDDI_SDP_NODE_INTERFACE
author: windows-driver-content
description: The BTHDDI_SDP_NODE_INTERFACE structure provides functions for manipulating SDP records, including converting them to and from a tree representation that profile drivers can more easily parse.
old-location: bltooth\bthddi_sdp_node_interface.htm
old-project: bltooth
ms.assetid: c9aeaaed-f017-4b23-b867-d704c4f8afb6
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: BTHDDI_SDP_NODE_INTERFACE, BTHDDI_SDP_NODE_INTERFACE, *PBTHDDI_SDP_NODE_INTERFACE
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
req.iface: 
---

# BTHDDI_SDP_NODE_INTERFACE structure



## -description
<p>The BTHDDI_SDP_NODE_INTERFACE structure provides functions for manipulating SDP records, including
  converting them to and from a tree representation that profile drivers can more easily parse.</p>


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
<dl>

### -field Interface

<dd>
<p>A structure that describes the 
     <b>BTHDDI_SDP_NODE_INTERFACE</b> interface for use by profile drivers. For more information about this
     structure, see 
     <a href="..\wdm\ns-wdm--interface.md">INTERFACE</a>.</p>
</dd>

### -field SdpCreateNodeTree

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodetree.md">SdpCreateNodeTree</a> function.</p>
</dd>

### -field SdpFreeTree

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpfreetree.md">SdpFreeTree</a> function
     <i>.</i></p>
</dd>

### -field SdpCreateNodeNil

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodenil.md">SdpCreateNodeNil</a> function.</p>
</dd>

### -field SdpCreateNodeBoolean

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeboolean.md">SdpCreateNodeBoolean</a> function.</p>
</dd>

### -field SdpCreateNodeUint8

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeuint8.md">SdpCreateNodeUInt8</a> function.</p>
</dd>

### -field SdpCreateNodeUint16

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeuint16.md">SdpCreateNodeUInt16</a> function.</p>
</dd>

### -field SdpCreateNodeUint32

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeuint32.md">SdpCreateNodeUInt32</a> function.</p>
</dd>

### -field SdpCreateNodeUint64

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeuint64.md">SdpCreateNodeUInt64</a> function.</p>
</dd>

### -field SdpCreateNodeUint128

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeuint128.md">SdpCreateNodeUInt128</a> function.</p>
</dd>

### -field SdpCreateNodeInt8

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeuint128.md">SdpCreateNodeInt8</a> function.</p>
</dd>

### -field SdpCreateNodeInt16

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeint16.md">SdpCreateNodeInt16</a> function.</p>
</dd>

### -field SdpCreateNodeInt32

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeint32.md">SdpCreateNodeInt32</a> function.</p>
</dd>

### -field SdpCreateNodeInt64

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeint64.md">SdpCreateNodeInt64</a> function.</p>
</dd>

### -field SdpCreateNodeInt128

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeint128.md">SdpCreateNodeInt128</a> function.</p>
</dd>

### -field SdpCreateNodeUuid16

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeuuid16.md">SdpCreateNodeUUID16</a> function.</p>
</dd>

### -field SdpCreateNodeUuid32

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeuuid32.md">SdpCreateNodeUUID32</a> function.</p>
</dd>

### -field SdpCreateNodeUuid128

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeuuid128.md">SdpCreateNodeUUID128</a> function.</p>
</dd>

### -field SdpCreateNodeString

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodestring.md">SdpCreateNodeString</a> function.</p>
</dd>

### -field SdpCreateNodeUrl

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodeurl.md">SdpCreateNodeUrl</a> function.</p>
</dd>

### -field SdpCreateNodeAlternative

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodealternative.md">
     SdpCreateNodeAlternative</a> function.</p>
</dd>

### -field SdpCreateNodeSequence

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpcreatenodesequence.md">
     SdpCreateNodeSequence</a> function.</p>
</dd>

### -field SdpAddAttributeToTree

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpaddattributetotree.md">
     SdpAddAttributeToTree</a> function.</p>
</dd>

### -field SdpAppendNodeToContainerNode

<dd>
<p>A pointer to the 
     <a href="..\sdplib\nf-sdplib-sdpappendnodetocontainernode.md">
     SdpAppendNodeToContainerNode</a> function.</p>
</dd>
</dl>

## -remarks
<p>Profile drivers should specify the 
    <b>GUID_BTHDDI_SDP_NODE_INTERFACE</b> GUID to query for an instance of the BTHDDI_SDP_NODE_INTERFACE
    structure from the Bluetooth driver stack.</p>

<p>All the members of this structure, other than the 
    <b>Interface</b> member, are function pointers.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows Vista, and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="..\wdm\ns-wdm--interface.md">INTERFACE</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodetree.md">SdpCreateNodeTree</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpfreetree.md">SdpFreeTree</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodenil.md">SdpCreateNodeNil</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeboolean.md">SdpCreateNodeBoolean</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeuint8.md">SdpCreateNodeUInt8</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeuint16.md">SdpCreateNodeUInt16</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeuint32.md">SdpCreateNodeUInt32</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeuint64.md">SdpCreateNodeUInt64</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeuint128.md">SdpCreateNodeUInt128</a>
</dt>
<dt><b>SdpCreateNodeInt8</b></dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeint16.md">SdpCreateNodeInt16</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeint32.md">SdpCreateNodeInt32</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeint64.md">SdpCreateNodeInt64</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeint128.md">SdpCreateNodeInt128</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeuuid16.md">SdpCreateNodeUUID16</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeuuid32.md">SdpCreateNodeUUID32</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeuuid128.md">SdpCreateNodeUUID128</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodestring.md">SdpCreateNodeString</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodeurl.md">SdpCreateNodeUrl</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodealternative.md">SdpCreateNodeAlternative</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpcreatenodesequence.md">SdpCreateNodeSequence</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpaddattributetotree.md">SdpAddAttributeToTree</a>
</dt>
<dt>
<a href="..\sdplib\nf-sdplib-sdpappendnodetocontainernode.md">SdpAppendNodeToContainerNode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20BTHDDI_SDP_NODE_INTERFACE structure%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
