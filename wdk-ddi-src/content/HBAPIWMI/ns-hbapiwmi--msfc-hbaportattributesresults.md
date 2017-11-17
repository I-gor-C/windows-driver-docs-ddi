---
UID: NS.hbapiwmi._MSFC_HBAPortAttributesResults
title: MSFC_HBAPortAttributesResults
author: windows-driver-content
description: The structure is used by the GetDiscoveredPortAttributes WMI method to report the attributes for a specified remote fibre channel port.
old-location: storage\msfc_hbaportattributesresults.htm
ms.assetid: cd6797a3-3128-4100-81f0-82e4d6f209b4
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h, Hbaapi.h, Hbaapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSFC_HBAPortAttributesResults
req.alt-loc: hbapiwmi.h
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
ms.keywords: MSFC_HBAPortAttributesResults, MSFC_HBAPortAttributesResults, *PMSFC_HBAPortAttributesResults
req.iface: 
---

# MSFC_HBAPortAttributesResults structure



## -description
<p>The  structure is used by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553925">GetDiscoveredPortAttributes</a> WMI method to report the attributes for a specified remote fibre channel port.</p>


## -syntax

````
typedef struct _MSFC_HBAPortAttributesResults {
  UCHAR NodeWWN[8];
  UCHAR PortWWN[8];
  ULONG PortFcId;
  ULONG PortType;
  ULONG PortState;
  ULONG PortSupportedClassofService;
  UCHAR PortSupportedFc4Types[32];
  UCHAR PortActiveFc4Types[32];
  ULONG PortSupportedSpeed;
  ULONG PortSpeed;
  ULONG PortMaxFrameSize;
  UCHAR FabricName[8];
  ULONG NumberofDiscoveredPorts;
} MSFC_HBAPortAttributesResults, *PMSFC_HBAPortAttributesResults;
````


## -struct-fields
<dl>

### -field <b>NodeWWN</b>

<dd>
<p>Contains a 64 bit world-wide name (WWN) that uniquely identifies the fibre channel node associated with <b>PortWWN</b>. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification.</p>
</dd>

### -field <b>PortWWN</b>

<dd>
<p>Contains a 64 bit world-wide name (WWN) that uniquely identifies the fibre channel port. For a discussion of worldwide names, see the T11 committee's <i>Fibre Channel HBA API</i> specification.</p>
</dd>

### -field <b>PortFcId</b>

<dd>
<p>Contains the current fibre channel address of <b>PortWWN</b>. The high order byte of this member contains the first byte of the address, and successively lower order bytes of this member contain successively lower bytes of the address. The lowest order byte of this member must be zero. </p>
</dd>

### -field <b>PortType</b>

<dd>
<p>Indicates the port type. This member must have one of the following values: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_UNKNOWN</p>
</td>
<td>
<p>Unknown port type. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_OTHER</p>
</td>
<td>
<p>Value that is not a port type. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_NOTPRESENT</p>
</td>
<td>
<p>Port not present.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_NPORT</p>
</td>
<td>
<p>Fabric. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_NLPORT</p>
</td>
<td>
<p>Public loop.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_FLPORT</p>
</td>
<td>
<p>Fabric on a loop. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_FPORT</p>
</td>
<td>
<p>Fabric port. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_EPORT</p>
</td>
<td>
<p>Fabric expansion port. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_GPORT</p>
</td>
<td>
<p>Generic Fabric. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_LPORT</p>
</td>
<td>
<p>Private loop port. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTTYPE_PTP</p>
</td>
<td>
<p>Point to point. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PortState</b>

<dd>
<p>Contains the state of the port indicated by <b>PortWWN</b>. This member must have one of the following values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>HBA_PORTSTATE_UNKNOWN</p>
</td>
<td>
<p>Unknown. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSTATE_ONLINE</p>
</td>
<td>
<p>Operational. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSTATE_OFFLINE</p>
</td>
<td>
<p>User Offline</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSTATE_BYPASSED</p>
</td>
<td>
<p>Bypassed. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSTATE_DIAGNOSTICS</p>
</td>
<td>
<p>In diagnostics mode.</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSTATE_LINKDOWN</p>
</td>
<td>
<p>Link Down</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSTATE_ERROR</p>
</td>
<td>
<p>Port Error. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSTATE_LOOPBACK</p>
</td>
<td>
<p>Loopback. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PortSupportedClassofService</b>

<dd>
<p>Indicates the class of service that are supported by <b>PortWWN</b>. For a list of the differences classes of service and the values that must be assigned to this member for each class, see the ANSI standard for <i>Fibre Channel Generic Services 4th Generation</i> (FC-GS-4).</p>
</dd>

### -field <b>PortSupportedFc4Types</b>

<dd>
<p>Indicates the FC-4 types that are supported by <b>PortWWN</b>. For a discussion FC-4 types, see the ANSI standard for <i>Fibre Channel Generic Services 4th Generation</i> (FC-GS-4). </p>
</dd>

### -field <b>PortActiveFc4Types</b>

<dd>
<p>Indicates the FC-4 types that are currently available on <b>PortWWN</b>. For a discussion FC-4 types, see the ANSI standard for <i>Fibre Channel Generic Services 4th Generation</i> (FC-GS-4).</p>
</dd>

### -field <b>PortSupportedSpeed</b>

<dd>
<p>Indicates the signaling bit rates at which <b>PortWWN</b> can operate. For a list of the values that this member supports, see <b>PortSpeed</b>. </p>
</dd>

### -field <b>PortSpeed</b>

<dd>
<p>Indicates the signaling bit rates at which <b>PortWWN</b> is currently operating. This member must have one of the following values: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_UNKNOWN</p>
</td>
<td>
<p>Speed unknown. The transceiver is incapable of reporting the speed. </p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_1GBIT</p>
</td>
<td>
<p>1 gigabit per sec</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_2GBIT</p>
</td>
<td>
<p>2 gigabits per sec</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_4GBIT</p>
</td>
<td>
<p>4 gigabits per sec</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_10GBIT</p>
</td>
<td>
<p>10 gigabits per sec</p>
</td>
</tr>
<tr>
<td>
<p>HBA_PORTSPEED_NOT_NEGOTIATED</p>
</td>
<td>
<p>The speed at which the port will operate has not yet been established. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>PortMaxFrameSize</b>

<dd>
<p>Indicates the maximum frame size, in bytes, that is supported by <b>PortWWN</b>.</p>
</dd>

### -field <b>FabricName</b>

<dd>
<p>Contains the name identifier for the fabric to which <b>PortWWN</b> is attached. </p>
</dd>

### -field <b>NumberofDiscoveredPorts</b>

<dd>
<p>Indicates the number of ports that are visible to <b>PortWWN</b>. For a more detailed explanation of the sorts of ports that this number takes into consideration, see the T11 committee's specification for <i>Fibre Channel HBA API</i> (FC-HBA). </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h, Hbaapi.h, or Hbaapi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553925">GetDiscoveredPortAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MSFC_HBAPortAttributesResults structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
